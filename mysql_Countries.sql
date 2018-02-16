select countries.name, languages.language
from countries, languages
where countries.id = languages.country_id
and languages.language ="Slovene"; 

-- --------------------------------------------
-- --------------------------------------------
