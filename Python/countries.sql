-- Question 1
SELECT countries.name, languages.language, languages.percentage
FROM countries 
JOIN languages ON countries.id = languages.country_id
WHERE languages.language = 'Slovene'
ORDER BY languages.percentage DESC;
-- Question 2
SELECT countries.name, COUNT(cities.id) as num_cities
FROM countries
JOIN cities ON countries.id = cities.country_id
GROUP BY countries.name
ORDER BY num_cities DESC;
-- Question 3
SELECT cities.name, cities.population
FROM countries
JOIN cities ON countries.id = cities.country_id
WHERE countries.name = 'Mexico' AND cities.population > 500000
ORDER BY cities.population DESC;
-- Question 4
SELECT countries.name, languages.language, languages.percentage
FROM countries
JOIN languages ON countries.id = languages.country_id
WHERE languages.percentage > 89
ORDER BY languages.percentage DESC;
-- Question 5
SELECT name, surface_area, population 
FROM countries
WHERE surface_area < 501 AND population > 100000;
-- Question 6 
SELECT name, government_form, capital, life_expectancy 
FROM countries
WHERE government_form = 'Constitutional Monarchy' AND capital > 200 AND life_expectancy > 75;
-- Question 7 
SELECT countries.name, cities.name, cities.district, cities.population
FROM countries
JOIN cities ON countries.id = cities.country_id
WHERE cities.district = 'Buenos Aires' AND cities.population > 500000;
-- Question 8 
SELECT region, COUNT(countries.id) as num_countries
FROM countries
GROUP BY countries.region
ORDER BY num_countries DESC;
