# Assessment Test

```sql
/* Return the customer IDs of customers who have spent at least $110
 * with the staff member who has an ID of 2 */

SELECT customer_id, staff_id, SUM(amount) AS sum_amount
FROM payment
WHERE staff_id = 2
GROUP BY customer_id
HAVING SUM(amount) > 110
ORDER BY sum_amount DESC;
```

```sql
/* How many films begin with the letter J? */

SELECT COUNT(*) as count_title_begins_with_j
FROM film
WHERE title LIKE 'J%' OR title LIKE 'j%';
```

```sql
/* What customer has the highest customer ID number whose name starts
 * with an 'E' and has an address ID lower than 500? */

SELECT customer_id, first_name, last_name
FROM customer
WHERE first_name LIKE 'E%' AND address_id < 500
ORDER BY customer_id DESC
LIMIT 1;
```
