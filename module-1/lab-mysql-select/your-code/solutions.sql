--CHALLENGE1
SELECT authors.au_id AS "AUTHOR ID", authors.au_fname "AS FIRST NAME", authors.au_lname AS "LAST NAME", titles.title AS "TITLE", pub_name AS "PUBLISHER"
FROM authors
INNER JOIN titleauthor ON authors.au_id = titleauthor.au_id
INNER JOIN titles ON titles.title_id = titleauthor.title_id
INNER JOIN publishers ON titles.pub_id = publishers.pub_id;

--CHALLENGE2
SELECT authors.au_id AS 'AUTHOR ID', authors.au_fname AS 'FIRST NAME', 
authors.au_lname AS 'LAST NAME', 
publishers.pub_name AS 'PUBLISHER',
COUNT(titles.title) AS 'TITLE COUNT'
FROM authors
INNER JOIN titleauthor ON authors.au_id = titleauthor.au_id
INNER JOIN titles ON titles.title_id = titleauthor.title_id
INNER JOIN publishers ON titles.pub_id = publishers.pub_id
GROUP BY authors.au_id, publishers.pub_name;

--Challenge3 (NO TERMINADO)
SELECT authors.au_id AS 'AUTHOR ID', authors.au_fname AS 'FIRST NAME', 
authors.au_lname AS 'LAST NAME', 
COUNT(sales.qty) AS 'TOTAL'
FROM authors
INNER JOIN titleauthor ON authors.au_id = titleauthor.au_id
INNER JOIN titles ON titles.title_id = titleauthor.title_id
INNER JOIN publishers ON titles.pub_id = publishers.pub_id
INNER JOIN sales ON titles.title_id = sales.title_id
GROUP BY authors.au_id
ORDER BY sum();