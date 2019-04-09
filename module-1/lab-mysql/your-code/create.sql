-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- ----------CarsCarsCarsCars-------------------------------------------
-- Schema lab_mysql
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema lab_mysql
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `lab_mysql` DEFAULT CHARACTER SET utf8 ;
USE `lab_mysql` ;

-- -----------------------------------------------------
-- Table `lab_mysql`.`Cars`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `lab_mysql`.`Cars` (
  `idCar` INT NOT NULL,
  `vin` VARCHAR(45) NULL,
  `manufacturer` VARCHAR(45) NULL,
  `model` VARCHAR(45) NULL,
  `year` VARCHAR(45) NULL,
  `colour` VARCHAR(45) NULL,
  PRIMARY KEY (`idCar`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `lab_mysql`.`Customers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `lab_mysql`.`Customers` (
  `idCustomers` INT NOT NULL,
  `name` VARCHAR(45) NULL,
  `phone number` VARCHAR(45) NULL,
  `email` VARCHAR(45) NULL,
  `address` VARCHAR(45) NULL,
  `state/prov` VARCHAR(45) NULL,
  `country` VARCHAR(45) NULL,
  `postal` VARCHAR(45) NULL,
  `Cars_idCar` INT NOT NULL,
  PRIMARY KEY (`idCustomers`),
  INDEX `fk_Customers_Cars1_idx` (`Cars_idCar` ASC),
  CONSTRAINT `fk_Customers_Cars1`
    FOREIGN KEY (`Cars_idCar`)
    REFERENCES `lab_mysql`.`Cars` (`idCar`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `lab_mysql`.`Salespersons`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `lab_mysql`.`Salespersons` (
  `idStaff` INT NOT NULL,
  `name` VARCHAR(45) NULL,
  `store` VARCHAR(45) NULL,
  PRIMARY KEY (`idStaff`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `lab_mysql`.`Invoices`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `lab_mysql`.`Invoices` (
  `idInvoice` INT NOT NULL,
  `date` DATE NULL,
  `Cars_idCar` INT NOT NULL,
  `Customers_idCustomers` INT NOT NULL,
  `Salespersons_idStaff` INT NOT NULL,
  PRIMARY KEY (`idInvoice`),
  INDEX `fk_Invoices_Cars_idx` (`Cars_idCar` ASC),
  INDEX `fk_Invoices_Customers1_idx` (`Customers_idCustomers` ASC),
  INDEX `fk_Invoices_Salespersons1_idx` (`Salespersons_idStaff` ASC),
  CONSTRAINT `fk_Invoices_Cars`
    FOREIGN KEY (`Cars_idCar`)
    REFERENCES `lab_mysql`.`Cars` (`idCar`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Invoices_Customers1`
    FOREIGN KEY (`Customers_idCustomers`)
    REFERENCES `lab_mysql`.`Customers` (`idCustomers`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Invoices_Salespersons1`
    FOREIGN KEY (`Salespersons_idStaff`)
    REFERENCES `lab_mysql`.`Salespersons` (`idStaff`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `lab_mysql`.`Salespersons_has_Cars`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `lab_mysql`.`Salespersons_has_Cars` (
  `Salespersons_idStaff` INT NOT NULL,
  `Cars_idCar` INT NOT NULL,
  PRIMARY KEY (`Salespersons_idStaff`, `Cars_idCar`),
  INDEX `fk_Salespersons_has_Cars_Cars1_idx` (`Cars_idCar` ASC),
  INDEX `fk_Salespersons_has_Cars_Salespersons1_idx` (`Salespersons_idStaff` ASC),
  CONSTRAINT `fk_Salespersons_has_Cars_Salespersons1`
    FOREIGN KEY (`Salespersons_idStaff`)
    REFERENCES `lab_mysql`.`Salespersons` (`idStaff`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Salespersons_has_Cars_Cars1`
    FOREIGN KEY (`Cars_idCar`)
    REFERENCES `lab_mysql`.`Cars` (`idCar`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
