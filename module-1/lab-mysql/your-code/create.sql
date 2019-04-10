-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
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
  `ID` INT NOT NULL AUTO_INCREMENT,
  `VIN` VARCHAR(45) NULL,
  `Manufacturer` VARCHAR(45) NULL,
  `Model` VARCHAR(45) NULL,
  `Year` YEAR(4) NULL,
  `Color` VARCHAR(45) NULL,
  PRIMARY KEY (`ID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `lab_mysql`.`Salesperson`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `lab_mysql`.`Salesperson` (
  `ID` INT NOT NULL AUTO_INCREMENT,
  `Staff ID` VARCHAR(45) NULL,
  `Name` VARCHAR(45) NULL,
  `Store` VARCHAR(45) NULL,
  PRIMARY KEY (`ID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `lab_mysql`.`Customers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `lab_mysql`.`Customers` (
  `ID` INT NOT NULL AUTO_INCREMENT,
  `Customer` VARCHAR(45) NULL,
  `Name` VARCHAR(45) NULL,
  `Phone` VARCHAR(45) NULL,
  `Email` VARCHAR(45) NULL,
  `Address` VARCHAR(45) NULL,
  `City` VARCHAR(45) NULL,
  `State` VARCHAR(45) NULL,
  `Country` VARCHAR(45) NULL,
  `Zip Code` VARCHAR(45) NULL,
  `Cars_ID` INT NOT NULL,
  PRIMARY KEY (`ID`),
  INDEX `fk_Customers_Cars1_idx` (`Cars_ID` ASC) VISIBLE,
  CONSTRAINT `fk_Customers_Cars1`
    FOREIGN KEY (`Cars_ID`)
    REFERENCES `lab_mysql`.`Cars` (`ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `lab_mysql`.`Invoices`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `lab_mysql`.`Invoices` (
  `ID` INT NOT NULL AUTO_INCREMENT,
  `Invoice Number` VARCHAR(45) NULL,
  `Date` DATE NULL,
  `Cars_ID` INT NOT NULL,
  `Salesperson_ID` INT NOT NULL,
  `Customers_ID` INT NOT NULL,
  PRIMARY KEY (`ID`),
  INDEX `fk_Invoices_Cars_idx` (`Cars_ID` ASC) VISIBLE,
  INDEX `fk_Invoices_Salesperson1_idx` (`Salesperson_ID` ASC) VISIBLE,
  INDEX `fk_Invoices_Customers1_idx` (`Customers_ID` ASC) VISIBLE,
  CONSTRAINT `fk_Invoices_Cars`
    FOREIGN KEY (`Cars_ID`)
    REFERENCES `lab_mysql`.`Cars` (`ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Invoices_Salesperson1`
    FOREIGN KEY (`Salesperson_ID`)
    REFERENCES `lab_mysql`.`Salesperson` (`ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Invoices_Customers1`
    FOREIGN KEY (`Customers_ID`)
    REFERENCES `lab_mysql`.`Customers` (`ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `lab_mysql`.`Customers_has_Salesperson`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `lab_mysql`.`Customers_has_Salesperson` (
  `Customers_ID` INT NOT NULL,
  `Salesperson_ID` INT NOT NULL,
  PRIMARY KEY (`Customers_ID`, `Salesperson_ID`),
  INDEX `fk_Customers_has_Salesperson_Salesperson1_idx` (`Salesperson_ID` ASC) VISIBLE,
  INDEX `fk_Customers_has_Salesperson_Customers1_idx` (`Customers_ID` ASC) VISIBLE,
  CONSTRAINT `fk_Customers_has_Salesperson_Customers1`
    FOREIGN KEY (`Customers_ID`)
    REFERENCES `lab_mysql`.`Customers` (`ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Customers_has_Salesperson_Salesperson1`
    FOREIGN KEY (`Salesperson_ID`)
    REFERENCES `lab_mysql`.`Salesperson` (`ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
