SELECT authors.au_id AS "Author's ID", authors.au_fname AS "Name", authors.au_lname AS "Surname", publishers.pub_name AS "Publisher", titles.title AS "Book Title"
	FROM titles 
    INNER JOIN publishers ON titles.pub_id = publishers.pub_id
    INNER JOIN titleauthor ON titles.title_id = titleauthor.title_id
    INNER JOIN authors ON titleauthor.au_id = authors.au_id;
