USE Sakila;
-- Question 1 
SELECT customer.first_name, customer.last_name, customer.email, address.address, address.address2, address.postal_code
FROM customer 
JOIN address ON customer.address_id = address.address_id
WHERE city_id = 312;
-- Question 2 
SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name
FROM film
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON film_category.category_id = category.category_id
WHERE category.name = 'Comedy';
-- Question 3 
SELECT actor.actor_id, actor.first_name, actor.last_name, film.title, film.description, film.release_year
FROM film 
JOIN film_actor ON film.film_id = film_actor.film_id
JOIN actor ON film_actor.actor_id = actor.actor_id
WHERE actor.actor_id = 5;
-- Question 4 
SELECT customer.first_name, customer.last_name, customer.email, address.address
FROM customer
JOIN address ON customer.address_id = address.address_id
JOIN city ON address.city_id = city.city_id
WHERE customer.store_id = 1 AND city.city_id IN (1, 42, 312, 459);
-- Question 5
SELECT title, description, release_year, rating, special_features
FROM film 
JOIN film_actor ON film.film_id = film_actor.film_id
JOIN actor ON film_actor.actor_id = actor.actor_id
WHERE actor.actor_id = 15 AND film.rating = 'G' AND film.special_features LIKE '%behind the scenes%';
-- Question 6
SELECT film.film_id, film.title, actor.actor_id, actor.first_name, actor.last_name
FROM film 
JOIN film_actor ON film.film_id = film_actor.film_id
JOIN actor ON film_actor.actor_id = actor.actor_id
WHERE film.film_id = 369;
-- Question 7 
SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name
FROM film
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON film_category.category_id = category.category_id
WHERE category.name = 'DRAMA' AND film.rental_rate = 2.99;
-- Question 8 
SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name, actor.first_name, actor.last_name
FROM film 
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON film_category.category_id = category.category_id
JOIN film_actor ON film.film_id = film_actor.film_id
JOIN actor ON film_actor.actor_id = actor.actor_id
WHERE category.name = 'Action' AND actor.first_name = 'Sandra' AND actor.last_name = 'Kilmer';