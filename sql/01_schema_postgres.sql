-- Reference schema for PostgreSQL / BigQuery-style modeling
CREATE TABLE IF NOT EXISTS customers (
    customer_id     INT PRIMARY KEY,
    signup_date     DATE NOT NULL,
    country         VARCHAR(2) NOT NULL
);

CREATE TABLE IF NOT EXISTS sessions (
    session_id      INT PRIMARY KEY,
    session_date    DATE NOT NULL,
    channel         VARCHAR(32) NOT NULL,
    campaign        VARCHAR(64) NOT NULL,
    landing_page    VARCHAR(128),
    device          VARCHAR(16)
);

CREATE TABLE IF NOT EXISTS orders (
    order_id        INT PRIMARY KEY,
    customer_id     INT NOT NULL REFERENCES customers(customer_id),
    order_date      DATE NOT NULL,
    channel         VARCHAR(32) NOT NULL,
    campaign        VARCHAR(64) NOT NULL,
    gross_amount    NUMERIC(12, 2),
    discount_amount NUMERIC(12, 2),
    net_revenue     NUMERIC(12, 2),
    currency        CHAR(3) DEFAULT 'USD'
);

CREATE TABLE IF NOT EXISTS campaign_spend (
    spend_date      DATE NOT NULL,
    channel         VARCHAR(32) NOT NULL,
    campaign        VARCHAR(64) NOT NULL,
    impressions     INT,
    clicks          INT,
    spend_usd       NUMERIC(12, 2),
    PRIMARY KEY (spend_date, channel, campaign)
);
