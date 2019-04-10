SELECT authors.au_id AS "AUTHOR ID", authors.au_lname AS "LAST NAME", authors.au_fname AS "FIRST NAME", SUM(sales.qty) AS TOTAL
    FROM titles
    INNER JOIN titleauthor ON titles.title_id=titleauthor.title_id
    INNER JOIN authors ON authors.au_id=titleauthor.au_id
    INNER JOIN sales ON sales.title_id=titles.title_id
    GROUP BY authors.au_id
    ORDER BY SUM(sales.qty) DESC
    LIMIT 3;


  
