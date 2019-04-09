INSERT INTO `mydb`.`car` (`idcar`, `VIN`, `manufacturer`, `model`, `year`, `color`) VALUES (0, '3K096I98581DHSNUP', 'Volkswagen', 'Tiguan', '2019', 'Blue');
INSERT INTO `mydb`.`car` (`idcar`, `VIN`, `manufacturer`, `model`, `year`, `color`) VALUES (1, 'ZM8G7BEUQZ97IH46V', 'Peugeot', 'Rifter', '2019', 'Red');
INSERT INTO `mydb`.`car` (`idcar`, `VIN`, `manufacturer`, `model`, `year`, `color`) VALUES (2, 'RKXVNNIHLVVZOUB4M', 'Ford', 'Fusion', '2018', 'White');
INSERT INTO `mydb`.`car` (`idcar`, `VIN`, `manufacturer`, `model`, `year`, `color`) VALUES (3, 'HKNDGS7CU31E9Z7JW', 'Toyota', 'RAV4', '2018', 'Silver');
INSERT INTO `mydb`.`car` (`idcar`, `VIN`, `manufacturer`, `model`, `year`, `color`) VALUES (4, 'DAM41UDN3CHU2WVF6', 'Volvo', 'V60', '2019', 'Gray');
INSERT INTO `mydb`.`car` (`idcar`, `VIN`, `manufacturer`, `model`, `year`, `color`) VALUES (5, 'DAM41UDN3CHU2WVF6', 'Volvo', 'V60 Cross Country', '2019', 'Gray');

INSERT INTO `mydb`.`invoice` (`idinvoice`, `invoicenumber`, `date`, `car`, `customer`, `salesperson`) VALUES ('0', '852399038', '22-08-2018', '0', '1', '3');
INSERT INTO `mydb`.`invoice` (`idinvoice`, `invoicenumber`, `date`, `car`, `customer`, `salesperson`) VALUES ('1', '731166526', '31-12-2018', '3', '0', '5');
INSERT INTO `mydb`.`invoice` (`idinvoice`, `invoicenumber`, `date`, `car`, `customer`, `salesperson`) VALUES ('2', '271135104', '22-01-2019', '2', '2', '7');

INSERT INTO `mydb`.`salesperson` (`idsalesperson`, `staffid`, `name`, `store`) VALUES (0, '00008', 'Petey Cruiser', 'Madrid');
INSERT INTO `mydb`.`salesperson` (`idsalesperson`, `staffid`, `name`, `store`) VALUES (1, '00001', 'Anna Sthesia', 'Barcelona');
INSERT INTO `mydb`.`salesperson` (`idsalesperson`, `staffid`, `name`, `store`) VALUES (2, '00002', 'Paul Molive', 'Berlin');
INSERT INTO `mydb`.`salesperson` (`idsalesperson`, `staffid`, `name`, `store`) VALUES (3, '00003', 'Gail Forcewind', 'Paris');
INSERT INTO `mydb`.`salesperson` (`idsalesperson`, `staffid`, `name`, `store`) VALUES (4, '00004', 'Paige Turner', 'Mimia');
INSERT INTO `mydb`.`salesperson` (`idsalesperson`, `staffid`, `name`, `store`) VALUES (5, '00005', 'Bob Frapples', 'Mexico City');
INSERT INTO `mydb`.`salesperson` (`idsalesperson`, `staffid`, `name`, `store`) VALUES (6, '00006', 'Walter Melon', 'Amsterdam');
INSERT INTO `mydb`.`salesperson` (`idsalesperson`, `staffid`, `name`, `store`) VALUES (7, '00007', 'Shonda Leer', 'SãoPaulo');

INSERT INTO `mydb`.`customer` (`idcustomer`, `customerid`, `name`, `phonenumber`, `email`, `adress`, `city`, `state`, `country`, `zip`) VALUES (0, '10001', 'Pablo Picasso', '+34 636 17 63 82', '-', 'Paseo de la Chopera, 14', 'Madrid', 'Madrid', 'Spain', '28045');
INSERT INTO `mydb`.`customer` (`idcustomer`, `customerid`, `name`, `phonenumber`, `email`, `adress`, `city`, `state`, `country`, `zip`) VALUES (1, '20002', 'Abraham Lincoln', '+1 305 907 7086', '-', '120 SW 8th St', 'Miami', 'Florida', 'United States', '33130');
INSERT INTO `mydb`.`customer` (`idcustomer`, `customerid`, `name`, `phonenumber`, `email`, `adress`, `city`, `state`, `country`, `zip`) VALUES (2, '30002', 'Napoléon Bonaparter', '+33 1 79 75 40 00', '-', '40 Rue du Colisée', 'Paris', 'Île-de-France', 'France', '75008');