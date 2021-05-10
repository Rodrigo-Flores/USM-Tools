from time import *
import random
import csv

AF = 3.075
HC = 1.025
BK = 2.25

# ATTEMPT 1

lst = [AF, HC, BK]

n = 1
'''
while True:
    for i in lst:
        ran1 = random.randint(0,2)
        ran2 = random.randint(0,2)
        ran3 = random.randint(0,2)

        print("\t\t\t\tTEST", n)

        print(lst[ran1], lst[ran2], lst[ran3], " -> " ,(lst[ran1]) + (lst[ran2]) - (lst[ran3]))
        print(lst[ran1], lst[ran2], lst[ran3], " -> " ,(lst[ran1]) - (lst[ran2]) + (lst[ran3]))
        print(lst[ran1], lst[ran2], lst[ran3], " -> " ,(lst[ran1]) - (lst[ran2]) - (lst[ran3]))
        print(lst[ran1], lst[ran2], lst[ran3], " -> " ,(lst[ran1]) + (lst[ran2]) + (lst[ran3]))

        print(lst[ran1], lst[ran2], lst[ran3], " -> " ,(lst[ran1]) * (lst[ran2]) + (lst[ran3]))
        print(lst[ran1], lst[ran2], lst[ran3], " -> " ,(lst[ran1]) * (lst[ran2]) - (lst[ran3]))
        print(lst[ran1], lst[ran2], lst[ran3], " -> " ,(lst[ran1]) - (lst[ran2]) * (lst[ran3]))
        print(lst[ran1], lst[ran2], lst[ran3], " -> " ,(lst[ran1]) * (lst[ran2]) * (lst[ran3]))
        print(lst[ran1], lst[ran2], lst[ran3], " -> " ,(lst[ran1]) + (lst[ran2]) * (lst[ran3]))

        print(lst[ran1], lst[ran2], lst[ran3], " -> " ,(lst[ran1]) / (lst[ran2]) + (lst[ran3]))
        print(lst[ran1], lst[ran2], lst[ran3], " -> " ,(lst[ran1]) / (lst[ran2]) - (lst[ran3]))
        print(lst[ran1], lst[ran2], lst[ran3], " -> " ,(lst[ran1]) - (lst[ran2]) / (lst[ran3]))
        print(lst[ran1], lst[ran2], lst[ran3], " -> " ,(lst[ran1]) / (lst[ran2]) / (lst[ran3]))
        print(lst[ran1], lst[ran2], lst[ran3], " -> " ,(lst[ran1]) + (lst[ran2]) / (lst[ran3]))
        print(lst[ran1], lst[ran2], lst[ran3], " -> " ,(lst[ran1]) * (lst[ran2]) / (lst[ran3]))
        print(lst[ran1], lst[ran2], lst[ran3], " -> " ,(lst[ran1]) / (lst[ran2]) * (lst[ran3]))
        

        print()

        n += 1

        sleep(5)
'''

# ATTEMPT 2

def csv_header(file_name, headers):
    with open(file_name, 'w', newline='') as file:
        write = csv.writer(file)
        write.writerow(headers)

def csv_writer(file_name, data):
    with open(file_name, 'a+', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

csv_header("fisica.csv", ["a", "b", "c", "RESULTADO"])

while True:
    a = random.randint(-5, 5)
    b = random.randint(-5, 5)
    c = random.randint(-5, 5)

    result = (AF * a) + (HC * b) + (BK * c)

    print(a, b, c, " -> ", round(result, 2))

    csv_writer("fisica.csv", [a, b, c ,result])

    sleep(1*(10**(-2)))