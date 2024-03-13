from datetime import datetime, timedelta

users = [
    {"name": "John Doe", "birthday": "1985.03.2"},
    {"name": "John Doe", "birthday": "1985.03.7"},
    {"name": "John Doe", "birthday": "1985.03.10"},
    {"name": "Jane Smith", "birthday": "1990.03.11"},
    {"name": "Adelina Ford", "birthday": "1999.03.14"},
    {"name": "Adelan Hord", "birthday": "1997.03.16"}
]

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = datetime(today.year, birthday.month, birthday.day).date() # визначення дн для поточного року

        start_of_week = today - timedelta(days=today.weekday()) #Визначення першого дня поточного тижня (понеділок)

        if start_of_week <= birthday_this_year <= start_of_week + timedelta(days=7):
            # якщо дн вже було в цьому році, переносимо його на наступний рік
            if birthday_this_year < today:
                birthday_this_year += timedelta(days=365)

            while birthday_this_year.weekday() >= 5: #Перенесення дати привітання на наступний понеділок, якщо вихідний
             birthday_this_year += timedelta(days=1)
       
            #додавання інформації до списку
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": birthday_this_year.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
