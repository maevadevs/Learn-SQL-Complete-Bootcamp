# SELECT Statements

- `select`
- `select distinct`
- `select where`
- `and, or, not`
- `count()`
- `limit`
- `order by`
- `between`
- `in`
- `like`
- `ilike`

## `SELECT`

- Select data from columns in a table

```sql
SELECT column1, column2,...
FROM table_name;
```

```sql
/* This is usually not used because of performance */
SELECT *
FROM table_name;
```

## `SELECT DISTINCT`

- A column may contain duplicate values
- Use `distinct` to only return the distinct (different) values
- If multiple columns, it is about the distinct combinations
- This is similar to running `set()` on the column's values

```sql
SELECT DISTINCT column1, column2,...
FROM table_name;
```

## `COUNT()` Function

- Returns the number of input rows that match the condition
- Note: It does not consider `NULL` values in the column
- It is better to run it on the Primary Key

```sql
SELECT COUNT(colum_name)
FROM table_name;
```

```sql
SELECT COUNT(DISTINCT colum_name)
FROM table_name;
```

```sql
SELECT COUNT(DISTINCT(column_name1, column_name1))
FROM table_name;
```

## `SELECT WHERE`

- Adding conditions to a `SELECT` statement
- Filter the results returned from the `SELECT` statement

```sql
SELECT column1, column2,...
FROM table_name
WHERE condition;
```

### Comparison Operators

- `=`: Equal
- `>`: Greater than
- `<`: Less than
- `>=`: Greater than or equal
- `<=`: Less than or equal
- `!=`: Not equal
- `<>`: Not equal
- `AND`: And
- `OR`: Or
- `NOT`: Not

## `ORDER BY`

- Default order of return is by the order in the table
- To sort the result, use this statement
- We can order by multiple columns: The same as using `then`
- The default order is `ASC`
- In PostgreSQL, it is possible to sort by a column that is not in the SELECT clause
  - This might not be the case with other SQL engines
- It is always better to select the column(s) you want to order by

```sql
SELECT column1, column2, column3...
FROM table_name
ORDER BY column1 ASC/DESC, column2 ASC/DESC;
```

## `LIMIT`

- Limit the number of rows we get from the query
- A great way to get a quick summary/overview
- Goes at the very end of a query
- Good use case to use with `ORDER BY` for getting tops and bottoms (top 10, top 50,...)

```sql
SELECT *
FROM table_name
LIMIT 50;
```

## `BETWEEN`

- Operator to match a value against a range of value
- Inclusive on both end (`LOW <= x <= HIGH`)

```sql
SELECT *
FROM table_name
WHERE column1 BETWEEN 1 AND 100;
```

```sql
/* Same as the following */
SELECT *
FROM table_name
WHERE column1 => 1 AND column1 <= 100;
```

- We can use the `NOT` operator for negation
- This makes `BETWEEN` become exclusive

```sql
SELECT *
FROM table_name
WHERE column1 NOT BETWEEN 1 AND 100;
```

```sql
/* Same as the following */
SELECT *
FROM table_name
WHERE column1 < 1 OR column1 > 100;
```

## `IN`

- To check if a value matches any values in a list of values
- Useful when dealing with subqueries
- Compared to `BETWEEN`, this can be more specific list than just a range

```sql
SELECT *
FROM table_name
WHERE column1 IN (value1, value2, value3...);
```

- Value can also be the result of a subquery
- We can use the `NOT` operator for negation

```sql
SELECT *
FROM table_name
WHERE column1 NOT IN (
  SELECT column2
  FROM table_name2
  WHERE condition2;
);
```

## `LIKE`

- This is partial matching or pattern matching
- Mostly used for strings
- Using `%` as a wildcard character

```sql
SELECT *
FROM table_name
WHERE column1 LIKE `%abc%`;
```

- `%`: Match any sequence of character
- `_`: Match any single character
- We can use the `NOT` operator for negation

```sql
SELECT *
FROM table_name
WHERE column1 NOT LIKE `%abc%`;
```

### `ILIKE`

- Specific to PostgreSQL
- `LIKE` is case-sensitive but `ILIKE` is case-insensitive
