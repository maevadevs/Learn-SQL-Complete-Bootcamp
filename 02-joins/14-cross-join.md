# `CROSS JOIN`

- Produces the cartesian product of rows from both tables by crossing everything
- Returns the product of each rows from the left table matched one by one with each rows of the right table
- It does not have a matching condition `ON`
- BE CAREFUL: Cross Join can produce a very large dataset (n x m)

## Equivalent In Other SQL Engines

- CROSS JOIN is equivalent to an INNER JOIN with always-true `ON` condition

```sql
SELECT tA.pk, tA.colA1, tB.pk, tB.colB1
FROM table_A as tA INNER JOIN table_B as tB
ON true;
```

## Code Steps

1. Specify the columns from both tables (specify table names to avoid ambiguity): If it is obvious and there is no ambiguity, the table names can be dropped
1. Specify the Main table (`table_A`) Alias can be used
1. Specify the table that joins the Main table (`table_B`) Alias can be used

```sql
SELECT tA.pk, tA.colA1, tB.pk, tB.colB1
FROM table_A as tA CROSS JOIN table_B as tB
WHERE condition;
```

## Pseudo-Code Interpretation of CROSS JOIN

```python
def cross_join(table_A, table_B):
  result_set = ()
  for row_A in table_A:
    for row_B in table_B:
        result_set.append(row_A.columns) + result_set.append(row_B.columns)
  return result_set
```

## Example of Advanced Use

```sql
/* BE CAREFUL: Cross Join can produce a very large dataset */
SELECT
  cst.customer_id AS "Customer ID - CST",
  pmt.customer_id AS "Customer ID - PMT", /* We can select from both tables */
  cst.email AS "Email Address",
  sum(pmt.amount) AS "Total Amount"
FROM customer AS cst CROSS JOIN payment as pmt /* No `ON` condition */
WHERE pmt.customer_id IS NOT NULL /* Where condition */
GROUP BY "Customer ID - CST", pmt.customer_id /* Aliases can be used here */
ORDER BY "Total Amount" DESC
LIMIT 10;
```

## Cross Join Example

```visual
table_a             table_b

id  name            id  name
**  ****            **  ****
1   Pirate          1   Rutabaga
2   Monkey          2   Pirate
3   Ninja           3   Darth Vader
4   Spaghetti       4   Ninja
```

### Query

```sql
SELECT *
FROM table_a CROSS JOIN table_b;
```

### Result

```visual
a.id  a.name    b.id  b.name
****  ******    ****  ******
1     Pirate    1     Rutabaga
1     Pirate    2     Pirate
1     Pirate    3     Darth Vader
1     Pirate    4     Ninja
2     Monkey    1     Rutabaga
2     Monkey    2     Pirate
2     Monkey    3     Darth Vader
2     Monkey    4     Ninja
3     Ninja     1     Rutabaga
3     Ninja     2     Pirate
3     Ninja     3     Darth Vader
3     Ninja     4     Ninja
4     Spaghetti 1     Rutabaga
4     Spaghetti 2     Pirate
4     Spaghetti 3     Darth Vader
4     Spaghetti 4     Ninja
```
