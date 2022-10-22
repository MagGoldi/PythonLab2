import os
import datetime
import csv

#Написать скрипт, который разобъёт исходный csv файл на файл X.csv и Y.csv, 
#с одинаковым количеством строк. Первый будет содержать даты, второй - данные.


def make_dir():
    if not os.path.isdir("File_folder"):
        os.mkdir("File_folder")
    

def split_file(path_to_csv=os.path.join("File_folder", "dataset.csv")):
    pass

def run_1(path_to_csv=os.path.join("File_folder", "dataset.csv")):
    make_dir()
    file_x = open("X.csv", "w", encoding="utf-8")
    file_y = open("Y.csv", "w", encoding="utf-8")
    file_main = open(path_to_csv, "w", encoding="utf-8")

    file_x.close()
    file_y.close()
    file_main.close()
