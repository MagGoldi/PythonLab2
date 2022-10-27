class Iterator:

    def __init__(self, name_of_file):
        self.name_of_file = name_of_file
        self.counter = 0
        self.list = []
        file = open(self.name_of_file, "r", encoding="utf-8")
        for row in file:
            self.list.append(row)
        file.close

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < len(self.list):
            tmp = self.list[self.counter]
            self.counter += 1
            return tmp
        else:
            raise StopIteration


def run_5():
    file_name = "File_folder/scrnipt_2/20220901_20220130.csv"
    s_iter1 = Iterator(file_name)
    for val in s_iter1:
        print(val, end="")
    print("\nscript_5 has finished working\n")
