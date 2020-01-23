import datetime

def counter():

    def plural(count, titles):
        count = count % 100
        count1 = count % 10
        if count > 10 and count < 20:
            return titles[2]
        if count1 > 1 and count1 < 5:
            return titles[1]
        if count1 == 1:
            return titles[0]
        return titles[2]

    dt = datetime.datetime.now()
    new_year = (dt.year + 1, 1, 1, 00, 00)

    c = datetime.datetime(*new_year) - dt
    days = c.days
    seconds = c.seconds
    hours = seconds // 3600
    minutes = (seconds - hours *3600) // 60

    pr = (str(days), plural(days, ['день', 'дня', 'дней']),
          str(hours), plural(hours, ['час', 'часа', 'часов']),
          str(minutes), plural(minutes, ['минута', 'минуты', 'минут'])
    )
    return ' '.join(pr)
