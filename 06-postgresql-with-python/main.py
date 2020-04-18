# psycopg2 - Allows to connect to PostgreSQL
import psycopg2 as pg2


# Establish connection to PostgreSQL
conn = pg2.connect(database='dvdrental', user='postgres', password='yourpasswordhere')


# Retrieve the cursor
# A cursor is a control structure that enables traversal over the records 
# in a database. You can think of it as an iterator or pointer for Sql data 
# retrieval
cur = conn.cursor()


# Now, we can execute SQL queries with the cursor
# NOTE: Do not use string formatting here
# It is always best practice to put the entire string for SQL queries
cur.execute('SELECT * FROM payment LIMIT 1;')


# The cursor has some methods associated with it
#   cur.fetchone() - Returns the first row from the executed query as tuple
#   cur.fetchmany(n) - Returns n rows from the executed query as a list of tuples
#   cur.fetchall() - Returns all the rows from the executed query as a list of tuples

result = cur.fetchone()
print("SELECT * FROM payment LIMIT 1")
print(result)


# When done, we close the connection
cur.close() # optional, closing connection always closes any associated cursors
conn.close()



# TESTING: CREATING A NEW DATABASE
# Creating a new database
# Normally we execute "temporary transactions"
# But database-wide operations cannot be run temporarily

conn2 = pg2.connect(database='dvdrental', user='postgres', password='yourpasswordhere')
conn2.set_session(autocommit = True)
cur2 = conn2.cursor()

try:
  cur2.execute('CREATE DATABASE lecture')
  print('Database "lecture" created successfully!')
except Exception as e:
  print('An error occured:', str(e))

# Reconnect to the new database
conn2.close()
conn3 = pg2.connect(database='lecture', user='postgres', password='yourpasswordhere')
conn3.set_session(autocommit = True)
cur3 = conn3.cursor()



# TESTING: CREATING A NEW TABLE
try:
  query1 = '''
  CREATE TABLE logins (
    userid integer,
    tmstmp timestamp, 
    type varchar(10)
  );
  '''
  print('Executing query1:', cur3.execute(query1))
except Exception as e:
  print('An error occured:', str(e))


# TESTING: INSERTING CSV INTO TABLE
try:
  query2 = '''
  COPY logins 
  FROM '/path/to/data/logins01.csv'
  DELIMITER ',' 
  CSV;
  '''
  print('Executing query2:', cur3.execute(query2))
except Exception as e:
  print('An error occured:', str(e))
