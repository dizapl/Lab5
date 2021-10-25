import csv
import sys
import os
import random
import shutil

fname = "doc.txt" 
x=int(input('Виберіть опцію: 1- читання з файлу 2- запис у файл 3- дозапис  4- копіювання файлу 5- перейменування файлу 6- видалення файлу'))

def read(fname): 
        fd = open(fname,'r')
        reader = csv.reader(fd,delimiter='\t')
        for row in reader:
            print(row)
            fd.close()
            print("Зчитування файла виконано")
        
def write(fname):
    fd = open(fname, 'w')
    for i in range(8):
         A = i*13
         fd.write('%i\t%.1f\n'%(i,A))
         fd.close()
         print("Запис у файл виконано")
                    
def append(fname):
    fd = open(fname,'a')
    for i in range(8):
        A = random(int(20),int(30))
        fd.write("%i\t%.1f\n"%(i,A))
        fd.close()
        print("Дозапис у кінець файла виконано")

def copy(fname):
    shutil.copyfile("C:Lab\doc.txt", "C:\Lab\mydoc_2.txt")
    print("Копіювання файлу виконано")
                               
def rename(fname):
    os.rename("C:\Lab\doc.txt", "C:\Lab\myfile.txt")
    print("Перейменування файлу виконано")

def remove(fname):
    os.remove("C:\Lab\doc.txt")
    print("Видалення файлу виконано")

mode= ''
if x==1:
    read(fname)
elif x==2:
    write(fname) 
elif x==3:
    append(fname)
elif x==4:
    copy(fname)
elif x==5:
    rename(fname)
elif x==6:
    remove(fname)



