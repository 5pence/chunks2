MINIMUM_DRINKING_AGE = 18


def allowed_to_get_drunk(name, age):
    """ Using f strings print '{name} is allowed to get drunk' or '{name} is not allowed to get drunk'
    checking teh passed in age against the MINIMUM_DRINKING_AGE constant - 1 point
    """
    is_allowed = 'is allowed' if age >= MINIMUM_DRINKING_AGE else 'is not allowed'
    print(f'{name} {is_allowed} to get drunk')
