# `SELF JOIN`

- Join a table to itself
- Useful for comparing values in a column of rows within the same table
- Must use a table alias to help distinguish the tables
- Sometimes, it can also be described using subquery

## Code Steps

1. Specify the columns from both tables (specify table names alias to avoid ambiguity)
1. Specify the table with an alias (`table_A A1`)
1. Specify the same table to join with another alias (`table_A A2`)
1. Eliminate cases where a value would be equal to itself

```sql
SELECT A1.col1 first_case, A2.col1 second_case
FROM table_A A1, table_A A2
ON A1.pk = A2.pk;
```

## Use Case

- When we have subtypes of the record type as part of the record
- Example: `Manager` would be a subtype of `Employee` but both could be recorded in the `employee` table

## Example

```sql
SELECT e1.employee_name
FROM employees e1, employees e2
WHERE (
  e1.employee_location = e2.employee_location
  AND e2.employee_name = "Joe"
);
```

```sql
/*
 * Select the customers whose first name match the last name of another customer */
SELECT
  c1.first_name,
  c1.last_name,
  c2.first_name,
  c2.last_name
FROM customer c1, customer c2
WHERE c1.first_name = c2.last_name;
```

- NOTE: We can also use `JOIN` statement explicitly instead of a comma
- We simply need to use `ON` instead of `WHERE`
- It is also possible to be more explicit with the type of join
- But most of the time, it is going to be an inner join

```sql
/*
 * Select the customers whose first name match the last name of another customer */
SELECT
  c1.first_name,
  c1.last_name,
  c2.first_name,
  c2.last_name
FROM customer c1 JOIN customer c2
ON c1.first_name = c2.last_name;
```
