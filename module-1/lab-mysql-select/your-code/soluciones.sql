SELECT authors.au_id as AUTHORID, au_lname as LASTNAME, au_fname AS FIRSTNAME, title AS TITLE, publishers.pub_name AS PUBLISHER
from titleauthor
inner join authors on authors.au_id=titleauthor.au_id
inner join titles on titleauthor.title_id=titles.title_id
inner join publishers on titles.pub_id=publishers.pub_id;


  
