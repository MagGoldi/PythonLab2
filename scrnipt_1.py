import os
import datetime


def work_file(path_to_csv=os.path.join("File_folder", "dataset.csv")):
    file_main = open(path_to_csv, "a", encoding="utf-8")
    year, mounth, day = 2022, 10, 14
    for day in range(day, 32):
        date_f = str(datetime.date(year, mounth, day)) #2022-
        data_f = "data" + str(day-13)
        file_main.write(date_f + "," + data_f)
        file_main.write("\n")

def make_dir():
    if not os.path.isdir("File_folder"):
        os.mkdir("File_folder")

def split_file(path_to_csv=os.path.join("File_folder", "dataset.csv")):
    pass

def run_1(path_to_csv=os.path.join("File_folder", "dataset.csv")):
    make_dir()
    file_main = open(path_to_csv, "w", encoding="utf-8")
    work_file()
    file_main.close()
