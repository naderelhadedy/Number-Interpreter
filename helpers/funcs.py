"""
This module holds helper functions
"""


def interpret_num(input_num):
    """
    This function interprets a number to its equivalent words

    >> interpret_num(42)
      fortytwo
    """
    one_digit = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    two_digits = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    parent_digits = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety", "hundred"]

    if input_num < 10:
        return one_digit[input_num]
    if input_num < 20:
        return two_digits[input_num % 10]
    if input_num <= 100:
        return parent_digits[input_num // 10] + (one_digit[input_num % 10] if input_num % 10 != 0 else "")
