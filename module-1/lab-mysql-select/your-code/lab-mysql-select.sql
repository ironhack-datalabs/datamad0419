select authors.au_id as "AUTHOR ID",
	au_lname AS "lAST NAME" ,
    au_fname AS "FIRST NAME",
    title AS "TITLE",
    publishers.pub_name AS "PUBLISHER"
	from titleauthor
	inner join authors on authors.au_id = titleauthor.au_id
    inner join titles on titleauthor.title_id = titles.title_id
    inner join publishers on publishers.pub_id = titles.pub_id;
    
-- ejercicio 2
select authors.au_id as "AUTHOR ID",
	au_lname AS "LAST NAME" ,
	au_fname AS "FIRST NAME",
    title AS "TITLE",
    publishers.pub_name AS "PUBLISHER",
    COUNT(titles.title) AS "TITLE COUNT"
		from titleauthor
			inner join authors on authors.au_id = titleauthor.au_id
			inner join titles on titleauthor.title_id = titles.title_id
			inner join publishers on publishers.pub_id = titles.pub_id
    GROUP BY (titles.title_id);

-- ejercicio 3
select authors.au_id as "AUTHOR ID",
	authors.au_lname AS "LAST NAME" ,
	authors.au_fname AS "FIRST NAME",
    sum(sales.qty) as "Total"
		from titleauthor
			inner join authors on authors.au_id = titleauthor.au_id
			inner join titles on titleauthor.title_id = titles.title_id
			inner join publishers on publishers.pub_id = titles.pub_id
            inner join sales on sales.title_id= titles.title_id
            GROUP BY (authors.au_id)
            order by sum(sales.qty) desc
            limit 3;

-- ejercicio 4

select authors.au_id as "AUTHOR ID",
	authors.au_lname AS "LAST NAME" ,
	authors.au_fname AS "FIRST NAME",
    ifnull(sum(sales.qty),0) as "Total"
		from titleauthor
			right join authors on authors.au_id = titleauthor.au_id
			left join titles on titleauthor.title_id = titles.title_id
			left join publishers on publishers.pub_id = titles.pub_id
            left join sales on sales.title_id= titles.title_id
            GROUP BY (authors.au_id)
            order by sum(sales.qty) desc
            
