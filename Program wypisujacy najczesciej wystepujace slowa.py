from collections import Counter

def najczesciej_wystepujace_slowa(plik, n=5):
    try:
        with open(plik, 'r') as f:
            # Wczytaj słowa z pliku i podziel je na tokeny
            slowa = f.read().split()

            # Użyj Counter do zliczenia wystąpień każdego słowa
            counter = Counter(slowa)

            # Znajdź n najczęściej występujących słów
            najczestsze = counter.most_common(n)

            # Wypisz najczęściej występujące słowa
            print(f"5 najczęściej występujących słów w pliku '{plik}':")
            for slowo, liczba_wystapien in najczestsze:
                print(f"{slowo}: {liczba_wystapien}")

    except FileNotFoundError:
        print("Plik nie został znaleziony.")

# Testowanie programu
plik = input("Podaj nazwę pliku tekstowego: ")
plik = "D:\Python\lista_slow.txt"
najczesciej_wystepujace_slowa(plik)
