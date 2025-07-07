
-- clique_bait_analysis.sql

-- 1. Total number of users
SELECT COUNT(DISTINCT user_id) AS total_users
FROM clique_bait.users;

-- 2. Average number of cookies per user
SELECT 
  COUNT(DISTINCT cookie_id) * 1.0 / COUNT(DISTINCT user_id) AS avg_cookies_per_user
FROM clique_bait.users;

-- 3. Unique number of visits by all users per month
SELECT 
  DATE_TRUNC('month', event_time) AS month,
  COUNT(DISTINCT visit_id) AS unique_visits
FROM clique_bait.events
GROUP BY month
ORDER BY month;

-- 4. Number of events for each event type
SELECT 
  ei.event_name,
  COUNT(*) AS event_count
FROM clique_bait.events e
JOIN clique_bait.event_identifier ei 
  ON e.event_type = ei.event_type
GROUP BY ei.event_name
ORDER BY event_count DESC;


-- 5. Percentage of visits with a purchase event
WITH visits_with_purchase AS (
  SELECT DISTINCT visit_id
  FROM clique_bait.events e
  JOIN clique_bait.event_identifier ei 
    ON e.event_type = ei.event_type
  WHERE LOWER(ei.event_name) = 'purchase'
),
all_visits AS (
  SELECT DISTINCT visit_id
  FROM clique_bait.events
)
SELECT 
  COUNT(vwp.visit_id) * 100.0 / COUNT(av.visit_id) AS pct_visits_with_purchase
FROM all_visits av
LEFT JOIN visits_with_purchase vwp
  ON av.visit_id = vwp.visit_id;


-- 6. Percentage of visits with checkout page view but no purchase
WITH checkout_visits AS (
  SELECT DISTINCT visit_id
  FROM clique_bait.events e
  JOIN clique_bait.page_hierarchy ph 
    ON e.page_id = ph.page_id
  WHERE LOWER(ph.page_name) = 'checkout'
),
purchase_visits AS (
  SELECT DISTINCT visit_id
  FROM clique_bait.events e
  JOIN clique_bait.event_identifier ei 
    ON e.event_type = ei.event_type
  WHERE LOWER(ei.event_name) = 'purchase'
)
SELECT 
  COUNT(cv.visit_id) * 100.0 / NULLIF((SELECT COUNT(DISTINCT visit_id) FROM clique_bait.events), 0) AS pct_checkout_no_purchase
FROM checkout_visits cv
LEFT JOIN purchase_visits pv ON cv.visit_id = pv.visit_id
WHERE pv.visit_id IS NULL;


-- 7. Top 3 pages by number of views
SELECT 
  ph.page_name,
  COUNT(*) AS view_count
FROM clique_bait.events e
JOIN clique_bait.event_identifier ei ON e.event_type = ei.event_type
JOIN clique_bait.page_hierarchy ph ON e.page_id = ph.page_id
WHERE LOWER(ei.event_name) = 'page view'
GROUP BY ph.page_name
ORDER BY view_count DESC
LIMIT 3;


-- 8. Views and cart adds for each product category
SELECT 
  ph.product_category,
  SUM(CASE WHEN LOWER(ei.event_name) = 'page view' THEN 1 ELSE 0 END) AS views,
  SUM(CASE WHEN LOWER(ei.event_name) = 'add to cart' THEN 1 ELSE 0 END) AS cart_adds
FROM clique_bait.events e
JOIN clique_bait.event_identifier ei ON e.event_type = ei.event_type
JOIN clique_bait.page_hierarchy ph ON e.page_id = ph.page_id
WHERE ph.product_category IS NOT NULL
GROUP BY ph.product_category;


-- 9. Top 3 products by purchases
SELECT 
  ph.page_name AS product_name,
  COUNT(*) AS purchase_count
FROM clique_bait.events e
JOIN clique_bait.event_identifier ei ON e.event_type = ei.event_type
JOIN clique_bait.page_hierarchy ph ON e.page_id = ph.page_id
WHERE LOWER(ei.event_name) = 'purchase'
GROUP BY ph.page_name
ORDER BY purchase_count DESC
LIMIT 3;

