-- Creates the hbtn_0d_usa database and states table
-- The states table has an id that is unique, auto-generated, cannot be null, and is a primary key
-- The name VARCHAR(256) cannot be null
-- Ensures the operations do not fail if the database or table already exists
-- Attempt to create the database if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Select the database for subsequent operations
USE hbtn_0d_usa;
-- Attempt to create the table if it doesn't already exist
CREATE TABLE IF NOT EXISTS states (
  id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(256) NOT NULL,
  PRIMARY KEY (id)
);
