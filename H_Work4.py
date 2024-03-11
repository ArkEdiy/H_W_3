from datetime import datetime, timedelta

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Adelina Ford", "birthday": "1999.03.13"},
    {"name": "Adelan Hord", "birthday": "1997.03.15"}
]

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = datetime(today.year, birthday.month, birthday.day).date() # визначення дн для поточного року

        # якщо дн вже було в цьому році, переносимо його на наступний рік
        if birthday_this_year < today:
            birthday_this_year += timedelta(days=365)

        days_until_birthday = (birthday_this_year - today).days # знаходження кількості днів до дн

        # Перевірка,чи день народженя випадає вперед на 7 днів і чи це не вихідний
        if 0 <= days_until_birthday <= 7 and birthday_this_year.weekday() < 5:
            #додавання інформації до списку
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": birthday_this_year.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
