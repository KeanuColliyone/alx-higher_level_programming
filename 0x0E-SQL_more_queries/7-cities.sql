-- Creates the hbtn_0d_usa database and cities table
-- The cities table has an id that is unique, auto-generated, cannot be null, and is a primary key
-- The state_id INT cannot be null and must be a FOREIGN KEY that references the id of the states table
-- The name VARCHAR(256) cannot be null
-- Ensures the operations do not fail if the database or table already exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
  id INT NOT NULL AUTO_INCREMENT,
  state_id INT NOT NULL,
  name VARCHAR(256) NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (state_id) REFERENCES states(id)
);
