# JOIN Statements

- Instructions to combine data from two sets of data (tables) in the DB
- Allows to relate data in one table to data in another table (Relational DB)
- It can be really useful to reference JOINS as a Venn Diagram

## Types of Joins

- Supported by ANSI SQL:
  - `INNER JOIN` / `JOIN`
  - `FULL OUTER JOIN` / `FULL JOIN`
  - `LEFT OUTER JOIN` / `LEFT JOIN`
  - `RIGHT OUTER JOIN` / `RIGHT JOIN`
  - `CROSS JOIN` (Cartesian Product)
- Additionally Supported by PostgreSQL:
  - `FULL OUTER JOIN` / `FULL JOIN` with `WHERE`
  - `LEFT OUTER JOIN` with `WHERE`
  - `RIGHT OUTER JOIN` with `WHERE`
  - `NATURAL JOIN` (Implicit Join)
  - `SELF JOIN`
- Others:
  - `SEMI JOIN`
  - `ANTI SEMI JOIN`

## `AS`

- Allows to rename columns or table selection with an alias
- Cannot be used when using `HAVING`: SQL will rename the column, after the `HAVING` operation, but before the `ORDER BY` operation

```sql
SELECT column1 AS first_column, COUNT(column2) AS count_col2, SUM(column3) AS sum_col3
FROM table_name AS tbn
WHERE column3 > 5
GROUP BY first_column
HAVING SUM(column3) > 200 /* Cannot use alias sum_col3 here */
ORDER BY sum_col3 DESC;
```

- In practice, `AS` can also be replaced with just a space character
- This is a personal taste

```sql
SELECT
  column1 first_column,
  COUNT(column2) count_col2,
  SUM(column3) sum_col3
FROM table_name tbn
WHERE column3 > 5
GROUP BY first_column
HAVING SUM(column3) > 200 /* Cannot use alias sum_col3 here */
ORDER BY sum_col3 DESC;
```

## Visualization

```visual
***********               ***********
| table_A |               | table_B |
***********               ***********
| pk: INT | ------|       | pk: INT |
| colA1   |       |-----> | fk: INT |
| colA2   |               | colB1   |
***********               ***********  
```

### Result Set

```visual
****************
| table_Result |
****************
| pk: INT      |
| colA1        |
| colA2        |
| colB1        |
****************
```

## Joins Type Support By RDBMS

<table>
<thead>
  <th></th>
  <th>ANSI SQL</th>
  <th>Oracle</th>
  <th>MySQL</th>
  <th>MS SQL Server</th>
  <th>PostgreSQL</th>
  <th>IBM DB2</th>
  <th>MS Access (O365)</th>
  <th>SQLite</th>
  <th>MariaDB</th>
</thead>
<tbody>
  <tr>
    <th>INNER JOIN</th>
    <td>Yes</td>
    <td>Yes</td>
    <td>Yes</td>
    <td>Yes</td>
    <td>Yes</td>
    <td>Yes</td>
    <td>Yes</td>
    <td>Yes</td>
  <tr>
  <tr>
    <th>FULL OUTER JOIN</th>
    <td>Yes</td>
    <td>Yes</td>
    <td>No</td>
    <td>Yes</td>
    <td>Yes</td>
    <td>Yes</td>
    <td>No</td>
    <td>No</td>
  <tr>
  <tr>
    <th>LEFT OUTER JOIN</th>
    <td>Yes</td>
    <td>Yes</td>
    <td>Yes</td>
    <td>Yes</td>
    <td>Yes</td>
    <td>Yes</td>
    <td>Yes</td>
    <td>Yes</td>
  <tr>
  <tr>
    <th>RIGHT OUTER JOIN</th>
    <td>Yes</td>
    <td>Yes</td>
    <td>Yes</td>
    <td>Yes</td>
    <td>Yes</td>
    <td>Yes</td>
    <td>Yes</td>
    <td>No</td>
  <tr>
  <tr>
    <th>CROSS JOIN</th>
    <td>Yes</td>
    <td>Yes</td>
    <td>Yes</td>
    <td>Yes</td>
    <td>Yes</td>
    <td>Yes</td>
    <td>No</td>
    <td>Yes</td>
  <tr>
  <tr>
    <th>FULL OUTER JOIN EXCLUSIVE</th>
    <td>Yes</td>
    <td>Yes</td>
    <td>No</td>
    <td>Yes</td>
    <td>Yes</td>
    <td>Yes</td>
    <td>No</td>
    <td>No</td>
  <tr>
  <tr>
    <th>LEFT OUTER JOIN EXCLUSIVE</th>
    <td>Yes</td>
    <td>Yes</td>
    <td>Yes</td>
    <td>Yes</td>
    <td>Yes</td>
    <td>Yes</td>
    <td>Yes</td>
    <td>Yes</td>
  <tr>
  <tr>
    <th>RIGHT OUTER JOIN EXCLUSIVE</th>
    <td>Yes</td>
    <td>Yes</td>
    <td>Yes</td>
    <td>Yes</td>
    <td>Yes</td>
    <td>Yes</td>
    <td>Yes</td>
    <td>No</td>
  <tr>
  <tr>
    <th>NATURAL JOIN</th>
    <td>No</td>
    <td>Yes</td>
    <td>Yes</td>
    <td>No</td>
    <td>Yes</td>
    <td>No</td>
    <td></td>
    <td>Yes</td>
  <tr>
  <tr>
    <th>SELF JOIN</th>
    <td>No</td>
    <td>Yes</td>
    <td>Yes</td>
    <td>Yes</td>
    <td>Yes</td>
    <td>Yes</td>
    <td>Yes</td>
    <td>Yes</td>
  <tr>
  <tr>
    <th>SEMI JOIN</th>
    <td>No</td>
    <td>Yes</td>
    <td>Yes</td>
    <td>Yes</td>
    <td>Yes</td>
  <tr>
  <tr>
    <th>ANTI JOIN/ANTI SEMI-JOIN</th>
    <td>No</td>
    <td>Yes</td>
    <td>Yes</td>
    <td>Yes</td>
    <td>Yes</td>
  <tr>
</tbody>
</table>
