-- MySQL Script generated by MySQL Workbench
-- Tue Apr  9 23:45:13 2019
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema lab-mysql
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema lab-mysql
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `lab-mysql` DEFAULT CHARACTER SET utf8 ;
USE `lab-mysql` ;

-- -----------------------------------------------------
-- Table `lab-mysql`.`cars`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `lab-mysql`.`cars` (
  `car_ID` INT NOT NULL AUTO_INCREMENT,
  `VIN` VARCHAR(20) NOT NULL,
  `manufacturer` VARCHAR(45) NULL DEFAULT NULL,
  `model` VARCHAR(45) NOT NULL,
  `year` INT NULL DEFAULT NULL,
  `color` VARCHAR(45) NULL DEFAULT NULL,
  `carscol` VARCHAR(45) NULL,
  PRIMARY KEY (`car_ID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `lab-mysql`.`customers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `lab-mysql`.`customers` (
  `customer_ID` INT NOT NULL AUTO_INCREMENT,
  `customer_id_number` VARCHAR(20) NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `phone` VARCHAR(45) NULL,
  `email` VARCHAR(45) NULL,
  `address` VARCHAR(45) NULL,
  `city` VARCHAR(45) NULL,
  `state` VARCHAR(45) NULL,
  `country` VARCHAR(45) NULL,
  `postal_code` VARCHAR(45) NULL,
  PRIMARY KEY (`customer_ID`),
  UNIQUE INDEX `customer_id_number_UNIQUE` (`customer_id_number` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `lab-mysql`.`salespersons`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `lab-mysql`.`salespersons` (
  `staff_ID` INT NOT NULL AUTO_INCREMENT,
  `staff_id_number` VARCHAR(15) NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `store` VARCHAR(45) NOT NULL,
  UNIQUE INDEX `staff_id_number_UNIQUE` (`staff_id_number` ASC) VISIBLE,
  PRIMARY KEY (`staff_ID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `lab-mysql`.`invoices`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `lab-mysql`.`invoices` (
  `invoice_ID` INT NOT NULL AUTO_INCREMENT,
  `invoice_number` INT NOT NULL,
  `emission_date` DATE NOT NULL,
  `cars_car_ID` INT NOT NULL,
  `salespersons_staff_ID` INT NOT NULL,
  PRIMARY KEY (`invoice_ID`),
  INDEX `fk_invoices_cars1_idx` (`cars_car_ID` ASC) VISIBLE,
  INDEX `fk_invoices_salespersons1_idx` (`salespersons_staff_ID` ASC) VISIBLE,
  CONSTRAINT `fk_invoices_cars1`
    FOREIGN KEY (`cars_car_ID`)
    REFERENCES `lab-mysql`.`cars` (`car_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_invoices_salespersons1`
    FOREIGN KEY (`salespersons_staff_ID`)
    REFERENCES `lab-mysql`.`salespersons` (`staff_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `lab-mysql`.`invoice_customer`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `lab-mysql`.`invoice_customer` (
  `invoices_invoice_ID` INT NOT NULL,
  `customers_customer_ID` INT NOT NULL,
  `percentage_customer1` DECIMAL(2) NULL,
  PRIMARY KEY (`invoices_invoice_ID`, `customers_customer_ID`),
  INDEX `fk_invoice_customer_customers1_idx` (`customers_customer_ID` ASC) VISIBLE,
  CONSTRAINT `fk_invoice_customer_invoices1`
    FOREIGN KEY (`invoices_invoice_ID`)
    REFERENCES `lab-mysql`.`invoices` (`invoice_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_invoice_customer_customers1`
    FOREIGN KEY (`customers_customer_ID`)
    REFERENCES `lab-mysql`.`customers` (`customer_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
