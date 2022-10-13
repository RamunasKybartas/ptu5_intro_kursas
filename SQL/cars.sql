-- platesnis where panaudojimas, between AND
SELECT * FROM cars WHERE price BETWEEN 10000 and 30000;
-- galim atikrinti ir pagal sarasa
SELECT * from cars WHERE year in (2005, 2010, 2011) ORDER by year;
-- paieska texte
select * FROM cars WHERE make like "t%";
select * FROM cars WHERE make like "%a";
select * FROM cars WHERE make like "%t%";
-- placeholderis
SELECT * FROM cars WHERE model like "__";
SELECT * FROM cars WHERE model like "X_";
SELECT * FROM cars WHERE model like "X%";
select * FROM cars WHERE make like "__n%";
-- NULL
SELECT * FROM cars WHERE color is NULL;

UPDATE cars SET color="Ugly" WHERE color is NULL;
SELECT * FROM cars WHERE color is "Ugly";
-- and, or, not salygos
SELECT * FROM cars WHERE make="Ford" AND price>40000;
select * FROM cars WHERE (price<40000 or color ="Pink") AND year > 2000;
SELECT * FROM cars WHERE color not in ("Violet", "Pink", "Yellow", "Ugly", "Turquoise", "Red", "Maroon");
SELECT * FROM cars WHERE (make = "Volvo" or make = "Ford") and price NOT BETWEEN 10000 and 50000;
-- rusiavimas
SELECT * FROM cars ORDER by year desc LIMIT 5;
SELECT * FROM cars ORDER by year desc LIMIT 5 OFFSET 5;
select * FROM cars ORDER by make;
-- nekreipti demesio i raidziu dydi
select * FROM cars WHERE make="toyota" COLLATE nocase;
-- rezultatu manipuliavimas su || operatorium
SELECT "Gamintojas: " || make as gamintojas, model as modelis FROM cars LIMIT 10;
SELECT make, model, price, round(price/3.4528, 2) as kaina_eur FROM cars;
SELECT make || " " || model || " , " || year as car_model_year FROM cars ORDER by year;
-- amziaus skaiciavimas
SELECT make, model, 2022 - year as age from cars order by age;
SELECT make, model, price, round(price/1.18) as price_ex_vat from cars order by price_ex_vat;
-- teisingas grupavimas
--avg()
--min() max()
--count()
--sum()
SELECT sum(price) from cars;
select make, sum(price) from cars GROUP by make;
SELECT make, avg(year) FROM cars group by make;
SELECT make, avg(year), count(*) FROM cars GROUP by make HAVING count(*) > 1;
SELECT make, avg(price), count(*) FROM cars GROUP by make HAVING count(*) > 1;
select min(price), max(price), avg(price) from cars;
SELECT max(price), make, model from cars;
select color, max(price), make, model, count(*) FROM cars GROUP by color order by price desc;
select color, min(price), make, model, count(*) FROM cars GROUP by color order by price desc;
select color, round(avg(price)), make, model, count(*) FROM cars GROUP by color order by price desc;