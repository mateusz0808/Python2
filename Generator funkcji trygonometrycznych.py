import math

def generator_funkcji_trygonometrycznych(start, stop, krok):
    x = start
    while x <= stop:
        yield math.sin(x), math.cos(x), math.tan(x)
        x += krok

# Testowanie generatora
start = 0
stop = math.pi
krok = 0.1

for sin_x, cos_x, tan_x in generator_funkcji_trygonometrycznych(start, stop, krok):
    print(f"x = {start:.2f} | sin(x) = {sin_x:.2f} | cos(x) = {cos_x:.2f} | tan(x) = {tan_x:.2f}")
    start += krok  # Dodajemy wartość kroku do x przy każdej iteracji

