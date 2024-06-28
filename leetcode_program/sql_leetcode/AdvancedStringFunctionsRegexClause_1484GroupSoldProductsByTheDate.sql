-- sell_dateごとに各日の販売された商品の情報を取得
SELECT
    -- sell_date列を選択
    sell_date,
    -- 各sell_dateごとにユニークなproductの数をカウントし、num_soldとして出力
    COUNT(DISTINCT product) AS num_sold,
    -- 各sell_dateごとにユニークなproductをカンマで区切って連結し、productsとして出力
    GROUP_CONCAT(DISTINCT product ORDER BY product ASC SEPARATOR ',') AS products
FROM 
    -- データのソースとなるActivitiesテーブルを指定
    Activities
GROUP BY
    -- sell_dateごとにグループ化して集計
    sell_date;
