-- CHALLENGE 1 v1--

SELECT authors.au_id AS 'AUTHOR ID',
	   authors.au_lname AS 'LAST NAME',
       authors.au_fname AS 'FIRST NAME',
       titles.title AS TITLE,
       (SELECT publishers.pub_name FROM publishers WHERE pub_id = titles.pub_id) AS PUBLISHERS
	FROM titleauthor
    INNER JOIN titles ON (titles.title_id = titleauthor.title_id)
    INNER JOIN authors ON (authors.au_id = titleauthor.au_id);
    
-- CHALLENGE 1 v2--

SELECT authors.au_id AS 'AUTHOR ID',
	   authors.au_lname AS 'LAST NAME',
       authors.au_fname AS 'FIRST NAME',
       titles.title AS TITLE,
       publishers.pub_name AS PUBLISHERS
	FROM titleauthor
    INNER JOIN authors ON (authors.au_id = titleauthor.au_id)
    INNER JOIN titles ON (titles.title_id = titleauthor.title_id)
    INNER JOIN publishers ON (publishers.pub_id = titles.pub_id);
    
-- CHALLENGE 2--

SELECT authors.au_id AS 'AUTHOR ID',
	   authors.au_lname AS 'LAST NAME',
       authors.au_fname AS 'FIRST NAME',
       publishers.pub_name AS PUBLISHERS,
       COUNT(titles.title_id) AS 'COUNT TITLES'
	FROM titleauthor
    INNER JOIN authors ON (authors.au_id = titleauthor.au_id)
    INNER JOIN titles ON (titles.title_id = titleauthor.title_id)
    INNER JOIN publishers ON (publishers.pub_id = titles.pub_id)
    GROUP BY authors.au_id, publishers.pub_name
    ORDER BY authors.au_id DESC;
    
-- CHALLENGE 3--
-- HE utilizado la tabla ventas --

SELECT authors.au_id AS 'AUTHOR ID',
	   authors.au_lname AS 'LAST NAME',
       authors.au_fname AS 'FIRST NAME',
       SUM(sales.qty) AS TOTAL
	FROM titleauthor
    INNER JOIN authors ON (authors.au_id = titleauthor.au_id)
    INNER JOIN titles ON (titles.title_id = titleauthor.title_id)
    INNER JOIN sales ON (sales.title_id = titles.title_id)
    GROUP BY authors.au_id
    ORDER BY TOTAL DESC LIMIT 3;
    
-- CHALLENGE 4 --
SELECT authors.au_id AS 'AUTHOR ID',
	   authors.au_lname AS 'LAST NAME',
       authors.au_fname AS 'FIRST NAME',
       IFNULL(SUM(sales.qty), 0) AS TOTAL 
	FROM titleauthor
	RIGHT JOIN authors ON (authors.au_id = titleauthor.au_id)
	LEFT JOIN titles ON (titles.title_id = titleauthor.title_id)
    LEFT JOIN sales ON (sales.title_id = titles.title_id)
    GROUP BY authors.au_id
    ORDER BY TOTAL DESC;
    
-- BONUS --
-- He utilizado los datos de las ventas/año y advance de titles, obteniendo la parte para cada --
-- autor por title y después agrupando la suma por autor para obtener los que han obtenido más beneficios --

SELECT authors.au_id AS 'AUTHOR ID',
	   authors.au_lname AS 'LAST NAME',
       authors.au_fname AS 'FIRST NAME',
       SUM((titles.advance * titleauthor.royaltyper / 100) + ((titles.price * titles.ytd_sales) * titleauthor.royaltyper / 100)) AS TOTAL
	FROM titleauthor
	INNER JOIN authors ON (authors.au_id = titleauthor.au_id)
	INNER JOIN titles ON (titles.title_id = titleauthor.title_id)
    GROUP BY authors.au_id
    ORDER BY TOTAL DESC
    LIMIT 3;

    