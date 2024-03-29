-- Creates table unique_id with a unique ID and a VARCHAR name column
-- The id INT has a default value of 1 and must be unique
-- The name VARCHAR(256) can store a string
-- Ensures the operation does not fail if the table already exists
CREATE TABLE IF NOT EXISTS unique_id (
  id INT DEFAULT 1,
  name VARCHAR(256),
  UNIQUE(id)
);
