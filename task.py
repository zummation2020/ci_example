import random
from typing import List


# Pull request 1


def exponential(x: float, y: float) -> float:
    """takes two numbers x and y and returns x raised to the power of y """
    return x**y

# Pull request 2


def create_list_of_random_ints(num, filter="all") -> List[int]:
    """Creates a list of length num of random numbers between 1 and 1000,
    optionally specify a filter for only even numbers or only odd numbers"""
    num_list = []
    while len(num_list) <= num:
        new_random_number = random.randint(1, 1000)
        if filter == "odd":
            if new_random_number % 2 == 1:
                num_list.append(new_random_number)
        if filter == "even":
            if new_random_number % 2 == 0:
                num_list.append(new_random_number)
        elif filter == "all":
            num_list.append(new_random_number)
    return num_list


# Pull request 3
def check_for_val(self, target) -> bool:
    """This member function checks to see if val exists in the class member
    values and returns True if found"""
    return target in self.values


# Pull request 4


def get_val_index(arr, val) -> int:
    """Searches arr for val and returns the index if found, otherwise -1"""
    for i, cur_elt in enumerate(arr):
        if cur_elt == val:
            return i
    return -1

# Pull request 5


def create_double_array_values(arr: List) -> List:
    """sort the list (ascending) and double the value of each element of
       the list and return without changing the state of the original list"""
    new_arr = arr.copy()
    new_arr.sort()
    for i in range(len(arr)):
        new_arr[i] = new_arr[i] * 2
    return new_arr

# pull request 6


def conv_endian(num, endian='big') -> str:
    """Takes an integer value 'num' and converts it to a hexadecimal
    number. Endian type is specified by the optional flag 'endian'. Number is
    converted to hex and returned as a string.
    """
    sign = ""
    if num < 0:
        sign = "-"

    if endian != 'big' and endian != 'little':
        return None

    map_decimal_to_hex = {
        0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6",
        7: "7", 8: "8", 9: "9", 10: "A", 11: "B", 12: "C", 13: "D",
        14: "E", 15: "F"
    }

    hex_digits = []
    abs_num = abs(num)

    while abs_num > 15:
        hex_digits.append(map_decimal_to_hex[abs_num % 16])
        abs_num = abs_num // 16
    hex_digits.append(map_decimal_to_hex[abs_num])
    if len(hex_digits) % 2 != 0:
        hex_digits.append("0")
    hex_bytes = hex_bits_to_byte(hex_digits, endian)
    return sign + hex_bytes


def hex_bits_to_byte(bits: List[str], endian) -> str:
    """Returns a string of space separated bytes
     from bit_list"""

    # convert strings to bits and combine bits based on endian
    hex_num = ""
    while len(bits) > 0:
        first = bits.pop(0)
        second = bits.pop(0)
        if endian == "big":
            hex_num = second + first + " " + hex_num
        elif endian == "little":
            hex_num += second + first + " "
    return hex_num[:-1]
