import datetime
import random

def calculate_days_until(target_date):
    today = datetime.date.today()
    return (target_date - today).days

def print_countdown(event, target_date):
    days_until = calculate_days_until(target_date)
    encouragements = ["to już blisko 🚀", "ja też nie mogę się doczekać 😄", "czas leci! ⏳", "już prawie! 🎉"]
    print(f"Do {event} zostało {days_until} dni. {random.choice(encouragements)}")

def main():
    events = {
        "Święta Bożego Narodzenia": datetime.date(datetime.date.today().year, 12, 25),
        "Sylwester": datetime.date(datetime.date.today().year, 12, 31),
        "Wakacje": datetime.date(datetime.date.today().year, 7, 1),
    }

    print("Wybierz wydarzenie, aby sprawdzić, ile dni zostało:")
    for idx, (event, _) in enumerate(events.items(), start=1):
        print(f"{idx}. {event}")

    choice = int(input("Wpisz numer wydarzenia: "))
    event = list(events.keys())[choice - 1]
    print_countdown(event, events[event])

if __name__ == "__main__":
    main()