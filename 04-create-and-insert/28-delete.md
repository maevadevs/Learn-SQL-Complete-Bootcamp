# DELETE

- Allows to delete a row from a table
- Returns the number of rows deleted
- If no rows are deleted, it will return `0`
- We can also use `RETURNING` to return the columns that were deleted

```sql
DELETE FROM table_name
WHERE condition;
```

- NOTE: Make sure to define the WHERE clause. Without condition, this will delete all the rows in the table
