-- CTE（共通テーブル式）を定義する
WITH CTE AS (
    -- 各emailごとに最小のidを選択する
    SELECT MIN(id) AS min_id
    FROM Person
    GROUP BY email
)
-- Personテーブルから削除操作を行う
DELETE FROM Person
WHERE id NOT IN (
    -- CTEから最小のidを持つ行を選択し、それ以外の行を削除する
    SELECT min_id FROM CTE
);
