

-- -----------#1---------------------------------
-- 
-- ------------------------------------------------



select countries.name, languages.language
from countries, languages

where countries.id = languages.country_id
 
and languages.language ="Slovene"; 



-- -----------#2---------------------------------
-- 
-- ----------------------------------------------



select countries.name,  count(cities.id)

from countries 

join cities on cities.country_id = countries.id

group by country_id



-- -----------#3---------------------------------
-- 
-- ----------------------------------------------




select countries.name, cities.name, cities.population

from cities

join countries on countries.id = cities.country_id

Where countries.name = "Mexico"

And cities.population > 500000
 
order by cities.population desc

-- -----------#4---------------------------------
-- 
-- ----------------------------------------------



select countries.name, languages.language, languages.percentage

from countries

join languages on countries.id = languages.country_id

where languages.percentage > 89


-- -----------#5---------------------------------
-- 
-- ----------------------------------------------




select countries.name, countries.surface_area, countries.population

from countries

where surface_area <501

and countries.population > 100000



-- -----------#6---------------------------------
-- 
-- ----------------------------------------------



select countries.name, countries.surface_area, countries.population

from countries

where government_form = "Constitutional Monarchy"

and capital > 200

and life_expectancy > 75



-- ------------#7--------------------------------
-- 
-- ----------------------------------------------



select countries.name, cities.name, cities.district, cities.population
from countries

join cities on countries.id = cities.country_id

where countries.name = "Argentina"

and cities.district = "Buenos Aires"

and countries.population > 500000

-- -----------#8---------------------------------
-- 
-- ----------------------------------------------



select countries.region, count(countries.id)

from countries

group by countries.region

