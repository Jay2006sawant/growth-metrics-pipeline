-- BigQuery tables with partition and clustering hints for production loads

CREATE SCHEMA IF NOT EXISTS growth_metrics OPTIONS (location = "US");

CREATE OR REPLACE TABLE growth_metrics.orders (
  order_id INT64 NOT NULL,
  customer_id INT64 NOT NULL,
  order_date DATE NOT NULL,
  channel STRING NOT NULL,
  campaign STRING NOT NULL,
  gross_amount NUMERIC,
  discount_amount NUMERIC,
  net_revenue NUMERIC NOT NULL,
  currency STRING
)
PARTITION BY order_date
CLUSTER BY channel, campaign;

CREATE OR REPLACE TABLE growth_metrics.sessions (
  session_id INT64 NOT NULL,
  session_date DATE NOT NULL,
  channel STRING NOT NULL,
  campaign STRING NOT NULL,
  landing_page STRING,
  device STRING
)
PARTITION BY session_date
CLUSTER BY channel;

CREATE OR REPLACE TABLE growth_metrics.campaign_spend (
  spend_date DATE NOT NULL,
  channel STRING NOT NULL,
  campaign STRING NOT NULL,
  impressions INT64,
  clicks INT64,
  spend_usd NUMERIC
)
PARTITION BY spend_date
CLUSTER BY channel, campaign;
