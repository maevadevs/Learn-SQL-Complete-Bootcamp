# USING POSTGRESQL WITH PYTHON

- We use the `psycopg2` library to connect Python to PostgreSQL
- `psycopg2` - A library that allows Python to connect to an existing PostgreSQL database to utilize SQL functionality (http://initd.org/psycopg/docs/install.html)

```sh
pip install psycopg2
```

- Your data is in a SQL database, but your machine learning tools are in Python
- We can run SQL queries from Python
- Very useful for scaled data pipelines, pre-cleaning, data exploration
- Allows for dynamic query generation

## Creating Tables

- Normally we execute "temporary transactions", but database-wide operations cannot be run temporarily

```python
conn = pg2.connect(dbname = 'postgres', user='brad', password='yourdbpasswordhere')
conn.set_session(autocommit = True)

cur = conn.cursor()
cur.execute('CREATE DATABASE lecture')
```
