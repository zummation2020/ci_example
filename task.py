def my_func():
    return "Hello World"

def my_datetime(num_sec: int) -> str:

    def is_leap(year: int) -> bool:
        # If a year is divisible by 4 but not 100 or if it is divisible by 400
        # then it is a leap year
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    def days_in_month(year: int, month: int) -> int:
        DAYS_IN_MONTH = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        FEBRUARY = 2

        if is_leap(year) and month == FEBRUARY:
            return 29

        return DAYS_IN_MONTH[month]

    SECONDS_PER_DAY = 24 * 60 * 60

    # how many days have elapsed since start of epoch
    days_elapsed = num_sec // SECONDS_PER_DAY

    day = 1
    month = 1
    year = 1970

    while True:
        days_in_current_month = days_in_month(year, month)
        # when the remaining days elapsed is
        # less than those in the current month
        # the date to return has been found
        if days_elapsed < days_in_current_month:
            # remainder of days elapsed is the day in the date
            day += days_elapsed
            break
        # subtract the days in the current month from total elapsed
        days_elapsed -= days_in_current_month
        # and increment the month by one
        month += 1

        # when months are incremented to 12
        if month > 12:
            # wrap months back to January
            month = 1
            # increment the year by one
            year += 1

    return f'{month:02d}-{day:02d}-{year}'
