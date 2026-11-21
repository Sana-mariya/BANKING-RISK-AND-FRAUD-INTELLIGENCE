USE banking_fraud_analytics;
DESCRIBE creditcard_transactions;
SELECT COUNT(*)
FROM creditcard_transactions;
SHOW VARIABLES LIKE 'local_infile';
SET GLOBAL local_infile = 1;
SHOW VARIABLES LIKE 'secure_file_priv';
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/cleaned_creditcard.csv'
INTO TABLE creditcard_transactions
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

SELECT COUNT(*)
FROM creditcard_transactions;

SELECT *
FROM creditcard_transactions
LIMIT 5;

SELECT 
    Class,
    COUNT(*) AS Total_Transactions
FROM creditcard_transactions
GROUP BY Class;

SELECT COUNT(*) AS Fraud_Count
FROM creditcard_transactions
WHERE Class = 1;

SELECT SUM(Amount) AS Total_Fraud_Amount
FROM creditcard_transactions
WHERE Class = 1;

SELECT Class, AVG(Amount) AS Average_Amount
FROM creditcard_transactions
GROUP BY Class;

SELECT Time, Amount
FROM creditcard_transactions
WHERE Class = 1
LIMIT 10;
    
    SELECT Amount
FROM creditcard_transactions
WHERE Class = 1
ORDER BY Amount DESC
LIMIT 5;

SELECT Amount
FROM creditcard_transactions
WHERE Class = 1 AND Amount < 100;

SELECT
    Amount,
    Time
FROM creditcard_transactions
WHERE Class = 1
ORDER BY Amount DESC
LIMIT 5;

SELECT
    Amount,
    Time
FROM creditcard_transactions
WHERE Class = 1
ORDER BY Amount ASC
LIMIT 5;

SELECT
    SUM(Amount) AS Total_Genuine_Amount
FROM creditcard_transactions
WHERE Class = 0;

SELECT
    COUNT(*) AS Total_Transactions
FROM creditcard_transactions
WHERE Amount BETWEEN 100 AND 500;

SELECT
    COUNT(*) AS Transactions_Above_500
FROM creditcard_transactions
WHERE Amount > 500;

SELECT
    COUNT(*) AS Transactions_Below_100
FROM creditcard_transactions
WHERE Amount < 100;

SELECT
    MAX(Amount) AS Highest_Transaction
FROM creditcard_transactions;

SELECT
    MIN(Amount) AS Lowest_Transaction
FROM creditcard_transactions;

SELECT
    ROUND(AVG(Amount), 2) AS Average_Transaction
FROM creditcard_transactions;

SELECT
    Class,
    COUNT(*) AS Total_Transactions
FROM creditcard_transactions
GROUP BY Class;
