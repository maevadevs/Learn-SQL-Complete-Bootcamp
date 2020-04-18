# `CREATE TABLE`

To create tables in SQL, we use the `CREATE TABLE` statement

```sql
CREATE TABLE table_name (
  column_name TYPE column_constraint, table_constraint
  column_name TYPE column_constraint, table_constraint
  column_name TYPE column_constraint, table_constraint
)
INHERITS existing_table_name;
```

## Inheriting From An Existing Table

- It means that the new table will contains all the columns from the existing table + the new columns
- Inheritance is optional

## Column Constraints

Applied to each individual column

- `NOT NULL`: The values in the column are required and cannot be `NULL`
- `UNIQUE`: The values in the column must be unique
  - In PostgreSQL, each `NULL` are considered to be `UNIQUE`
  - In SQL ANSI, `UNIQUE` means `NULL` can only appear once
- `PRIMARY KEY`: Combination of `NOT NULL` and `UNIQUE`
  - In case of multiple PK, use table-leve constraint
- `CHECK`: Enables to check a condition when inserting or updating data
- `REFERENCES`: Restrict the possible value to be those of another column in another table
  - This is the case to define FOREIGN KEYs

## Table Constraints

Applied to the entire table rather than to individual columns

- `UNIQUE(column_list)`: Force the value stored in the columns to be unique
- `PRIMARY KEY(column_list)`: Define primary key that consists of multiple columns
- `CHECK(condition)`: Check the condition when inserting/updating data
- `REFERENCES`: Restrict the possible value to be those of another column in another table

```schema
-------------------           ------------------           -----------------
|     account     |           |  account_role  |           |     role      |
-------------------           ------------------           -----------------
| PK  user_id     |-----------| PK  user_id    |     |-----| PK  role_id   |
|     username    |           | PK  role_id    |-----|     |     role_name |
|     password    |           |     grant_date |           -----------------
|     email       |           ------------------
|     created_on  |
|     last_login  |
-------------------
```

```sql
/* Creating the "account" table */
CREATE TABLE account (
  user_id serial PRIMARY KEY, /* Auto-increment */
  username VARCHAR (50) UNIQUE NOT NULL,
  password VARCHAR (50) NOT NULL,
  email VARCHAR (355) UNIQUE NOT NULL,
  created_on TIMESTAMP NOT NULL,
  last_login TIMESTAMP
);
```

```sql
/* Creating the "role" table */
CREATE TABLE role (
  role_id serial PRIMARY KEY, /* Auto-increment */
  role_name VARCHAR (255) UNIQUE NOT NULL
);
```

```sql
/* Creating the "account_role" table */
CREATE TABLE account_role (
  user_id integer NOT NULL,
  role_id integer NOT NULL,
  grant_date timestamp without time zone,
  /* Table Constraints */
  PRIMARY KEY (user_id, role_id),
  /* Foreign Key Constraint 1: user_id */
  CONSTRAINT account_role_role_id_fkey FOREIGN KEY (role_id)
      REFERENCES role (role_id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION,
  /* Foreign Key Constraint 2: role_id */
  CONSTRAINT account_role_user_id_fkey FOREIGN KEY (user_id)
      REFERENCES account (user_id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION
);
```

## Create from an existing table structure

- We can create a new table based on the structure of an existing table
- This will keep all the columns of the original table without the data

```sql
CREATE TABLE table1_copy (LIKE table1);
```
