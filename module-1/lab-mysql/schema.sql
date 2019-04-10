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
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`car`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`car` (
  `idcar` INT NOT NULL,
  `vin_number` VARCHAR(45) NOT NULL,
  `manufacturer` VARCHAR(45) NULL,
  `model` VARCHAR(45) NOT NULL,
  `year` YEAR(4) NULL,
  `color` VARCHAR(45) NULL,
  PRIMARY KEY (`idcar`),
  UNIQUE INDEX `vin_number_UNIQUE` (`vin_number` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`invoice`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`invoice` (
  `invoice_number` INT NOT NULL,
  `date` DATE NOT NULL,
  `car_idcar` INT NOT NULL,
  PRIMARY KEY (`invoice_number`),
  INDEX `fk_invoice_car_idx` (`car_idcar` ASC) VISIBLE,
  CONSTRAINT `fk_invoice_car`
    FOREIGN KEY (`car_idcar`)
    REFERENCES `mydb`.`car` (`idcar`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`customer`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`customer` (
  `idcustomer` INT NOT NULL,
  `vat_number` VARCHAR(45) NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `phone` BIGINT(15) NULL,
  `email` VARCHAR(45) NULL,
  `address` VARCHAR(45) NULL,
  `city` VARCHAR(45) NULL,
  `state` VARCHAR(45) NULL,
  `invoice_invoice_number` INT NOT NULL,
  PRIMARY KEY (`idcustomer`),
  UNIQUE INDEX `vat_number_UNIQUE` (`VAT_number` ASC) VISIBLE,
  INDEX `fk_customer_invoice1_idx` (`invoice_invoice_number` ASC) VISIBLE,
  CONSTRAINT `fk_customer_invoice1`
    FOREIGN KEY (`invoice_invoice_number`)
    REFERENCES `mydb`.`invoice` (`invoice_number`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`salesperson`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`salesperson` (
  `idsalesperson` INT NOT NULL,
  `staff_id` INT NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `store` VARCHAR(45) NULL,
  `invoice_invoice_number` INT NOT NULL,
  PRIMARY KEY (`idsalesperson`),
  UNIQUE INDEX `staff_id_UNIQUE` (`staff_id` ASC) VISIBLE,
  INDEX `fk_salesperson_invoice1_idx` (`invoice_invoice_number` ASC) VISIBLE,
  CONSTRAINT `fk_salesperson_invoice1`
    FOREIGN KEY (`invoice_invoice_number`)
    REFERENCES `mydb`.`invoice` (`invoice_number`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
