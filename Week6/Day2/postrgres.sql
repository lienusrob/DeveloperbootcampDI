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

-or 

CREATE TABLE purchase (
customers_id INTEGER,
items_id INTEGER,
FOREIGN KEY (customers_id) REFERENCES customers (customers_id),
FOREIGN KEY (items_id) REFERENCES items (items_id)
);

INSERT INTO purchases (customers_id, items_id) VALUES 

INSERT INTO purchases (customers_id, items_id) VALUES (4,3,)

SELECT * FROM purchase -- not usefull doont know who bought what need the names to have any use 



--All purchases, joining with the customers table.
SELECT * FROM purchase 
INNER JOIN customers
ON purchase.items_id = customers.customers_id;

--Purchases of the customer with the ID equal to 4.
SELECT purchase.customers_id 
FROM purchase 
INNER JOIN customers 
ON purchase.items_id = customers.customers_id
WHERE customers.customers_id = 4

Purchases for a large desk AND a small desk
SELECT purchase.items_id 
FROM purchase 
INNER JOIN customers 
ON purchase.items_id = items.items_id 
WHERE items.items_id = 1 OR 2 

-- We will use the newly installed dvdrental database.

-- Write a query to select all the columns from the table “customer” in the database named dvdrental.

-- Write a query to display the names (first_name, last_name) using an alias named “full_name”.

-- You want to know every date where one or several accounts were created. Write a query to select the dates of creation from the “customer” table, it shouldn’t have duplicates.
SELECT * 
-- Write a query to get the details of all customers from the customer table in descending order by their first name.
SELECT* FROM customers ORDER BY first_name DESC;
-- Write a query to get the film ID, title, description, year of release and rental rate in ascending order according to their rental rate.
SELECT film_id, title, description, release_year, rental_rate FROM film ORDER BY rental_rate ASC;
-- Write a query to get the address, the district and the phone number from the customers living in the district Texas in the “address” table.
SELECT address, district, phone FROM address WHERE district = ‘Texas’;
-- Write a query to retrieve the details of the movies with the id 15 and 150.
SELECT * FROM film WHERE film_id= 15 OR film_id= 150
-- Pick your favorite movie. Write a query to see if the rental shop owns it. Write a query to get the film ID, the title, the description, the length and the rental rate from the film table for your movie title.
--Academy Dinosaur
SELECT* FROM film WHERE title= Academy Dinosaur
SELECT film_id, title, description, length, rental_rate FROM film WHERE title= 'Academy Dinosaur';
-- Didn’t find it ? Maybe you made a mistake in the name. Write a query to get the film ID, the title, the description, 
--the length and the rental rate from the “film” table for all the movies starting with the two first letters of your movie.
SELECT film_id, title, description, length, rental_rate FROM film WHERE SUBSTRING(title,1,2)= 'Ac';

SELECT film_id, title, description, length, rental_rate FROM film WHERE title LIKE ‘St%’;
-- You want to have a choice between ten propositions of movies and you want the cheapest ones. Write a query to find the 10th cheapest movies.
SELECT film_id, title, description, release_year, rental_rate FROM film ORDER BY rental_rate ASC WHERE film_id<10;
SELECT * FROM film ORDER BY replacement_cost  ASC LIMIT 10;
-- You are not satisfied with the results. Write a query to find the 10th next cheapest movies.
-- Bonus: Try to not use LIMIT.
SELECT  * FROM film  ORDER BY replacement_cost ASC LIMIT 10 OFFSET 10;

SELECT * FROM film ORDER BY replacement_cost  ASC  10 FETCH  50  ;

-- Write a query to join the data of the customer table and the payment table. 
--You want to get the amount and the date of every payment made by a customer, ordered by his id (from 1 to…).
SELECT custumer_id 
FROM Customer 
INNER JOIN payment
ON customer.customer_id=customer.customer_id 
INNER JOIN salesman c 
ON a.salesman_id=c.salesman_id;

SELECT a.ord_no,a.ord_date,a.purch_amt,
b.cust_name AS "Customer Name", b.grade, 
c.name AS "Salesman", c.commission 
FROM orders a 
INNER JOIN customer b 
ON a.customer_id=b.customer_id 
INNER JOIN salesman c 
ON a.salesman_id=c.salesman_id;


SELECT custumer_id, first_name
FROM customer
RIGHT JOIN payment
ON customer.custumer_id=payment.custumer_id;

SELECT customer.first_name, customer.last_name, payment.amount, payment.payment_date
FROM payment
INNER JOIN customer ON payment.customer_id = customer.customer_id
-- You need to check your inventory. Write a query to get all the movies which are not in the inventory.

SELECT  inventory_id  as DVD_OnRent
FROM rental
WHERE return_date IS NULL;

-- Write a query to find which city is in which country.

-- 15.Bonus :You want to be assured of the performance of your sellers. Write a query to get the customer’s id, names (first and last), the amount and the date of payment ordered by the id of the staff who sold them the dvd.

