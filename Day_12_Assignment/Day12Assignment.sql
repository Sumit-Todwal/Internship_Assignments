-- assignment no 12
1. Total amount each customer spent
SELECT
  s.customer_id,
  SUM(m.price) AS total_amount
FROM sales s
JOIN menu m ON s.product_id = m.product_id
GROUP BY s.customer_id;

-- 2. How many days each customer visited
SELECT
  customer_id,
  COUNT(DISTINCT order_date) AS visit_days
FROM sales
GROUP BY customer_id;

-- 3. First item purchased by each customer
SELECT customer_id, product_name
FROM (
  SELECT
    s.customer_id,
    s.order_date,
    m.product_name,
    RANK() OVER (PARTITION BY s.customer_id ORDER BY s.order_date) AS rnk
  FROM sales s
  JOIN menu m ON s.product_id = m.product_id
) ranked
WHERE rnk = 1;

-- 4. Most purchased item and how many times
SELECT
  m.product_name,
  COUNT(*) AS total_orders
FROM sales s
JOIN menu m ON s.product_id = m.product_id
GROUP BY m.product_name
ORDER BY total_orders DESC
LIMIT 1;

-- 5. Most popular item for each customer
SELECT customer_id, product_name, order_count
FROM (
  SELECT
    s.customer_id,
    m.product_name,
    COUNT(*) AS order_count,
    RANK() OVER (PARTITION BY s.customer_id ORDER BY COUNT(*) DESC) AS rnk
  FROM sales s
  JOIN menu m ON s.product_id = m.product_id
  GROUP BY s.customer_id, m.product_name
) ranked
WHERE rnk = 1;

-- 6. First item after becoming member
SELECT customer_id, product_name
FROM (
  SELECT
    s.customer_id,
    s.order_date,
    m.product_name,
    RANK() OVER (PARTITION BY s.customer_id ORDER BY s.order_date) AS rnk
  FROM sales s
  JOIN menu m ON s.product_id = m.product_id
  JOIN members mem ON s.customer_id = mem.customer_id
  WHERE s.order_date >= mem.join_date
) ranked
WHERE rnk = 1;

-- 7. Last item before becoming member
SELECT customer_id, product_name
FROM (
  SELECT
    s.customer_id,
    s.order_date,
    m.product_name,
    RANK() OVER (PARTITION BY s.customer_id ORDER BY s.order_date DESC) AS rnk
  FROM sales s
  JOIN menu m ON s.product_id = m.product_id
  JOIN members mem ON s.customer_id = mem.customer_id
  WHERE s.order_date < mem.join_date
) ranked
WHERE rnk = 1;

-- 8. Total items and amount before becoming member
SELECT
  s.customer_id,
  COUNT(*) AS total_items,
  SUM(m.price) AS total_amount
FROM sales s
JOIN menu m ON s.product_id = m.product_id
JOIN members mem ON s.customer_id = mem.customer_id
WHERE s.order_date < mem.join_date
GROUP BY s.customer_id;

-- 9. Points with $1 = 10 points and sushi = 2x
SELECT
  s.customer_id,
  SUM(
    CASE
      WHEN m.product_name = 'sushi' THEN m.price * 20
      ELSE m.price * 10
    END
  ) AS points
FROM sales s
JOIN menu m ON s.product_id = m.product_id
GROUP BY s.customer_id;

-- 10. Points in first week after joining for A and B
SELECT
  s.customer_id,
  SUM(m.price * 20) AS double_points
FROM sales s
JOIN menu m ON s.product_id = m.product_id
JOIN members mem ON s.customer_id = mem.customer_id
WHERE s.customer_id IN ('A', 'B')
  AND s.order_date BETWEEN mem.join_date AND DATE_ADD(mem.join_date, INTERVAL 6 DAY)
GROUP BY s.customer_id;
"""