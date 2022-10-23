import csv
import os



# Написать скрипт, который разобъёт исходный csv файл на N файлов, 
# где каждый отдельный файл будет соответствовать одной неделе. 
# Файлы называются по первой и последней дате, которую они содержат.

def make_dir():
    if not os.path.isdir("File_folder/scrnipt_3"):
        os.mkdir("File_folder/scrnipt_3")


def sort_week(all_data):
    day = len(all_data)
    week = []
    count = 0
    while (day != 0):
        if (day >= 7):
            for i in range(7):
                week.append(all_data[count])
                count += 1
            work_file(week)
            day -= 7
        elif (day < 7):
            for i in range(day):
                week.append(all_data[count])
                count += 1
            work_file(week)
            day = 0
        week = []


def work_file(week):
    date_1 = week[0][0][8:10]
    date_2 = week[-1][0][8:10]
    name_file = 'File_folder/scrnipt_3/' + str(week[0][0][:4]) + "_" + str(
        week[0][0][5:7]) + "_" + date_1 + "_" + date_2 + ".csv"
    print(name_file)
    with open(name_file, 'w', newline='', encoding = "utf-8") as file_scr3:
        writer = csv.writer(file_scr3)
        for i in range(len(week)):
            writer.writerow(week[i])


def run_3():
    make_dir()
    set1 = set()
    with open('File_folder/dataset.csv', 'r', newline='', encoding = "utf-8") as csvfile:
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            set1.add(row[0][:4])
    set1 = sorted(list(set1), reverse=True)
    n = len(set1)

    with open('File_folder/dataset.csv', 'r', newline='', encoding = "utf-8") as csvfile:
        file_reader = list(csv.reader(csvfile))
        all_data = []
        month, year = 9, 2022
        while(year != 2009):
            for row in file_reader:
                if (int(row[0][5:7]) == month):
                    all_data.append(row)
                elif (int(row[0][5:7]) > month):
                    month = int(row[0][5:7])
                    year -=1
                elif (int(row[0][5:7]) < month):
                    print(month, year)
                    month -= 1
                    if(month == 1):
                        pass
                    sort_week(all_data)
                    all_data = []
                    all_data.append(row)
    csvfile.close()
    print("\nscript_3 has finished working\n")


  