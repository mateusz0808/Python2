import random

# Generowanie i wypisywanie 10 losowych liczb
print("10 losowych liczb z zakresu od 1 do 100:")
for _ in range(10):
    liczba = random.randint(1, 100)
    print(liczba)
