import string

def generator_slow(plik):
    with open(plik, 'r') as f:
        for linia in f:
            for slowo in linia.split():
                slowo = slowo.strip(string.punctuation)
                if slowo:
                    yield slowo

# Testowanie generatora
plik = "lista_slow.txt"  # Tutaj podaj nazwę pliku tekstowego
plik = "D:\Python\lista_slow.txt"

for slowo in generator_slow(plik):
    print(slowo)
