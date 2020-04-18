# GROUP BY Statements

- One of the most useful tool in SQL
- Combines the rows returned by the `SELECT` statement into aggregate groups
- Returns a summary of the data based on the column and the aggregate function
- Without aggregate function, it act as `SELECT DISTINCT`
- For each group, we can apply an aggregate function
- The `GROUP BY` column must appear in the `SELECT` clause or be used in an aggregate function
- It is a good practice to always select the column that you are going to group by
- We can also use `ORDER BY` after this clause

```sql
SELECT column1, COUNT(column2) as count_col2, SUM(column3) as sum_col3
FROM table_name
GROUP BY column1;
```

## `HAVING`

- `HAVING` is used for conditions for `GROUP BY`
- It is similar to `WHERE` for regular `SELECT` statements
- `HAVING` applies to aggregated rows after the `GROUP BY` clause has been applied
- `WHERE` applies to individual rows before the `GROUP BY` clause is applied
- NOTE: Aliases of aggregate function cannot be used in `HAVING`

```sql
SELECT column1, COUNT(column2) as count_col2, SUM(column3) as sum_col3
FROM table_name
WHERE column3 > 5
GROUP BY column1
HAVING SUM(column3) > 200 /* Cannot use alias sum_col3 here */
ORDER BY sum_col3 DESC;
```
