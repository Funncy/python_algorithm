
#최대 공약수 GCD

def finding_gcd(a ,b):
    while (b != 0):
        result = b
        a , b = b , a % b
    return result

def test_finding_gcd():
    number1 = 21
    number2 = 12
    assert(finding_gcd(number1, number2) == 3)
    print("test_finding_gcd 테스트 통과")

test_finding_gcd()