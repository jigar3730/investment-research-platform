-- 1. Create the Weekly OHLCV Table
CREATE TABLE IF NOT EXISTS ohlcv_weekly (
    ticker VARCHAR,
    date DATE,
    open DOUBLE,
    high DOUBLE,
    low DOUBLE,
    close DOUBLE,
    volume BIGINT,
    PRIMARY KEY (ticker, date)
);

-- 2. Create the Universe Mapping Table natively from the static CSV
-- Note: '/app/data/...' is the path inside the Docker container
CREATE TABLE IF NOT EXISTS universe_mapping AS 
SELECT 
    UPPER(TRIM(Ticker)) AS ticker,
    UPPER(TRIM(Universe)) AS universe_name,
    CURRENT_DATE AS added_at
FROM read_csv_auto('/app/data/seed/universes.csv');
