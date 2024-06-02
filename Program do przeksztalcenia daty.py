from datetime import datetime

def wczytaj_date():
    while True:
        data_input = input("Podaj datę w formacie RRRR-MM-DD: ")
        try:
            data = datetime.strptime(data_input, "%Y-%m-%d")
            return data
        except ValueError as e:
            print("Wystąpił błąd:", e)
            print("Spróbuj ponownie.")

# Testowanie funkcji
data = wczytaj_date()
print("Wczytana data:", data)
