# INSERT

- When we create atable, we give its general structure and constraints
- But it does not have any data yet
- After we create the table, we can start populating it with data
- `insert` allows to add one or more rows into a table at a time
- The values list must be in the same column list

```sql
INSERT INTO table_name (column1, column2 , ...)
VALUES
  (value1, value2, ...),
  (value1, value2, ...),
  (value1, value2, ...);
```

- We can also insert data that comes from a different table
- However, this will copy all the column data (even Primary keys) if using `*`
- Make sure to only select the columns that should be copied over

```sql
INSERT INTO new_table
SELECT (column1, column2, ...)
FROM older_table
WHERE condition;
```

## Example

```sql
/* Create a table */
CREATE TABLE link (
  id serial PRIMARY KEY,
  url varchar(255) NOT NULL,
  name varchar(255) NOT NULL,
  description varchar(255),
  rel varchar(50)
);

/* Start adding data */
INSERT INTO link (url, name)
VALUES
('www.google.com', 'google'),
('www.microsoft.com', 'microsoft'),
('www.facebook.com', 'facebook');
```
