# NOT NULL CONSTRAINT

- `NULL`: Unknown or missing information
- Not the same as `0` or empty string
- `NULL` really stands for the `I don't know` option
- `NOT NULL` constraint enforce a column to not accept `NULL` values

```sql
CREATE TABLE user (
  user_id serial PRIMARY KEY,
  fname varchar(50) NOT NULL,
  lname varchar(50) NOT NULL,
  email varchar(150) NOT NULL
);
```
