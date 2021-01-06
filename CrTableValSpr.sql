CREATE TABLE `sampledb`.`valut` (
  `cod_val` INT NOT NULL,
  `cod_val_LIT` VARCHAR(3) NULL,
  `count` INT NULL,
  `name_val_UKR` VARCHAR(45) NULL,
  `name_val_RUS` VARCHAR(45) NULL,
  PRIMARY KEY (`cod_val`));


Соединение с БД установлено
[('sampledb.course', 'check', 'Error', "Table 'sampledb.course' doesn't exist"), 
('sampledb.course', 'check', 'status', 'Operation failed')]

Соединение с БД установлено
[('sampledb.valut', 'check', 'status', 'OK')]