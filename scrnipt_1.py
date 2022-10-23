import csv
import os


def make_dir():
    if not os.path.isdir("File_folder"):
        os.mkdir("File_folder")
    if not os.path.isdir("File_folder/scrnipt_1"):
        os.mkdir("File_folder/scrnipt_1")


def run_1():
    make_dir()
    list1 = []
    with open('File_folder/dataset.csv', 'r', newline='', encoding = "utf-8") as csvfile:
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            list1.append(row)

    for i in range(0, len(list1)):
        with open("File_folder/scrnipt_1/X.csv", "a", newline="", encoding = "utf-8") as csvfile_x:
            all_data = [list1[i][0]]
            writer = csv.writer(csvfile_x)
            writer.writerow(all_data)

        with open("File_folder/scrnipt_1/Y.csv", "a", newline="", encoding = "utf-8") as csvfile_y:
            all_data = list1[i][1:]
            writer = csv.writer(csvfile_y)
            writer.writerow(all_data)
    
    csvfile_x.close()
    csvfile_y.close()
    csvfile.close()
    print("\nscript_1 has finished working\n")
