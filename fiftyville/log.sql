-- Keep a log of any SQL queries you execute as you solve the mystery

-- find crime scene description
SELECT description
 FROM crime_scene_reports
 WHERE year = 2021
 AND month = 7
 AND day = 28
 AND street = ' Humphrey Street';
-- check the interviews table
.schema interviews
CREATE TABLE interviews (
    id INTEGER,
    name TEXT,
    year INTEGER,
    month INTEGER,
    day INTEGER,
    transcript TEXT,
    PRIMARY KEY(id)
--finding out what thetranscripts points to
    SELECT transcript
   ...> FROM interviews
   ...> WHERE year = 2021
   ...> AND month = 7
   ...> AND day = 28
   ...> AND transcript LIKE '%bakery%';

   CREATE TABLE bakery_security_logs (
    id INTEGER,
    year INTEGER,
    month INTEGER,
    day INTEGER,
    hour INTEGER,
    minute INTEGER,
    activity TEXT,
    license_plate TEXT,
    PRIMARY KEY(id)
);

-- looking for anyone who entered the car ten mins of the time of theft 10:25ish
SELECT license_plate
   ...> FROM bakery_security_logs
   ...> WHERE year = 2021
   ...> AND month = 7
   ...> AND day = 28
   ...> AND hour = 10
   ...> AND minute <= 25
   ...> AND activity LIKE "%exit%"
   ...> LIMIT 10;
   +---------------+
| license_plate |
+---------------+
| 5P2BI95       |
| 94KL13X       |
| 6P58WS2       |
| 4328GD8       |
| G412CB7       |
| L93JTIZ       |
| 322W7JE       |
| 0NTHK55       |
+---------------+
-- Check the atm_transactions .schema to find out how to look for anyone withdrawing money earlier that morning
CREATE TABLE atm_transactions (
    id INTEGER,
    account_number INTEGER,
    year INTEGER,
    month INTEGER,
    day INTEGER,
    atm_location TEXT,
    transaction_type TEXT,
    amount INTEGER,
    PRIMARY KEY(id)

SELECT account_number, amount
FROM atm_transactions
WHERE year = 2021
AND month = 7
AND day = 28
AND atm_location LIKE "%Leggett Street%"
AND transaction_type LIKE "%withdraw%";
+----------------+--------+
| account_number | amount |
+----------------+--------+
| 28500762       | 48     |
| 28296815       | 20     |
| 76054385       | 60     |
| 49610011       | 50     |
| 16153065       | 80     |
| 25506511       | 20     |
| 81061156       | 30     |
| 26013199       | 35     |
+----------------+--------+
Check bank accounts matching theses account info
check .schema bank_accounts to see whats there
CREATE TABLE bank_accounts (
    account_number INTEGER,
    person_id INTEGER,
    creation_year INTEGER,
    FOREIGN KEY(person_id) REFERENCES people(id)
);
SELECT *
FROM bank_accounts
WHERE account_number =
 (SELECT account_number
FROM atm_transactions
WHERE year = 2021
AND month = 7
AND day = 28
AND atm_location LIKE "%Leggett Street%"
AND transaction_type LIKE "%withdraw%");
+----------------+-----------+---------------+
| account_number | person_id | creation_year |
+----------------+-----------+---------------+
| 28500762       | 467400    | 2014          |
+----------------+-----------+---------------+


Cross reference peoples table to find out who this person_id belong to.
check .schema people
CREATE TABLE people (
    id INTEGER,
    name TEXT,
    phone_number TEXT,
    passport_number INTEGER,
    license_plate TEXT,
    PRIMARY KEY(id)
);
join people to bank_accounts
SELECT id, name, phone_number, passport_number, license_plate
FROM people
JOIN people ON people.id = bank_accounts.person_id
JOIN bank_accounts ON bank_accounts.person_id = people.id
WHERE person_id = 467400;

SELECT *
FROM people
WHERE license_plate LIKE "%5P2BI95%"
+--------+---------+----------------+-----------------+---------------+
|   id   |  name   |  phone_number  | passport_number | license_plate |
+--------+---------+----------------+-----------------+---------------+
| 221103 | Vanessa | (725) 555-4692 | 2963008352      | 5P2BI95       |
+--------+---------+----------------+-----------------+---------------+

SELECT *
   ...> FROM people
   ...> WHERE license_plate LIKE "%94KL13X%";
+--------+-------+----------------+-----------------+---------------+
|   id   | name  |  phone_number  | passport_number | license_plate |
+--------+-------+----------------+-----------------+---------------+
| 686048 | Bruce | (367) 555-5533 | 5773159633      | 94KL13X       |
+--------+-------+----------------+-----------------+---------------+
+-----+----------------+----------------+------+-------+-----+----------+
| id  |     caller     |    receiver    | year | month | day | duration |
+-----+----------------+----------------+------+-------+-----+----------+
| 233 | (367) 555-5533 | (375) 555-8161 | 2021 | 7     | 28  | 45       |
| 236 | (367) 555-5533 | (344) 555-9601 | 2021 | 7     | 28  | 120      |
| 245 | (367) 555-5533 | (022) 555-4052 | 2021 | 7     | 28  | 241      |
| 285 | (367) 555-5533 | (704) 555-5790 | 2021 | 7     | 28  | 75       |
+-----+----------------+----------------+------+-------+-----+----------+

SELECT *
   ...> FROM people
   ...> WHERE phone_number LIKE "%(375) 555-8161%";
+--------+-------+----------------+-----------------+---------------+
|   id   | name  |  phone_number  | passport_number | license_plate |
+--------+-------+----------------+-----------------+---------------+
| 864400 | Robin | (375) 555-8161 | NULL            | 4V16VO0       |
+--------+-------+----------------+-----------------+---------------+
SELECT *
FROM phone_calls
WHERE year = 2021
AND month = 7
AND day = 28
AND caller LIKE "%(725) 555-4692%";
+-----+----------------+----------------+------+-------+-----+----------+
| id  |     caller     |    receiver    | year | month | day | duration |
+-----+----------------+----------------+------+-------+-----+----------+
| 257 | (725) 555-4692 | (821) 555-5262 | 2021 | 7     | 28  | 456      |


check .schema airports
CREATE TABLE airports (
    id INTEGER,
    abbreviation TEXT,
    full_name TEXT,
    city TEXT,
    PRIMARY KEY(id)
);
Check for flights leaving fiftyville
SELECT *
   ...> FROM airports
   ...> WHERE full_name LIKE "%fiftyville%";
+----+--------------+-----------------------------+------------+
| id | abbreviation |          full_name          |    city    |
+----+--------------+-----------------------------+------------+
| 8  | CSF          | Fiftyville Regional Airport | Fiftyville |
SELECT *
FROM airports
WHERE id = 4;
+----+--------------+-------------------+---------------+
| id | abbreviation |     full_name     |     city      |
+----+--------------+-------------------+---------------+
| 4  | LGA          | LaGuardia Airport | New York City |
+----+--------------+-------------------+---------------+




check .schema on flights
CREATE TABLE flights (
    id INTEGER,
    origin_airport_id INTEGER,
    destination_airport_id INTEGER,
    year INTEGER,
    month INTEGER,
    day INTEGER,
    hour INTEGER,
    minute INTEGER,
    PRIMARY KEY(id),
    FOREIGN KEY(origin_airport_id) REFERENCES airports(id),
    FOREIGN KEY(destination_airport_id) REFERENCES airports(id)
);


Check the earliest flights out of fiftyville on 7,29,2021
SELECT *
FROM passengers
WHERE passport_number LIKE "%2963008352%"
+-----------+-----------------+------+
| flight_id | passport_number | seat |
+-----------+-----------------+------+
| 2         | 2963008352      | 6C   |
| 20        | 2963008352      | 6B   |
| 39        | 2963008352      | 8C   |
+-----------+-----------------+------+

SELECT *
   ...> FROM passengers
   ...> WHERE passport_number LIKE "%5773159633%";
   BRUCE
+-----------+-----------------+------+
| flight_id | passport_number | seat |
+-----------+-----------------+------+
| 36        | 5773159633      | 4A   |
+-----------+-----------------+------+
SELECT *
   ...> FROM flights
   ...> WHERE origin_airport_id = 8
   ...> AND year = 2021
   ...> AND month = 7
   ...> AND day = 29
   ...> AND hour <= 10;
+----+-------------------+------------------------+------+-------+-----+------+--------+
| id | origin_airport_id | destination_airport_id | year | month | day | hour | minute |
+----+-------------------+------------------------+------+-------+-----+------+--------+
| 36 | 8                 | 4                      | 2021 | 7     | 29  | 8    | 20     |
| 43 | 8                 | 1                      | 2021 | 7     | 29  | 9    | 30     |
+----+-------------------+------------------------+------+-------+-----+------+--------+
 36        | 7214083635      | 2A   |
| 36        | 1695452385      | 3B   |
| 36        | 5773159633      | 4A   |
| 36        | 1540955065      | 5C   |
| 36        | 8294398571      | 6C   |
| 36        | 1988161715      | 6D   |
| 36        | 9878712108      | 7A   |
| 36        | 8496433585      | 7B   |
+------+
sqlite> SELECT *
   ...> FROM people
   ...> WHERE passprt_number LIKE "%1695452385%";
Parse error: no such column: passprt_number
  SELECT * FROM people  WHERE passprt_number LIKE "%1695452385%";
                error here ---^
sqlite> SELECT *
   ...> FROM people
   ...> WHERE passport_number LIKE "%1695452385%";
+--------+-------+----------------+-----------------+---------------+
|   id   | name  |  phone_number  | passport_number | license_plate |
+--------+-------+----------------+-----------------+---------------+
| 398010 | Sofia | (130) 555-0289 | 1695452385      | G412CB7       |
+--------+-------+----------------+-----------------+---------------+
sqlite> SELECT *
   ...> FROM people
   ...> WHERE passport_number LIKE "%7214083635%";
+--------+-------+----------------+-----------------+---------------+
|   id   | name  |  phone_number  | passport_number | license_plate |
+--------+-------+----------------+-----------------+---------------+
| 953679 | Doris | (066) 555-9701 | 7214083635      | M51FA04       |
+--------+-------+----------------+-----------------+---------------+
sqlite> SELECT *
   ...> FROM people
   ...> WHERE passport_number LIKE "%1540955065%";
+--------+--------+----------------+-----------------+---------------+
|   id   |  name  |  phone_number  | passport_number | license_plate |
+--------+--------+----------------+-----------------+---------------+
| 651714 | Edward | (328) 555-1152 | 1540955065      | 130LD9Z       |
+--------+--------+----------------+-----------------+---------------+
sqlite> SELECT *
   ...> FROM people
   ...> WHERE passport_number LIKE "%8294398571%";
+--------+--------+----------------+-----------------+---------------+
|   id   |  name  |  phone_number  | passport_number | license_plate |
+--------+--------+----------------+-----------------+---------------+
| 560886 | Kelsey | (499) 555-9472 | 8294398571      | 0NTHK55       |
+--------+--------+----------------+-----------------+---------------+
sqlite> SELECT *
   ...> FROM people
   ...> WHERE passport_number LIKE "%1988161715%";
+--------+--------+----------------+-----------------+---------------+
|   id   |  name  |  phone_number  | passport_number | license_plate |
+--------+--------+----------------+-----------------+---------------+
| 449774 | Taylor | (286) 555-6063 | 1988161715      | 1106N58       |
+--------+--------+----------------+-----------------+---------------+
sqlite> SELECT *
   ...> FROM people
   ...> WHERE passport_number LIKE "%9878712108%";
+--------+-------+----------------+-----------------+---------------+
|   id   | name  |  phone_number  | passport_number | license_plate |
+--------+-------+----------------+-----------------+---------------+
| 395717 | Kenny | (826) 555-1652 | 9878712108      | 30G67EN       |
+--------+-------+----------------+-----------------+---------------+
sqlite> SELECT *
   ...> FROM people
   ...> WHERE passport_number LIKE "%8496433585%";
+--------+------+----------------+-----------------+---------------+
|   id   | name |  phone_number  | passport_number | license_plate |
+--------+------+----------------+-----------------+---------------+
| 467400 | Luca | (389) 555-5198 | 8496433585      | 4328GD8       |
+--------+------+----------------+-----------------+---------------+
sqlite> SELECT *
   ...> FROM people
   ...> WHERE passport_number LIKE "%577315963%";
+--------+-------+----------------+-----------------+---------------+
|   id   | name  |  phone_number  | passport_number | license_plate |
+--------+-------+----------------+-----------------+---------------+
| 686048 | Bruce | (367) 555-5533 | 5773159633      | 94KL13X       |
+--------+-------+----------------+-----------------+---------------+