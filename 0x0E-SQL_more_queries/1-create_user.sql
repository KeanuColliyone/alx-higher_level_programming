-- Attempt to create the user. This will fail if the user already exists, but that's fine.
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- Grant all privileges to the user on all databases.
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;
-- Apply changes immediately
FLUSH PRIVILEGES;
