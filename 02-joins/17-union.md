# UNION

- Combines the result sets of 2 or more `SELECT` statements into a single result set
- NOTE: Removes all duplicate rows (unless using `UNION ALL`)
- Rows from both table could be in any order
- To sort the result set, use `ORDER BY`
- Often used to combine data from similar tables that are not perfectly normalized
- Tables often found in reporting or data warehouse systems

```sql
SELECT column1, column2, column3
FROM table1
UNION
SELECT columnA, columnB, columnC
FROM table2;
```

## REQUIREMENTS FOR UNION

- Both queries must return the same number of columns
- The corresponding columns in each query must have compatible types 
