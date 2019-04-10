-- CHALLENGE 1

SELECT authors.au_id AS 'AUTHOR ID', authors.au_lname AS 'LAST NAME', authors.au_fname AS 'FIRST NAME',
titles.title as TITLE, publishers.pub_name as PUBLISHER
FROM titleauthor INNER JOIN authors ON titleauthor.au_id = authors.au_id
INNER JOIN titles ON titleauthor.title_id = titles.title_id
INNER JOIN publishers ON titles.pub_id = publishers.pub_id;
ORDER BY authors.au_id

-- CHALLENGE 2

SELECT authors.au_id AS 'AUTHOR ID', authors.au_lname AS 'LAST NAME', authors.au_fname AS 'FIRST NAME',
publishers.pub_name as PUBLISHER, COUNT(titles.title) as 'TITLE COUNT'
FROM titleauthor INNER JOIN authors ON titleauthor.au_id = authors.au_id
INNER JOIN titles ON titleauthor.title_id = titles.title_id
INNER JOIN publishers ON titles.pub_id = publishers.pub_id
GROUP BY authors.au_id, publishers.pub_name
ORDER BY authors.au_id DESC

-- CHALLENGE 3

SELECT authors.au_id AS 'AUTHOR ID', authors.au_lname AS 'LAST NAME', authors.au_fname AS 'FIRST NAME',
SUM(sales.qty) as TOTAL
FROM titleauthor
INNER JOIN authors ON titleauthor.au_id = authors.au_id
INNER JOIN sales ON titleauthor.title_id = sales.title_id
GROUP BY authors.au_id
ORDER BY TOTAL DESC
LIMIT 3;

-- CHALLENGE 4

SELECT authors.au_id AS 'AUTHOR ID', authors.au_lname AS 'LAST NAME', authors.au_fname AS 'FIRST NAME', COALESCE(SUM(sales.qty), 0) AS TOTAL FROM authors
LEFT JOIN titleauthor
ON authors.au_id = titleauthor.au_id
LEFT JOIN sales
ON titleauthor.title_id = sales.title_id
GROUP BY authors.au_id
ORDER BY TOTAL DESC
LIMIT 23;
