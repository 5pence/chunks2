from spin import spin


def test_small_rotate():
    assert spin('hello', 2) == 'llohe'
    assert spin('hello', -2) == 'lohel'


def test_bigger_rotation_of_positive_n():
    string = 'andy and georgie are a good laugh!'
    expected = 'e are a good laugh!andy and georgi'
    assert spin(string, 15) == expected


def test_bigger_rotation_of_negative_n():
    string = 'andy and georgie are a good laugh!'
    expected = 'e a good laugh!andy and georgie ar'
    assert spin(string, -15) == expected


def test_rotation_of_n_same_as_len_str():
    string = expected = 'andy and georgie are a good laugh!'
    assert spin(string, len(string)) == expected


def test_rotation_of_n_bigger_than_string():
    """
    Why are there two expected results for this test?

    1. A slice of size n moved from one end of the string to the other
    2. A continual rotation, character by character, n number of times

    Both interpretations result in identical output, except in the case
    where the rotation size exceeds the length of the string.

    Case 1) With a slice method, slicing an entire string and placing
    it at either the beginning or end of itself simply results in the
    the original string = expected_solution1

    Case 2) With a continual rotation, rotating the string len(string)
    number of times produces a string idential to the original string.
    This means any additional rotations can be considered equivalent to
    rotating the string by rotations % len(string) = expected_solution2
    """
    string = 'spence and dem!'
    expected_solution1 = 'spence and dem!'
    expected_solution2 = ' dem!spence and'
    assert spin(string, 100) in (expected_solution1,
                                   expected_solution2)

    mod = 100 % len(string)  # 10
    assert spin(string, mod) in (expected_solution1,
                                   expected_solution2)