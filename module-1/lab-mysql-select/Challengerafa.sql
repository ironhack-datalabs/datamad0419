-- challenge 1

SELECT authors.au_id, authors.au_lname, authors.au_fname, titles.title, publishers.pub_name
FROM titles
INNER JOIN publishers ON titles.pub_id = publishers.pub_id
INNER JOIN titleauthor ON titles.title_id = titleauthor.title_id 
INNER JOIN authors ON titleauthor.au_id = authors.au_id;

-- challenge 2

SELECT authors.au_id, authors.au_lname, authors.au_fname, publishers.pub_name,
	COUNT(titles.title_id) AS Titles
	FROM titles
	INNER JOIN publishers ON titles.pub_id = publishers.pub_id
	INNER JOIN titleauthor ON titles.title_id = titleauthor.title_id 
	INNER JOIN authors ON titleauthor.au_id = authors.au_id
	GROUP BY authors.au_id, publishers.pub_name
    ORDER BY COUNT(titles.title_id) DESC;
    
    -- challenge 3
    
    SELECT authors.au_id, authors.au_lname, authors.au_fname, sales.qty,
	SUM(sales.qty) as Total
	FROM titles
	INNER JOIN sales ON titles.title_id = sales.title_id
	INNER JOIN titleauthor ON titles.title_id = titleauthor.title_id 
	INNER JOIN authors ON titleauthor.au_id = authors.au_id
    GROUP BY authors.au_id
    ORDER BY SUM(sales.qty) DESC
    LIMIT 3;
    
    -- challenge 4
    
    SELECT authors.au_id, authors.au_lname, authors.au_fname,
	SUM(sales.qty) as Total
	FROM titles
	RIGHT JOIN sales ON titles.title_id = sales.title_id
	RIGHT JOIN titleauthor ON titles.title_id = titleauthor.title_id 
	RIGHT JOIN authors ON titleauthor.au_id = authors.au_id
    GROUP BY authors.au_id
    ORDER BY SUM(sales.qty) DESC