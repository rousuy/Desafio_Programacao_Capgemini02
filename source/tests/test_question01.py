from questions.question01 import order_int_list, find_middle


def test_is_ordered_list():
    """
    checks if the function order_int_list() will return the same values in ascending order as expected variable
    """
    expected = [1, 2, 3, 4, 5, 6, 7]
    assert order_int_list([5, 4, 2, 1, 3, 7, 6]) == expected


def test_is_middle_number():
    """
    checks if the function find_middle() will return the same value as expected variable
    """
    list = [1, 2, 3, 4, 5, 6, 7]
    middle_index = 3
    expected = list[middle_index]
    assert expected == find_middle([5, 4, 2, 1, 3, 7, 6])
