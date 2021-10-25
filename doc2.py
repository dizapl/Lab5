import csv
import os
import random
import shutil
def read(filename):
    fd = open(filename, "r")
    reader = csv.reader(fd, delimiter="\t")
    for row in reader:
        print(row)
    fd.close()
    print("зчитування файлу виконано")
def write(filename):
    fd = open(filename, "w")
    for i in range(10):
        A = i*15
        fd.write("%i\t%.1f\n" % (i, A))
    fd.close()
    print("запис файлу виконано")
def append(filename): 
    fd = open(filename, "a")
    for i in range(10):
        A = random.randint(30,40)
        fd.write("%i\t%.1f\n" % (i, A))
    fd.close()
    print("дозапис у кінець файлу виконано") 
def rename(filename):
    os.rename("H:\lab\mydata.txt", "H:\lab\data.txt")
    print("перейменування файлу виконано") 
def delete(filename):
    os.remove("H:\lab\data.txt")
    print("видалення файлу виконано")
def copy(filename):
    shutil.copyfile("H:\lab\mydata.txt", "H:\lab\data2.txt")
    print("копіювання файлу виконано")   
filename = "mydata.txt"
x=int(input("виберіть режим роботи з файлом: 1 - читати з файла 2 - записати у файл 3 - дозапис у файл 4 - перейменувати файл 5 - видалити файл 6 - зробити копію файлу"))          

mode=' '
if x==1:
    read(filename)
elif x==2:
    write(filename)
elif x==3:
    append(filename) 
elif x==4:
    rename(filename)
elif x==5:
    delete(filename)         
elif x==6:
    copy(filename)
else:
    print("немає такого вибору, оберіть те, що є")    