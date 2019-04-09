-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema labmysql
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema labmysql
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `labmysql` DEFAULT CHARACTER SET utf8 ;
USE `labmysql` ;

-- -----------------------------------------------------
-- Table `labmysql`.`cars`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `labmysql`.`cars` (
  `idcar` INT NOT NULL AUTO_INCREMENT,
  `vin` VARCHAR(20) NULL,
  `manufacturer` VARCHAR(45) NULL,
  `model` VARCHAR(45) NULL,
  `year_car` INT NULL,
  `color` VARCHAR(20) NULL,
  PRIMARY KEY (`idcar`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `labmysql`.`customers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `labmysql`.`customers` (
  `idcustomer` INT NOT NULL AUTO_INCREMENT,
  `customer_id` INT NULL,
  `name` VARCHAR(45) NULL,
  `phone` VARCHAR(45) NULL,
  `email` VARCHAR(45) NULL,
  `address` VARCHAR(150) NULL,
  `city` VARCHAR(45) NULL,
  `state_province` VARCHAR(45) NULL,
  `country` VARCHAR(45) NULL,
  `postal` VARCHAR(6) NULL,
  PRIMARY KEY (`idcustomer`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `labmysql`.`salespersons`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `labmysql`.`salespersons` (
  `idsalesperson` INT NOT NULL AUTO_INCREMENT,
  `staff_id` VARCHAR(5) NULL,
  `name` VARCHAR(45) NULL,
  `store` VARCHAR(45) NULL,
  PRIMARY KEY (`idsalesperson`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `labmysql`.`invoices`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `labmysql`.`invoices` (
  `idinvoice` INT NOT NULL AUTO_INCREMENT,
  `invoice_number` VARCHAR(12) NULL,
  `date_inv` DATE NULL,
  `customer` INT NOT NULL,
  `car` INT NOT NULL,
  `salesperson` INT NOT NULL,
  PRIMARY KEY (`idinvoice`, `customer`, `car`, `salesperson`),
  INDEX `fk_invoices_customers1_idx` (`customer` ASC),
  INDEX `fk_invoices_cars1_idx` (`car` ASC),
  INDEX `fk_invoices_salespersons1_idx` (`salesperson` ASC),
  CONSTRAINT `fk_invoices_customers1`
    FOREIGN KEY (`customer`)
    REFERENCES `labmysql`.`customers` (`idcustomer`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_invoices_cars1`
    FOREIGN KEY (`car`)
    REFERENCES `labmysql`.`cars` (`idcar`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_invoices_salespersons1`
    FOREIGN KEY (`salesperson`)
    REFERENCES `labmysql`.`salespersons` (`idsalesperson`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
