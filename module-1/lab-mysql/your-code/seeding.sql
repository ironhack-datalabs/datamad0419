Select* from lab_mysql.Vendedor;

INSERT INTO `lab_mysql`.`Coche` (`idCoche`, `VIN`, `Fabricante`, `modelo`, `año`, `Color`) VALUES ('01', '32432424FSF', 'PEUGEOT', 'RANCHERA', '2019', 'ROJO');
INSERT INTO `lab_mysql`.`Coche` (`idCoche`, `VIN`, `Fabricante`, `modelo`, `año`, `Color`) VALUES ('02', '1SDFDFSDFF', 'RENAULT', 'RANCHERA', '2012', 'AZUL');
INSERT INTO `lab_mysql`.`Coche` (`idCoche`, `VIN`, `Fabricante`, `modelo`, `año`, `Color`) VALUES ('03', '1324234ASD', 'PEUGEOT', 'ELECTRICO', '2011', 'ROJO');
INSERT INTO `lab_mysql`.`Coche` (`idCoche`, `VIN`, `Fabricante`, `modelo`, `año`, `Color`) VALUES ('04', 'asdasdasd22', 'CITROEN', 'MONOVOLUMEN', '2015', 'VERDE');

INSERT INTO `lab_mysql`.`Comprador` (`idComprador`, `Name`, `Telefono`, `email`, `ciudad`, `pais`) VALUES ('1', 'ANTONIO', '6453621', 'HOLA@GMAIL.COM', 'MADRID', 'ESP');
INSERT INTO `lab_mysql`.`Comprador` (`idComprador`, `Name`, `Telefono`, `email`, `ciudad`, `pais`) VALUES ('2', 'JUAN', '936453621', 'ADIOS@GMAIL.COM', 'BCN', 'ESP');
INSERT INTO `lab_mysql`.`Comprador` (`idComprador`, `Name`, `Telefono`, `email`, `ciudad`, `pais`) VALUES ('3', 'CARLOS', '94964453621', 'QUINTIN@GMAIL.COM', 'GUADALAJARA', 'ESP');
INSERT INTO `lab_mysql`.`Comprador` (`idComprador`, `Name`, `Telefono`, `email`, `ciudad`, `pais`) VALUES ('4', 'ANTONIO', '916453621', 'CRESPT@GMAIL.COM', 'MADRID', 'ESP');

INSERT INTO `lab_mysql`.`Factura` (`idFactura`, `numero factura`, `Fecha`, `coches`, `numero vendedor`, `numero cliente`) VALUES ('3', '0000000012', '21-04-12', '2', '45', '01');
INSERT INTO `lab_mysql`.`Factura` (`idFactura`, `numero factura`, `Fecha`, `coches`, `numero vendedor`, `numero cliente`) VALUES ('4', '0000000123', '22-09-14', '1', '23', '02');
INSERT INTO `lab_mysql`.`Factura` (`idFactura`, `numero factura`, `Fecha`, `coches`, `numero vendedor`, `numero cliente`) VALUES ('5', '0000000011', '02-07-15', '1', '56', '03');
INSERT INTO `lab_mysql`.`Factura` (`idFactura`, `numero factura`, `Fecha`, `coches`, `numero vendedor`, `numero cliente`) VALUES ('6', '0000000015', '12-05-17', '2', '34', '04');

INSERT INTO `lab_mysql`.`Vendedor` (`idvendedor`, `staff`, `Nombre`, `Vendedorcol`) VALUES ('3', '32', 'JUAN', 'MADRID');

INSERT INTO `lab_mysql`.`Vendedor` (`idvendedor`, `staff`, `Nombre`, `Vendedorcol`) VALUES ('4', '35', 'JUAN', 'MADRID');

INSERT INTO `lab_mysql`.`Vendedor` (`idvendedor`, `staff`, `Nombre`, `Vendedorcol`) VALUES ('3', '32', 'ANTONIO', 'BARCELONA');

