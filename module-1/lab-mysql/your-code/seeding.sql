
-- IMPORTANT: the IDs of the different tables are auto incremental, starting from 1 if not specified in the inserts.
-- As these inserts do not specifie the IDs, the rows of these tables start from 1 instead of 0, as seen in the Github README.

-- We first start seeding cars table. The car_ID is not included as is auto incremental in case of not provided
INSERT INTO cars (VIN, manufacturer, model, year, color) VALUES ('3K096I98581DHSNUP', 'Volkswagen', 'Tiguan', 2019, 'Blue');
INSERT INTO cars (VIN, manufacturer, model, year, color) VALUES ('ZM8G7BEUQZ97IH46V', 'Peugeot', 'Rifter', 2019, 'Red');
INSERT INTO cars (VIN, manufacturer, model, year, color) VALUES ('RKXVNNIHLVVZOUB4M', 'Ford', 'Fusion', 2018, 'White');
INSERT INTO cars (VIN, manufacturer, model, year, color) VALUES ('HKNDGS7CU31E9Z7JW', 'Toyota', 'RAV4', 2018, 'Silver');
INSERT INTO cars (VIN, manufacturer, model, year, color) VALUES ('DAM41UDN3CHU2WVF6', 'Volvo', 'V60', 2019, 'Gray');
INSERT INTO cars (VIN, manufacturer, model, year, color) VALUES ('DAM41UDN3CHU2WVF6', 'Volvo', 'V60 Cross Country', 2019, 'Gray');

-- Seeding customers (the customer_ID is used as PK instead of ID)
INSERT INTO customers (customer_id_number, name, phone, email, address, city, state, country, postal_code) VALUES ('10001',	'Pablo Picasso',	'+34 636 17 63 82', '-', 'Paseo de la Chopera, 14',	'Madrid',	'Madrid',	'Spain',	'28045');
INSERT INTO customers (customer_id_number, name, phone, email, address, city, state, country, postal_code) VALUES ('20001',	'Abraham Lincoln',	'+1 305 907 7086',	'-', '120 SW 8th St',	'Miami',	'Florida',	'United States',	'33130');
INSERT INTO customers (customer_id_number, name, phone, email, address, city, state, country, postal_code) VALUES ('30001',	'Napoléon Bonaparte',	'+33 1 79 75 40 00',	'-',	'40 Rue du Colisée',	'Paris',	'Île-de-France',	'France',	'75008');

-- Seeding salespersons (the staff_ID is used as PK instead of ID)
INSERT INTO salespersons (staff_id_number, name, store) VALUES ('00001',	'Petey Cruiser',	'Madrid');
INSERT INTO salespersons (staff_id_number, name, store) VALUES ('00002',	'Anna Sthesia',	'Barcelona');
INSERT INTO salespersons (staff_id_number, name, store) VALUES ('00003',	'Paul Molive',	'Berlin');
INSERT INTO salespersons (staff_id_number, name, store) VALUES ('00004',	'Gail Forcewind',	'Paris');
INSERT INTO salespersons (staff_id_number, name, store) VALUES ('00005',	'Paige Turner',	'Mimia');
INSERT INTO salespersons (staff_id_number, name, store) VALUES ('00006',	'Bob Frapples',	'Mexico City');
INSERT INTO salespersons (staff_id_number, name, store) VALUES ('00007',	'Walter Melon',	'Amsterdam');
INSERT INTO salespersons (staff_id_number, name, store) VALUES ('00008',	'Shonda Leer',	'São Paulo');

-- Seeding invoices
INSERT INTO invoices (invoice_number, emission_date, cars_car_ID, salespersons_staff_ID) VALUES ('852399038',	'2018-08-22', 1,	4);
INSERT INTO invoices (invoice_number, emission_date, cars_car_ID, salespersons_staff_ID) VALUES ('731166526',	'2018-12-31',	4,	6);
INSERT INTO invoices (invoice_number, emission_date, cars_car_ID, salespersons_staff_ID) VALUES ('731166526',	'2018-12-31',	3,	7);

--Seeding invoices-customers to create the relation between previous invoices with the specified customers
