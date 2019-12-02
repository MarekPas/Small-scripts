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
    print("1 - Gaderypoluki  2- Padykinozetu  3 - Kuralyminote  4 - Koniecmatury  0 - zakończenie programu")
    try:
        code = int(input("Wybierz szyfr: "))
    except:
        print("Błąd! Musisz wpisać liczbę z przedziału 0-4!")
    else:
        if code == 1:
            text = str(input("Podaj text do przetłumaczenia na Gaderypoluki:\n"))
            gaderypoluki(text)
        elif code == 2:
            text = str(input("Podaj text do przetłumaczenia na Padykinozetu:\n"))
            padykinozetu(text)
        elif code == 3:
            text = str(input("Podaj text do przetłumaczenia na Kuralyminote:\n"))
            kuralyminote(text)
        elif code == 4:
            text = str(input("Podaj text do przetłumaczenia na Koniecmatury:\n"))
            koniecmatury(text)
        elif code == 0:
            not_end = False
        else:
            print("Błąd! Wpisana liczba musi być z przedziału 0-4!")
