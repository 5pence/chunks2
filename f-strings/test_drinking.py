from drinking import allowed_to_get_drunk


def test_not_allowed_to_get_drunk(capfd):
    allowed_to_get_drunk('tim', 17)
    output = capfd.readouterr()[0].strip()
    assert output == 'tim is not allowed to get drunk'


def test_allowed_to_get_drunk(capfd):
    allowed_to_get_drunk('bob', 18)
    output = capfd.readouterr()[0].strip()
    assert output == 'bob is allowed to get drunk'


def test_allowed_to_get_drunk_other(capfd):
    allowed_to_get_drunk('fred', 19)
    output = capfd.readouterr()[0].strip()
    assert output == 'fred is allowed to get drunk'
