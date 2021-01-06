#получение курсов валют через api нацбанка Украині
#и запись всего этого добра в БД MySQL
import requests
import configparser
import os
import mysql.connector

#Считаем конфигурационный файл со статичным названием config.ini
path_config = os.getcwd()+'\config.ini'

config = configparser.ConfigParser()
config.read(path_config)


#соединение с базой данных
dbconfig = {
	'host':config.get('Connect_Params','host'),
	'user':config.get('Connect_Params','user'),
	'password':config.get('Connect_Params','password'),
	'database':config.get('Connect_Params','base')
}
conn = mysql.connector.connect(**dbconfig)
cursor = conn.cursor()

cursor.execute("show databases")
print(cursor.fetchall())


print('Получение курсов валют')


response = requests.get('https://bank.gov.ua/NBU_Exchange/exchange?date=26.12.2020&json')

if response.status_code == 200:
	print('Запрос рабочий, статус ответа:',response.status_code)
	print(response.json())
elif response.status_code != 200:
	print('Запрос нерабочий, проверьте, не изменился ли запрос на сайте bank.gov.ua', responce.status_code)



