-- Attempt to create user_0d_1 if not exists
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';

-- Grant all privileges to user_0d_1
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

-- Flush privileges to ensure the changes take effect
FLUSH PRIVILEGES;

-- Show privileges for user_0d_1
SHOW GRANTS FOR 'user_0d_1'@'localhost';

-- Repeat the process for user_0d_2
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_2'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;
SHOW GRANTS FOR 'user_0d_2'@'localhost';
