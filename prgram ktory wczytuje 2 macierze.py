def wczytaj_macierz():
    rows = int(input("Podaj liczbę wierszy: "))
    columns = int(input("Podaj liczbę kolumn: "))

    macierz = []
    print("Wprowadź elementy macierzy:")
    for i in range(rows):
        row = []
        for j in range(columns):
            element = float(input(f"Podaj element [{i+1},{j+1}]: "))
            row.append(element)
        macierz.append(row)

    return macierz

def dodaj_macierze(macierz1, macierz2):
    if len(macierz1) != len(macierz2) or len(macierz1[0]) != len(macierz2[0]):
        raise ValueError("Macierze muszą mieć takie same rozmiary.")
    
    suma_macierzy = []
    for i in range(len(macierz1)):
        row = []
        for j in range(len(macierz1[0])):
            row.append(macierz1[i][j] + macierz2[i][j])
        suma_macierzy.append(row)
    
    return suma_macierzy

def odejmij_macierze(macierz1, macierz2):
    if len(macierz1) != len(macierz2) or len(macierz1[0]) != len(macierz2[0]):
        raise ValueError("Macierze muszą mieć takie same rozmiary.")
    
    roznica_macierzy = []
    for i in range(len(macierz1)):
        row = []
        for j in range(len(macierz1[0])):
            row.append(macierz1[i][j] - macierz2[i][j])
        roznica_macierzy.append(row)
    
    return roznica_macierzy

def pomnoz_macierze(macierz1, macierz2):
    if len(macierz1[0]) != len(macierz2):
        raise ValueError("Liczba kolumn pierwszej macierzy musi być równa liczbie wierszy drugiej macierzy.")

    wynik = []
    for i in range(len(macierz1)):
        row = []
        for j in range(len(macierz2[0])):
            suma = 0
            for k in range(len(macierz2)):
                suma += macierz1[i][k] * macierz2[k][j]
            row.append(suma)
        wynik.append(row)
    
    return wynik

try:
    print("Wczytaj pierwszą macierz:")
    macierz1 = wczytaj_macierz()

    print("\nWczytaj drugą macierz:")
    macierz2 = wczytaj_macierz()

    print("\nMacierz 1:")
    for row in macierz1:
        print(row)

    print("\nMacierz 2:")
    for row in macierz2:
        print(row)

    suma = dodaj_macierze(macierz1, macierz2)
    print("\nSuma macierzy:")
    for row in suma:
        print(row)

    roznica = odejmij_macierze(macierz1, macierz2)
    print("\nRóżnica macierzy:")
    for row in roznica:
        print(row)

    iloczyn = pomnoz_macierze(macierz1, macierz2)
    print("\nIloczyn macierzy:")
    for row in iloczyn:
        print(row)

except ValueError as e:
    print(f"Wystąpił błąd: {e}")
except Exception as e:
    print(f"Wystąpił nieoczekiwany błąd: {e}")
