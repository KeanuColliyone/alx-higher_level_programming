-- Check and list privileges for 'user_0d_1'@'localhost'
SELECT CONCAT('User user_0d_1 exists with privileges: ', GROUP_CONCAT(privilege_type))
FROM information_schema.user_privileges
WHERE grantee = '\'user_0d_1\'@\'localhost\''
GROUP BY grantee
UNION
SELECT 'User user_0d_1 does not exist or has no privileges'
WHERE NOT EXISTS (
    SELECT *
    FROM information_schema.user_privileges
    WHERE grantee = '\'user_0d_1\'@\'localhost\''
);

-- Check and list privileges for 'user_0d_2'@'localhost'
SELECT CONCAT('User user_0d_2 exists with privileges: ', GROUP_CONCAT(privilege_type))
FROM information_schema.user_privileges
WHERE grantee = '\'user_0d_2\'@\'localhost\''
GROUP BY grantee
UNION
SELECT 'User user_0d_2 does not exist or has no privileges'
WHERE NOT EXISTS (
    SELECT *
    FROM information_schema.user_privileges
    WHERE grantee = '\'user_0d_2\'@\'localhost\''
);
