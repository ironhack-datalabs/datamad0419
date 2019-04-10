-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mysql_lab
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mysql_lab
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mysql_lab` DEFAULT CHARACTER SET utf8 ;
USE `mysql_lab` ;

-- -----------------------------------------------------
-- Table `mysql_lab`.`Customers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mysql_lab`.`Customers` (
  `CustomerID` INT NOT NULL,
  `Name` VARCHAR(45) NOT NULL,
  `Phone number` VARCHAR(45) NOT NULL,
  `Email` VARCHAR(45) NULL,
  `Adress` VARCHAR(45) NULL,
  `City` VARCHAR(45) NULL,
  `State/province` VARCHAR(45) NULL,
  `Country` VARCHAR(45) NULL,
  `Zip Postal Code` VARCHAR(45) NULL,
  `Cars_VIN` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`CustomerID`),
  INDEX `fk_Customers_Cars2_idx` (`Cars_VIN` ASC) VISIBLE,
  CONSTRAINT `fk_Customers_Cars2`
    FOREIGN KEY (`Cars_VIN`)
    REFERENCES `mysql_lab`.`Cars` (`VIN`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mysql_lab`.`Cars`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mysql_lab`.`Cars` (
  `VIN` VARCHAR(45) NOT NULL,
  `Manufacturer` VARCHAR(45) NOT NULL,
  `Model` VARCHAR(45) NOT NULL,
  `Year` VARCHAR(45) NOT NULL,
  `Color` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`VIN`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mysql_lab`.`Customers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mysql_lab`.`Customers` (
  `CustomerID` INT NOT NULL,
  `Name` VARCHAR(45) NOT NULL,
  `Phone number` VARCHAR(45) NOT NULL,
  `Email` VARCHAR(45) NULL,
  `Adress` VARCHAR(45) NULL,
  `City` VARCHAR(45) NULL,
  `State/province` VARCHAR(45) NULL,
  `Country` VARCHAR(45) NULL,
  `Zip Postal Code` VARCHAR(45) NULL,
  `Cars_VIN` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`CustomerID`),
  INDEX `fk_Customers_Cars2_idx` (`Cars_VIN` ASC) VISIBLE,
  CONSTRAINT `fk_Customers_Cars2`
    FOREIGN KEY (`Cars_VIN`)
    REFERENCES `mysql_lab`.`Cars` (`VIN`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mysql_lab`.`Salespersons`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mysql_lab`.`Salespersons` (
  `Staff ID` INT NOT NULL,
  `Name` VARCHAR(45) NULL,
  `Store` VARCHAR(45) NULL,
  PRIMARY KEY (`Staff ID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mysql_lab`.`Invoices`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mysql_lab`.`Invoices` (
  `Invoice number` INT NOT NULL,
  `Data` DATE NULL,
  `Customers_CustomerID` INT NOT NULL,
  `Salespersons_Staff ID` INT NOT NULL,
  `Cars_VIN` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`Invoice number`),
  INDEX `fk_Invoices_Customers2_idx` (`Customers_CustomerID` ASC) VISIBLE,
  INDEX `fk_Invoices_Salespersons2_idx` (`Salespersons_Staff ID` ASC) VISIBLE,
  INDEX `fk_Invoices_Cars1_idx` (`Cars_VIN` ASC) VISIBLE,
  CONSTRAINT `fk_Invoices_Customers2`
    FOREIGN KEY (`Customers_CustomerID`)
    REFERENCES `mysql_lab`.`Customers` (`CustomerID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Invoices_Salespersons2`
    FOREIGN KEY (`Salespersons_Staff ID`)
    REFERENCES `mysql_lab`.`Salespersons` (`Staff ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Invoices_Cars1`
    FOREIGN KEY (`Cars_VIN`)
    REFERENCES `mysql_lab`.`Cars` (`VIN`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mysql_lab`.`Cars`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mysql_lab`.`Cars` (
  `VIN` VARCHAR(45) NOT NULL,
  `Manufacturer` VARCHAR(45) NOT NULL,
  `Model` VARCHAR(45) NOT NULL,
  `Year` VARCHAR(45) NOT NULL,
  `Color` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`VIN`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mysql_lab`.`Customers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mysql_lab`.`Customers` (
  `CustomerID` INT NOT NULL,
  `Name` VARCHAR(45) NOT NULL,
  `Phone number` VARCHAR(45) NOT NULL,
  `Email` VARCHAR(45) NULL,
  `Adress` VARCHAR(45) NULL,
  `City` VARCHAR(45) NULL,
  `State/province` VARCHAR(45) NULL,
  `Country` VARCHAR(45) NULL,
  `Zip Postal Code` VARCHAR(45) NULL,
  `Cars_VIN` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`CustomerID`),
  INDEX `fk_Customers_Cars2_idx` (`Cars_VIN` ASC) VISIBLE,
  CONSTRAINT `fk_Customers_Cars2`
    FOREIGN KEY (`Cars_VIN`)
    REFERENCES `mysql_lab`.`Cars` (`VIN`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mysql_lab`.`Salespersons`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mysql_lab`.`Salespersons` (
  `Staff ID` INT NOT NULL,
  `Name` VARCHAR(45) NULL,
  `Store` VARCHAR(45) NULL,
  PRIMARY KEY (`Staff ID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mysql_lab`.`Invoices`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mysql_lab`.`Invoices` (
  `Invoice number` INT NOT NULL,
  `Data` DATE NULL,
  `Customers_CustomerID` INT NOT NULL,
  `Salespersons_Staff ID` INT NOT NULL,
  `Cars_VIN` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`Invoice number`),
  INDEX `fk_Invoices_Customers2_idx` (`Customers_CustomerID` ASC) VISIBLE,
  INDEX `fk_Invoices_Salespersons2_idx` (`Salespersons_Staff ID` ASC) VISIBLE,
  INDEX `fk_Invoices_Cars1_idx` (`Cars_VIN` ASC) VISIBLE,
  CONSTRAINT `fk_Invoices_Customers2`
    FOREIGN KEY (`Customers_CustomerID`)
    REFERENCES `mysql_lab`.`Customers` (`CustomerID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Invoices_Salespersons2`
    FOREIGN KEY (`Salespersons_Staff ID`)
    REFERENCES `mysql_lab`.`Salespersons` (`Staff ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Invoices_Cars1`
    FOREIGN KEY (`Cars_VIN`)
    REFERENCES `mysql_lab`.`Cars` (`VIN`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mysql_lab`.`Salespersons_has_Customers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mysql_lab`.`Salespersons_has_Customers` (
  `Salespersons_Staff ID` INT NOT NULL,
  `Customers_CustomerID` INT NOT NULL,
  PRIMARY KEY (`Salespersons_Staff ID`, `Customers_CustomerID`),
  INDEX `fk_Salespersons_has_Customers_Customers1_idx` (`Customers_CustomerID` ASC) VISIBLE,
  INDEX `fk_Salespersons_has_Customers_Salespersons1_idx` (`Salespersons_Staff ID` ASC) VISIBLE,
  CONSTRAINT `fk_Salespersons_has_Customers_Salespersons1`
    FOREIGN KEY (`Salespersons_Staff ID`)
    REFERENCES `mysql_lab`.`Salespersons` (`Staff ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Salespersons_has_Customers_Customers1`
    FOREIGN KEY (`Customers_CustomerID`)
    REFERENCES `mysql_lab`.`Customers` (`CustomerID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
