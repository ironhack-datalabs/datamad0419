USE mydb;
INSERT INTO car (idcar, vin_number, manufacturer, model, year, color)
VALUES (0, 'A0001', 'Volkswagen', 'Tiguan', 2012, 'Red');
INSERT INTO invoice (invoice_number, date, car_idcar) 
VALUES (001, '2019/03/05', 0);
INSERT INTO salesperson (idsalesperson, staff_id, name, store, invoice_invoice_number)
VALUES (0, 0, 'Enrique Torres', 'Madrid Sol', 001);
INSERT INTO customer (idcustomer, vat_number, name, phone, email, address, city, state, invoice_invoice_number)
VALUES (0, 'A000125', 'Sonia Gadea', 34-6586547895, 'sonia.g@gmail.com', 'Plaza de Legazpi, 25', 'Madrid', 'Madrid', 001);