from datetime import datetime, timedelta

def get_birthdays_per_week(birthdays):
    today = datetime.now()
    week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    weekly_birthdays = {day: [] for day in week_days}

    for name, date_str in birthdays.items():
        birth_date = datetime.strptime(date_str, '%Y-%m-%d').replace(year=today.year)
        
        # Check if birthday already passed this year and adjust to next year if necessary
        if birth_date < today:
            birth_date = birth_date.replace(year=today.year + 1)
        
        day_of_week = week_days[birth_date.weekday()]
        
        # If birthday falls on a weekend, greet on Monday
        if day_of_week == "Saturday" or day_of_week == "Sunday":
            day_of_week = "Monday"
        
        weekly_birthdays[day_of_week].append(name)
    
    # Filter out only the next 7 days
    result = {}
    for i in range(7):
        current_day = week_days[(today.weekday() + i) % 7]
        if weekly_birthdays[current_day]:
            result[current_day] = ", ".join(weekly_birthdays[current_day])

    return result

birthdays = {
    "Bill Gates": "1955-10-28",
    "Jill Valentine": "1974-11-01",
    "Kim Kardashian": "1980-10-21",
    "Jan Koum": "1976-02-24"
}

results = get_birthdays_per_week(birthdays)
for day, names in results.items():
    print(f"{day}: {names}")

