-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`customer`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`customer` (
  `idcustomer` INT NOT NULL,
  `customerid` INT NOT NULL,
  `name` VARCHAR(45) NULL,
  `phonenumber` VARCHAR(45) NULL,
  `email` VARCHAR(45) NULL,
  `address` VARCHAR(45) NULL,
  `city` VARCHAR(45) NULL,
  `state` VARCHAR(45) NULL,
  `country` VARCHAR(45) NULL,
  `zip` VARCHAR(45) NULL,
  PRIMARY KEY (`idcustomer`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`salesperson`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`salesperson` (
  `idsalesperson` INT NOT NULL,
  `staffid` INT NOT NULL,
  `name` VARCHAR(45) NULL,
  `store` VARCHAR(45) NULL,
  PRIMARY KEY (`idsalesperson`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`car`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`car` (
  `idcar` INT NOT NULL,
  `VIN` VARCHAR(45) NULL,
  `manufacturer` VARCHAR(45) NULL,
  `model` VARCHAR(45) NULL,
  `year` VARCHAR(45) NULL,
  `color` VARCHAR(45) NULL,
  PRIMARY KEY (`idcar`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`invoice`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`invoice` (
  `idinvoice` INT NOT NULL,
  `invoicenumber` INT NOT NULL,
  `date` INT NULL,
  `car` INT NULL,
  `customer` INT NULL,
  `salesperson` INT NULL,
  `customer_idcustomer` INT NOT NULL,
  `salesperson_idsalesperson` INT NOT NULL,
  `car_idcar` INT NOT NULL,
  PRIMARY KEY (`idinvoice`),
  INDEX `fk_invoice_customer1_idx` (`customer_customerid` ASC) VISIBLE,
  INDEX `fk_invoice_salesperson1_idx` (`salesperson_staffid` ASC) VISIBLE,
  INDEX `fk_invoice_car1_idx` (`car_idcar` ASC) VISIBLE,
  CONSTRAINT `fk_invoice_customer1`
    FOREIGN KEY (`customer_customerid`)
    REFERENCES `mydb`.`customer` (`customerid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_invoice_salesperson1`
    FOREIGN KEY (`salesperson_staffid`)
    REFERENCES `mydb`.`salesperson` (`staffid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_invoice_car1`
    FOREIGN KEY (`car_idcar`)
    REFERENCES `mydb`.`car` (`idcar`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
