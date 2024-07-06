-- 変換されたidとstudentのカラムを選択
SELECT 
    -- 新しいidの値を決定するためのCASE文
    CASE 
        -- idが奇数で、かつ最後のidでない場合、idを1増やす
        WHEN MOD(id, 2) = 1 AND id < (SELECT MAX(id) FROM Seat) THEN id + 1
        -- idが偶数の場合、idを1減らす
        WHEN MOD(id, 2) = 0 THEN id - 1
        -- 上記の条件に当てはまらない場合（最後のidが奇数の場合）、idはそのまま
        ELSE id
    END AS id, 
    -- studentカラムをそのまま選択
    student
-- Seatテーブルから選択
FROM Seat
-- 変換されたidで結果を昇順に並び替え
ORDER BY id;
