from datetime import datetime

def get_days_from_today(date):
    transf_date = datetime.strptime(date, '%Y-%m-%d')
    current_date = datetime.today()
    difference_days = (transf_date - current_date).days
    return difference_days

date_task = '2020-10-09'
result = get_days_from_today(date_task)
print(f'Різниця в днях між {date_task} та поточною датою: {result}')