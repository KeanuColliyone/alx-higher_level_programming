-- Attempt to set or update the user's password
SET PASSWORD FOR 'user_0d_1'@'localhost' = PASSWORD('user_0d_1_pwd');
-- Grant all privileges to the user, creating the user if it doesn't exist
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd' WITH GRANT OPTION;
-- Apply changes immediately
FLUSH PRIVILEGES;
