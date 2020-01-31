import string


def gaderypoluki(text):
    kod = "GADERYPOLUKIgaderypoluki"
    kod2 = "AGEDYROPULIKagedyropulik"
    text2 = str.maketrans(kod, kod2)
    print(text.translate(text2))


def padykinozetu(text):
    kod = "PADYKINOZETUpadykinozetu"
    kod2 = "APYDIKONEZUTapydikonezut"
    text2 = str.maketrans(kod, kod2)
    print(text.translate(text2))


def kuralyminote(text):
    kod = "kuralyminoteKURALYMINOTE"
    kod2 = "ukarylimonetUKARYLIMONET"
    text2 = str.maketrans(kod, kod2)
    print(text.translate(text2))

#below is another way to translate
def koniecmatury(text):
    complement = {'k': 'o', 'o': 'k', 'n': 'i', 'i': 'n', 'e': 'c', 'c': 'e', 'm': 'a', 'a': 'm', 't': 'u', 'u': 't',
                  'r': 'y', 'y': 'r', ' ': ' '}
    res = []
    for i in text:
        if i.lower() not in complement:
            res.append(i)
        else:
            if i.isupper() is True:
                res.append(complement[i.lower()].upper())
            else:
                res.append(complement[i])
    print(''.join(res))


not_end = True
while not_end:
    print("\n 1 - Gaderypoluki\n 2 - Padykinozetu\n 3 - Kuralyminote\n 4 - Koniecmatury\n 0 - Close program")
    try:
        code = int(input("Select encryption: "))
    except:
        print("Error! You must enter digit from the range of 0-4! ")
    else:
        if code == 1:
            text = str(input("Enter text to crypt/encrypt to/from Gaderypoluki:\n"))
            gaderypoluki(text)
        elif code == 2:
            text = str(input("Enter text to crypt/encrypt to/from Padykinozetu:\n"))
            padykinozetu(text)
        elif code == 3:
            text = str(input("Enter text to crypt/encrypt to/from Kuralyminote:\n"))
            kuralyminote(text)
        elif code == 4:
            text = str(input("Enter text to crypt/encrypt to/from Koniecmatury:\n"))
            koniecmatury(text)
        elif code == 0:
            not_end = False
        else:
            print("Error! You must enter digit from the range of 0-4! ")
