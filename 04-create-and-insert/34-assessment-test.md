# Assessment Test

Create a new database called "School" this database should have two tables: teachers and students.

The students table should have columns for student_id, first_name,last_name, homeroom_number, phone,email, and graduation year

The teachers table should have columns for teacher_id, first_name, last_name, homeroom_number, department, email, and phone

- We must have a phone number to contact students in case of an emergency.
- We must have ids as the primary key of the tables
- Phone numbers and emails must be unique to the individual

```sql
CREATE TABLE students(
  student_id serial PRIMARY KEY,
  first_name varchar(100) NOT NULL,
  last_name varchar(100) NOT NULL,
  homeroom_number integer,
  phone varchar(50) UNIQUE NOT NULL,
  email varchar(100) UNIQUE,
  graduation_year integer CHECK(graduation_year > 1900)
);

CREATE TABLE teachers(
  teacher_id serial PRIMARY KEY,
  first_name varchar(100) NOT NULL,
  last_name varchar(100) NOT NULL,
  homeroom_number integer,
  department varchar(50),
  email varchar(100) UNIQUE,
  phone varchar(50) UNIQUE NOT NULL
);
```

Once you've made the tables, insert a student named Mark Watney (student_id=1) who has a phone number of 777-555-1234 and doesn't have an email. He graduates in 2035 and has 5 as a homeroom number

```sql
INSERT INTO students (
  first_name,
  last_name,
  phone,
  graduation_year,
  homeroom_number
)
VALUES (
  'Mark',
  'Watney',
  '777-555-1234',
  2035,
  5
);
```

Then insert a teacher names Jonas Salk (teacher_id = 1) who as a homeroom number of 5 and is from the Biology department. His contact info is: jsalk@school.org and a phone number of 777-555-4321

```sql
INSERT INTO teachers (
  first_name,
  last_name,
  homeroom_number,
  department,
  email,
  phone
)
VALUES (
  'Jonas',
  'Salk',
  5,
  'Biology',
  'jsalk@school.org',
  '777-555-4321'
);
```
