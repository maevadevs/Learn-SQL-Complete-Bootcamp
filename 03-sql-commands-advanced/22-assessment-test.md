# Assessment Test

```sql
/* Retrieve all information from cd.facilities table */
SELECT * 
FROM cd.facilities;



/* You want to print out a list of all of the facilities and their cost to members. 
 * How would you retrieve a list of only facility names and costs? */
SELECT name, membercost 
FROM cd.facilities;



/* How can you produce a list of facilities that charge a fee to members? */
SELECT * 
FROM cd.facilities 
WHERE membercost > 0;



/* How can you produce a list of facilities that charge a fee to members, 
 * and that fee is less than 1/50th of the monthly maintenance cost? 
 * Return the facid, facility name, member cost, and monthly maintenance 
 * of the facilities in question. */
SELECT 
	facid,
	name,
	membercost,
	monthlymaintenance
FROM cd.facilities
WHERE membercost > 0 AND (membercost < monthlymaintenance / 50);



/* How can you produce a list of all facilities with the word 'Tennis' in their name? */
SELECT * 
FROM cd.facilities
WHERE "name" lIKE '%Tennis%';



/* How can you retrieve the details of facilities with ID 1 and 5? 
 * Try to do it without using the OR operator. */
SELECT * 
FROM cd.facilities
WHERE facid IN (1, 5);



/* How can you produce a list of members who joined after the start of September 2012? 
 * Return the memid, surname, firstname, and joindate of the members in question. */
SELECT 
	memid,
	surname,
	firstname,
	joindate
FROM cd.members
WHERE joindate > '2012-09-01'::date;



/* How can you produce an ordered list of the first 10 surnames in the members table?
 * The list must not contain duplicates. */
SELECT DISTINCT surname 
FROM cd.members 
ORDER BY surname 
LIMIT 10;



/* You'd like to get the signup date of your last member. How can you retrieve this information? */
SELECT joindate AS latest
FROM cd.members 
ORDER BY joindate DESC
LIMIT 1;

SELECT MAX(joindate) AS latest 
FROM cd.members;



/* Produce a count of the number of facilities that have a cost to guests of 10 or more. */
SELECT COUNT(*) as count_facilities_with_guest_10_plus
FROM cd.facilities
WHERE guestcost >= 10;



/* Produce a list of the total number of slots booked per facility in the month of September 2012. 
 * Produce an output table consisting of facility id and slots, sorted by the number of slots. */
SELECT 
  facid, 
  SUM(slots) AS slots 
FROM cd.bookings
WHERE EXTRACT(month from starttime) = 09 AND EXTRACT(year from starttime) = 2012
-- WHERE starttime >= '2012-09-01' AND starttime < '2012-10-01' /* Similar */
GROUP BY facid
ORDER BY slots DESC;



/* Produce a list of facilities with more than 1000 slots booked.
 * Produce an output table consisting of facility id and total slots, sorted by facility id. */
SELECT
	fc.facid AS facid,
	fc.name AS fcname,
	SUM(bk.slots) AS total_booked_slots
from cd.bookings bk JOIN cd.facilities fc
ON bk.facid = fc.facid
GROUP BY fc.facid, fc.name
HAVING SUM(bk.slots) >= 1000
ORDER BY facid DESC;



/* How can you produce a list of the start times for bookings for tennis courts, 
 * for the date '2012-09-21'? Return a list of start time and facility name 
 * pairings, ordered by the time. */
SELECT 
	bk.starttime::time AS start_time,
	fc.name AS facname
FROM cd.facilities fc JOIN cd.bookings bk
ON fc.facid = bk.facid
WHERE (
  fc.facid in (0,1)
	AND bk.starttime::date = '2012-09-21'
)
ORDER BY start_time;



/* How can you produce a list of the start times for bookings by members 
 * named 'David Farrell'? */
 SELECT 
	bk.bookid,
	bk.starttime AS book_start_time,
	mb.surname AS lname,
	mb.firstname AS fname
FROM cd.bookings bk JOIN cd.members mb
ON bk.memid = mb.memid
WHERE mb.firstname = 'David' 
AND mb.surname = 'Farrell'
ORDER BY book_start_time DESC;
