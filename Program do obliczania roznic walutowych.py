import json
from datetime import datetime
import requests

class InvoiceCalculator:
    def __init__(self):
        self.invoices = []
        self.payments = []

    def add_invoice(self, amount, currency, issue_date):
        invoice = {
            'amount': float(amount),
            'currency': currency,
            'issue_date': issue_date
        }
        self.invoices.append(invoice)

    def add_payment(self, amount, currency, payment_date):
        payment = {
            'amount': float(amount),
            'currency': currency,
            'payment_date': payment_date
        }
        self.payments.append(payment)

    def get_exchange_rate(self, currency, date):
        url = f'http://api.nbp.pl/api/exchangerates/rates/A/{currency}/{date}/'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            rate = data['rates'][0]['mid']
            return rate
        else:
            return None

    def calculate_exchange_difference(self, invoice, payment):
        invoice_date = datetime.strptime(invoice['issue_date'], '%Y-%m-%d').date()
        print(invoice_date)
        payment_date = datetime.strptime(payment['payment_date'], '%Y-%m-%d').date()
        print(payment_date)

        invoice_rate = self.get_exchange_rate(invoice['currency'], invoice_date)
        print(invoice_rate)
        payment_rate = self.get_exchange_rate(payment['currency'], payment_date)
        print(payment_rate)

        if invoice_rate is not None and payment_rate is not None:
            difference = invoice['amount'] * (payment_rate / invoice_rate) - payment['amount']
            print(difference)
            return round(difference, 2)
        else:
            return None

    def save_results(self, filename):
        results = []
        for invoice in self.invoices:
            for payment in self.payments:
                try:
                    difference = self.calculate_exchange_difference(invoice, payment)
                    if difference is not None:
                        result = {
                            'invoice_amount': invoice['amount'],
                            'invoice_currency': invoice['currency'],
                            'invoice_date': invoice['issue_date'],
                            'payment_amount': payment['amount'],
                            'payment_currency': payment['currency'],
                            'payment_date': payment['payment_date'],
                            'exchange_difference': difference
                        }
                        results.append(result)
                        print(f"Różnica kursowa dla faktury z {invoice['issue_date']} i płatności z {payment['payment_date']}: {difference}")
                except Exception as e:
                    print(f"Błąd przy przetwarzaniu faktury {invoice} i płatności {payment}: {str(e)}")

        if results:
            with open(filename, 'w') as file:
                json.dump(results, file, indent=2)
            print("Wyniki zostały zapisane do pliku:", filename)
        else:
            print("Brak danych do zapisu. Sprawdź, czy wprowadziłeś poprawne informacje o fakturze, płatności lub czy data nie wypada w weekend/święto")

if __name__ == "__main__":
    calculator = InvoiceCalculator()

    try:
        invoice_amount = input("Podaj kwotę faktury: ")
        invoice_currency = input("Podaj walutę faktury (np. USD): ")
        issue_date = input("Podaj datę wystawienia faktury (RRRR-MM-DD): ")

        calculator.add_invoice(invoice_amount, invoice_currency, issue_date)

        payment_amount = input("Podaj kwotę płatności: ")
        payment_currency = input("Podaj walutę płatności (np. EUR): ")
        payment_date = input("Podaj datę płatności (RRRR-MM-DD): ")

        calculator.add_payment(payment_amount, payment_currency, payment_date)

        calculator.save_results('results.json')

    except ValueError as ve:
        print(f"Błąd: Nieprawidłowy format danych. Upewnij się, że wprowadziłeś poprawne liczby.")
    except Exception as e:
        print(f"Wystąpił błąd: {str(e)}")
