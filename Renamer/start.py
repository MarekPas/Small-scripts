import os, os_rename

source = input("Source of files to rename: ")
os.chdir(source)

add = "y"
while add == "y":
    replace = (os_rename.adding())
    file_list = os.listdir()
    print("Changing",replace[0],"to",replace[1])
    for i in file_list:
        os.rename(i, os_rename.replacing(i, replace))
    add = str(input("Do you want to add another condition? (type \"y\" if yes) "))