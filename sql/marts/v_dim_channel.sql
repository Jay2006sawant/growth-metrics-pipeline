-- Channel dimension for BI joins (SQLite view)

CREATE VIEW IF NOT EXISTS v_dim_channel AS
SELECT DISTINCT
    channel,
    CASE channel
        WHEN 'organic' THEN 'unpaid'
        WHEN 'email' THEN 'owned'
        ELSE 'paid'
    END AS channel_group,
    CASE channel
        WHEN 'paid_search' THEN 1
        WHEN 'paid_social' THEN 2
        WHEN 'affiliate' THEN 3
        WHEN 'email' THEN 4
        WHEN 'organic' THEN 5
        ELSE 99
    END AS sort_key
FROM (
    SELECT channel FROM orders
    UNION
    SELECT channel FROM sessions
    UNION
    SELECT channel FROM campaign_spend
);
