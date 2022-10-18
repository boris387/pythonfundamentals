finish_date = start_date
    available_days = mandays
    while True:
        if finish_date.weekday() < 5:
            available_days -= 1
        if available_days == 0:
            break
        finish_date += timedelta(days=1)