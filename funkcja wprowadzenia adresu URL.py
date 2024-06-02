import urllib.request
from urllib.error import URLError, HTTPError

def pobierz_zawartosc_strony():
    while True:
        adres_url = input("Podaj adres URL: ")
        try:
            with urllib.request.urlopen(adres_url) as response:
                zawartosc_strony = response.read().decode('utf-8')
            return zawartosc_strony
        
        except (URLError, HTTPError) as e:
            print("Wystąpił błąd:", e)
            print("Spróbuj ponownie.")

# Testowanie funkcji
zawartosc = pobierz_zawartosc_strony()
if zawartosc:
    print("Zawartość strony:")
    print(zawartosc)
