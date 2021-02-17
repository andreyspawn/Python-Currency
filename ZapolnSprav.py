# считывание текстовых данных из файла с разделителем в виде табуляции
# и занесение в таблицу MySQL - в данном случае - заполнение справочника валют
import os
import configparser
import mysql.connector
import csv

#процедура открывание ini-файла на чтение в текущем каталоге
# возвращает объект config, связанный с открытм файлом
def open_ini(file_name:str):
	path_config = os.getcwd()+'\\'+file_name
	config = configparser.ConfigParser()
	config.read(path_config)
	return config

# открываем файл и считываем строки с преобразованием их в список наборов
# def form_list_valut(file_name:str):
# 	list_valut = []
# 	with open(file_name,encoding='utf-8') as file_sprav:
# 		for chore in file_sprav:
# 			print(chore)
# 			list_valut.append(chore.split('\t'))
# 			# list_valut .append(chore_list) 
# 	return list_valut


# читаем текстовый файл, как csv 
# и все его записи возвращаем в виде списка словарей
def read_Currency_list(file_name:str):
	currency_list = []
	with open(file_name, encoding='utf-8') as csvfile:
		csvfile_read = csv.DictReader(csvfile,delimiter=':')
		for row in csvfile_read:
			currency_list.append(row)
	return currency_list

# ТЕЛО СКРИПТА

#initialize ini-file
config = open_ini('config.ini')

# write to dictionary connection parameters for database, that was point in ini-file 
dbconfig = {
	'host':config.get('Connect_Params','host'),
	'user':config.get('Connect_Params','user'),
	'password':config.get('Connect_Params','password'),
	'database':config.get('Connect_Params','base')
	}

# try connect to database
try:
	conn = mysql.connector.connect(**dbconfig)
except Exception:
	print('Не могу открыть БД')
else:
	print('Соединение с БД установлено')
	cursor = conn.cursor()


# variant 2 to check for extension table in database 
_SQL = 'show tables like ' + '\'currency\''
cursor.execute(_SQL)
slst = cursor.fetchall()
print(slst)
try:
	if 'currency' in slst[0]:
		print('Табличка есть')
except Exception:
	print('Таблички нет!!!!!')

# делаем заливку данных по валюте из CSV в базу данных - таблица currency
# считываем в переменную currency_list список словарей
currency_list = read_Currency_list('SpravVal.txt')
# Перебираем список поэлементно - выбираем каждый словарь из списка
for row in currency_list:
	# Делаем запрос из таблицы справочника валют по коду валюты
	_SQL = 'SELECT CurrencyCode from currency where CurrencyCode = \'' + row['CurrencyCode']+'\''
	cursor.execute(_SQL)
	#Если результат запроса пустой - то есть длина списка равна 0 
	sql_list = cursor.fetchall()
	if len(sql_list) == 0:
			# if row['CurrencyCode'] in sql_list[0]:
			# Тогда формируем запрос на добавление новой строки в справочник
			_SQL = 'INSERT Currency(CurrencyCode,CurrencyCodeL,Units,CurrencyNameUA,CurrencyNameRU) VALUES(\'' + \
		 	        row['CurrencyCode'] + '\',\'' + \
		 	        row['CurrencyCodeL'] + '\',' + \
		 	        row['Units'] + ',\'' + \
		 	        row['CurrencyNameUA'] + '\',\'' + \
		 	        row['CurrencyNameRU'] + '\')'
			cursor.execute(_SQL)
			cursor.execute('COMMIT')