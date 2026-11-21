SELECT
    Time,
    Amount
FROM creditcard_transactions
WHERE Class = 1
AND Amount > 500
ORDER BY Amount DESC;

SELECT
    COUNT(*) AS Fraud_Count
FROM creditcard_transactions
WHERE Class = 1
AND Amount BETWEEN 100 AND 500;

SELECT SUM(Amount) AS Total_Fraud_Amount
FROM creditcard_transactions
WHERE Class = 1
AND Amount BETWEEN 100 AND 500;

SELECT
    Class,
    COUNT(*) AS Total_Transactions
FROM creditcard_transactions
WHERE Amount BETWEEN 100 AND 500
GROUP BY Class;a