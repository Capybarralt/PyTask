import datetime

def weekend_generator(start, end):

    while start < end:
        if start.weekday() >= 5:
            yield start
        start = start + datetime.timedelta(days=1)
