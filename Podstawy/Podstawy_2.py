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