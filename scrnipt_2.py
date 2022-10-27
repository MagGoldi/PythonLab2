import csv
import os
import re

# Написать скрипт, который разобъёт исходный csv файл на N файлов,
# где каждый отдельный файл будет соответствовать одному году.
# Файлы называются по первой и последней дате, которую они содержат.
# (если файл содержит данные с первого января 2001 по 31 декабря 2001, то файл назвать 20010101_20011231.csv)

def make_dir():
    if not os.path.isdir("File_folder/scrnipt_2"):
        os.mkdir("File_folder/scrnipt_2")


def work_file(date_1, date_2, list1_years):
    name_file = 'File_folder/scrnipt_2/' + date_1 + "_" + date_2 + ".csv"
    print("create file: ", name_file)
    with open(name_file, 'w', newline='', encoding="utf-8") as namefile:
        writer = csv.writer(namefile)
        for i in range(len(list1_years)):
            writer.writerow(list1_years[i])


def run_2(path_to_csv=os.path.join("C:/","PYTHON", "PythonLab2-1", "File_folder")):
    make_dir()
    set1 = set()
    list1_years = []
    with open(path_to_csv+'dataset.csv', 'r', newline='', encoding="utf-8") as csvfile:
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            set1.add(row[0][:4])
    set1 = sorted(list(set1), reverse=True)
    n = len(set1)

    with open(path_to_csv+'dataset.csv', 'r', newline='', encoding="utf-8") as csvfile:
        file_reader = list(csv.reader(csvfile))
        for i in range(n):
            for j in range(len(file_reader)):
                if (file_reader[j][0][:4] == set1[i]): list1_years.append(file_reader[j])
            print(list1_years[0][0])
            date_1 = str(re.sub(r'[-]', '', list1_years[0][0]))
            date_2 = str(re.sub(r'[-]', '', list1_years[-1][0]))
            work_file(date_1, date_2, list1_years)
            list1_years = []

    csvfile.close()
    print("\nscript_2 has finished working\n")