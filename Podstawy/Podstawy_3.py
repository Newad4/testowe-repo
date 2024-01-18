def funkcja():
    #gromadzenie wielu instrukcji
    pass

def czy_mam_dostep(wiek):
    if wiek >=18 and wiek < 120:
        return True
    else:
        return False


def is_allowed(age):
    if age >=18 and age <120:
        return True
    else:
        return False

wiek = int(input("podaj wiek: "))

if czy_mam_dostep(wiek):
    print('zapraszam!')
else:
    print("precz!")
