# TIMESTAMPS AND `EXTRACT()`

- Different SQL engines might use slightly different syntax
- A data-type to maintain time information
- Use `EXTRACT()` to extract parts from a date: `EXTRACT(unit from date)`
- We can extract many types of time-based information

```table
Unit            Explanation
****            ***********
day             Day of the month  (1 - 31)
dow             Day of the week   (0=Sunday... 6=Saturday)
doy             Day of the year   (1... 365/366)
epoch           Number of seconds since UNIX Epoch (1970-01-01 00:00:00 UTC)
hour            Hour    (0-23)
microseconds    Seconds * 1,000,000
millenium       Millenium value
milliseconds    Seconds * 1,000
minute          Minute  (0-59)
month           Month value (1-12) or Month interval (0-11)
quarter         Quarter (1-4)
second          Seconds and fractional seconds
week            Number of the week of the year, ISO 8601
year            Year    (YYYY)
```

- DateTime has some functions and operations
- Refer to the documentation on how those works for each SQL engine

```sql
/* Examples of DateTime Operations */

DATE '2001-09-28' + INTEGER '7'
/* > Result: DATE '2001-10-05': Adds 7 days */

DATE '2001-09-28' + INTERVAL '1 hour'
/* > Result: TIMESTAMP 2001-09-28:01:00:00 Adds 1 hour */

DATE '2001-09-28' + TIME '03:00'
/* > Result: TIMESTAMP 2001-09-28:03:00:00 Adds 3 hours */
```

## `SHOW` command

- Allows to look into values of runtime parameters for PostgreSQL
- `SHOW ALL` shows all the parameters
- `SHOW X` will show the specific `X` parameter

## `NOW()` and `TIMEOFDAY()`

- Allows to get the current timestamp
- `SELECT NOW()` will return the current timestamp
- `SELECT TIMEOFDAY()` will return the same information but in a string format

## `CURRENT_DATE` and `CURRENT_TIME`

- Allows to return the current date and the current time with timezone
- Note that these are not functions

## Example Using `EXTRACT`

- Casing does not matter but it helps with visualizing the codes
- Using `extract()` allows to manipulate the data encapsulated in the date string

```sql
SELECT
  customer_id,
  extract(day from payment_date) AS payment_day,
  extract(month from payment_date) AS payment_month,
  extract(year from payment_date) AS payment_year
FROM payment;
```

```sql
/* What is the total amount expenditure by month? */
SELECT
  sum(amount) AS total,
  extract(month from payment_date) AS month
FROM payment
GROUP BY total
ORDER BY sum(amount) DESC;
```

## `AGE()`

- Calculates and returns the current age given a timestamp
- Basically calculate the difference in time between the timestamp and `NOW()`

```sql
SELECT
  AGE(date_col)
FROM table_name;
```

## `TO_CHAR()`

- General function to convert data types to text
- Useful for timestamp formatting

```sql
SELECT
  TO_CHAR(date_col, `mm-dd-yyyy`)
FROM table_name;
```
