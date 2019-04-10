-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema lab_mysql
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema lab_mysql
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `lab_mysql` DEFAULT CHARACTER SET utf8 ;
USE `lab_mysql` ;

-- -----------------------------------------------------
-- Table `lab_mysql`.`Vendedor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `lab_mysql`.`Vendedor` (
  `idvendedor` INT NOT NULL,
  `staff` VARCHAR(45) NULL,
  `Nombre` VARCHAR(45) NULL,
  `Vendedorcol` VARCHAR(45) NULL,
  PRIMARY KEY (`idvendedor`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `lab_mysql`.`Comprador`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `lab_mysql`.`Comprador` (
  `idComprador` INT NOT NULL,
  `Name` VARCHAR(45) NULL,
  `Telefono` VARCHAR(45) NULL,
  `email` VARCHAR(45) NULL,
  `ciudad` VARCHAR(45) NULL,
  `pais` VARCHAR(45) NULL,
  `Vendedor_idvendedor` INT NOT NULL,
  PRIMARY KEY (`idComprador`, `Vendedor_idvendedor`),
  INDEX `fk_Comprador_Vendedor1_idx` (`Vendedor_idvendedor` ASC),
  CONSTRAINT `fk_Comprador_Vendedor1`
    FOREIGN KEY (`Vendedor_idvendedor`)
    REFERENCES `lab_mysql`.`Vendedor` (`idvendedor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `lab_mysql`.`Coche`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `lab_mysql`.`Coche` (
  `idCoche` INT NOT NULL,
  `VIN` VARCHAR(45) NULL,
  `Fabricante` VARCHAR(45) NULL,
  `modelo` VARCHAR(45) NULL,
  `año` DATE NULL,
  `Color` VARCHAR(45) NULL,
  `Comprador_idComprador` INT NOT NULL,
  `Vendedor_idvendedor` INT NOT NULL,
  PRIMARY KEY (`idCoche`, `Comprador_idComprador`, `Vendedor_idvendedor`),
  INDEX `fk_Coche_Comprador1_idx` (`Comprador_idComprador` ASC),
  INDEX `fk_Coche_Vendedor1_idx` (`Vendedor_idvendedor` ASC),
  CONSTRAINT `fk_Coche_Comprador1`
    FOREIGN KEY (`Comprador_idComprador`)
    REFERENCES `lab_mysql`.`Comprador` (`idComprador`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Coche_Vendedor1`
    FOREIGN KEY (`Vendedor_idvendedor`)
    REFERENCES `lab_mysql`.`Vendedor` (`idvendedor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `lab_mysql`.`Factura`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `lab_mysql`.`Factura` (
  `idFactura` INT NOT NULL AUTO_INCREMENT,
  `numero factura` VARCHAR(45) NULL,
  `Fecha` VARCHAR(45) NULL,
  `coches` VARCHAR(45) NULL,
  `numero vendedor` VARCHAR(45) NULL,
  `numero cliente` VARCHAR(45) NULL,
  `Vendedor_idvendedor` INT NOT NULL,
  `Comprador_idComprador` INT NOT NULL,
  `Coche_idCoche` INT NOT NULL,
  PRIMARY KEY (`idFactura`, `Vendedor_idvendedor`, `Coche_idCoche`),
  INDEX `fk_Factura_Vendedor_idx` (`Vendedor_idvendedor` ASC),
  INDEX `fk_Factura_Comprador1_idx` (`Comprador_idComprador` ASC),
  INDEX `fk_Factura_Coche1_idx` (`Coche_idCoche` ASC),
  CONSTRAINT `fk_Factura_Vendedor`
    FOREIGN KEY (`Vendedor_idvendedor`)
    REFERENCES `lab_mysql`.`Vendedor` (`idvendedor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Factura_Comprador1`
    FOREIGN KEY (`Comprador_idComprador`)
    REFERENCES `lab_mysql`.`Comprador` (`idComprador`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Factura_Coche1`
    FOREIGN KEY (`Coche_idCoche`)
    REFERENCES `lab_mysql`.`Coche` (`idCoche`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
