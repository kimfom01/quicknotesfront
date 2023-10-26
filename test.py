def capital_case(x):
    """
        Capitalize the first letter of the word or sentence
    """
    return x.capitalize()


def test_capital_case():
    """
        test capital case
    """
    assert capital_case('semaphore') == 'Semaphore'
