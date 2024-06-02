# kryptografia.py
def szyfr_cezara(tekst, przesuniecie):
    zaszyfrowany_tekst = ""
    for znak in tekst:
        if znak.isalpha():
            if znak.isupper():
                zaszyfrowany_tekst += chr((ord(znak) + przesuniecie - 65) % 26 + 65)
            else:
                zaszyfrowany_tekst += chr((ord(znak) + przesuniecie - 97) % 26 + 97)
        else:
            zaszyfrowany_tekst += znak
    return zaszyfrowany_tekst

def deszyfr_cezara(tekst, przesuniecie):
    return szyfr_cezara(tekst, -przesuniecie)
