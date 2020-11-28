


CREATE TABLE items (

items_id SERIAL PRIMARY KEY,
items VARCHAR(500)NOT NULL, 
price SERIAL NOT NULL 
);

INSERT INTO items (item, price)
VALUES('Small desk', 300 );


INSERT INTO items (item, price )
VALUES('Large desk', 500 );


INSERT INTO items (item, price )
VALUES('Fan', 80 );


INSERT INTO items (item, price )
VALUES('Harddrive', 80 );
-- //here is is giving me an error tried to move the ) down to the end of the table but i get an error in the line below 
CREATE TABLE  customers (

customers_id SERIAL PRIMARY KEY,
first_name VARCHAR(500)NOT NULL, 
last_name VARCHAR(500)NOT NULL
);

INSERT INTO customers (first_name, last_name )
VALUES('Greg', 'Jones' );

INSERT INTO customers (first_name, last_name )
VALUES('Sandra', 'Jones' );

INSERT INTO customers (first_name, last_name )
VALUES('Scott', 'Scott' );

INSERT INTO customers (first_name, last_name )
VALUES('Trevor', 'Green' );

INSERT INTO customers (first_name, last_name )
VALUES('Melanie', 'Johnson' );

INSERT INTO customers (first_name, last_name )
VALUES('Emmy', 'Snickars' );


SELECT * FROM public.items.

SELECT * FROM items WHERE price > 80;
SELECT * FROM items WHERE price <300;
SELECT * FROM customers WHERE last_name = 'Smith'; -- no reslut empty table 
SELECT * FROM customers WHERE last_name = 'Jones';-- 2 etntries 
SELECT * FROM customers WHERE last_name != 'Scott';


Gold
-- Create a database named bootcamp.
-- Create a table students.
-- Add the columns: id, last_name, first_name, birth_date.
-- The id has to be auto_incremented.
-- You have to choose the best data type for each column.
-- To help you, here is the data that you will have to insert. (How to we insert date to a table?)


CREATE TABLE students (

student_id SERIAL PRIMARY KEY,
last_name VARCHAR(50)NOT NULL, 
first_name VARCHAR(50)NOT NULL, 
dob date NOT NULL 
);
INSERT INTO students(first_name, last_name, dob)
VALUES('Amelia', 'Dux', '07/04/1996')
INSERT INTO students(first_name, last_name, dob)
VALUES('David', 'Grez', '14/06/2003')
INSERT INTO students(first_name, last_name, dob)
VALUES('Omer', 'Grez', '03/10/1980')


-- Create a table students.
-- Add the columns: id, last_name, first_name, birth_date.
-- The id has to be auto_incremented.
-- You have to choose the best data type for each column.
-- To help you, here is the data that you will have to insert. (How to we insert date to a table?)

-- Fetch all the data from the table.
SELECT * FROM students
-- Fetch all the students first_name and last_name.
SELECT first_name, last_name FROM students
-- For the following questions, only fetch the first_name and last_name of the students.
SELECT first_name, last_name FROM students i dont know what the diffrence is with the question before 
-- Fetch the student which id is equal to 2.
SELECT * FROM students WHERE student_id=2 
-- Fetch the student with the last_name Benichou AND the first_name Marc.
SELECT * FROM students WHERE first_name= 'Marc' AND last_name='Benicho' dont know how to do this oone 
-- Fetch the students with the last_name Benichou OR the first_name Marc.

SELECT students FROM students WHERE last_name= 'Benichou' OR first_name ='Marc'

there are two 'benichou' so the returns for the two inputs will be different. the OR will also give you Lea
-- Check the difference between the request 2 and 3.
-- Fetch the students which first_name contains the letter a.
SELECT  (first_name) FROM students WHERE first_name LIKE '%a%'

-- Fetch the students which first_name starts with the letter a.

SELECT LEFT (first_name,1) FROM students WHERE first_name='%A%'
-- Fetch the students which first_name ends with the letter a.

SELECT RIGHT (first_name,1) FROM students WHERE first_name = 'a' but not working 
-- Fetch the students where the second to last letter of the first_name is a (Example: Leah).
-- Fetch the students which the id are 1 AND 3
SELECT * FROM students WHERE student_id = '1' OR student_id= '3'

Fetch the students, which birth_date is equal or after the 1/01/2000. (show their first_name, last_name and birth_date)
SELECT * FROM WHERE dob 

SELECT * FROM table WHERE TheNameOfTimestampColumn > '2009-01-28 21:00:00'
--day2
-- We will work on the public database that we created yesterday.

-- Use SQL to get the following from the database:
-- All items, ordered by price (lowest to highest).
-- Items with a price above 80 (80 included), ordered by price (highest to lowest).
-- The first 3 customers in alphabetical order (A-Z) – exclude ‘id’ from the results.
-- All last names (no other columns!), in reverse alphabetical order (Z-A)

SELECT * FROM items ORDER BY price ASC;
SELECT * FROM items WHERE price > 79 ORDER BY price ASC;
SELECT * FROM items WHERE price > 79 ORDER BY price DESC;
SELECT * FROM customers WHERE customers_id <4 ORDER BY first_name ASC;
SELECT * FROM customers ORDER BY last_name DESC;

Create a table named purchases. It should have 2 columns : custumer_id and item_id. These columns are 
references from the tables customers and items. Edit the data of the purchases table:
Add a row which references a customer by ID, but does not reference an item by ID (leave it blank). Does this work? Why/why not?
Add 5 rows which reference existing customers and items.
--wrong
-- CREATE TABLE purchases (
-- items_id SERIAL
-- customers_id SERIAL

-- );



CREATE TABLE purchases(



items_id INTEGER REFERENCES items (items_id)
customers_id INTEGER REFERENCES customers (customers_id) 
);

--or 

CREATE TABLE purchase (
customers_id INTEGER,
items_id INTEGER,
FOREIGN KEY (customers_id) REFERENCES customers (customers_id),
FOREIGN KEY (items_id) REFERENCES items (items_id)
);

INSERT INTO purchases (customers_id, items_id) VALUES 

INSERT INTO purchases (customers_id, items_id) VALUES (4,3,)

SELECT * FROM purchase -- not usefull odnt know how bought what need the names to have any use 



--All purchases, joining with the customers table.
SELECT * FROM purchase 
INNER JOIN customers
ON purchase.items_id = customers.customers_id;

--Purchases of the customer with the ID equal to 4.
SELECT purchase.customers_id FROM purchase INNER JOIN customers ON purchase.items_id = customers.customers_id WHERE customers.customers_id = 4

Purchases for a large desk AND a small desk
SELECT purchase.items_id FROM purchase INNER JOIN customers ON purchase.items_id = items.items_id WHERE items.items_id = 1 OR 2 

--SELECT count (*) as number_actors FROM actors WHERE number_Oscars > 0 Group my counttry 
--count(*)
-- groupe by country 
-- where number of oscatts >0 










