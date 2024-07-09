-- 部署ごとに給与のランクを計算するための一時的なCTE（共通テーブル式）を定義
WITH RankedSalaries AS (
    SELECT
        E.id, -- 従業員のID
        E.name, -- 従業員の名前
        E.salary, -- 従業員の給与
        E.departmentId, -- 従業員の部署ID
        DENSE_RANK() OVER (PARTITION BY E.departmentId ORDER BY E.salary DESC) AS salary_rank -- 部署ごとに給与を降順でランク付け
    FROM
        Employee E -- Employeeテーブルからデータを取得
)
-- 高給者を取得するためのメインクエリ
SELECT
    D.name AS Department, -- 部署名
    RS.name AS Employee, -- 従業員の名前
    RS.salary AS Salary -- 従業員の給与
FROM
    RankedSalaries RS -- ランク付けされた給与データを持つCTE
    JOIN Department D ON RS.departmentId = D.id -- 部署IDでDepartmentテーブルと結合
WHERE
    RS.salary_rank <= 3 -- 上位3位以内のランクの従業員を選択
ORDER BY
    D.name, -- 部署名で並び替え
    RS.salary_rank; -- ランクで並び替え
