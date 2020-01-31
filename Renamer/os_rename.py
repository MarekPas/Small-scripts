
def replacing(file,conds):
    renamed_file = file.replace(conds[0],conds[1])
    print(file,"renamed to",renamed_file)
    return renamed_file

def adding():
    first = input("Symbol to replace: ")
    second = input("Replace with: ")
    cond = [first,second]
    return cond



