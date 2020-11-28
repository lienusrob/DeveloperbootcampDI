Exercise 1 : Dvd Rental
--Get a list of all film languages
SELECT * FROM language
--Get a list of all films joined with their languages – select only the film title, description, and language name.
 --Try your query with different joins:
-- Get all films, even if they don’t have languages
-- Get all languages, even if there are no films in those languages. Which languages are these?

SELECT film.title, film.description, language.name
FROM film
INNER JOIN language
ON film.language_id = language.language_id

SELECT film.title, film.description, language.name
FROM film
LEFT JOIN language
ON film.language_id = language.language_id

SELECT film.title, film.description, language.name
FROM film
LEFT OUTER JOIN  language
ON film.language_id = language.language_id
--lastt one not tcorrect but almost

-- Create a new table called customer_review, to contain data about film reviews that customers will make.
-- Think about the DELETE constraint: if a film is deleted, it’s review should be automatically deleted
-- It should have the following columns:
-- review_id – a primary key, non null, auto-increment
-- film_id – references the film table. The film that is being reviewed.
-- language_id – references the language table. What language the review is in.
-- title – the title of the review
-- score – the rating of the review (1-10)
-- review_text – the text of the review. No limit on the length.
-- last_update – when the review was last updated.

-- edited question  
-- My suggestion would be to make a second toy table called 
-- film2 which an id and a name, insert a bit of data, and connect the review table to that table.
-- Then perform the delete in order to see the cascade effect.
CREATE TABLE film2(
film2_id SERIAL PRIMARY KEY,
name2 VARCHAR(250)
);


INSERT INTO film2 (name2)
VALUES('hello');


INSERT INTO film2 (name2 )
VALUES('YES' );


CREATE TABLE  customer_review(
film_review_id SERIAL PRIMARY KEY,
film_review VARCHAR (600),
CONSTRAINT film_id
FOREIGN KEY (film_review_id) REFERENCES film (film_id)
ON DELETE CASCADE
); 



Add 2 movie reviews. Make sure you link them to valid objects in the other tables.

INSERT INTO customer_review(film_review)

VALUES ('hello fim is stunning');


INSERT INTO customer_review(film_review)
VALUES ('YES fim is stunning');
--delete a movie and checkifi its delted in the review table as well it worked.
DELETE FROM film2 WHERE film2_id=1

Exercise 2 : Dvd Rental

1. Use UPDATE to change the language of some films. Make sure that you use valid languages…

UPDATE film
SET language_id = 2
WHERE
film_id=1;

2. Which foreign keys (references) are defined for the customer table? 
How does this affect the way in which we INSERT into the customer table?
-- i dont know what i am supposed to do. 

3. DROP TABLE customer_review-- simple step. since it is a child table not a parent table 
--it is independent and does not effect any other tabels 


4. 
Find out how many rentals are still outstanding. (ie. have not been returned to the store yet)
SELECT COUNT( inventory_id ) as DVD_OnRent
FROM rental
WHERE return_date IS NULL;

5. Mark the 30 most expensive movies which are outstanding (ie. have not been returned to the store yet)

i dont know how to do this 
SELECT COUNT( inventory_id ) as DVD_OnRent
FROM rental
WHERE return_date IS NULL;
LEFT JOIn
SELECT * FROM public.payment
ORDER BY amount DESC 

6. 
