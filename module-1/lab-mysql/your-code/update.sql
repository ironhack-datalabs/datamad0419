-- Correction: Miami instead of Mimia for Paige
UPDATE salespersons SET store = 'Miami' WHERE (`staff_ID` = '5');

-- The mails of the customers are now included
UPDATE customers SET email = 'ppicaso@gmail.com' WHERE (`customer_ID` = '1');
UPDATE customers SET email = 'lincoln@us.gov' WHERE (`customer_ID` = '2');
UPDATE customers SET email = 'hello@napoleon.me' WHERE (`customer_ID` = '3');
