def calculate_difference(array: list, x: int) -> int:
    """
    calculates the number of even elements given the difference between the value of x

    Args:
        array (list): integers to be calculated
        x (int): difference between list numbers

    Returns:
        int: number of occurrences where the difference of x and each element of the list is even
    """
    even_numbers = 0
    for num in range(0, len(array)):
        for n in array:
            if (array[num] - n) == x and x % 2 == 0:
                even_numbers += 1
    return even_numbers


if __name__ == "__main__":
    n = [1, 5, 3, 4, 2]
    x = 2
    print(calculate_difference(n, x))
