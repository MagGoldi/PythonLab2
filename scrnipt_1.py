import os
import datetime


def work_file(path_to_csv=os.path.join("File_folder", "dataset.csv")):
    file_main = open(path_to_csv, "a", encoding="utf-8")
    today = str(datetime.date.today())
    file_main.write(today)
    file_main.write("\n")

def make_dir():
    if not os.path.isdir("File_folder"):
        os.mkdir("File_folder")

def run_1(path_to_csv=os.path.join("File_folder", "dataset.csv")):
    make_dir()
    file_main = open(path_to_csv, "w", encoding="utf-8")
    work_file()
    file_main.close()
