from datetime import datetime
from itertools import islice

from gendate import gen_special_dates


def test_gen_special_dates():
    gen = gen_special_dates()
    dates = list(islice(gen, 10))

    expected = [datetime(2017, 3, 29, 0, 0),
                datetime(2017, 7, 7, 0, 0),
                datetime(2017, 10, 15, 0, 0),
                datetime(2017, 12, 19, 0, 0),
                datetime(2018, 1, 23, 0, 0),
                datetime(2018, 5, 3, 0, 0),
                datetime(2018, 8, 11, 0, 0),
                datetime(2018, 11, 19, 0, 0),
                datetime(2018, 12, 19, 0, 0),
                datetime(2019, 2, 27, 0, 0)]

    assert dates == expected