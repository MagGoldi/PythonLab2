def next(count):
    file = open("dataset.csv", "r")
    data = []
    for row in file:
        data.append(row)
    print(data[count])
    file.close
    count+=1
    return count

next(6)    