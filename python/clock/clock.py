class Clock(object):
    def __init__(self, hour, minute):
        self.hour, self.minute = hour, minute
        self.change(0)

    def __repr__(self):
        return '{}:{}'.format(str(self.hour).zfill(2), str(self.minute).zfill(2))

    def __eq__(self, other):
        return self.hour == other.hour and self.minute == other.minute

    def change(self, minutes):
        self.minute += minutes
        while self.minute >= 60 or self.minute < 0:
            if self.minute >= 60:
                self.hour += 1
                self.minute -= 60
            elif self.minute < 0:
                self.hour -= 1
                self.minute += 60
        self.hour = self.hour % 24
        return self.__repr__()

    def __add__(self, minutes):
        return self.change(minutes)

    def __sub__(self, minutes):
        return self.change(-minutes)