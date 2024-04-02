-- Write SQL queries to answer these questions using the data you have loaded into BigQuery:
-- 1. Find the top 5 users with the highest number of posts.
-- 2. For each of these top 5 users, calculate the average post length.
-- 3. Identify the day of the week when the most `lengthy` posts are created (assume all posts were created in the UTC timezone).

-- 1. Find the top 5 users with the highest number of posts.
SELECT user_id, COUNT(*) AS num_posts
FROM js_posts
GROUP BY user_id
ORDER BY num_posts DESC
LIMIT 5;

-- 2. For each of these top 5 users, calculate the average post length.
SELECT user_id, AVG(LENGTH(body)) AS avg_post_length
FROM js_posts
WHERE user_id IN (SELECT user_id FROM top_5_users)
GROUP BY user_id;
-- 3. Identify the day of the week when the most `lengthy` posts are created (assume all posts were created in the UTC timezone).
SELECT STRFTIME('%w', created_at) AS day_of_week, COUNT(*) AS num_lengthy_posts
FROM js_posts
WHERE status = 'lengthy'
GROUP BY day_of_week
ORDER BY num_lengthy_posts DESC
LIMIT 1;

