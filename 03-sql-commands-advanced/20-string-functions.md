# STRING FUNCTIONS AND OPERATORS

- SQL comes with a lot of string operators and functions already built-in
- The functions here are similar to those in other programming languages
- Syntaxes might differ a bit depending database engine
- We can also use Regular Expressions

```sql
/* String Concatenation */
SELECT first_name || ' ' || last_name AS full_name
FROM customer;

/* String Length */
SELECT first_name, CHAR_LENGTH(first_name) AS fname_length
FROM customer;
```
