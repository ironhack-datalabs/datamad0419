INSERT INTO `cardealdb`.`Car` (`idCar`,`VIN`, `manufacturer`, `model`, `year`, `color`) VALUES ('1','3K096I98581DHSNUPVINVIN', 'Volkswagen', 'Tiguan', '2019', 'Blue');
INSERT INTO `cardealdb`.`Car` (`idCar`,`VIN`, `manufacturer`, `model`, `year`, `color`) VALUES ('2','ZM8G7BEUQZ97IH46V', 'Peugeot', 'Rifter', '2019', 'Red');
INSERT INTO `cardealdb`.`Car` (`idCar`,`VIN`, `manufacturer`, `model`, `year`, `color`) VALUES ('3','RKXVNNIHLVVZOUB4M', 'Ford', 'Fusion', '2019', 'White');
INSERT INTO `cardealdb`.`Car` (`idCar`,`VIN`, `manufacturer`, `model`, `year`, `color`) VALUES ('4','HKNDGS7CU31E9Z7JW', 'Toyota', 'RAV4', '2018', 'Silver');
INSERT INTO `cardealdb`.`Car` (`idCar`,`VIN`, `manufacturer`, `model`, `year`, `color`) VALUES ('5','DAM41UDN3CHU2WVF6', 'Volvo', 'V60', '2019', 'Gray');
INSERT INTO `cardealdb`.`Car` (`idCar`,`VIN`, `manufacturer`, `model`, `year`, `color`) VALUES ('6','DAM41UDN3CHU2WVF6', 'Volvo', 'V60 Cross Country', '2019', 'Gray');

INSERT INTO `cardealdb`.`Customer` (`idCustomer`, `CustomerID`, `name`, `phone`, `address`, `city`, `state`, `country`) VALUES ('0', '10001', 'Pablo Picasso', '+34 636 17 63 82', 'Paseo de la Chopera, 14', 'Madrid', 'Spain', '28045');
INSERT INTO `cardealdb`.`Customer` (`idCustomer`, `CustomerID`, `name`, `phone`, `address`, `city`, `state`, `country`) VALUES ('1', '20001', 'Abraham Lincoln', '+1 305 907 7086', '120 SW 8th St', 'Paris', 'United States', '33130');
INSERT INTO `cardealdb`.`Customer` (`idCustomer`, `CustomerID`, `name`, `phone`, `address`, `city`, `state`, `country`) VALUES ('2', '30001', 'Napoléon Bonaparte', '+33 1 79 75 40 00', '40 Rue du Colisée', 'Miami', 'France', '75008');

INSERT INTO `cardealdb`.`SalesPerson` (`idSalesPerson`, `SalesPersonID`, `name`, `store`) VALUES ('1', '00001', 'Petey Cruiser', 'Madrid');
INSERT INTO `cardealdb`.`SalesPerson` (`idSalesPerson`, `SalesPersonID`, `name`, `store`) VALUES ('2', '00002', 'Anna Sthesia', 'Barcelona');
INSERT INTO `cardealdb`.`SalesPerson` (`idSalesPerson`, `SalesPersonID`, `name`, `store`) VALUES ('3', '00003', 'Paul Molive', 'Berlin');
INSERT INTO `cardealdb`.`SalesPerson` (`idSalesPerson`, `SalesPersonID`, `name`, `store`) VALUES ('4', '00004', 'Gail Forcewind', 'Paris');
INSERT INTO `cardealdb`.`SalesPerson` (`idSalesPerson`, `SalesPersonID`, `name`, `store`) VALUES ('5', '00005', 'Paige Turner', 'Mimia');
INSERT INTO `cardealdb`.`SalesPerson` (`idSalesPerson`, `SalesPersonID`, `name`, `store`) VALUES ('6', '00006', 'Bob Frapples', 'Mexico City');
INSERT INTO `cardealdb`.`SalesPerson` (`idSalesPerson`, `SalesPersonID`, `name`, `store`) VALUES ('7', '00007', 'Walter Melon', 'Amsterdam');
INSERT INTO `cardealdb`.`SalesPerson` (`idSalesPerson`, `SalesPersonID`, `name`, `store`) VALUES ('8', '00008', 'Shonda Leer', 'São Paulo');

INSERT INTO `cardealdb`.`Invoice` (`idInvoice`, `invoicenumber`, `date`, `Customer_idCustomer`, `Car_idCar`, `SalesPerson_idSalesPerson`) VALUES ('1', '852399038', '22-08-2018	', '2', '1', '4');
INSERT INTO `cardealdb`.`Invoice` (`idInvoice`, `invoicenumber`, `date`, `Customer_idCustomer`, `Car_idCar`, `SalesPerson_idSalesPerson`) VALUES ('2', '731166526', '31-12-2018', '1', '4', '6');
INSERT INTO `cardealdb`.`Invoice` (`idInvoice`, `invoicenumber`, `date`, `Customer_idCustomer`, `Car_idCar`, `SalesPerson_idSalesPerson`) VALUES ('3', '271135104', '22-01-2019', '3', '3', '8');