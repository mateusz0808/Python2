import string

def szyfruj_cezarem(zdanie, przesuniecie):
    alfabet = string.ascii_lowercase  # Uzyskujemy alfabet małych liter

    zaszyfrowane_zdanie = ""
    for litera in zdanie:
        if litera.isalpha():  # Sprawdzamy, czy litera jest literą alfabetu
            # Określamy indeks litery w alfabecie
            indeks = (alfabet.index(litera.lower()) + przesuniecie) % 26
            
            # Dodajemy zaszyfrowaną literę do zaszyfrowanego zdania
            zaszyfrowane_zdanie += alfabet[indeks]
        else:
            # Jeśli to nie litera, dodajemy bez zmian
            zaszyfrowane_zdanie += litera

    return zaszyfrowane_zdanie

# Wczytanie zdania od użytkownika
zdanie = input("Podaj zdanie do zaszyfrowania: ")

# Wczytanie przesunięcia
przesuniecie = int(input("Podaj przesunięcie (liczba całkowita): "))

# Szyfrowanie zdania
zaszyfrowane_zdanie = szyfruj_cezarem(zdanie, przesuniecie)

# Wyświetlenie zaszyfrowanego zdania
print("Zaszyfrowane zdanie:", zaszyfrowane_zdanie)
