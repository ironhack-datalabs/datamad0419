-- CHALLENGE 1

SELECT authors.au_id AS 'AUTHOR ID', authors.au_lname AS 'LAST NAME', authors.au_fname AS 'FIRST NAME',
titles.title as TITLE, publishers.pub_name as PUBLISHER
FROM titleauthor INNER JOIN authors ON titleauthor.au_id = authors.au_id
INNER JOIN titles ON titleauthor.title_id = titles.title_id
INNER JOIN publishers ON titles.pub_id = publishers.pub_id;
ORDER BY authors.au_id