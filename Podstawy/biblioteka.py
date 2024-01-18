wiek = int(input("Podaj wiek: "))

if wiek >= 18 and wiek <= 120:
    print("Zapraszamy!")
    print("Proszę!")
elif wiek > 120:
    print("Podaj właściwy wiek")
else:
    print("Spadaj, mały!")
print("Koniec")

# Pętla for #1
# Wykonywanie instrukcji na elemencie iterowalnym (dla każdego elementu)
napis = "ala ma kota"

for litera in napis:
    # Instrukcje wykonywane w pętli (w kółko)
    print(litera)

# Pętla for #2
for i in range(10):
    # Wykonaj coś 10 razy
    print("Python")

for i in range(10, 30, 3):
    # Wykonaj coś w określonym zakresie
    print(i, end=" ")

# Pętla while
i = 0
while i < 10:
    print(i)
    # if i == 5:
    #     break
    i += 1

###
# Match
polecenie = "Zapisz"
match polecenie:
    case "Zapisz":
        print("Zapisuję..")
    case "Wyświetl":
        print("Wyświetlam")
    case "A" | "B":
        print("A lub B")
    case _:
        print("Eeee.")

if polecenie == "Zapisz":
    print("Zapisuję...")
elif polecenie == "Wyświetl":
    print("Wyświetlam")
elif polecenie == "A" or polecenie == "B":
    print("A lub B")
else:
    print("Eeee.")


######
def czy_ma_dostep(wiek):
    if wiek >= 18 and wiek < 120:
        return True
    else:
        return False


def is_allowed(age):
    if age >= 18 and age < 120:
        return True
    else:
        return False


wiek = int(input("Podaj wiek: "))

if czy_ma_dostep(wiek):
    print("Zapraszam!")
else:
    print("Precz!")
