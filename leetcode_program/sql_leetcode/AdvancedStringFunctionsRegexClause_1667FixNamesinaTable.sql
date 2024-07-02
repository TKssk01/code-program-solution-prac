SELECT 
    -- `trans_date`列の日付を年-月の形式でフォーマットし、`month`というエイリアスを付けます
    DATE_FORMAT(trans_date, '%Y-%m') AS month,
    -- `country`列をそのまま選択します
    country,
    -- 全トランザクションの数をカウントし、`trans_count`というエイリアスを付けます
    COUNT(*) AS trans_count,
    -- 承認されたトランザクションの数をカウントし、`approved_count`というエイリアスを付けます
    -- `state`が'approved'の場合は1、それ以外の場合は0をカウントします
    SUM(CASE WHEN state = 'approved' THEN 1 ELSE 0 END) AS approved_count,
    -- 全トランザクションの金額を合計し、`trans_total_amount`というエイリアスを付けます
    SUM(amount) AS trans_total_amount,
    -- 承認されたトランザクションの金額を合計し、`approved_total_amount`というエイリアスを付けます
    -- `state`が'approved'の場合のみ`amount`を合計します
    SUM(CASE WHEN state = 'approved' THEN amount ELSE 0 END) AS approved_total_amount
-- `trans_date`列の年-月と`country`列ごとにデータをグループ化します
FROM
    Transactions
GROUP BY
    DATE_FORMAT(trans_date, '%Y-%m'),
    country;
