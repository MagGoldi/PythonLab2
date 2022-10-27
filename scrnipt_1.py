import csv
import os


def make_dir():
    if not os.path.isdir("File_folder"):
        os.mkdir("File_folder")
    if not os.path.isdir("File_folder/scrnipt_1"):
        os.mkdir("File_folder/scrnipt_1")


def run_1(path_to_csv=os.path.join("C:/","PYTHON", "PythonLab2-1", "File_folder")):
    make_dir()
    list1 = []
    with open(path_to_csv + "\dataset.csv", 'r', newline='') as csvfile: #C:\PYTHON\PythonLab2-1\File_folder\dataset.csv
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            list1.append(row)

    with open(path_to_csv + "/scrnipt_1/X.csv", 'w', newline="") as csvfile_x:  
        for i in range(0, len(list1)):
                all_data = [list1[i][0]]
                writer = csv.writer(csvfile_x)
                writer.writerow(all_data)

    with open(path_to_csv + "/scrnipt_1/Y.csv", "w", newline="") as csvfile_y:
        for i in range(0, len(list1)):
            all_data = list1[i][1:]
            writer = csv.writer(csvfile_y)
            writer.writerow(all_data)
    
    print("\nscript_1 has finished working\n")
