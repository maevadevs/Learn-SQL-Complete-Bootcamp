# DROP

- Allows to delete an existing table completely

```sql
DROP TABLE table_name;
```

- We can use a `IF EXISTS` conditioning before dropping the table too
- This helps to avoid errors if the table does not exist

```sql
DROP TABLE IF EXISTS table_name;
```

- Can also be used with `ALTER TABLE` to drop columns

```sql
ALTER TABLE table_name
DROP column_name;
```

- NOTE: Dropping a table should be a restricted operation
  - If there is any object dependent on it, it should not be dropped
  - To make sure of this, we can use `RESTRICT`
- PostgreSQL uses `RESTRICT` by default

```sql
DROP TABLE IF EXISTS table_name RESTRICT;
```

- If we want to drop the table and remove all dependants altogether, we can use `CASCADE`

```sql
DROP TABLE IF EXISTS table_name CASCADE;
```
