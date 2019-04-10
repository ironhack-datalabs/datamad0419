SET sql_mode = '';
SET GLOBAL sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));


SELECT authors.au_id as AUTHORID, au_lname as LASTNAME, au_fname AS FIRSTNAME, title AS TITLE, publishers.pub_name AS PUBLISHER, COUNT(titles.title_id) as TITLES
from titleauthor
inner join authors on authors.au_id=titleauthor.au_id
inner join titles on titleauthor.title_id=titles.title_id
inner join publishers on titles.pub_id=publishers.pub_id
GROUP BY publishers.pub_name, titleauthor.title_id;


  
