SELECT authors.au_id, authors.au_lname, authors.au_fname, titleauthor.title_id, titles.title, titles.pub_id, publishers.name FROM authors
INNER JOIN titleauthor
ON authors.au_id = titleauthor.au_id 
INNER JOIN titles
ON titleauthor.title_id  = titles.title_id
INNER JOIN publishers
ON titles.pub_id  = publishers.pub_id;