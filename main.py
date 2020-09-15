from datetime import date, time, datetime
from math import floor


DAYS_PER_YEAR = 365


class Decalander:

    MONTHS_PER_YEAR = 10
    DAYS_PER_MONTH = floor(DAYS_PER_YEAR / MONTHS_PER_YEAR)

    def __init__(self, year: int, ordinal: int):
        self.year = year
        self.ordinal = ordinal

    def __str__(self):
        dpm = Decalander.DAYS_PER_MONTH
        month = self.ordinal // dpm + 1
        if month == 11:
            month = "c"
        day = self.ordinal % dpm + 1
        return "{}-{}-{}".format(self.year, month, day)

    @staticmethod
    def today():
        return Decalander.from_gregorian(date.today())

    @ staticmethod
    def from_gregorian(greg: date):
        # special case, our leap day is the last day
        if greg.month == 2 and greg.day == 29:
            year_ordinal = 365
        else:
            year_ordinal = (date(1999, greg.month, greg.day) -
                            date(1999, 1, 1)).days
        return Decalander(greg.year, year_ordinal)


TIME_FORMAT = "%H:%M:%S"
MIDNIGHT = datetime.strptime("00:00:00", TIME_FORMAT)
GREG_SECONDS_PER_DAY = 24*60*60


class Decatime:
    HOURS_PER_DAY = 10
    MINUTES_PER_HOUR = 100
    SECONDS_PER_MINUTE = 100
    SECONDS_PER_HOUR = SECONDS_PER_MINUTE * MINUTES_PER_HOUR
    SECONDS_PER_DAY = SECONDS_PER_HOUR * HOURS_PER_DAY
    RATIO = SECONDS_PER_DAY/GREG_SECONDS_PER_DAY

    def __init__(self, seconds_am: int):
        self.seconds_am = seconds_am*Decatime.RATIO

    def __str__(self):
        seconds = self.seconds_am % Decatime.SECONDS_PER_MINUTE
        minutes = (self.seconds_am //
                   Decatime.SECONDS_PER_MINUTE) % Decatime.MINUTES_PER_HOUR
        hours = self.seconds_am // Decatime.SECONDS_PER_HOUR
        return "{:>1d}:{:>02d}:{:>02d}".format(int(hours), int(minutes), int(seconds))

    @staticmethod
    def now():
        return Decatime.from_greg_time(datetime.now())

    @ staticmethod
    def from_greg_time(greg: datetime):
        time_am = (greg - MIDNIGHT)
        seconds_after_midnight = time_am.seconds
        seconds_after_midnight += time_am.microseconds / 1e6
        return Decatime(seconds_after_midnight)


if __name__ == "__main__":
    dates = [date(2000, 1, 1), date(2000, 12, 31),
             date(1989, 12, 14), date(1992, 12, 14),
             date(1991, 5, 25), date(2000, 2, 29)]
    for d in dates:
        print("gregorian: {}, decalendar: {}".format(
            d, Decalander.from_gregorian(d)))
    now = datetime.now()
    times = [
        datetime.strptime("00:00:00", TIME_FORMAT),
        datetime.strptime("12:00:00", TIME_FORMAT),
        datetime.strptime("23:59:59", TIME_FORMAT),
        now
    ]
    for t in times:
        print("gregorian: {}, decitime: {}".format(
            t, Decatime.from_greg_time(t)))
