-- 顧客IDを選択する
SELECT
    customer_id
FROM
    Customer
-- 顧客IDごとにグループ化する
GROUP BY
    customer_id
-- グループごとにユニークな商品キーの数をカウントし、
-- その数が全製品数と一致するグループのみを選択する
HAVING 
    COUNT(DISTINCT product_key) = (
        -- Productテーブルから全ての製品の数を取得するサブクエリ
        SELECT COUNT(*) 
        FROM Product
    );
