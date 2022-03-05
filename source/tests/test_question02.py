from questions.question02 import calculate_difference


def test_is_same_value():
    """
    calculates whether the return of the function calculate_difference() is the same as expected variable,
    given the value of numbers in a list, equal to the number x and be even
    """
    x = 2
    list_number = [2, 2, 2, 2, 2]
    expected = len(list_number)
    assert expected == calculate_difference([1, 5, 3, 4, 2, 6, 8], x)
