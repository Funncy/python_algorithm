"""
2020.01.17

Python Algorithm

진법 변환 문제
"""

# n진법 -> 10진수


def convert_to_decimal(number, base):
    result = 0
    multiplier = 0
    while number > 0:
        result += (number % 10) * (base ** multiplier)
        multiplier += 1
        number = number // 10
    return result

# 10진수 -> n진법


def convert_from_decimal(number, base):
    result = 0
    multiplier = 0
    while number > 0:
        result += (number % base) * (10 ** multiplier)
        multiplier += 1
        number = number // base
    return result

# 10진수 -> n진법 (16진수 포함)
def convert_from_decimal_larger_bases(number, base):
    strings = "0123456789ABCDEFGHIJ"
    result = ""
    while number > 0:
        digit = number % base
        result = strings[digit] + result
        number = number // base
    return result

#10진수 -> n진법 (16진수 포함) - 재귀
def convert_dec_to_any_base_rec(number, base):
    convertString = "0123456789ABCDEFGHIJ"
    if number < base:
        return convertString[number]
    else:
        return convert_dec_to_any_base_rec(number // base, base) \
            + convertString[number % base]


def test_convert_to_decimal():
    number, base = 1001, 2
    assert(convert_to_decimal(number, base) == 9)
    number, base = 1234, 8
    assert(convert_to_decimal(number, base) == 668)
    number, base = 1234, 16
    assert(convert_to_decimal(number, base) == 4660)
    print("test_convert_to_decimal 통과")


def test_convert_from_decimal():
    number, base = 9, 2
    assert(convert_from_decimal(number, base) == 1001)
    number, base = 1234, 8
    assert(convert_from_decimal(number, base) == 2322)
    print("convert_from_decimal 통과")

def test_convert_from_decimal_larger_bases():
    number, base = 31, 16
    assert(convert_from_decimal_larger_bases(number, base) == "1F")
    number, base = 123, 16
    assert(convert_from_decimal_larger_bases(number, base) == "7B")
    print("test_convert_from_decimal_larger_bases 통과")

def test_convert_dec_to_any_base_rec():
    number, base = 9, 2
    assert(convert_dec_to_any_base_rec(number, base) == "1001")
    number, base = 123, 16
    assert(convert_dec_to_any_base_rec(number, base) == "7B")
    print("test_convert_dec_to_any_base_rec 통과")


test_convert_to_decimal()
test_convert_from_decimal()
test_convert_from_decimal_larger_bases()
test_convert_dec_to_any_base_rec()
