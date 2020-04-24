# AGGREGATE FUNCTIONS

- Takes multiple data and combine them into a single value, depending on the function
- Used a lot with the `GROUP BY` statements
- List of Aggregate Functions studied here:
  - `count()`
  - `avg()`
  - `min()`
  - `max()`
  - `sum()`

## `COUNT()`

- Returns the number of input rows that match the condition
- Note: It does not consider NULL values in the column
- It is better to run it on the Primary Key

```sql
SELECT COUNT(colum_name)
FROM table_name;
```

```sql
SELECT COUNT(DISTINCT colum_name)
FROM table_name;
```

## `AVG()`

- Returns the average of all the column's values
- We can use `ROUND(val, prec)` to limit the precision

```sql
SELECT AVG(column_name)
FROM table_name;
```

## `MIN()`

- Returns the minimum of all the column's values

```sql
SELECT MIN(column_name)
FROM table_name;
```

## `MAX()`

- Returns the maximum of all the column's values

```sql
SELECT MAX(column_name)
FROM table_name;
```

## `SUM()`

- Returns the sum of all the values in the column

```sql
SELECT SUM(column_name)
FROM table_name;
```
