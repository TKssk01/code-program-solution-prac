-- tiv_2016の合計を計算し、2桁に丸めて表示
SELECT
    ROUND(SUM(t1.tiv_2016), 2) AS tiv_2016
FROM
    -- Insuranceテーブルにエイリアスt1を付けて参照
    Insurance t1
WHERE
    -- tiv_2015が他の保険契約者と同じ値を持つ行をフィルタリング
    t1.tiv_2015 IN (
        SELECT
            t2.tiv_2015
        FROM
            -- Insuranceテーブルにエイリアスt2を付けて参照
            Insurance t2
        -- tiv_2015でグループ化
        GROUP BY
            t2.tiv_2015
        -- グループのカウントが1より大きいものを選択
        HAVING
            COUNT(*) > 1
    )
AND
    -- 緯度と経度の組み合わせがユニークな行をフィルタリング
    (t1.lat, t1.lon) IN (
        SELECT
            t3.lat, t3.lon
        FROM
            -- Insuranceテーブルにエイリアスt3を付けて参照
            Insurance t3
        -- 緯度と経度の組み合わせでグループ化
        GROUP BY
            t3.lat, t3.lon
        -- グループのカウントが1のものを選択
        HAVING
            COUNT(*) = 1
    );
