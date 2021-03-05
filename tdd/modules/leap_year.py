from datetime import datetime

class LeapYear:
    def __init__(self):
        pass

    @staticmethod
    def is_leap_year(year):
        try:
            date = datetime(year, 2, 29)
            leap = True
        except ValueError as _e:
            leap = False

        return leap
