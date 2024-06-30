SELECT 
    user_id,
    name,
    mail
FROM 
    Users
WHERE 
    mail LIKE '%@leetcode.com' 
    AND
    mail REGEXP '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    AND
    mail NOT REGEXP '[-!#$%&\'*+/=?^_`{|}~]'
