-- マネージャーのID、名前、直属の部下の数、および直属の部下の平均年齢を取得するクエリ
SELECT
    e.employee_id, 
    e.name, 
    COUNT(r.employee_id) AS reports_count, 
    ROUND(AVG(r.age)) AS average_age
FROM
    Employees e
-- マネージャー（e）とその直属の部下（r）を結合する
JOIN
    Employees r ON e.employee_id = r.reports_to
-- マネージャーごとにグループ化する
GROUP BY
    e.employee_id, e.name
-- 結果をマネージャーの社員ID順に並べ替える
ORDER BY
    e.employee_id
