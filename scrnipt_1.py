import os
import datetime


def work_file(path_to_csv=os.path.join("PYTHON", "dataset.csv")):
    file_main = open(path_to_csv, "a", encoding="utf-8")
    today = datetime.date.today()
    file_main.write(today)
    file_main.write("\n")

def make_dir():
    if not os.path.isdir("PYTHON"):
        os.mkdir("PYTHON")

def run_1(path_to_csv=os.path.join("PYTHON", "dataset.csv")):
    file_main = open(path_to_csv, "w", encoding="utf-8")
    make_dir()
    work_file()
    file_main.close()
