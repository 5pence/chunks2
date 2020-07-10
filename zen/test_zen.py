from zen import strip_vowels, text


def test_strip_vowels_on_zen():
    output, number_replacements = strip_vowels(text)

    assert number_replacements == 262

    assert 'Th* Z*n *f Pyth*n, by T*m P*t*rs' in output
    assert 'B***t*f*l *s b*tt*r th*n *gly' in output
    assert 'N*m*sp*c*s *r* *n* h*nk*ng gr**t *d**' in output


def test_strip_vowels_on_other_text():
    text = """Hello world!
    We hope that you are learning a lot of Python.
    Have fun with our Chunks of Py.
    Keep calm and code in Python!
    Become a PyChunks wizard!
    All the way"""

    output, number_replacements = strip_vowels(text)

    assert number_replacements == 44
    assert 'H*ll* w*rld' in output
