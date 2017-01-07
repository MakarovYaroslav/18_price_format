def add_spaces_around_symbols(price_as_string):
    count_of_symbols_to_separate = 3
    new_price_as_string = str()
    while len(price_as_string) >= count_of_symbols_to_separate:
        new_price_as_string = "%s %s" % (
            price_as_string[-count_of_symbols_to_separate:],
            new_price_as_string)
        price_as_string = price_as_string[:-count_of_symbols_to_separate]
    if price_as_string:
        return "%s %s" % (price_as_string, new_price_as_string)
    else:
        return new_price_as_string


def test_price(price):
    try:
        float(price)
        left_part_of_price, right_part_of_price = price.split('.')
        return True
    except ValueError:
        return False


def format_price(price):
    fractional_part_max_value = 5
    if not test_price(price):
        return None
    integer_part, fractional_part = price.split('.')
    if int(fractional_part[0]) >= fractional_part_max_value:
        integer_part = str(int(integer_part) + 1)
    int_part_with_spaces = add_spaces_around_symbols(integer_part)
    return int_part_with_spaces


if __name__ == '__main__':
    price_to_format = input("Введите цену,"
                            " которую необходимо отформатировать: ")
    formatted_price = format_price(price_to_format)
    if formatted_price is None:
        print("Введите корректное значение!")
    else:
        print("Отформатированная цена: %s" % formatted_price)
