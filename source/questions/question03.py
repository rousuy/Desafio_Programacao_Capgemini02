# Question 3

import six
from math import sqrt, ceil, floor


def encrypt_message(message: str) -> print:
    """
    encrypt a message, based on the square root of the string size,
    where your grid will be based creating a matrix composed of its
    square root, given the smallest area.

    Args:
        message (str): convert to a matrix

    Returns:
        print: the encrypted message of the array in transposed form
    """
    message = message.replace(' ', '')
    message_list = list(message)
    sqrt_message = sqrt(len(message))
    area = sqrt_message * sqrt_message

    if area >= floor(area):
        grid_number = ceil(sqrt_message)
    else:
        grid_number = floor(sqrt_message)

    grid = []
    for x in range(0, grid_number):
        grid.append(message_list[:grid_number])
        del message_list[:grid_number]

    # library six.moves to resolve python 3 incompatibility to accept more than 2 lists in zip() method format
    output = list(map(list, six.moves.zip_longest(*grid)))

    for i in output:
        for n in i:
            if n is not None:
                print(n, end='')
        print(' ', end='')


if __name__ == "__main__":
    encrypt_message('ola mundo')
