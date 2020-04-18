# VIEWS

- A view is a database object that is of a stored query
- Can be accessible as a virtual table in PostgreSQL
- A logical table that represents data of one or more underlying tables through SELECT statement
- When a query is very involved, storing the query in a view can save a lot of time
- This allows to run simple select later on

```sql
SELECT * FROM view;
```

- A view does not store data physically
- Simplifies the complexity of a query: You can query based on a view as if it were a table, using `SELECT` statements

## CREATING A VIEW

- Use the `CREATE VIEW` statement

```sql
CREATE VIEW view_name AS select_query;
```

### Example

```sql
CREATE VIEW customer_info AS
SELECT
  first_name,
  last_name,
  email,
  address,
  phone
FROM customer c JOIN address a
ON c.address_id = a.address_id;
```

Now, we can use `customer_info` as an actual table even though it not a table

```sql
SELECT * FROM customer_info;
```

## ALTER VIEW / RENAME TO

Allows to rename the view

```sql
ALTER VIEW view_name RENAME TO new_view_name;
```

## DROP VIEW

Allows to drop/delete a view

```sql
DROP VIEW view_name;
```

- Note: Using this syntax can also throw an error if the view does not exists
- Using `IF EXISTS` is also safer here

```sql
DROP VIEW IF EXISTS view_name;
```
