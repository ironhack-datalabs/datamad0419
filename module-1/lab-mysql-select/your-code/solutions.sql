# Challenge 1
SELECT authors.au_id AS "Author's ID", authors.au_fname AS "Name", authors.au_lname AS "Surname", publishers.pub_name AS "Publisher", titles.title AS "Book Title"
	FROM titles 
    INNER JOIN publishers ON titles.pub_id = publishers.pub_id
    INNER JOIN titleauthor ON titles.title_id = titleauthor.title_id
    INNER JOIN authors ON titleauthor.au_id = authors.au_id;

#Challenge 2
SELECT  authors.au_id AS "Author's ID", authors.au_fname AS "Name", authors.au_lname AS "Surname",
	publishers.pub_name AS "Publisher",
	COUNT(authors.au_id) AS "Title Count"
	FROM titles 
    INNER JOIN publishers ON titles.pub_id = publishers.pub_id
    INNER JOIN titleauthor ON titles.title_id = titleauthor.title_id
    INNER JOIN authors ON titleauthor.au_id = authors.au_id
    GROUP BY authors.au_id;
    
#Challenge 3
SELECT  authors.au_id AS "Author's ID", authors.au_fname AS "Name", authors.au_lname AS "Surname",
	sales.qty AS "Total",
    SUM(sales.qty)
	FROM titles 
    INNER JOIN publishers ON titles.pub_id = publishers.pub_id
    INNER JOIN titleauthor ON titles.title_id = titleauthor.title_id
    INNER JOIN authors ON titleauthor.au_id = authors.au_id
    INNER JOIN sales ON titles.title_id = sales.title_id
    GROUP BY (authors.au_id) 
    ORDER BY SUM(sales.qty) DESC LIMIT 3;
