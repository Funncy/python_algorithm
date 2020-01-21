import decimal

name = "스칼렛"

# 문자 처음부터 width(50개), fillchar(-)
print(name.ljust(50, '-'))

# 문자 끝에서부터 width(50개),  fillchar(-)
print(name.rjust(50, '-'))

# format
print("이름:{who} 나이:{age}".format(who="효준", age=28))
print("이름:{} 나이:{}".format("효준", 28))

# format 지정 문자열 : s는 문자열 r은 표현형식 a는 아스키 코드 형식
print("{0}, {0!s}, {0!r}, {0!a}".format(decimal.Decimal("99.9")))

# 문자열 언패킹
hero = "버피"
number = 99
print("{number}: {hero}".format(**locals()))

# splitlines 줄바꿈 기준으로 물자열 분리
slayers = "로미오\n줄리엣"
print(slayers.splitlines())

# strip() A.strip(B) A 문자열 앞뒤의 문자열 B에 속하면 제거
slayers = "9로미오 & 줄리엣&"
print(slayers.strip("9&"))