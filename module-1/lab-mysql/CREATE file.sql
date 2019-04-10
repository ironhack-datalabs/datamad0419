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
-- Table `lab-mysql`.`concessionaire`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `lab-mysql`.`concessionaire` (
  `idconcessionaire` INT NOT NULL,
  `name` VARCHAR(45) NULL,
  `address` VARCHAR(45) NULL,
  `phone` VARCHAR(45) NULL,
  `VATcode` VARCHAR(45) NULL,
  PRIMARY KEY (`idconcessionaire`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `lab-mysql`.`Manufacturer`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `lab-mysql`.`Manufacturer` (
  `idmanufacturer` INT NOT NULL,
  `name` VARCHAR(45) NULL,
  PRIMARY KEY (`idmanufacturer`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `lab-mysql`.`Car brand`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `lab-mysql`.`Car brand` (
  `idCar brand` INT NOT NULL,
  `brand name` VARCHAR(45) NULL,
  `Automotion groups_idAutomotion groups` INT NOT NULL,
  PRIMARY KEY (`idCar brand`, `Automotion groups_idAutomotion groups`),
  INDEX `fk_Car brand_Automotion groups1_idx` (`Automotion groups_idAutomotion groups` ASC) VISIBLE,
  CONSTRAINT `fk_Car brand_Automotion groups1`
    FOREIGN KEY (`Automotion groups_idAutomotion groups`)
    REFERENCES `lab-mysql`.`Manufacturer` (`idmanufacturer`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `lab-mysql`.`Clients`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `lab-mysql`.`Clients` (
  `idClients` INT NOT NULL,
  `name` VARCHAR(45) NULL,
  `surname` VARCHAR(45) NULL,
  `adress` VARCHAR(45) NULL,
  `phone` VARCHAR(45) NULL,
  `inscription_date` DATE NULL,
  PRIMARY KEY (`idClients`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `lab-mysql`.`Job`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `lab-mysql`.`Job` (
  `idJob` INT NOT NULL,
  `job title` VARCHAR(45) NULL,
  `fix salary` VARCHAR(45) NULL,
  `variable salary` VARCHAR(45) NULL,
  `date_jobassign` VARCHAR(45) NULL,
  `contract_type` VARCHAR(45) NULL,
  PRIMARY KEY (`idJob`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `lab-mysql`.`Employee`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `lab-mysql`.`Employee` (
  `idEmployee` INT NOT NULL,
  `name` VARCHAR(45) NULL,
  `surname` VARCHAR(45) NULL,
  `ss_code` VARCHAR(45) NULL,
  `phone` VARCHAR(45) NULL,
  `seniority_date` DATE NULL,
  `job` VARCHAR(45) NULL,
  `Job_idJob` INT NOT NULL,
  `concessionaire_idconcessionaire` INT NOT NULL,
  PRIMARY KEY (`idEmployee`, `concessionaire_idconcessionaire`),
  INDEX `fk_Employee_Job1_idx` (`Job_idJob` ASC) VISIBLE,
  INDEX `fk_Employee_concessionaire1_idx` (`concessionaire_idconcessionaire` ASC) VISIBLE,
  CONSTRAINT `fk_Employee_Job1`
    FOREIGN KEY (`Job_idJob`)
    REFERENCES `lab-mysql`.`Job` (`idJob`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Employee_concessionaire1`
    FOREIGN KEY (`concessionaire_idconcessionaire`)
    REFERENCES `lab-mysql`.`concessionaire` (`idconcessionaire`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `lab-mysql`.`Retail Shop`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `lab-mysql`.`Retail Shop` (
  `idRetail Shop` INT NOT NULL,
  `address` VARCHAR(45) NULL,
  `phone` VARCHAR(45) NULL,
  `concessionaire_idconcessionaire` INT NOT NULL,
  `Employee_idEmployee` INT NOT NULL,
  `Bill_idbill` INT NOT NULL,
  `Bill_Clients_idClients` INT NOT NULL,
  `Bill_concessionaire_idconcessionaire` INT NOT NULL,
  `Bill_Employee_idEmployee` INT NOT NULL,
  `Bill_Retail Shop_idRetail Shop` INT NOT NULL,
  `Bill_Retail Shop_concessionaire_idconcessionaire` INT NOT NULL,
  `Bill_Retail Shop_Employee_idEmployee` INT NOT NULL,
  PRIMARY KEY (`idRetail Shop`, `concessionaire_idconcessionaire`, `Employee_idEmployee`, `Bill_idbill`, `Bill_Clients_idClients`, `Bill_concessionaire_idconcessionaire`, `Bill_Employee_idEmployee`, `Bill_Retail Shop_idRetail Shop`, `Bill_Retail Shop_concessionaire_idconcessionaire`, `Bill_Retail Shop_Employee_idEmployee`),
  INDEX `fk_Retail Shop_concessionaire1_idx` (`concessionaire_idconcessionaire` ASC) VISIBLE,
  INDEX `fk_Retail Shop_Employee1_idx` (`Employee_idEmployee` ASC) VISIBLE,
  INDEX `fk_Retail Shop_Bill1_idx` (`Bill_idbill` ASC, `Bill_Clients_idClients` ASC, `Bill_concessionaire_idconcessionaire` ASC, `Bill_Employee_idEmployee` ASC, `Bill_Retail Shop_idRetail Shop` ASC, `Bill_Retail Shop_concessionaire_idconcessionaire` ASC, `Bill_Retail Shop_Employee_idEmployee` ASC) VISIBLE,
  CONSTRAINT `fk_Retail Shop_concessionaire1`
    FOREIGN KEY (`concessionaire_idconcessionaire`)
    REFERENCES `lab-mysql`.`concessionaire` (`idconcessionaire`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Retail Shop_Employee1`
    FOREIGN KEY (`Employee_idEmployee`)
    REFERENCES `lab-mysql`.`Employee` (`idEmployee`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Retail Shop_Bill1`
    FOREIGN KEY (`Bill_idbill` , `Bill_Clients_idClients` , `Bill_concessionaire_idconcessionaire` , `Bill_Employee_idEmployee` , `Bill_Retail Shop_idRetail Shop` , `Bill_Retail Shop_concessionaire_idconcessionaire` , `Bill_Retail Shop_Employee_idEmployee`)
    REFERENCES `lab-mysql`.`Bill` (`idbill` , `Clients_idClients` , `concessionaire_idconcessionaire` , `Employee_idEmployee` , `Retail Shop_idRetail Shop` , `Retail Shop_concessionaire_idconcessionaire` , `Retail Shop_Employee_idEmployee`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `lab-mysql`.`discount`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `lab-mysql`.`discount` (
  `iddiscount` INT NOT NULL,
  `date` DATETIME NULL,
  `discount` INT NULL,
  `Car model_idCar model` INT NOT NULL,
  `Car model_Car brand_idCar brand` INT NOT NULL,
  `Car model_Car brand_Automotion groups_idAutomotion groups` INT NOT NULL,
  `Car model_Bill_idbill` INT NOT NULL,
  `Car model_Bill_Clients_idClients` INT NOT NULL,
  `Car model_Bill_concessionaire_idconcessionaire` INT NOT NULL,
  `Car model_Bill_Employee_idEmployee` INT NOT NULL,
  `Car model_Retail Shop_idRetail Shop` INT NOT NULL,
  `Car model_Retail Shop_concessionaire_idconcessionaire` INT NOT NULL,
  `Car model_Retail Shop_Employee_idEmployee` INT NOT NULL,
  `Car model_Retail Shop_Bill_idbill` INT NOT NULL,
  `Car model_Retail Shop_Bill_Clients_idClients` INT NOT NULL,
  `Car model_Retail Shop_Bill_concessionaire_idconcessionaire` INT NOT NULL,
  `Car model_Retail Shop_Bill_Employee_idEmployee` INT NOT NULL,
  `Car model_Retail Shop_Bill_Retail Shop_idRetail Shop` INT NOT NULL,
  `Car model_Retail Shop_Bill_Retail Shop_concessionaire_idconcessionaire` INT NOT NULL,
  `Car model_Retail Shop_Bill_Retail Shop_Employee_idEmployee` INT NOT NULL,
  PRIMARY KEY (`iddiscount`, `Car model_idCar model`, `Car model_Car brand_idCar brand`, `Car model_Car brand_Automotion groups_idAutomotion groups`, `Car model_Bill_idbill`, `Car model_Bill_Clients_idClients`, `Car model_Bill_concessionaire_idconcessionaire`, `Car model_Bill_Employee_idEmployee`, `Car model_Retail Shop_idRetail Shop`, `Car model_Retail Shop_concessionaire_idconcessionaire`, `Car model_Retail Shop_Employee_idEmployee`, `Car model_Retail Shop_Bill_idbill`, `Car model_Retail Shop_Bill_Clients_idClients`, `Car model_Retail Shop_Bill_concessionaire_idconcessionaire`, `Car model_Retail Shop_Bill_Employee_idEmployee`, `Car model_Retail Shop_Bill_Retail Shop_idRetail Shop`, `Car model_Retail Shop_Bill_Retail Shop_concessionaire_idconcessionaire`, `Car model_Retail Shop_Bill_Retail Shop_Employee_idEmployee`),
  INDEX `fk_discount_Car model1_idx` (`Car model_idCar model` ASC, `Car model_Car brand_idCar brand` ASC, `Car model_Car brand_Automotion groups_idAutomotion groups` ASC, `Car model_Bill_idbill` ASC, `Car model_Bill_Clients_idClients` ASC, `Car model_Bill_concessionaire_idconcessionaire` ASC, `Car model_Bill_Employee_idEmployee` ASC, `Car model_Retail Shop_idRetail Shop` ASC, `Car model_Retail Shop_concessionaire_idconcessionaire` ASC, `Car model_Retail Shop_Employee_idEmployee` ASC, `Car model_Retail Shop_Bill_idbill` ASC, `Car model_Retail Shop_Bill_Clients_idClients` ASC, `Car model_Retail Shop_Bill_concessionaire_idconcessionaire` ASC, `Car model_Retail Shop_Bill_Employee_idEmployee` ASC, `Car model_Retail Shop_Bill_Retail Shop_idRetail Shop` ASC, `Car model_Retail Shop_Bill_Retail Shop_concessionaire_idconcessionaire` ASC, `Car model_Retail Shop_Bill_Retail Shop_Employee_idEmployee` ASC) VISIBLE,
  CONSTRAINT `fk_discount_Car model1`
    FOREIGN KEY (`Car model_idCar model` , `Car model_Car brand_idCar brand` , `Car model_Car brand_Automotion groups_idAutomotion groups` , `Car model_Bill_idbill` , `Car model_Bill_Clients_idClients` , `Car model_Bill_concessionaire_idconcessionaire` , `Car model_Bill_Employee_idEmployee` , `Car model_Retail Shop_idRetail Shop` , `Car model_Retail Shop_concessionaire_idconcessionaire` , `Car model_Retail Shop_Employee_idEmployee` , `Car model_Retail Shop_Bill_idbill` , `Car model_Retail Shop_Bill_Clients_idClients` , `Car model_Retail Shop_Bill_concessionaire_idconcessionaire` , `Car model_Retail Shop_Bill_Employee_idEmployee` , `Car model_Retail Shop_Bill_Retail Shop_idRetail Shop` , `Car model_Retail Shop_Bill_Retail Shop_concessionaire_idconcessionaire` , `Car model_Retail Shop_Bill_Retail Shop_Employee_idEmployee`)
    REFERENCES `lab-mysql`.`Car model` (`idCar model` , `Car brand_idCar brand` , `Car brand_idmanufact` , `Bill_idbill` , `Bill_Clients_idClients` , `Bill_conc_idconc` , `Bill_Employee_idEmployee` , `Retail Shop_idRetail Shop` , `Retail Shop_conc_idconc` , `Retail Shop_Employee_idEmployee` , `Retail Shop_Bill_idbill` , `Retail Shop_Bill_Clients_idClients` , `Retail Shop_Bill_conc_idconc` , `Retail Shop_Bill_Employee_idEmployee` , `Retail Shop_Bill_Retail Shop_idRetail Shop` , `Retail Shop_Bill_Retail Shop_conc_idconc` , `Retail Shop_Bill_Retail Shop_Emp_idEmp`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `lab-mysql`.`Bill`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `lab-mysql`.`Bill` (
  `idbill` INT NOT NULL,
  `Clients_idClients` INT NOT NULL,
  `concessionaire_idconcessionaire` INT NOT NULL,
  `Employee_idEmployee` INT NOT NULL,
  `Retail Shop_idRetail Shop` INT NOT NULL,
  `Retail Shop_concessionaire_idconcessionaire` INT NOT NULL,
  `Retail Shop_Employee_idEmployee` INT NOT NULL,
  `Retail Shop_idRetail Shop1` INT NOT NULL,
  `Retail Shop_concessionaire_idconcessionaire1` INT NOT NULL,
  `Retail Shop_Employee_idEmployee1` INT NOT NULL,
  `Retail Shop_Bill_idbill` INT NOT NULL,
  `Retail Shop_Bill_Clients_idClients` INT NOT NULL,
  `Retail Shop_Bill_concessionaire_idconcessionaire` INT NOT NULL,
  `Retail Shop_Bill_Employee_idEmployee` INT NOT NULL,
  `Retail Shop_Bill_Retail Shop_idRetail Shop` INT NOT NULL,
  `Retail Shop_Bill_Retail Shop_concessionaire_idconcessionaire` INT NOT NULL,
  `Retail Shop_Bill_Retail Shop_Employee_idEmployee` INT NOT NULL,
  `discount_iddiscount` INT NOT NULL,
  `discount_Car model_idCar model` INT NOT NULL,
  `discount_Car model_Car brand_idCar brand` INT NOT NULL,
  `discount_Car model_Car brand_Automotion groups_idAutomotion groups` INT NOT NULL,
  `discount_Car model_Bill_idbill` INT NOT NULL,
  `discount_Car model_Bill_Clients_idClients` INT NOT NULL,
  `discount_Car model_Bill_concessionaire_idconcessionaire` INT NOT NULL,
  `discount_Car model_Bill_Employee_idEmployee` INT NOT NULL,
  `discount_Car model_Retail Shop_idRetail Shop` INT NOT NULL,
  `discount_Car model_Retail Shop_concessionaire_idconcessionaire` INT NOT NULL,
  `discount_Car model_Retail Shop_Employee_idEmployee` INT NOT NULL,
  `discount_Car model_Retail Shop_Bill_idbill` INT NOT NULL,
  `discount_Car model_Retail Shop_Bill_Clients_idClients` INT NOT NULL,
  `discount_Car model_Retail Shop_Bill_concessionaire_idconcessionaire` INT NOT NULL,
  `discount_Car model_Retail Shop_Bill_Employee_idEmployee` INT NOT NULL,
  `discount_Car model_Retail Shop_Bill_Retail Shop_idRetail Shop` INT NOT NULL,
  `discount_Car model_Retail Shop_Bill_Retail Shop_concessionaire_idconcessionaire` INT NOT NULL,
  `discount_Car model_Retail Shop_Bill_Retail Shop_Employee_idEmployee` INT NOT NULL,
  PRIMARY KEY (`idbill`, `Clients_idClients`, `concessionaire_idconcessionaire`, `Employee_idEmployee`, `Retail Shop_idRetail Shop`, `Retail Shop_concessionaire_idconcessionaire`, `Retail Shop_Employee_idEmployee`, `Retail Shop_idRetail Shop1`, `Retail Shop_concessionaire_idconcessionaire1`, `Retail Shop_Employee_idEmployee1`, `Retail Shop_Bill_idbill`, `Retail Shop_Bill_Clients_idClients`, `Retail Shop_Bill_concessionaire_idconcessionaire`, `Retail Shop_Bill_Employee_idEmployee`, `Retail Shop_Bill_Retail Shop_idRetail Shop`, `Retail Shop_Bill_Retail Shop_concessionaire_idconcessionaire`, `Retail Shop_Bill_Retail Shop_Employee_idEmployee`, `discount_iddiscount`, `discount_Car model_idCar model`, `discount_Car model_Car brand_idCar brand`, `discount_Car model_Car brand_Automotion groups_idAutomotion groups`, `discount_Car model_Bill_idbill`, `discount_Car model_Bill_Clients_idClients`, `discount_Car model_Bill_concessionaire_idconcessionaire`, `discount_Car model_Bill_Employee_idEmployee`, `discount_Car model_Retail Shop_idRetail Shop`, `discount_Car model_Retail Shop_concessionaire_idconcessionaire`, `discount_Car model_Retail Shop_Employee_idEmployee`, `discount_Car model_Retail Shop_Bill_idbill`, `discount_Car model_Retail Shop_Bill_Clients_idClients`, `discount_Car model_Retail Shop_Bill_concessionaire_idconcessionaire`, `discount_Car model_Retail Shop_Bill_Employee_idEmployee`, `discount_Car model_Retail Shop_Bill_Retail Shop_idRetail Shop`, `discount_Car model_Retail Shop_Bill_Retail Shop_concessionaire_idconcessionaire`, `discount_Car model_Retail Shop_Bill_Retail Shop_Employee_idEmployee`),
  INDEX `fk_Bill_Clients1_idx` (`Clients_idClients` ASC) VISIBLE,
  INDEX `fk_Bill_concessionaire1_idx` (`concessionaire_idconcessionaire` ASC) VISIBLE,
  INDEX `fk_Bill_Employee1_idx` (`Employee_idEmployee` ASC) VISIBLE,
  INDEX `fk_Bill_Retail Shop1_idx` (`Retail Shop_idRetail Shop` ASC, `Retail Shop_concessionaire_idconcessionaire` ASC, `Retail Shop_Employee_idEmployee` ASC) VISIBLE,
  INDEX `fk_Bill_Retail Shop2_idx` (`Retail Shop_idRetail Shop1` ASC, `Retail Shop_concessionaire_idconcessionaire1` ASC, `Retail Shop_Employee_idEmployee1` ASC, `Retail Shop_Bill_idbill` ASC, `Retail Shop_Bill_Clients_idClients` ASC, `Retail Shop_Bill_concessionaire_idconcessionaire` ASC, `Retail Shop_Bill_Employee_idEmployee` ASC, `Retail Shop_Bill_Retail Shop_idRetail Shop` ASC, `Retail Shop_Bill_Retail Shop_concessionaire_idconcessionaire` ASC, `Retail Shop_Bill_Retail Shop_Employee_idEmployee` ASC) VISIBLE,
  INDEX `fk_Bill_discount1_idx` (`discount_iddiscount` ASC, `discount_Car model_idCar model` ASC, `discount_Car model_Car brand_idCar brand` ASC, `discount_Car model_Car brand_Automotion groups_idAutomotion groups` ASC, `discount_Car model_Bill_idbill` ASC, `discount_Car model_Bill_Clients_idClients` ASC, `discount_Car model_Bill_concessionaire_idconcessionaire` ASC, `discount_Car model_Bill_Employee_idEmployee` ASC, `discount_Car model_Retail Shop_idRetail Shop` ASC, `discount_Car model_Retail Shop_concessionaire_idconcessionaire` ASC, `discount_Car model_Retail Shop_Employee_idEmployee` ASC, `discount_Car model_Retail Shop_Bill_idbill` ASC, `discount_Car model_Retail Shop_Bill_Clients_idClients` ASC, `discount_Car model_Retail Shop_Bill_concessionaire_idconcessionaire` ASC, `discount_Car model_Retail Shop_Bill_Employee_idEmployee` ASC, `discount_Car model_Retail Shop_Bill_Retail Shop_idRetail Shop` ASC, `discount_Car model_Retail Shop_Bill_Retail Shop_concessionaire_idconcessionaire` ASC, `discount_Car model_Retail Shop_Bill_Retail Shop_Employee_idEmployee` ASC) VISIBLE,
  CONSTRAINT `fk_Bill_Clients1`
    FOREIGN KEY (`Clients_idClients`)
    REFERENCES `lab-mysql`.`Clients` (`idClients`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Bill_concessionaire1`
    FOREIGN KEY (`concessionaire_idconcessionaire`)
    REFERENCES `lab-mysql`.`concessionaire` (`idconcessionaire`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Bill_Employee1`
    FOREIGN KEY (`Employee_idEmployee`)
    REFERENCES `lab-mysql`.`Employee` (`idEmployee`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Bill_Retail Shop1`
    FOREIGN KEY (`Retail Shop_idRetail Shop` , `Retail Shop_concessionaire_idconcessionaire` , `Retail Shop_Employee_idEmployee`)
    REFERENCES `lab-mysql`.`Retail Shop` (`idRetail Shop` , `concessionaire_idconcessionaire` , `Employee_idEmployee`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Bill_Retail Shop2`
    FOREIGN KEY (`Retail Shop_idRetail Shop1` , `Retail Shop_concessionaire_idconcessionaire1` , `Retail Shop_Employee_idEmployee1` , `Retail Shop_Bill_idbill` , `Retail Shop_Bill_Clients_idClients` , `Retail Shop_Bill_concessionaire_idconcessionaire` , `Retail Shop_Bill_Employee_idEmployee` , `Retail Shop_Bill_Retail Shop_idRetail Shop` , `Retail Shop_Bill_Retail Shop_concessionaire_idconcessionaire` , `Retail Shop_Bill_Retail Shop_Employee_idEmployee`)
    REFERENCES `lab-mysql`.`Retail Shop` (`idRetail Shop` , `concessionaire_idconcessionaire` , `Employee_idEmployee` , `Bill_idbill` , `Bill_Clients_idClients` , `Bill_concessionaire_idconcessionaire` , `Bill_Employee_idEmployee` , `Bill_Retail Shop_idRetail Shop` , `Bill_Retail Shop_concessionaire_idconcessionaire` , `Bill_Retail Shop_Employee_idEmployee`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Bill_discount1`
    FOREIGN KEY (`discount_iddiscount` , `discount_Car model_idCar model` , `discount_Car model_Car brand_idCar brand` , `discount_Car model_Car brand_Automotion groups_idAutomotion groups` , `discount_Car model_Bill_idbill` , `discount_Car model_Bill_Clients_idClients` , `discount_Car model_Bill_concessionaire_idconcessionaire` , `discount_Car model_Bill_Employee_idEmployee` , `discount_Car model_Retail Shop_idRetail Shop` , `discount_Car model_Retail Shop_concessionaire_idconcessionaire` , `discount_Car model_Retail Shop_Employee_idEmployee` , `discount_Car model_Retail Shop_Bill_idbill` , `discount_Car model_Retail Shop_Bill_Clients_idClients` , `discount_Car model_Retail Shop_Bill_concessionaire_idconcessionaire` , `discount_Car model_Retail Shop_Bill_Employee_idEmployee` , `discount_Car model_Retail Shop_Bill_Retail Shop_idRetail Shop` , `discount_Car model_Retail Shop_Bill_Retail Shop_concessionaire_idconcessionaire` , `discount_Car model_Retail Shop_Bill_Retail Shop_Employee_idEmployee`)
    REFERENCES `lab-mysql`.`discount` (`iddiscount` , `Car model_idCar model` , `Car model_Car brand_idCar brand` , `Car model_Car brand_Automotion groups_idAutomotion groups` , `Car model_Bill_idbill` , `Car model_Bill_Clients_idClients` , `Car model_Bill_concessionaire_idconcessionaire` , `Car model_Bill_Employee_idEmployee` , `Car model_Retail Shop_idRetail Shop` , `Car model_Retail Shop_concessionaire_idconcessionaire` , `Car model_Retail Shop_Employee_idEmployee` , `Car model_Retail Shop_Bill_idbill` , `Car model_Retail Shop_Bill_Clients_idClients` , `Car model_Retail Shop_Bill_concessionaire_idconcessionaire` , `Car model_Retail Shop_Bill_Employee_idEmployee` , `Car model_Retail Shop_Bill_Retail Shop_idRetail Shop` , `Car model_Retail Shop_Bill_Retail Shop_concessionaire_idconcessionaire` , `Car model_Retail Shop_Bill_Retail Shop_Employee_idEmployee`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `lab-mysql`.`Car model`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `lab-mysql`.`Car model` (
  `idCar model` INT NOT NULL,
  `name` VARCHAR(45) NULL,
  `price` FLOAT NULL,
  `Car brand_idCar brand` INT NOT NULL,
  `Car brand_idmanufact` INT NOT NULL,
  `vin` VARCHAR(45) NULL,
  `year` DATE NULL,
  `color` DATE NULL,
  `Bill_idbill` INT NOT NULL,
  `Bill_Clients_idClients` INT NOT NULL,
  `Bill_conc_idconc` INT NOT NULL,
  `Bill_Employee_idEmployee` INT NOT NULL,
  `Retail Shop_idRetail Shop` INT NOT NULL,
  `Retail Shop_conc_idconc` INT NOT NULL,
  `Retail Shop_Employee_idEmployee` INT NOT NULL,
  `Retail Shop_Bill_idbill` INT NOT NULL,
  `Retail Shop_Bill_Clients_idClients` INT NOT NULL,
  `Retail Shop_Bill_conc_idconc` INT NOT NULL,
  `Retail Shop_Bill_Employee_idEmployee` INT NOT NULL,
  `Retail Shop_Bill_Retail Shop_idRetail Shop` INT NOT NULL,
  `Retail Shop_Bill_Retail Shop_conc_idconc` INT NOT NULL,
  `Retail Shop_Bill_Retail Shop_Emp_idEmp` INT NOT NULL,
  PRIMARY KEY (`idCar model`, `Car brand_idCar brand`, `Car brand_idmanufact`, `Bill_idbill`, `Bill_Clients_idClients`, `Bill_conc_idconc`, `Bill_Employee_idEmployee`, `Retail Shop_idRetail Shop`, `Retail Shop_conc_idconc`, `Retail Shop_Employee_idEmployee`, `Retail Shop_Bill_idbill`, `Retail Shop_Bill_Clients_idClients`, `Retail Shop_Bill_conc_idconc`, `Retail Shop_Bill_Employee_idEmployee`, `Retail Shop_Bill_Retail Shop_idRetail Shop`, `Retail Shop_Bill_Retail Shop_conc_idconc`, `Retail Shop_Bill_Retail Shop_Emp_idEmp`),
  INDEX `fk_Car model_Car brand1_idx` (`Car brand_idCar brand` ASC, `Car brand_idmanufact` ASC) VISIBLE,
  INDEX `fk_Car model_Bill1_idx` (`Bill_idbill` ASC, `Bill_Clients_idClients` ASC, `Bill_conc_idconc` ASC, `Bill_Employee_idEmployee` ASC) VISIBLE,
  INDEX `fk_Car model_Retail Shop1_idx` (`Retail Shop_idRetail Shop` ASC, `Retail Shop_conc_idconc` ASC, `Retail Shop_Employee_idEmployee` ASC, `Retail Shop_Bill_idbill` ASC, `Retail Shop_Bill_Clients_idClients` ASC, `Retail Shop_Bill_conc_idconc` ASC, `Retail Shop_Bill_Employee_idEmployee` ASC, `Retail Shop_Bill_Retail Shop_idRetail Shop` ASC, `Retail Shop_Bill_Retail Shop_conc_idconc` ASC, `Retail Shop_Bill_Retail Shop_Emp_idEmp` ASC) VISIBLE,
  CONSTRAINT `fk_Car model_Car brand1`
    FOREIGN KEY (`Car brand_idCar brand` , `Car brand_idmanufact`)
    REFERENCES `lab-mysql`.`Car brand` (`idCar brand` , `Automotion groups_idAutomotion groups`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Car model_Bill1`
    FOREIGN KEY (`Bill_idbill` , `Bill_Clients_idClients` , `Bill_conc_idconc` , `Bill_Employee_idEmployee`)
    REFERENCES `lab-mysql`.`Bill` (`idbill` , `Clients_idClients` , `concessionaire_idconcessionaire` , `Employee_idEmployee`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Car model_Retail Shop1`
    FOREIGN KEY (`Retail Shop_idRetail Shop` , `Retail Shop_conc_idconc` , `Retail Shop_Employee_idEmployee` , `Retail Shop_Bill_idbill` , `Retail Shop_Bill_Clients_idClients` , `Retail Shop_Bill_conc_idconc` , `Retail Shop_Bill_Employee_idEmployee` , `Retail Shop_Bill_Retail Shop_idRetail Shop` , `Retail Shop_Bill_Retail Shop_conc_idconc` , `Retail Shop_Bill_Retail Shop_Emp_idEmp`)
    REFERENCES `lab-mysql`.`Retail Shop` (`idRetail Shop` , `concessionaire_idconcessionaire` , `Employee_idEmployee` , `Bill_idbill` , `Bill_Clients_idClients` , `Bill_concessionaire_idconcessionaire` , `Bill_Employee_idEmployee` , `Bill_Retail Shop_idRetail Shop` , `Bill_Retail Shop_concessionaire_idconcessionaire` , `Bill_Retail Shop_Employee_idEmployee`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `lab-mysql`.`table1`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `lab-mysql`.`table1` (
)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
