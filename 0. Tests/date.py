from datetime import datetime, timedelta

def estimate_date(start_date, estimated_hours):
    """ Start date is expected in format 'day/month/year' """

    # Convert the date to datetime object without time
    
    start_date = datetime.strptime(start_date,'%d/%m/%Y')

    # Count number of full mandays

    working_day = 8
    mandays = estimated_hours // working_day

    if estimated_hours % working_day > 0:
        mandays+=1

    # Add mandays while skipping the weekends
    finish_date = start_date
    available_days = mandays
    if finish_date.weekday() < 5:
        available_days -= 1
    while available_days > 0:
        finish_date += timedelta(days=1)
        if finish_date.weekday() < 5:
            available_days -= 1
    
    # Convert the result back to the input format
    
    finish_date = finish_date.strftime('%m/%d/%Y')
    
    return mandays, finish_date


print(estimate_date("12/8/2023", 140))
