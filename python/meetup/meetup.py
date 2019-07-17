import datetime, pprint, calendar

ordinal_meaning = {
    'first' : 0,
    'second' : 1,
    'third' : 2,
    'fourth' : 3,
    'fifth' : 4,
    'last' : -1
}

weekday_meaning = {
    'monday' : 0,
    'tuesday' : 1,
    'wednesday' : 2,
    'thursday' : 3,
    'friday' : 4,
    'saturday' : 5,
    'sunday' : 6
}

class MeetupDayException(Exception):
    def __init__(self, expression, message):
        self.expression, self.message = expression, message

def meetup(year, month, week, day_of_week):
    # Get all days in a month
    days = [datetime.date(year, month, day) for day in range(1, calendar.monthrange(year, month)[1] + 1)]
    # Filter to the day of week being targeted
    days = [date for date in days if date.weekday() == weekday_meaning[day_of_week.lower()]]
    if week in ordinal_meaning.keys():
        return days[ordinal_meaning[week]]
    elif week == 'teenth':
        return [date for date in days if date.day <= 19 and date.day >= 13][0]
    else:
        try:
            return days[int(week[0]) - 1]
        except IndexError as err:
            raise MeetupDayException(err, "Invalid date parameter \'{}\'".format(week))