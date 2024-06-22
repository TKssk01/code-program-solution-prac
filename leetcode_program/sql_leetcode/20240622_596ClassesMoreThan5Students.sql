-- クラス名を選択
SELECT
    class
FROM
    Courses
-- クラスごとにグループ化
GROUP BY
    class
-- 各クラスの行数をカウントし、行数が5以上のクラスのみを選択
HAVING
    COUNT(class) >= 5;
