import requests
import configparser
import os
import mysql.connector
from datetime import datetime
import dbf

# https://bank.gov.ua/NBU_Exchange/exchange?json - текущая дата
# https://bank.gov.ua/NBU_Exchange/exchange?date=26.12.2020&json -на заданную дату


response = requests.get('https://bank.gov.ua/NBU_Exchange/exchange?json')

if response.status_code == 200:
	print('Запрос рабочий, статус ответа:',response.status_code)
	# print(response.json())
elif response.status_code != 200:
	print('Запрос нерабочий, проверьте, не изменился ли запрос на сайте bank.gov.ua', responce.status_code)


# преобразуем ответ в объект json
list_of_currency = response.json()

valut_db = dbf.Table("H:\\Dogovor\\Temp\\valut.dbf")
valut_db.open()
rate_db = dbf.Table("\\\\sukap\\vol\\dogovor\\temp\\valut_kurs.dbf")
rate_db.open(mode=dbf.READ_WRITE)
for item in valut_db:
    print(item)

for item in rate_db:
	if item['PARENTID'] == 33:
 		print(item)
# for datum in (('John Doe', 31, dbf.Date(1979, 9,13))


rate_db.close
valut_db.close