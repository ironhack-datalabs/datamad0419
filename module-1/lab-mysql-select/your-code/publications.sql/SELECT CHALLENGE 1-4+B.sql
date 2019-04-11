-- BONUS
SELECT authors.au_id AS 'AUTHOR ID', authors.au_lname AS 'LAST NAME', authors.au_fname AS 'FIRST NAME',
IFNULL(SUM(titles.advance + titles.ytd_sales * titles.price * titles.royalty/100), 0) AS PROFIT FROM authors
LEFT JOIN titleauthor
ON authors.au_id = titleauthor.au_id
LEFT JOIN titles
ON titleauthor.title_id = titles.title_id
GROUP BY authors.au_id
ORDER BY PROFIT DESC
LIMIT 23;