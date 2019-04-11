SELECT authors.au_id AS 'AUTHOR ID', authors.au_lname AS 'LAST NAME', authors.au_fname AS 'FIRST NAME', titles.title AS 'TITLE', publishers.pub_name AS 'PUBLISHER'
FROM authors, titleauthor, titles
INNER JOIN publishers
ON titles.pub_id = publishers.pub_id
