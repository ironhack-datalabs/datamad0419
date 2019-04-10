#SOLUTION
#Challenge 1 and 2 
SELECT authors.au_id, authors.au_lname, authors.au_fname, titles.title, publishers.pub_name,
		COUNT(titles.title)
		FROM titles
        
		INNER JOIN publishers
		ON titles.pub_id = publishers.pub_id
		INNER JOIN titleauthor
		ON titles.title_id=titleauthor.title_id
	INNER JOIN authors
	ON titleauthor.au_id=authors.au_id
    GROUP BY authors.au_lname, publishers.pub_name; 
#Challenge 3   
SELECT authors.au_id, authors.au_lname, authors.au_fname, 
	SUM(sales.qty) AS TOTAL
	FROM titles
	INNER JOIN titleauthor
	ON titles.title_id=titleauthor.title_id
	INNER JOIN authors
	ON titleauthor.au_id=authors.au_id
	INNER JOIN sales 
    ON titles.title_id=sales.title_id
    GROUP BY authors.au_id
    ORDER BY SUM(sales.qty) DESC
    LIMIT 3;
#Challenge 4
SELECT authors.au_id, authors.au_lname, authors.au_fname,
    SUM(sales.qty) AS TOTAL 
	FROM titles
	RIGHT JOIN sales 
    ON titles.title_id=sales.title_id
    RIGHT JOIN titleauthor
	ON titles.title_id=titleauthor.title_id
	RIGHT JOIN authors
	ON titleauthor.au_id=authors.au_id
    GROUP BY authors.au_id
    ORDER BY SUM(sales.qty) DESC;
	