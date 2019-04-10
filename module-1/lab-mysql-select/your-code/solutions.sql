-- CHALLENGE 1
SELECT 
	authors.au_id AS "AUTHOR ID", 
	authors.au_lname AS "LAST NAME", 
	authors.au_fname AS "FIRST NAME" ,
	titles.title AS "TITLE" , 
	publishers.pub_name AS PUBLISHER
	FROM authors
	INNER JOIN titleauthor ON titleauthor.au_id = authors.au_id
	INNER JOIN titles ON titles.title_id = titleauthor.title_id
	INNER JOIN publishers ON publishers.pub_id = titles.pub_id
;

-- CHALLENGE 2
-- Me daba un error 1055, buscando info encontré que era tema de configuración
-- Solucionando añadiendo las 2 siguientes lineas.
SET sql_mode = '';
SET GLOBAL sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));

SELECT 
	authors.au_id AS "AUTHOR ID", 
	authors.au_lname AS "LAST NAME", 
	authors.au_fname AS "FIRST NAME" ,
	publishers.pub_name AS "PUBLISHER",
    COUNT(titles.title) AS "TITLE COUNT"
	FROM authors
	INNER JOIN titleauthor ON titleauthor.au_id = authors.au_id
	INNER JOIN titles ON titles.title_id = titleauthor.title_id
	INNER JOIN publishers ON publishers.pub_id = titles.pub_id
    GROUP BY titles.title
;

-- CHALLENGE 3
