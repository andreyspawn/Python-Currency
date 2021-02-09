import os
import configparser
import mysql.connector

#открывание ini-файла на чтение в текущем каталоге
def open_ini(file_name:str):
	path_config = os.getcwd()+'\\'+file_name
	config = configparser.ConfigParser()
	config.read(path_config)
	return config


config = open_ini('config.ini')

dbconfig = {
	'host':config.get('Connect_Params','host'),
	'user':config.get('Connect_Params','user'),
	'password':config.get('Connect_Params','password'),
	'database':config.get('Connect_Params','base')
	}

try:
	conn = mysql.connector.connect(**dbconfig)
except Exception:
	print('Не могу открыть БД')
else:
	print('Соединение с БД установлено')
	cursor = conn.cursor()

# Создадим таблицу справочника валют с характеристиками
#cod_val INT - код валюты  
#cod_val_LIT VARCHAR(3) код валюты буквенный  
#count INT количество единиц валюты, для которых получаем курс  
#name_val_UKR VARCHAR(45) наименование валюты на украинском языке
#name_val_RUS VARCHAR(45) наименование валюты на русском языке

_SQL = 'CREATE TABLE  ' + dbconfig['database'] + '.valut (  `cod_val` INT NOT NULL,  `cod_val_LIT` VARCHAR(3) NULL,  `count` INT NULL,  `name_val_UKR` VARCHAR(45) NULL,  `name_val_RUS` VARCHAR(45) NULL,  PRIMARY KEY (`cod_val`));'
try:
	cursor.execute(_SQL)
except Exception:
	print('Проблема с созданием таблицы')

# таблица непосредственно для курсов
# data_currency DATA NULL дата курса
# cod_val INT количество единиц
# amount FLOAT(2) стоимость валюты
_SQL = 'CREATE TABLE  ' + dbconfig['database'] + '.currency (  `data_currency` DATE, `cod_val` INT NOT NULL, `amount` FLOAT(2) NOT NULL);'
try:
	cursor.execute(_SQL)
except Exception:
	print('Проблема с созданием таблицы')
