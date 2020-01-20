import math
import random

#전체 탐색
def finding_prime(number):
    #절대값 반환
    num = abs(number)
    if num < 4 : return True
    for x in range(2, num):
        if num % x == 0:
            return False
    return True

#제곱근 활용 (절반만 탐색)
def finding_prime_sqrt(number):
    num = abs(number)
    if num < 4 : return True
    for x in range(2, int(math.sqrt(num)) + 1):
        if number % x == 0:
            return False
    return True

#페르마의 소정리
def finding_prime_fermat(number):
    if number <= 102:
        for a in range(2, number):
            if pow(a, number-1, number) != 1:
                return False
        return True
    else:
        for i in range(100):
            a = random.randint(2, number - 1)
            if pow(a, number -1, number) != 1:
                return False
        return True

#소수 생성기 (number 자리수의 소수 생성)
def generate_prime(number=3):
    while 1:
        p = random.randint(pow(2, number-2), pow(2, number-1)-1)
        p = 2 * p + 1
        if finding_prime_sqrt(p):
            return p

def test_finding_prime():
    number1 = 17
    number2 = 20
    assert(finding_prime(number1) is True)
    assert(finding_prime(number2) is False)
    assert(finding_prime_sqrt(number1) is True)
    assert(finding_prime_sqrt(number2) is False)
    assert(finding_prime_fermat(number1) is True)
    assert(finding_prime_fermat(number2) is False)
    print("통과!!")

test_finding_prime()