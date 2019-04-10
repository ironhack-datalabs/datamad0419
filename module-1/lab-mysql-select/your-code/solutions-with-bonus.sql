-- Challenge 1

SELECT authors.au_id AS "Author ID", authors.au_lname AS "Last name", authors.au_fname AS "First name", titles.title as "Title", publishers.pub_name "Publisher"
	FROM authors
	INNER JOIN titleauthor ON authors.au_id = titleauthor.au_id
	INNER JOIN titles ON titleauthor.title_id = titles.title_id
	INNER JOIN publishers ON titles.pub_id = publishers.pub_id;

-- Challenge 2

SELECT authors.au_id AS "Author ID", authors.au_lname AS "Last name", authors.au_fname AS "First name", publishers.pub_name AS "Publisher", 
COUNT(titles.title_id) 
	FROM authors
	INNER JOIN titleauthor ON authors.au_id = titleauthor.au_id
	INNER JOIN titles ON titleauthor.title_id = titles.title_id
	INNER JOIN publishers ON titles.pub_id = publishers.pub_id
    GROUP BY authors.au_id, publishers.pub_id
	ORDER BY COUNT(titles.title_id) DESC;

-- Challenge 3

SELECT authors.au_id AS "Author ID", authors.au_lname AS "Last name", authors.au_fname AS "First name", SUM(sales.qty) AS "Total sales"
	FROM authors
	INNER JOIN titleauthor ON authors.au_id = titleauthor.au_id
	INNER JOIN titles ON titleauthor.title_id = titles.title_id
	INNER JOIN sales ON titles.title_id = sales.title_id
    GROUP BY authors.au_id
    ORDER BY SUM(sales.qty) DESC
    LIMIT 3;
    
-- Challenge 4

SELECT authors.au_id AS "Author ID", authors.au_lname AS "Last name", authors.au_fname AS "First name", 
CASE WHEN SUM(sales.qty) is NULL THEN 0 ELSE SUM(sales.qty) END AS "Total sales"
	FROM authors
	LEFT JOIN titleauthor ON authors.au_id = titleauthor.au_id
	LEFT JOIN titles ON titleauthor.title_id = titles.title_id
	LEFT JOIN sales ON titles.title_id = sales.title_id
    GROUP BY authors.au_id
    ORDER BY SUM(sales.qty) DESC;

-- Bonus

SELECT authors.au_id AS "Author ID", authors.au_lname AS "Last name", authors.au_fname AS "First name", 
((sales.qty*titles.price*(titles.royalty/100)*(titleauthor.royaltyper/100))+titles.advance) AS Profits
	FROM authors
	LEFT JOIN titleauthor ON authors.au_id = titleauthor.au_id
	LEFT JOIN titles ON titleauthor.title_id = titles.title_id
	LEFT JOIN sales ON titles.title_id = sales.title_id
	GROUP BY authors.au_id
    ORDER BY Profits DESC
    LIMIT 3;
    
    
