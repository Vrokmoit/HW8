from datetime import date, timedelta
import calendar


def get_birthdays_per_week(users):
    today = date.today()

    weekdays = {day: [] for day in calendar.day_name}

    for user in users:
        bd_next_year = user['birthday'].replace(year=today.year + 1)
        bd_this_year = user['birthday'].replace(year=today.year)

        list_bd = []

        if today <= bd_this_year <= today + timedelta(days=6):
            list_bd.append(bd_this_year)

        if today <= bd_next_year <= today + timedelta(days=6):
            list_bd.append(bd_next_year)

        for upcoming_birthday in list_bd:
            weekday = calendar.day_name[upcoming_birthday.weekday()]

            if weekday in ['Saturday', 'Sunday']:
                weekday = 'Monday'
            weekdays[weekday].append(user['name'])

    weekdays = {k: v for k, v in weekdays.items() if v}

    return weekdays
