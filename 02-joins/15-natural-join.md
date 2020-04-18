# `NATURAL JOIN`

- Creates an implicit join (inner, left, or right) based on the same column names in the joined tables
- If the join type to use is not specified, it defaults to `NATURAL INNER JOIN`
- If columns to return are not specified, returns:
  - All the common columns (same name found in both tables)
  - All column in the first and second tables that is not a common column
- Because the join condition is implicit, `ON` is dropped
- Does not require to specify the join clause because it uses an implicit join clause based on the common column
- NOTE: Avoid using the NATURAL JOIN whenever possible because sometimes it may cause an unexpected result. The join might be operated on a common column that should not be used for joining

## Equivalent In Other SQL Engines

- `NATURAL JOIN` is equivalent to its counterpart explicit `INNER JOIN`, `LEFT JOIN` or `RIGTH JOIN`

## Code Steps

1. Specify the columns from both tables (specify table names to avoid ambiguity): If it is obvious and there is no ambiguity, the table names can be dropped
1. Specify the Main table (`table_A`) Alias can be used
1. Specify the table that joins the Main table (`table_B`) Alias can be used

## Pseudo-Code Interpretation of CROSS JOIN

```python
def natural_join(table_A, table_B):
  on_condition = 'row_A.pk == row_B.fk'
  if LEFT:
    return left_outer_join(table_A, table_B, on_condition)
  elif RIGHT:
    return right_outer_join(table_A, table_B, on_condition)
  else:
    return inner_join(table_A, table_B, on_condition):
```

## Example of Advanced Use

```sql
/* BE CAREFUL: Avoid Natural Join as much as possible
 * Explicit is better than implicit
 */
SELECT
  cst.customer_id AS "Customer ID - CST",
  pmt.customer_id AS "Customer ID - PMT", /* We can select from both tables */
  cst.email AS "Email Address",
  sum(pmt.amount) AS "Total Amount"
FROM customer AS cst NATURAL JOIN payment as pmt /* No `ON` condition */
WHERE pmt.customer_id IS NOT NULL /* Where condition */
GROUP BY "Customer ID - CST", pmt.customer_id /* Aliases can be used here */
ORDER BY "Total Amount" DESC
LIMIT 10;
```

```sql
SELECT tA.pk, tA.colA1, tB.pk, tB.colB1
FROM table_A as tA NATURAL [INNER, LEFT, RIGHT] JOIN table_B as tB;
```

```visual
table_a             table_b

id  name            id  name
**  ****            **  ****
1   Pirate          1   Rutabaga
2   Monkey          2   Pirate
3   Ninja           3   Darth Vader
4   Spaghetti       4   Ninja
```

## Query

```sql
SELECT *
FROM table_a NATURAL JOIN table_b;
```

## Result

```visual
a.id  a.name    b.id  b.name
****  ******    ****  ******
1     Pirate    2     Pirate
3     Ninja     4     Ninja
```
