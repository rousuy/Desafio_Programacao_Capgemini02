# Question 01


def order_int_list(arr: list) -> list:
    """
    checks if each element in a list is of type integer and sorts in ascending order

    Args:
        arr (list): if the list element is not type of integer, returns an exception

    Returns:
        list: sorted in ascending order
    """
    try:
        sorted_arr = []
        while arr:
            min_number = arr[0]
            for num in arr:
                if num < min_number:
                    min_number = num
            sorted_arr.append(min_number)
            arr.remove(min_number)
        return sorted_arr
    except TypeError as error:
        return f"The element of the list must be a integer number. Error: {error}"


def find_middle(arr: list) -> int:
    """
    checks if the size of the list is odd, and will be sorted by the order_int_list()
    function, and return the median number

    Args:
        arr (list): if the size of the list is even, will return an raise ValueError

    Returns:
        int: the median number of the list
    """
    if len(arr) % 2 == 1:
        sorted_arr = order_int_list(arr)
        middle_index = (len(sorted_arr) - 1) // 2
        return sorted_arr[middle_index]
    else:
        raise ValueError("The length of the list must be odd")


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print(find_middle(arr))
