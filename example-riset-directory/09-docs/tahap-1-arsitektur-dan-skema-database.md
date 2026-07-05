# Tahap 1 — Perancangan Arsitektur & Skema Database

**Status:** Selesai
**Menjadi acuan untuk:** tahap-2-implementasi-gateway.md

---

## Tujuan

Merancang arsitektur sistem dan skema database yang memungkinkan perbandingan performa antara gateway tanpa mitigasi (baseline) dan dengan mitigasi (solusi) dalam menghadapi serangan JWKS Endpoint Flooding.

## Deliverable

- [x] **Arsitektur Sistem:** Menetapkan komponen utama: API Gateway (Go), Database (PostgreSQL), dan Cache (Redis).
- [x] **Mode Operasi Gateway:** Mendefinisikan dua mode yang akan diimplementasikan dan dibandingkan:
    - `none`: Mode baseline tanpa caching, setiap verifikasi kunci akan selalu mengakses database.
    - `hybrid`: Mode mitigasi dengan L1 cache di Redis dan L2 rate-limiter di PostgreSQL.
- [x] **Skema Database (PostgreSQL):** Merancang tabel yang dibutuhkan:
    - `signing_keys`: Menyimpan public key (JWKS).
    - `rate_limit_counters`: Menyimpan state untuk mekanisme rate-limiting per client IP.
- [x] **Mekanisme Mitigasi:** Merancang logika untuk *hybrid caching*:
    - *Positive Caching*: Menyimpan kunci yang valid di Redis untuk akses cepat.
    - *Negative Caching*: Menyimpan `kid` yang tidak valid di Redis untuk mencegah query berulang ke database.
    - *Rate Limiting*: Menggunakan counter di PostgreSQL untuk membatasi jumlah `kid` unik baru yang bisa dicari per satuan waktu dari satu IP.
- [x] **Alat Migrasi:** Memilih Sqitch sebagai alat untuk manajemen migrasi skema database.

## Keputusan Desain Arsitektur

- **API Gateway (Go):** Dipilih karena performa tinggi dan ekosistem yang matang untuk aplikasi jaringan. Library Echo digunakan untuk routing dan middleware.
- **PostgreSQL sebagai L2/Persistence:** Dipilih karena keandalannya dan dukungan untuk fungsi `UPSERT` yang efisien untuk implementasi rate limiter. Tabel `rate_limit_counters` akan menjadi "persistent L2 cache" untuk rate limiter.
- **Redis sebagai L1 Cache:** Dipilih karena kecepatan akses in-memory, cocok untuk caching kunci (positive) dan `kid` tidak valid (negative) dengan TTL.
- **Docker & Docker Compose:** Digunakan untuk orkestrasi dan memastikan lingkungan yang reprodusibel untuk pengembangan dan pengujian.
- **Fail-over Strategy:**
    - **Redis down (fail-open):** Jika Redis tidak tersedia, gateway akan *fallback* ke PostgreSQL. Ini memastikan ketersediaan layanan untuk pengguna valid, meskipun performa menurun.
    - **PostgreSQL down (fail-closed):** Jika database tidak tersedia, gateway akan gagal merespons. Ini adalah pilihan aman untuk mencegah gateway beroperasi dalam kondisi tidak terjamin.

## Skema Database Final

### Tabel `signing_keys`
```sql
CREATE TABLE signing_keys (
    kid VARCHAR(255) PRIMARY KEY,
    public_key TEXT NOT NULL,
    algorithm VARCHAR(50) NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
```
Tabel ini menyimpan kunci publik yang digunakan untuk verifikasi token JWT. `kid` adalah primary key.

### Tabel `rate_limit_counters`
```sql
CREATE TABLE rate_limit_counters (
    client_ip VARCHAR(45) NOT NULL,
    window_start TIMESTAMPTZ NOT NULL,
    request_count INTEGER NOT NULL DEFAULT 1,
    PRIMARY KEY (client_ip, window_start)
);
```
Tabel ini digunakan untuk mekanisme rate-limiting. Setiap baris mencatat jumlah permintaan dari `client_ip` tertentu dalam sebuah `window_start` (misalnya, per detik).

### Fungsi `upsert_rate_limit_counter`
Sebuah fungsi PL/pgSQL akan dibuat untuk menangani logika `INSERT ... ON CONFLICT UPDATE` secara atomik, yang menjadi inti dari rate limiter.
