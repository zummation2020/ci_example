def conv_num(num_str):
    # Check if the input is a non-empty string
    if not isinstance(num_str, str) or len(num_str) == 0:
        return None

    # Check if the string contains a decimal point
    if '.' in num_str:
        # If there are multiple decimal points, return None
        if num_str.count('.') > 1:
            return None
        try:
            # Check if the string represents a negative float
            if num_str.startswith('-'):
                return -float(num_str[1:])
            # Otherwise, return the float value
            return float(num_str)
        except ValueError:
            # If the string cannot be converted to a float, return None
            return None

    # Check if the string starts with '0x', indicating a hexadecimal number
    elif num_str.startswith('0x'):
        # Extract the hexadecimal digits
        hex_num = num_str[2:].lower()
        # Check if all characters in the hex_num string are valid hexadecimal digits
        if any(c not in '0123456789abcdef' for c in hex_num):
            return None
        try:
            # Convert the hexadecimal string to an integer and return it
            return int(hex_num, 16)
        except ValueError:
            # If the string cannot be converted to an integer, return None
            return None

    # If the string is not a float or a hexadecimal number, assume it's an integer
    else:
        try:
            # Check if the string represents a negative integer
            if num_str.startswith('-'):
                return -int(num_str[1:])
            # Otherwise, return the integer value
            return int(num_str)
        except ValueError:
            # If the string cannot be converted to an integer, return None
            return None
