def add_spaces_around_symbols(string):
    count_of_symbols_to_separate = 3
    new_string = str()
    while len(string) >= count_of_symbols_to_separate:
        new_string = string[-count_of_symbols_to_separate:] + ' ' + new_string
        string = string[:-count_of_symbols_to_separate]
    if string:
        return "%s %s" % (string, new_string)
    else:
        return new_string


def test_price(price):
    try:
        float(price)
        left, right = price.split('.')
    except ValueError:
        print("Введите корректное значение!")
        return False
    else:
        return True


def format_price(price):
    fractional_part_max_value = 5
    if not test_price(price):
        return False
    integer_part, fractional_part = price.split('.')
    if int(fractional_part[0]) >= fractional_part_max_value:
        integer_part = str(int(integer_part) + 1)
    int_part_with_spaces = add_spaces_around_symbols(integer_part)
    return int_part_with_spaces


if __name__ == '__main__':
    value = input("Введите цену, которую необходимо отформатировать: ")
    formatted_price = format_price(value)
    if formatted_price:
        print("Отформатированная цена: %s" % formatted_price)
