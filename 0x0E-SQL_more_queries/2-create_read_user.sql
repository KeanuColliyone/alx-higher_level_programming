-- Attempt to create the database hbtn_0d_2. This will not fail if the database already exists.
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- Attempt to create the user user_0d_2. This will not fail if the user already exists.
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- Grant only SELECT privilege to user_0d_2 on the hbtn_0d_2 database.
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
-- Apply the changes immediately.
FLUSH PRIVILEGES;
