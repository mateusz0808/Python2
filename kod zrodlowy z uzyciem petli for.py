import csv

# Przykładowa funkcja do analizy danych
def analyze_data_with_loops(filename):
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        sales_values = []  # Lista do przechowywania wartości dla obliczenia mediany
        total_sales = 0
        count = 0
        for row in reader:
            if (
                row["variable"] == "Sales, government funding, grants and subsidies"
                and row["unit"] == "DOLLARS(millions)"
            ):
                value = row["value"]
                if value.replace('.', '', 1).isdigit():
                    total_sales += float(value)
                    sales_values.append(float(value))  # Dodaj wartość do listy
                else:
                    total_sales += 0
                count += 1

        average_sales = total_sales / count if count else 0
        median_sales = calculate_median(sales_values)
        
        print(f"Average Sales: {average_sales}")
        print(f"Median Sales: {median_sales}")

def calculate_median(values):
    sorted_values = sorted(values)
    n = len(sorted_values)
    if n % 2 == 1:
        return sorted_values[n // 2]
    else:
        return (sorted_values[n // 2 - 1] + sorted_values[n // 2]) / 2

def main():
    # Wywołanie funkcji
    analyze_data_with_loops("C:/Users/mlewa/Downloads/dane.csv")

if __name__ == "__main__":
    main()
