# SQL Data Types

- PostgreSQL supports the folllowing Data Types
  - Boolean
  - Character
  - Number
  - Temporal (Date and Time-related)
  - Special Types
  - Array
- We need to specify the column data types when creating tables

## BOOLEAN

- `true` or `false`
- If unknown: `NULL`
- Keyword: `boolean` or `bool`
- Boolean values conversion:
  - 1, 'yes', 'y', 't', true => `true`
  - 0, 'no', 'n', 'f', false => `false`
- Displaying boolean columns:
  - `t` for `true`
  - `f` for `false`
  - ` ` for `NULL`

## CHARACTER

3 types or character data types:

- `char`: A single character
- `char(n)`: Fixed-length character string
  - Pad spaces if too short
  - Error if too long
- `varchar(n)`: Variable-length character string
  - Can store up to n characters
  - No padding
  - Error if too long

## NUMBER

2 types of numbers:

- Integers
- Floating-Point

### INTEGERS

There are 3 subtypes of integers:

- `smallint`: Small Integers
  - 2-bytes signed
  - [-32768, 32767]
- `int`: 32-bit Integers
  - 4-bytes signed
  - [-2147483648, 2147483647]
- `serial`: Similar to `int` but with auto-increment
  - 4-bytes unsigned
  - [1, 2147483647]
- `bigint`: 64-bit Integers
  - 8-bytes signed
  - [-9223372036854775808, 9223372036854775807]

### FLOATS

There are 3 subtypes of floats:

- `float(n)`: n-precision float
  - Up to a maximum of 8-bytes (64-bits)
- `real` or `float8`: double-precision 8-bytes (64-bits)
- `numeric` or `numeric(p,s)`: `p` leading digits and `s` numbers after decimal point

### TEMPORAL

Stores dates and time data

- `date`
- `time`
- `timestamp` is date + time
- `interval` is difference in timestamp
- `timestamptz` is timestamp with timezone data
