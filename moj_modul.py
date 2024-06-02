def powitanie():
    print("Witaj w moim module")

def dodaj(a, b):
    return a + b

# moj_modul.py
import liczby_zespolone
import kryptografia
import liczby_zespolone_z_obsluga_wyjatkow
import grafy
import wyszukiwanie_tekstowe

# Przykładowe użycie modułów

# Moduł liczby_zespolone
a = (1, 2)
b = (3, 4)
suma = liczby_zespolone.dodawanie(a, b)
print("Suma liczb zespolonych:", suma)

# Moduł kryptografia
tekst = "HelloWorld"
przesuniecie = 3
zaszyfrowany_tekst = kryptografia.szyfr_cezara(tekst, przesuniecie)
print("Zaszyfrowany tekst:", zaszyfrowany_tekst)

# Moduł liczby_zespolone_z_obsługa_wyjątków
c = (0, 0)
try:
    wynik_dzielenia = liczby_zespolone_z_obsluga_wyjatkow.dzielenie(a, c)
    print("Wynik dzielenia:", wynik_dzielenia)
except ValueError as e:
    print(f"Błąd: {e}")

# Moduł grafy
moj_graf = grafy.stworz_graf()
grafy.dodaj_wierzcholek(moj_graf, 'A')
grafy.dodaj_wierzcholek(moj_graf, 'B')
grafy.dodaj_wierzcholek(moj_graf, 'C')
grafy.dodaj_wierzcholek(moj_graf, 'D')
grafy.dodaj_wierzcholek(moj_graf, 'E')
grafy.dodaj_wierzcholek(moj_graf, 'F')
grafy.dodaj_krawedz(moj_graf, 'A', 'B')
grafy.dodaj_krawedz(moj_graf, 'B', 'C')
grafy.dodaj_krawedz(moj_graf, 'C', 'D')
grafy.dodaj_krawedz(moj_graf, 'C', 'E')
grafy.dodaj_krawedz(moj_graf, 'E', 'F')
grafy.rysuj_graf(moj_graf)

# Moduł wyszukiwanie_tekstowe
tekst_do_przeszukania = "ababcababcabcabc"
wzorzec_do_szukania = "abc"
wyniki_wyszukiwania = wyszukiwanie_tekstowe.wyszukaj_wzorzec(tekst_do_przeszukania, wzorzec_do_szukania)
print("Wyniki wyszukiwania:", wyniki_wyszukiwania)
