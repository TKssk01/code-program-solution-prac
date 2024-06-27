-- カラムx, y, zと三角形判定結果(triangle)を取得するSELECT文
SELECT 
    x,  -- テーブルのカラムxを選択
    y,  -- テーブルのカラムyを選択
    z,  -- テーブルのカラムzを選択
    CASE
        -- 三角形不等式を満たす場合、'Yes'を返す
        WHEN x + y > z AND x + z > y AND y + z > x THEN 'Yes'
        -- 三角形不等式を満たさない場合、'No'を返す
        ELSE 'No'
    END AS triangle  -- 'Yes' または 'No'を含む新しいカラムtriangleとして結果を返す
FROM
    Triangle;  -- テーブルTriangleからデータを取得
