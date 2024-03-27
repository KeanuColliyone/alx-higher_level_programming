-- Description: Print the full description of the first_table from the specified database.
SELECT
    table_name AS `Table`,
    GROUP_CONCAT(column_name ORDER BY ordinal_position) AS `Columns`
FROM
    information_schema.columns
WHERE
    table_schema = DATABASE() AND table_name = 'first_table';
