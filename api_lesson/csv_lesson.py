import csv


with open('D:/Selenium_Python/pythonProject/api_lesson/utilities/loanapp.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')
    # print(csvReader)
    # print(list(csvReader))

    names = []
    stats = []
    for row in csvReader:
        names.append(row[0])
        stats.append(row[1])
print(names)
print(stats)
Index = names.index('sam')
loan_status = stats[Index]
print("sams loan status is " + loan_status)
