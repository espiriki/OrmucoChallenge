def starts_first(line_1, line_2):
    if line_1[0] < line_2[0]:
        return 1
    else:
        return 2


def get_line_length(line):
    return abs(line[0] - line[1])


def get_line_atributes(line):
    length_line = get_line_length(line)

    if length_line == 0:
        start_line = line[0]
        end_line = start_line
    else:
        if line[0] < line[1]:
            start_line = line[0]
            end_line = line[1]
        else:
            start_line = line[1]
            end_line = line[0]

    return start_line, end_line, length_line


def check_overlap(line_1, line_2):
    """Returns TRUE if the lines overlap, and false otherwise"""

    start_line_1 = get_line_atributes(line_1)[0]
    end_line_1 = get_line_atributes(line_1)[1]
    length_line_1 = get_line_atributes(line_1)[2]

    start_line_2 = get_line_atributes(line_2)[0]
    end_line_2 = get_line_atributes(line_2)[1]
    length_line_2 = get_line_atributes(line_2)[2]

    if start_line_1 == start_line_2:

        # If we have two equal dots, I think this should return True, because it's like the dots are
        # stacked
        if length_line_1 == 0 and length_line_2 == 0:
            return True

        # If we have a dot and a line, this shouldn't overlap
        elif length_line_1 == 0 or length_line_2 == 0:
            return False

        # Base case where we have two lines that starts at the same point, so they overlap
        else:
            return True

    if starts_first(line_1, line_2) == 1:

        if end_line_1 > start_line_2:
            return True
        else:
            return False

    else:
        if end_line_2 > start_line_1:
            return True
        else:
            return False


if __name__ == '__main__':
    pass
