# `LEFT OUTER JOIN` or `LEFT JOIN` with `WHERE`

- **Left-Table Priority**: Returns everything from the left table but not in the right table
- Check for matches against the right table
  - If there are matches, add those cells from the right table to the matching cells of the left table
  - If there are no matches, replace the cell with `null`
- Filter the results further by applying a `WHERE` clause

## Code Steps

1. Specify the columns from both tables (specify table names to avoid ambiguity): If it is obvious and there is no ambiguity, the table names can be dropped
1. Specify the Main table (`table_A`) Alias can be used
1. Specify the table that joins the Main table (`table_B`) Alias can be used
1. Add a join condition `ON`
1. Add a `WHERE` condition

```sql
SELECT tA.pk, tA.colA1, tB.pk, tB.colB1
FROM table_A as tA LEFT OUTER JOIN table_B as tB
ON table_A.pk = table_B.fk
WHERE condition;
```

## Pseudo-Code Interpretation of LEFT OUTER JOIN with WHERE

```python
def left_outer_join_with_where(table_A, table_B, on_condition='row_A.pk == row_B.fk', where_condition):
  result_set = ()
  for row_A in table_A:
    for row_B in table_B:
      isMatch = search_match(row_A, row_B, on_condition)
      if isMatch:
        result_set.append(row_A.columns) + result_set.append(row_B.columns)
      else:
        result_set.append(row_A.columns) + result_set.append(null)
  return filter(result_set, where_condition)
```

## Example of Advanced Use

```sql
SELECT
  cst.customer_id AS "Customer ID - CST",
  pmt.customer_id AS "Customer ID - PMT", /* We can select from both tables */
  cst.email AS "Email Address",
  sum(pmt.amount) AS "Total Amount"
FROM customer AS cst LEFT OUTER JOIN payment as pmt
ON cst.customer_id = pmt.customer_id
WHERE pmt.customer_id IS NOT NULL /* Where condition */
GROUP BY "Customer ID - CST", pmt.customer_id /* Aliases can be used here */
ORDER BY "Total Amount" DESC
LIMIT 10;
```

## Left Outer Join With `Where` Example

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
FROM table_a LEFT OUTER JOIN table_b /* or just LEFT JOIN */
ON table_a.name = table_b.name
WHERE table_b.id IS NULL;
```

### Result

```visual
a.id  a.name    b.id  b.name
****  ******    ****  ******
2     Monkey    null  null
4     Spaghetti null  null
```
