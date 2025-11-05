In this document, I include only the solutions to several LeetCode exercises to refresh my SQL skills
select 
    M.name
FROM Employee as E
    JOIN Employee as M
        ON  E.managerID = M.id
GROUP BY M.id , M.name
    HAVING COUNT(E.id) >= 5

/*----------------------------------------------- */
SELECT
    DATE_FORMAT(trans_date, '%Y-%m') as month,
    country,
    COUNT(id) as trans_count,
    SUM(
        CASE
            WHEN state = 'approved'
                THEN 1
                ELSE 0
        END
        ) AS approved_count,
    SUM(amount) as trans_total_amount,
    SUM(
        CASE 
            WHEN state = 'approved'
                THEN amount 
                ELSE 0 
        END
        ) AS approved_total_amount 
FROM Transactions
GROUP BY month, country
ORDER BY month, country
    