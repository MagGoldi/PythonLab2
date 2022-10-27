import os
import csv
import re
import datetime

# Написать скрипт, содержащий функцию, 
# принимающую на вход дату (тип datetime) и возвращающий данные для этой даты (из файла) или 
# None если данных для этой даты нет. Функция должна быть представлена в четырёх версиях в зависимости от 
# типа входных файлов, из которых будут прочитаны данные (пункты 0–3). 
# 
# Написать функцию next(), 
# которая будет при первом вызове возвращать данные для самой ранней возможной даты (возвращается кортеж (дата, данные)), 
# а при каждом следующем вызове данные для следующей по порядку даты. Если попадается дата, для которой данные отсутствуют, 
# то она игнориуруется и возвращаются данные для следующей валидной даты.



def next(count):
    with open('File_folder/dataset.csv', 'r', newline='', encoding="utf-8") as csvfile:
        file_reader = list(csv.reader(csvfile))
        if(file_reader[count] == None): return None
        else:print(file_reader[count])

def work_0(date):
    with open('File_folder/dataset.csv', 'r', newline='', encoding="utf-8") as csvfile:
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            if (row[0] == date):  # если одинаковые даты - выводим
                print(*row)
                csvfile.close()
                break
        else:
            csvfile.close()
            return None


def work_1(date):
    with open('File_folder/scrnipt_1/X.csv', 'r', newline='', encoding="utf-8") as csvfile:
        file_reader = list(csv.reader(csvfile))
        for i in range(len(file_reader)):
            if (file_reader[i][
                0] == date):  # ищем в фале Х запоминаем номер строки, выводим данные по номеру строки в фале Y
                tmp = i
                break
        else:
            return None
    with open('File_folder/scrnipt_1/Y.csv', 'r', newline='', encoding="utf-8") as csvfile:
        file_reader = list(csv.reader(csvfile))
        print(*file_reader[tmp])
    csvfile.close()


def work_2(date):
    ways = os.listdir(path="File_folder/scrnipt_2")
    for i in range(len(ways)):
        if (ways[i][:4] == date[:4]):  # Ищем файл у которого аткой же год
            with open("File_folder/scrnipt_2/" + ways[i], 'r', newline='', encoding="utf-8") as csvfile:
                file_reader = csv.reader(csvfile)
                for row in file_reader:
                    if (row[0] == date):
                        print(*row)
                        csvfile.close()
                        break
    else:
        csvfile.close()
        return None


def work_3(date):
    ways = os.listdir(path="File_folder/scrnipt_3")
    list1 = []
    date = re.sub(r'[-]', '_', date)
    for i in range(len(ways)):  # выбираем одинаковые года и месяцы, записываем файлы в лист
        if (ways[i][:7] == date[:7]):
            list1.append(ways[i])
    if (list1 == None): return None
    for i in range(len(list1)):
        if (int(list1[i][11:13]) >= int(date[8:10]) >= int(
                list1[i][8:10])):  # если число находится в диапозоне недели то выводим его
            with open("File_folder/scrnipt_3/" + list1[i], 'r', newline='', encoding="utf-8") as csvfile:
                file_reader = csv.reader(csvfile)
                date = re.sub(r'[_]', '-', date)
                for row in file_reader:
                    if (row[0] == date):
                        print(*row)
                        csvfile.close()
                        break
    else:
        csvfile.close()
        return None


def run_4():
    date = datetime.date(2022, 12, 22)
    #work_0(date)
    #work_1(date)
    #work_2(date)
    #work_3(date)


    with open('File_folder/dataset.csv', 'r', newline='', encoding="utf-8") as csvfile:
        count = 0
        while(count !=50):
            next(count)
            count += 1

    csvfile.close()
    print("\nscript_4 has finished working\n")

