-- comment
mysql -u root -p "$1" -e "
SELECT 
    COLUMN_NAME AS 'Field',
    COLUMN_TYPE AS 'Type',
    IS_NULLABLE AS 'Null',
    COLUMN_KEY AS 'Key',
    COLUMN_DEFAULT AS 'Default',
    EXTRA AS 'Extra'
FROM information_schema.columns
WHERE table_schema = '$1'
  AND table_name = 'first_table'
ORDER BY ORDINAL_POSITION;
"

