# Primary Key and Foreign Key

## Primary Key

- A column or group of column used to uniquely identify a record (row)
- Defined with PK constraints
- A table can have one and only one PK
- Add a PK to every table
- In PostgreSQL, it is indexed
- A lot of time, we will be using a serial data type for a PK
- PK is defined when we define the table structure

```sql
CREATE TABLE table_name (
  column_name data_type PRIMARY KEY,
  column_name data_type,
  column_name data_type
);
```

## Foreign Key

- A column or group of column used to uniquely identify a record (row) in another table
- Data that refers to the PK of another table
- Defined with FK constraints
- Referencing Table/Child Table: The table that contains the FK
- Referenced Table/Parent Table: The table to which the FK references to
- A table can have multiple FK depending on its relationship with other tables
- FK constraint maintains referential integrity between child and parent tables
