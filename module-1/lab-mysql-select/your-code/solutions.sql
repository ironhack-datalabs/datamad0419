-- CHALLENGE 1 --

SELECT titleauthor.au_id AS 'AUTHOR ID', authors.au_lname AS 'LAST NAME', authors.au_fname AS 'FIRST NAME', titles.title AS 'TITLE', publishers.pub_name AS 'PUBLISHERS'
 FROM titles
 INNER JOIN publishers ON titles.pub_id = publishers.pub_id
 INNER JOIN titleauthor ON titles.title_id = titleauthor.title_id
 INNER JOIN authors ON titleauthor.au_id = authors.au_id

-- CHALLENGE 2 --
 
 SET sql_mode = '';
 SET GLOBAL sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));
 
SELECT titleauthor.au_id AS 'AUTHOR ID', authors.au_lname AS 'LAST NAME', authors.au_fname AS 'FIRST NAME', publishers.pub_name AS 'PUBLISHERS', 
 COUNT(titles.title_id)
 FROM titles
 INNER JOIN publishers 
 ON titles.pub_id = publishers.pub_id
 INNER JOIN titleauthor
 ON titles.title_id = titleauthor.title_id
 INNER JOIN authors
 ON titleauthor.au_id = authors.au_id
 GROUP BY authors.au_id, publishers.pub_name

-- CHALLENGE 3 --
 
SELECT titleauthor.au_id AS 'AUTHOR ID', authors.au_lname AS 'LAST NAME', authors.au_fname AS 'FIRST NAME',
 SUM(sales.qty) AS 'TOTAL'
 FROM titles
 INNER JOIN sales 
 ON titles.title_id = sales.title_id
 INNER JOIN titleauthor
 ON titles.title_id = titleauthor.title_id
 INNER JOIN authors
 ON titleauthor.au_id = authors.au_id
 GROUP BY titleauthor.au_id
 ORDER BY sales.qty asc
 LIMIT 3

-- CHALLENGE 4 --
 
SELECT authors.au_id AS 'AUTHOR ID', authors.au_lname AS 'LAST NAME', authors.au_fname AS 'FIRST NAME',
 SUM(sales.qty) AS 'TOTAL'
 FROM authors
 LEFT JOIN titleauthor ON authors.au_id = titleauthor.au_id
 LEFT JOIN sales ON titleauthor.title_id = sales.title_id 
 GROUP BY authors.au_id
 ORDER BY sales.qty DESC
