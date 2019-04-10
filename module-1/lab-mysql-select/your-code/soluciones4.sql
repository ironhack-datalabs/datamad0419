SELECT authors.au_id AS "AUTHOR ID", authors.au_lname AS "LAST NAME", authors.au_fname AS "FIRST NAME", 
    SUM(sales.qty) AS TOTAL
    FROM titles
    RIGHT JOIN sales ON sales.title_id=titles.title_id
    RIGHT JOIN titleauthor ON titles.title_id=titleauthor.title_id
    RIGHT JOIN authors ON authors.au_id=titleauthor.au_id
    GROUP BY authors.au_id
    ORDER BY SUM(sales.qty) DESC
    


  
