-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema cardealdb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema cardealdb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `cardealdb` ;
USE `cardealdb` ;

-- -----------------------------------------------------
-- Table `cardealdb`.`Car`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cardealdb`.`Car` (
  `idCar` INT NOT NULL AUTO_INCREMENT,
  `VIN` VARCHAR(30) NOT NULL,
  `manufacturer` VARCHAR(45) NULL,
  `model` VARCHAR(45) NULL,
  `year` YEAR(4) NULL,
  `color` VARCHAR(20) NULL,
  PRIMARY KEY (`idCar`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `cardealdb`.`Customer`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cardealdb`.`Customer` (
  `idCustomer` INT NOT NULL AUTO_INCREMENT,
  `CustomerID` VARCHAR(11) NOT NULL,
  `name` VARCHAR(80) NULL,
  `phone` CHAR(24) NULL,
  `email` VARCHAR(45) NULL,
  `address` VARCHAR(45) NULL,
  `city` VARCHAR(45) NULL,
  `state` CHAR(30) NULL,
  `country` VARCHAR(30) NULL,
  PRIMARY KEY (`idCustomer`, `CustomerID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `cardealdb`.`SalesPerson`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cardealdb`.`SalesPerson` (
  `idSalesPerson` INT NOT NULL AUTO_INCREMENT,
  `SalesPersonID` VARCHAR(11) NOT NULL,
  `name` VARCHAR(45) NULL,
  `store` VARCHAR(45) NULL,
  PRIMARY KEY (`idSalesPerson`, `SalesPersonID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `cardealdb`.`Invoice`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cardealdb`.`Invoice` (
  `idInvoice` INT NOT NULL,
  `invoicenumber` VARCHAR(20) NOT NULL,
  `date` DATE NULL,
  `Customer_idCustomer` INT NOT NULL,
  `Car_idCar` INT NOT NULL,
  `SalesPerson_idSalesPerson` INT NOT NULL,
  PRIMARY KEY (`idInvoice`),
  INDEX `fk_Invoice_Customer1_idx`(`Customer_idCustomer` ASC),
  INDEX `fk_Invoice_Car1_idx`(`Car_idCar` ASC),
  INDEX `fk_Invoice_SalesPerson1_idx`(`SalesPerson_idSalesPerson` ASC),
  CONSTRAINT `fk_Invoice_Customer1`
    FOREIGN KEY (`Customer_idCustomer`)
    REFERENCES `cardealdb`.`Customer` (`idCustomer`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Invoice_Car1`
    FOREIGN KEY (`Car_idCar`)
    REFERENCES `cardealdb`.`Car` (`idCar`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Invoice_SalesPerson1`
    FOREIGN KEY (`SalesPerson_idSalesPerson`)
    REFERENCES `cardealdb`.`SalesPerson` (`idSalesPerson`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
