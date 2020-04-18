# UPDATE

- To update existing data in a table

```sql
UPDATE table_name
SET
  column1 = value1,
  column2 = value2,
  column3 = value3,
  ...
WHERE condition;
```

- To return the record of the updated entry, we can use the keyword `RETURNING`

```sql
UPDATE table_name
SET
  column1 = value1,
  column2 = value2,
  column3 = value3,
  ...
WHERE condition
RETURNING column1, column2, column3...;
```

## Example

```sql
UPDATE link
SET
  description = 'Name starts with M'
WHERE name LIKE 'M%' or name LIKE 'm%'
RETURNING id, url, description;
```

