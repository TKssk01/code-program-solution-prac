-- 従業員テーブルからemployee_idを選択するクエリ
SELECT
    e.employee_id  -- メインクエリの結果として返されるカラム
FROM
    Employees e  -- メインクエリのテーブル（エイリアスe）
WHERE
    e.salary < 30000  -- 給料が30000ドル未満の従業員をフィルタリング
    AND e.employee_id != 'null'  -- employee_idがnullでない従業員をフィルタリング
    -- サブクエリを使用して、manager_idが存在しない従業員をフィルタリング
    AND e.manager_id NOT IN (
        SELECT DISTINCT e2.employee_id  -- 内部サブクエリ：一意のemployee_idを選択
        FROM Employees e2  -- サブクエリのテーブル（エイリアスe2）
    )
ORDER BY
    e.employee_id ASC;  -- 結果をemployee_idの昇順でソート
