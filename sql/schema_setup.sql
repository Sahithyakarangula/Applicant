-- SQL queries to set up schemas in BigQuery
CREATE TABLE your_dataset.js_posts (
    id INT64,
    title STRING,
    body STRING,
    user_id INT64,
    status STRING,
    user_name STRING,
    user_email STRING
);
CREATE TABLE your_dataset.js_users (
    id INT64,
    name STRING,
    username STRING,
    email STRING
);
-- SQL queries to set up schemas in BigQuery
