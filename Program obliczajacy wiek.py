from datetime import datetime

def oblicz_wiek_w_dniach(data_urodzenia):
    try:
        data_urodzenia = datetime.strptime(data_urodzenia, "%Y-%m-%d")
        dzisiaj = datetime.now()
        wiek_w_dniach = (dzisiaj - data_urodzenia).days
        return wiek_w_dniach
    except ValueError:
        print("Nieprawidłowy format daty. Wprowadź datę w formacie RRRR-MM-DD.")
        return None

# Wczytanie daty urodzenia od użytkownika
data_urodzenia = input("Podaj datę urodzenia w formacie RRRR-MM-DD: ")

# Obliczenie wieku w dniach i wyświetlenie wyniku
wiek = oblicz_wiek_w_dniach(data_urodzenia)
if wiek is not None:
    print(f"Twój wiek w dniach wynosi: {wiek} dni.")
