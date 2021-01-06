# считывание текстовых данных из файла с разделителем в виде табуляции
# и занесение в таблицу MySQL - в данном случае - заполнение справочника валют
import os
import configparser
import mysql.connector

#открывание ini-файла на чтение в текущем каталоге
def open_ini(file_name:str):
	path_config = os.getcwd()+'\\'+file_name
	config = configparser.ConfigParser()
	config.read(path_config)
	return config

# открываем файл и считываем строки с преобразованием их в список наборов
def form_list_valut():
	list_valut = []
	with open('SpravVal.txt',encoding='utf-8') as file_sprav:
		for chore in file_sprav:
			chore_list = chore.split('\t')
			# list_valut .append(chore_list) 
	# print(chore_list)
	return list_valut

#print form_list_valut()

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

_SQL = 'check table ' + dbconfig['database'] + '.valut'
cursor.execute(_SQL)
print(cursor.fetchall())

_SQL = 'show tables like ' + '\'course\''
cursor.execute(_SQL)
slst = cursor.fetchall()
print(slst)
try:
	if 'course' in slst[0]:
		print('Табличка есть')
except Exception:
	print('Таблички нет!!!!!')