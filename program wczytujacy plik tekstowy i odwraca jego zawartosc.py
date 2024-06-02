import os

def odwroc_zawartosc_pliku(plik_wejsciowy, plik_wyjsciowy):
    try:
        # Odczytaj zawartość pliku wejściowego
        with open(plik_wejsciowy, 'r') as f:
            zawartosc = f.read()

        # Odwróć zawartość pliku
        odwrocona_zawartosc = zawartosc[::-1]

        # Zapisz odwróconą zawartość do nowego pliku
        with open(plik_wyjsciowy, 'w') as f:
            f.write(odwrocona_zawartosc)

        print("Zawartość pliku została odwrócona i zapisana do nowego pliku.")
    
    except FileNotFoundError:
        print("Plik wejściowy nie został znaleziony.")
    
    except Exception as e:
        print(f"Wystąpił błąd podczas przetwarzania pliku: {e}")

# Testowanie programu
plik_wejsciowy = input("Podaj nazwę pliku tekstowego do odwrócenia: ")
plik_wejsciowy = "D:\Python\lista_slow.txt"
plik_wyjsciowy = input("Podaj nazwę nowego pliku, do którego zostanie zapisana odwrócona zawartość: ")

odwroc_zawartosc_pliku(plik_wejsciowy, plik_wyjsciowy)
