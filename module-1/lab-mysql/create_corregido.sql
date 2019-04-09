-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema lab_mysql
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema lab_mysql
-- ------------------Cars-----------------------------------
CREATE SCHEMA IF NOT EXISTS `lab_mysql` DEFAULT CHARACTER SET utf8 ;
USE `lab_mysql` ;

-- -----------------------------------------------------
-- Table `lab_mysql`.`Cars`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `lab_mysql`.`Cars` (
  `idCars` INT NOT NULL,
  `Manufacturer` VARCHAR(45) NULL,
  `Model` VARCHAR(45) NULL,
  `Year` VARCHAR(45) NULL,
  `Color` VARCHAR(45) NULL,
  PRIMARY KEY (`idCars`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `lab_mysql`.`Invoices`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `lab_mysql`.`Invoices` (
  `idInvoices` INT NOT NULL,
  `Date` DATETIME NULL,
  `Car` VARCHAR(45) NULL,
  `Customer` VARCHAR(45) NULL,
  `Salesperson` VARCHAR(45) NULL,
  `Cars_idCars` INT NOT NULL,
  PRIMARY KEY (`idInvoices`),
  INDEX `fk_Invoices_Cars1_idx` (`Cars_idCars` ASC) VISIBLE,
  CONSTRAINT `fk_Invoices_Cars1`
    FOREIGN KEY (`Cars_idCars`)
    REFERENCES `lab_mysql`.`Cars` (`idCars`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Customers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `lab_mysql`.`Customers` (
  `idCustomers` INT NOT NULL,
  `Name` VARCHAR(45) NULL,
  `Phone number` VARCHAR(45) NULL,
  `Email` VARCHAR(45) NULL,
  `Address` VARCHAR(45) NULL,
  `City` VARCHAR(45) NULL,
  `State/province` VARCHAR(45) NULL,
  `Country` VARCHAR(45) NULL,
  `Zip/Postal code` VARCHAR(45) NULL,
  `Cars_idCars` INT NOT NULL,
  `Invoices_idInvoices` INT NOT NULL,
  PRIMARY KEY (`idCustomers`),
  INDEX `fk_Customers_Cars_idx` (`Cars_idCars` ASC) VISIBLE,
  INDEX `fk_Customers_Invoices1_idx` (`Invoices_idInvoices` ASC) VISIBLE,
  CONSTRAINT `fk_Customers_Cars`
    FOREIGN KEY (`Cars_idCars`)
    REFERENCES `lab_mysql`.`Cars` (`idCars`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Customers_Invoices1`
    FOREIGN KEY (`Invoices_idInvoices`)
    REFERENCES `lab_mysql`.`Invoices` (`idInvoices`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `lab_mysql`.`Salesperson`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `lab_mysql`.`Salesperson` (
  `idSalesperson` INT NOT NULL,
  `Name` VARCHAR(45) NULL,
  `Store` VARCHAR(45) NULL,
  `Cars_idCars` INT NOT NULL,
  `Invoices_idInvoices` INT NOT NULL,
  PRIMARY KEY (`idSalesperson`),
  INDEX `fk_Salesperson_Cars1_idx` (`Cars_idCars` ASC) VISIBLE,
  INDEX `fk_Salesperson_Invoices1_idx` (`Invoices_idInvoices` ASC) VISIBLE,
  CONSTRAINT `fk_Salesperson_Cars1`
    FOREIGN KEY (`Cars_idCars`)
    REFERENCES `lab_mysql`.`Cars` (`idCars`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Salesperson_Invoices1`
    FOREIGN KEY (`Invoices_idInvoices`)
    REFERENCES `lab_mysql`.`Invoices` (`idInvoices`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `lab_mysql`.`Customers_has_Salesperson`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `lab_mysql`.`Customers_has_Salesperson` (
  `Customers_idCustomers` INT NOT NULL,
  `Salesperson_idSalesperson` INT NOT NULL,
  PRIMARY KEY (`Customers_idCustomers`, `Salesperson_idSalesperson`),
  INDEX `fk_Customers_has_Salesperson_Salesperson1_idx` (`Salesperson_idSalesperson` ASC) VISIBLE,
  INDEX `fk_Customers_has_Salesperson_Customers1_idx` (`Customers_idCustomers` ASC) VISIBLE,
  CONSTRAINT `fk_Customers_has_Salesperson_Customers1`
    FOREIGN KEY (`Customers_idCustomers`)
    REFERENCES `lab_mysql`.`Customers` (`idCustomers`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Customers_has_Salesperson_Salesperson1`
    FOREIGN KEY (`Salesperson_idSalesperson`)
    REFERENCES `lab_mysql`.`Salesperson` (`idSalesperson`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

