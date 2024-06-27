-- 最初に共通テーブル式 (CTE) を定義します。このCTEはFirstOrdersという名前で、各顧客の最初の注文日を取得します。
WITH FirstOrders AS (
    -- Deliveryテーブルから顧客ごとに最初の注文日を取得します。
    SELECT customer_id, MIN(order_date) AS first_order_date
    FROM Delivery
    GROUP BY customer_id
),
-- 次に、FirstOrderDetailsという名前のCTEを定義します。このCTEは各顧客の最初の注文の詳細を取得します。
FirstOrderDetails AS (
    -- FirstOrdersとDeliveryテーブルを結合して、各顧客の最初の注文の詳細を取得します。
    SELECT f.customer_id, d.order_date, d.customer_pref_delivery_date
    FROM FirstOrders f
    -- f.customer_idとd.customer_idが一致し、かつf.first_order_dateがd.order_dateに一致する行を結合します。
    JOIN Delivery d
    ON f.customer_id = d.customer_id AND f.first_order_date = d.order_date
)
-- 最終的に、FirstOrderDetailsから即時配達の割合を計算します。
SELECT 
    -- 即時配達の割合を計算し、小数点以下2桁に丸めて表示します。
    ROUND(100.0 * SUM(CASE WHEN order_date = customer_pref_delivery_date THEN 1 ELSE 0 END) / COUNT(*), 2) AS immediate_percentage
FROM FirstOrderDetails;
