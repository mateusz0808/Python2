# wyszukiwanie_tekstowe.py

def stworz_tablice_prefixowa(wzorzec):
    
    "Tworzy tablicę prefikso-sufiksową dla danego wzorca."
    
    m = len(wzorzec)
    tablica = [0] * m
    dlugosc = 0

    for i in range(1, m):
        while dlugosc > 0 and wzorzec[i] != wzorzec[dlugosc]:
            dlugosc = tablica[dlugosc - 1]

        if wzorzec[i] == wzorzec[dlugosc]:
            dlugosc += 1

        tablica[i] = dlugosc

    return tablica

def wyszukaj_wzorzec(tekst, wzorzec):
    
    "Wyszukuje wszystkie wystąpienia wzorca w tekście za pomocą algorytmu KMP."
    "Zwraca listę pozycji początkowych wystąpień."
    
    n = len(tekst)
    m = len(wzorzec)

    if m == 0:
        return []

    tablica = stworz_tablice_prefixowa(wzorzec)
    wyniki = []

    i = j = 0
    while i < n:
        if wzorzec[j] == tekst[i]:
            i += 1
            j += 1

            if j == m:
                wyniki.append(i - j)
                j = tablica[j - 1]
        else:
            if j != 0:
                j = tablica[j - 1]
            else:
                i += 1

    return wyniki
