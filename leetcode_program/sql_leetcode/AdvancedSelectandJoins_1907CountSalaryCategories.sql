-- 「Low Salary」カテゴリの名前と該当する銀行口座の数を選択
SELECT 'Low Salary' AS category,
    COUNT(*) AS accounts_count
FROM Accounts
WHERE income < 20000  -- 収入が$20,000未満の銀行口座をフィルタリング

UNION ALL  -- 結果を次のクエリと統合

-- 「Average Salary」カテゴリの名前と該当する銀行口座の数を選択
SELECT 'Average Salary' AS category,
    COUNT(*) AS accounts_count
FROM Accounts
WHERE income BETWEEN 20000 AND 50000  -- 収入が$20,000から$50,000の銀行口座をフィルタリング

UNION ALL  -- 結果を次のクエリと統合

-- 「High Salary」カテゴリの名前と該当する銀行口座の数を選択
SELECT 'High Salary' AS category,
    COUNT(*) AS accounts_count
FROM Accounts
WHERE income > 50000;  -- 収入が$50,000を超える銀行口座をフィルタリング