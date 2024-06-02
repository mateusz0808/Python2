import string

tekst = "To jest przykładowy tekst! Zawiera spacje i znaki interpunkcyjne."

litery = [litera for litera in tekst if litera.isalpha()]

print(litery)
