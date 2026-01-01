-- Switch to the correct database
USE alx_book_store;

-- Query the information schema to get the full description of the 'books' table
SELECT COLUMN_NAME, COLUMN_TYPE
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'alx_book_store'
  AND TABLE_NAME = 'books';

