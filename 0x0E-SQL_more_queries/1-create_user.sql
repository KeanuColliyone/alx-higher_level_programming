-- Check if the user exists and create if it does not
DELIMITER $$

CREATE PROCEDURE EnsureUserExists()
BEGIN
  IF NOT EXISTS (SELECT 1 FROM mysql.user WHERE user = 'user_0d_1') THEN
    CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
  END IF;
END$$

DELIMITER ;

CALL EnsureUserExists();
DROP PROCEDURE IF EXISTS EnsureUserExists;

-- Grant all privileges
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

-- Flush privileges to ensure the changes take effect
FLUSH PRIVILEGES;
