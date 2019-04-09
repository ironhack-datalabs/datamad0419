-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema lab-mysql-db
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema lab-mysql-db
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `lab-mysql-db` DEFAULT CHARACTER SET utf8 ;
USE `lab-mysql-db` ;

-- -----------------------------------------------------
-- Table `lab-mysql-db`.`Cars`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `lab-mysql-db`.`Cars` (
  `idCars` INT NOT NULL,
  `VIN` VARCHAR(45) NULL,
  `Manufacturer` VARCHAR(45) NULL,
  `Model` VARCHAR(45) NULL,
  `Year` INT NULL,
  `Color` VARCHAR(45) NULL,
  PRIMARY KEY (`idCars`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `lab-mysql-db`.`Customers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `lab-mysql-db`.`Customers` (
  `idCustomers` INT NOT NULL,
  `CostumerID` VARCHAR(45) NULL,
  `FirstName` VARCHAR(45) NULL,
  `LastName` VARCHAR(45) NULL,
  `PhoneNum` VARCHAR(45) NULL,
  `Email` VARCHAR(45) NULL,
  `Address` VARCHAR(150) NULL,
  `City` VARCHAR(45) NULL,
  `State/Province` VARCHAR(45) NULL,
  `PostalCode` VARCHAR(45) NULL,
  PRIMARY KEY (`idCustomers`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `lab-mysql-db`.`Salesperson`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `lab-mysql-db`.`Salesperson` (
  `idSalesperson` INT NOT NULL,
  `FirstName` VARCHAR(45) NULL,
  `LastName` VARCHAR(45) NULL,
  `StaffID` VARCHAR(45) NULL,
  `Store` VARCHAR(45) NULL,
  PRIMARY KEY (`idSalesperson`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `lab-mysql-db`.`Invoices`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `lab-mysql-db`.`Invoices` (
  `idInvoices` INT NOT NULL,
  `InvoiceNum` VARCHAR(45) NOT NULL,
  `Date` DATE NOT NULL,
  `Salesperson_idSalesperson` INT NOT NULL,
  `Customers_idCustomers` INT NOT NULL,
  `Cars_idCars` INT NOT NULL,
  PRIMARY KEY (`idInvoices`),
  INDEX `fk_Invoices_Salesperson1_idx` (`Salesperson_idSalesperson` ASC) VISIBLE,
  INDEX `fk_Invoices_Customers1_idx` (`Customers_idCustomers` ASC) VISIBLE,
  INDEX `fk_Invoices_Cars1_idx` (`Cars_idCars` ASC) VISIBLE,
  CONSTRAINT `fk_Invoices_Salesperson1`
    FOREIGN KEY (`Salesperson_idSalesperson`)
    REFERENCES `lab-mysql-db`.`Salesperson` (`idSalesperson`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Invoices_Customers1`
    FOREIGN KEY (`Customers_idCustomers`)
    REFERENCES `lab-mysql-db`.`Customers` (`idCustomers`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Invoices_Cars1`
    FOREIGN KEY (`Cars_idCars`)
    REFERENCES `lab-mysql-db`.`Cars` (`idCars`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
