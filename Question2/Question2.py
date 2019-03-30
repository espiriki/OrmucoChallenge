import re


def compare_each_subversion(val_1, val_2):
    if val_1 == val_2:
        return 0
    elif val_1 < val_2:
        return 1
    else:
        return -1


def compare_version_strings(string_1, string_2):
    str_1_with_dots = re.sub("[^0-9]", ".", string_1)
    str_2_with_dots = re.sub("[^0-9]", ".", string_2)

    str1_splitted = str_1_with_dots.split(".")
    str2_splitted = str_2_with_dots.split(".")

    str1_splitted_number = []
    for element in str1_splitted:
        str1_splitted_number.append(int(element))

    str2_splitted_number = []
    for element in str2_splitted:
        str2_splitted_number.append(int(element))

    max_length = max(len(str1_splitted_number), len(str2_splitted_number))
    min_length = min(len(str1_splitted_number), len(str2_splitted_number))

    check = 0
    for i in range(max_length):

        if check != 0:
            break

        if i > (min_length - 1):
            check = 1
            break

        check = compare_each_subversion(str1_splitted_number[i], str2_splitted_number[i])

    return check


if __name__ == '__main__':
    print(compare_version_strings("1.10", "1.9.5"))
    print(compare_version_strings("1.9", "1.9.5"))
