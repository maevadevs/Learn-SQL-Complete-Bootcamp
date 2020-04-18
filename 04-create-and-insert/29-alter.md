# ALTER

- Allows to modify the structure of a table

```sql
ALTER TABLE table_name
ACTION;
```

## Actions

PostgreSQL provides actions that allows to:

- Add columns to table: `ADD COLUMN`
- Remove columns from table: `DROP COLUMN`
- Rename columns of a table: `RENAME COLUMN`
- Set default value for columns
- Add CHECK constraints to columns: `ADD CONSTRAINT`
- Rename table: `RENAME TO`

### Adding a new column

```sql
ALTER TABLE table_name
ADD COLUMN column_name data_type;
```

### Deleting a column

```sql
ALTER TABLE table_name
DROP COLUMN column_name;
```

### Renaming a column

```sql
ALTER TABLE table_name
RENAME COLUMN column_name TO new_column_name;
```

### Rename a table

```sql
ALTER TABLE table_name
RENAME TO new_table_name;
```
