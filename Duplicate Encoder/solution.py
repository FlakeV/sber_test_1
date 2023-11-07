def duplicate_encoder_1(string: str) -> str:
    return ''.join([')' if string.count(char) > 1 else '(' for char in string.lower()])


def duplicate_encoder_2(string: str) -> str:
    char_dict = {}
    checked_string = ''
    string = string.lower()
    for char in string:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    for char in string:
        if char_dict[char] > 1:
            checked_string += ')'
        else:
            checked_string += '('
    return checked_string
