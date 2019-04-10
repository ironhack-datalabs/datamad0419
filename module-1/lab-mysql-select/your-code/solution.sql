
-- Apartado 1

SELECT authors.au_id AS "AUTHOR ID", au_lname AS "LAST NAME", au_fname AS "FIRST NAME", title AS TITLE, publishers.pub_name AS PUBLISHER, 
	FROM titleauthor
	INNER JOIN authors ON authors.au_id=titleauthor.au_id
	INNER JOIN titles ON titleauthor.title_id=titles.title_id
	INNER JOIN publishers ON titles.pub_id=publishers.pub_id;


-- Apartado 2

SELECT authors.au_id AS "AUTHOR ID", au_lname AS "LAST NAME", au_fname AS "FIRST NAME", title AS TITLE, publishers.pub_name AS PUBLISHER, 
COUNT(titles.title_id) AS "TITLE COUNT"
	FROM titleauthor
	INNER JOIN authors ON authors.au_id=titleauthor.au_id
	INNER JOIN titles ON titleauthor.title_id=titles.title_id
	INNER JOIN publishers ON titles.pub_id=publishers.pub_id
	GROUP BY authors.au_lname, publishers.pub_name; 


-- Apartado 3

SELECT authors.au_id AS "AUTHOR ID", authors.au_lname AS "LAST NAME", authors.au_fname AS "FIRST NAME", SUM(sales.qty) AS TOTAL
	FROM titles
	INNER JOIN titleauthor ON titles.title_id=titleauthor.title_id
	INNER JOIN authors ON authors.au_id=titleauthor.au_id
	INNER JOIN sales ON sales.title_id=titles.title_id
	GROUP BY authors.au_id
    	ORDER BY SUM(sales.qty) DESC
    	LIMIT 3;


-- Apartado 4

SELECT authors.au_id AS "AUTHOR ID", authors.au_lname AS "LAST NAME", authors.au_fname AS "FIRST NAME", SUM(sales.qty) AS TOTAL
	FROM titles
	RIGHT JOIN sales ON sales.title_id=titles.title_id
    RIGHT JOIN titleauthor ON titles.title_id=titleauthor.title_id
	RIGHT JOIN authors ON authors.au_id=titleauthor.au_id
	GROUP BY authors.au_id
    	ORDER BY SUM(sales.qty) DESC;
