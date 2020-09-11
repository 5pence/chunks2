from datetime import datetime, timedelta

BORN = datetime(year=2016, month=12, day=19)


def gen_special_pybites_dates():
    """Write a generator that returns the following "special" dates (datetime objects):

- Our birthday! What is the date every year going forward from the BORN date (datetime.datetime(2017, 12, 19, 0, 0),
datetime.datetime(2018, 12, 19, 0, 0), ...)?

- Return every 100th day counting forward from the BORN date (datetime(2017, 3, 29, 0, 0), datetime(2017, 7, 7, 0, 0), ...)

We're only calculating/ testing a few years ahead of the BORN date. This will omit the next leap year (2020) from the
challenge making it a bit easier for you (we will revisit this in an intermediate challenge). Have fun!
"""
    pass