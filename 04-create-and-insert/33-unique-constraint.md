# UNIQUE CONSTRAINT

- Ensure that the values in this column are unique
- Everytime you insert a new row, PostgreSQL will check the column
  - If the value is already existant, error message and rejection of action
- Same process for insert and update

```sql
CREATE TABLE people(
  id serial PRIMARY KEY,
  fname varchar(100) NOT NULL,
  lname VARCHAR(100) NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL,
);
```
