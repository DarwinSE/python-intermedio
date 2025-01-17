# Ejericio de Manejos de Ficheros

import os

# .txt file

txt_file = open('./my_file.txt', 'w+') # r+ es para leer y escribir # w+ es para leer y sobreescribir
txt_file.write('Me llamo Darwin\nMe apellido Guerra\n24 años\nMi alias es Lawi')
# print(txt_file.read())
# print(txt_file.read(10))
# print(txt_file.readline())
# print(txt_file.readlines())

for element in txt_file.readlines():
    print(element)

txt_file.write('\nMe gusta Python')
print(txt_file.readline())

txt_file.close()

# os.remove('./my_file.txt')


# .json file

import json

json_file = open('./my_file.json', 'w+')

json_data = {
    'name': 'Darwin',
    'surname': 'Guerra',
    'age': 24,
    'alias': 'Lawi',
    'languajes': ['Python', 'Java', 'C#']
}

json.dump(json_data, json_file, indent= 4) # indent es para darle un espaciado al json y que sea mas leible

json_file.close()

with open('./my_file.json') as my_other_file:
    for ele in my_other_file.readlines():
        print(ele)

json_dict = json.load(open('./my_file.json'))
print(json_dict)
print(json_dict['name'])


# .csv file

import csv

csv_file = open('./my_file.csv', 'w+')

csv_writer = csv.writer(csv_file)

csv_writer.writerow(['Name', 'Surname', 'Age', 'Alias'])
csv_writer.writerow(['Darwin', 'Guerra', 24, 'Lawi'])

csv_file.close()


# .xlsx file
#import xlrd # se debe instalar el modulo


# .xml file

import xml