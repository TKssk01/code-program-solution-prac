-- 外側のSELECT文。サブクエリの結果をSecondHighestSalaryとして選択します。
SELECT (
    -- サブクエリの開始。重複を除いたsalaryを降順に並べ替えます。
    SELECT DISTINCT salary
    FROM Employee
    ORDER BY salary DESC
    -- 並べ替えた結果から2番目の値を取得します。LIMIT 1は1つの行を返し、OFFSET 1は最初の行をスキップします。
    LIMIT 1 OFFSET 1
) AS SecondHighestSalary;
