# MATH FUNCTIONS and OPERATORS

- SQL comes with math functions built-in that are useful for numerical types
- We can use pretty much all of the basic math operations
- We also get the basic math functions as in other programming languages

```sql
/* Basic addition operation */
SELECT customer_id + rental_id AS new_id
FROM payment;

/* Basic subtraction operation */
SELECT customer_id - rental_id AS new_id
FROM payment;

/* Basic multiplication operation */
SELECT customer_id * rental_id AS new_id
FROM payment;

/* Basic truncate division operation */
SELECT customer_id / rental_id AS new_id
FROM payment;

/* Average Function */
SELECT ROUND(AVG(payment_amount), 2) AS avg_amount
FROM payment;
```
