SELECT
    product_id,  -- 選択する列：製品ID
    year as first_year,  -- 選択する列：年（列名をfirst_yearとしてエイリアスを付ける）
    quantity,  -- 選択する列：数量
    price  -- 選択する列：価格
FROM
    Sales  -- データを取得するテーブル：Sales
WHERE (product_id, year) IN(  -- 次のサブクエリの結果に含まれるproduct_idとyearのペアを持つ行を選択
    SELECT
        product_id,  -- サブクエリで選択する列：製品ID
        MIN(year)  -- サブクエリで選択する列：各製品IDに対する最小の年
    FROM
        Sales  -- サブクエリで使用するテーブル：Sales
    GROUP BY
        product_id  -- サブクエリで各製品IDごとにグループ化
)
ORDER BY
    product_id,  -- 最終結果を製品IDで並び替え
    year;  -- 最終結果を年で並び替え
