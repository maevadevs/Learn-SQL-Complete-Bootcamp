# SUB-QUERY

- Use multiple `SELECT` to create a query within a query
- The result of one query will be used as inputs for the other query
- Case Example: `Which films have rental rates greater than or equal to the average rental rate?`
- We can do this in 2 steps
- A sub-query is put inside of parenthesis `()`

1. Find the average rental rate

```sql
SELECT AVG(rental_rate) as avg_rental_rate
FROM film;
```

2. Compare each rental rate to the average rental rate

```sql
SELECT film_id, film_title, rental_rate
FROM film
WHERE rental_rate >= avg_rental_rate;
```

3. To combine the 2 queries into one, we use sub-query

```sql
SELECT film_id, title, rental_rate
FROM film
WHERE rental_rate >= (
  SELECT AVG(rental_rate) AS avg_rental_rate
  FROM film
)
ORDER BY rental_rate;
```

- If the subquery returns a single value, use single comparator for main query
- If the subquery returns a bunch of rows, use the `IN` operator to compare
