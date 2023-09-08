def add_time(start, duration, day=None):
    # Parse the start time
    start_time, period = start.split()
    start_hour, start_minute = map(int, start_time.split(':'))
    if period == 'PM':
        start_hour += 12

    # Parse the duration time
    duration_hour, duration_minute = map(int, duration.split(':'))

    # Calculate the total minutes
    total_minutes = start_hour * 60 + start_minute + duration_hour * 60 + duration_minute

    # Calculate the new time
    new_hour = total_minutes // 60 % 24
    new_minute = total_minutes % 60
    new_period = 'AM' if new_hour < 12 else 'PM'
    if new_hour >= 12:
        new_hour -= 12
    if new_hour == 0:
        new_hour = 12

    # Calculate the number of days later
    days_later = total_minutes // (24 * 60)

    # Calculate the new day of the week
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    if day:
        day = day.capitalize()
        current_day_index = days_of_week.index(day)
        new_day_index = (current_day_index + days_later) % 7
        new_day = days_of_week[new_day_index]

    # Construct the result string
    result = f"{new_hour}:{str(new_minute).zfill(2)} {new_period}"
    if day:
        if days_later == 1:
            result += f", {new_day} (next day)"
        elif days_later > 1:
            result += f", {new_day} ({days_later} days later)"
        else:
            result += f", {new_day}"
    elif days_later == 1:
        result += " (next day)"
    elif days_later > 1:
        result += f" ({days_later} days later)"

    return result
