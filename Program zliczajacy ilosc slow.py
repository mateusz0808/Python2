def zlicz_wystapienia_slow(plik):
    wystapienia = {}

    try:
        with open(plik, 'r') as f:
            for linia in f:
                slowa = linia.strip().split()
                for slowo in slowa:
                    if slowo in wystapienia:
                        wystapienia[slowo] += 1
                    else:
                        wystapienia[slowo] = 1
        return wystapienia
    
    except FileNotFoundError:
        print("Plik nie został znaleziony.")
        return None
    
    except Exception as e:
        print(f"Wystąpił błąd: {e}")
        return None

# Testowanie programu
plik = input("Podaj nazwę pliku tekstowego: ")
plik = "D:\Python\lista_slow.txt"
f = open(plik, "r")


wyniki = zlicz_wystapienia_slow(plik)
if wyniki is not None:
    print("Liczba wystąpień każdego słowa:")
    for slowo, liczba_wystapien in wyniki.items():
        print(f"{slowo}: {liczba_wystapien}")
