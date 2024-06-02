def oblicz_silnie():
    while True:
        try:
            n = int(input("Podaj liczbę całkowitą nieujemną: "))
            if n < 0:
                raise ValueError("Podano liczbę ujemną.")
            wynik = 1
            for i in range(1, n + 1):
                wynik *= i
            return wynik
        except ValueError as e:
            print(f"Wystąpił błąd: {e}. Spróbuj ponownie.")
        except Exception as e:
            print(f"Wystąpił nieoczekiwany błąd: {e}. Spróbuj ponownie.")

try:
    silnia = oblicz_silnie()
    print(f"Silnia podanej liczby wynosi: {silnia}")
except KeyboardInterrupt:
    print("\nPrzerwano przez użytkownika.")
