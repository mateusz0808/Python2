# liczby_zespolone.py

def dodawanie(a, b):
    return (a[0] + b[0], a[1] + b[1])

def odejmowanie(a, b):
    return (a[0] - b[0], a[1] - b[1])

def mnozenie(a, b):
    return (a[0]*b[0] - a[1]*b[1], a[0]*b[1] + a[1]*b[0])

def dzielenie(a, b):
    denominator = b[0]**2 + b[1]**2
    real_part = (a[0]*b[0] + a[1]*b[1]) / denominator
    imag_part = (a[1]*b[0] - a[0]*b[1]) / denominator
    return (real_part, imag_part)
