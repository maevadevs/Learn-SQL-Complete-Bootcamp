# CHECK CONSTRAINT

- Allows to specify a value in a column must meet a specific requirement
- `CHECK` uses Boolean expression to evaluate the values of a column
- If the values passes the check, PostgreSQL will insert or update the values
- Constraints can be named as well using the keyword `CONSTRAINT`

```sql
CREATE TABLE user (
  user_id serial PRIMARY KEY,
  first_name varchar(50),
  birth_date date CONSTRAINT must_birthdate_1900 CHECK(birth_date > '1900-01-01'),
  join_date date CHECK(join_date > birth_date),
  salary integer CONSTRAINT must_positive_salary CHECK(salary > 0)
);
```
