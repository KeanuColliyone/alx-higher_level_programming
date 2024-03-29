-- Creates the id_not_null table with a default id value and a name field
-- This table ensures that every record has an id, defaulting to 1 if not specified, and can store a name up to 256 characters.
CREATE TABLE IF NOT EXISTS id_not_null (
  -- id: Integer field with default value of 1
  id INT DEFAULT 1,
  -- name: Variable character field up to 256 characters
  name VARCHAR(256)
);
