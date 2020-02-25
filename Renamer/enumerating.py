import os

source = input("Source of files to rename: ")
os.chdir(source)
file_list = os.listdir()
k=0
for i in file_list:
    os.rename(file_list[k], str(k)+". "+file_list[k])
    print(file_list[k])
    k+=1
