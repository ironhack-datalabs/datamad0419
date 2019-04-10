#las otras tablas las he importado

INSERT INTO `lab_mysql`.`Customers` (`ID`, `Customer`, `Name`, `Phone`, `Address`, `City`, `State`, `Country`, `Zip Code`, `Cars_ID`) VALUES ('1', '10001', 'Picasso', '+34 666666666', 'Chopera 8', 'Madrid', 'Madrid', 'Spain', '28045', '1');
INSERT INTO `lab_mysql`.`Customers` (`ID`, `Customer`, `Name`, `Phone`, `Address`, `City`, `State`, `Country`, `Zip Code`, `Cars_ID`) VALUES ('2', '20001', 'Lincoln', '+34 666666661', 'SW 8th', 'Miami', 'Florida', 'USA', '33130', '2');
INSERT INTO `lab_mysql`.`Customers` (`ID`, `Customer`, `Name`, `Phone`, `Address`, `City`, `State`, `Country`, `Zip Code`, `Cars_ID`) VALUES ('3', '30001', 'Bonaparte', '+34 666666662', 'Rue', 'Paris', 'Ile', 'France', '75008', '3');

INSERT INTO `lab_mysql`.`Invoices` (`ID`, `Invoice Number`, `Date`, `Cars_ID`, `Salesperson_ID`, `Customers_ID`) VALUES ('1', '4372893744', '2018-08-22', '2', '1', '3');
INSERT INTO `lab_mysql`.`Invoices` (`ID`, `Invoice Number`, `Date`, `Cars_ID`, `Salesperson_ID`, `Customers_ID`) VALUES ('2', '432434234', '2018-12-31', '1', '3', '1');
INSERT INTO `lab_mysql`.`Invoices` (`ID`, `Invoice Number`, `Date`, `Cars_ID`, `Salesperson_ID`, `Customers_ID`) VALUES ('3', '423423423', '2019-01-22', '3', '2', '2');

INSERT INTO `lab_mysql`.`Customers_has_Salesperson` (`Customers_ID`, `Salesperson_ID`) VALUES ('1', '2');
INSERT INTO `lab_mysql`.`Customers_has_Salesperson` (`Customers_ID`, `Salesperson_ID`) VALUES ('1', '3');
INSERT INTO `lab_mysql`.`Customers_has_Salesperson` (`Customers_ID`, `Salesperson_ID`) VALUES ('2', '1');
INSERT INTO `lab_mysql`.`Customers_has_Salesperson` (`Customers_ID`, `Salesperson_ID`) VALUES ('3', '4');
INSERT INTO `lab_mysql`.`Customers_has_Salesperson` (`Customers_ID`, `Salesperson_ID`) VALUES ('2', '3');
