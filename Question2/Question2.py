import re
import string

SPLIT_CHARACTER = "."
REMOVE_NON_DIGITS_REGEX = "[^0-9]"
VERSIONS_ARE_EQUAL = 0
LHS_IS_BIGGER = 1
RHS_IS_BIGGER = -1


def compare_each_subversion(val_1, val_2):
    if val_1 == val_2:
        return 0
    elif val_1 < val_2:
        return 1
    else:
        return -1


def create_list_with_numbers(array_string):
    return [int(i) for i in array_string]


def remove_last_if_not_digit(str):
    _str = str

    if str[-1] not in string.digits:
        _str = _str[:-1]

    return _str


def compare_version_strings(string_1, string_2):
    """Returns:
         0 if both versions are equal
        -1 if LHS version is BIGGER than RHS version
         1 if LHS version is SMALLER than RHS version
     """

    string_1 = remove_last_if_not_digit(string_1)
    string_2 = remove_last_if_not_digit(string_2)

    str_1_with_dots_only = re.sub(REMOVE_NON_DIGITS_REGEX, SPLIT_CHARACTER, string_1)
    str_2_with_dots_only = re.sub(REMOVE_NON_DIGITS_REGEX, SPLIT_CHARACTER, string_2)

    str1_splitted = str_1_with_dots_only.split(SPLIT_CHARACTER)
    str2_splitted = str_2_with_dots_only.split(SPLIT_CHARACTER)

    str1_splitted_as_number = create_list_with_numbers(str1_splitted)
    str2_splitted_as_number = create_list_with_numbers(str2_splitted)

    len_str_1 = len(str1_splitted_as_number)
    len_str_2 = len(str2_splitted_as_number)

    max_length = max(len_str_1, len_str_2)
    min_length = min(len_str_1, len_str_2)

    check = 0
    for i in range(max_length):

        # If any of the sub-versions are not equal, we can return the result
        if check != 0:
            break

        # If strings are equal up to the point where one ends and the other continue,
        # the bigger string is the most recent
        if i > (min_length - 1):
            if len_str_1 < len_str_2:
                check = 1
            else:
                check = -1

            break

        # update the check variable to see if we need to keep looking
        check = compare_each_subversion(str1_splitted_as_number[i], str2_splitted_as_number[i])

    return check


if __name__ == '__main__':
    pass
