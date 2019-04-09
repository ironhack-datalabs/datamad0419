-- MySQL Script generated by MySQL Workbench
-- Tue Apr  9 18:01:25 2019
-- Model: New Model    Version: 1.0
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
-- Table `mydb`.`Costumers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Costumers` (
  `Costumer ID` VARCHAR(20) NOT NULL,
  `Name` VARCHAR(45) NOT NULL,
  `Phone Number` INT NULL,
  `Email` VARCHAR(45) NULL,
  `Address` VARCHAR(50) NULL,
  `City` VARCHAR(20) NULL,
  `State` VARCHAR(20) NULL,
  `Country` VARCHAR(20) NULL,
  `Zip Code` INT NULL,
  PRIMARY KEY (`Costumer ID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Invoices`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Invoices` (
  `Invoice #` VARCHAR(50) NOT NULL,
  `Date` DATE NOT NULL,
  `Car` VARCHAR(45) NOT NULL,
  `Costumer` VARCHAR(45) NOT NULL,
  `Sales person related to car` VARCHAR(45) NULL,
  `Costumers_Costumer ID` VARCHAR(20) NOT NULL,
  PRIMARY KEY (`Invoice #`, `Costumers_Costumer ID`),
  INDEX `fk_Invoices_Costumers1_idx` (`Costumers_Costumer ID` ASC) VISIBLE,
  CONSTRAINT `fk_Invoices_Costumers1`
    FOREIGN KEY (`Costumers_Costumer ID`)
    REFERENCES `mydb`.`Costumers` (`Costumer ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Salespersons`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Salespersons` (
  `Staff Id` VARCHAR(25) NOT NULL,
  `Name` VARCHAR(45) NOT NULL,
  `Store at your company` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`Staff Id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Cars`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Cars` (
  `Vehicle ID` INT NOT NULL,
  `Manufacturer` VARCHAR(45) NOT NULL,
  `Model` VARCHAR(45) NULL,
  `Year` INT NULL,
  `Color` VARCHAR(45) NULL,
  `Invoices_Invoice #` VARCHAR(50) NOT NULL,
  `Costumers_Costumer ID` VARCHAR(20) NOT NULL,
  `Salespersons_Staff Id` VARCHAR(25) NOT NULL,
  PRIMARY KEY (`Vehicle ID`, `Invoices_Invoice #`, `Costumers_Costumer ID`, `Salespersons_Staff Id`),
  INDEX `fk_Cars_Invoices_idx` (`Invoices_Invoice #` ASC) VISIBLE,
  INDEX `fk_Cars_Costumers1_idx` (`Costumers_Costumer ID` ASC) VISIBLE,
  INDEX `fk_Cars_Salespersons1_idx` (`Salespersons_Staff Id` ASC) VISIBLE,
  CONSTRAINT `fk_Cars_Invoices`
    FOREIGN KEY (`Invoices_Invoice #`)
    REFERENCES `mydb`.`Invoices` (`Invoice #`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Cars_Costumers1`
    FOREIGN KEY (`Costumers_Costumer ID`)
    REFERENCES `mydb`.`Costumers` (`Costumer ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Cars_Salespersons1`
    FOREIGN KEY (`Salespersons_Staff Id`)
    REFERENCES `mydb`.`Salespersons` (`Staff Id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Costumers_has_Salespersons`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Costumers_has_Salespersons` (
  `Costumers_Costumer ID` VARCHAR(20) NOT NULL,
  `Salespersons_Staff Id` VARCHAR(25) NOT NULL,
  PRIMARY KEY (`Costumers_Costumer ID`, `Salespersons_Staff Id`),
  INDEX `fk_Costumers_has_Salespersons_Salespersons1_idx` (`Salespersons_Staff Id` ASC) VISIBLE,
  INDEX `fk_Costumers_has_Salespersons_Costumers1_idx` (`Costumers_Costumer ID` ASC) VISIBLE,
  CONSTRAINT `fk_Costumers_has_Salespersons_Costumers1`
    FOREIGN KEY (`Costumers_Costumer ID`)
    REFERENCES `mydb`.`Costumers` (`Costumer ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Costumers_has_Salespersons_Salespersons1`
    FOREIGN KEY (`Salespersons_Staff Id`)
    REFERENCES `mydb`.`Salespersons` (`Staff Id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
