import math

# 반복문 사용 O(n)
def find_fibonacci_seq_iter(n):
    if n < 2 : return n
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

# 재귀 사용 O(n^2)
def find_fibonacci_seq_rec(n):
    if n < 2 : return n
    return find_fibonacci_seq_rec(n-1) + find_fibonacci_seq_rec(n-2)

#수식 사용 O(1) 단,70번쨰부터 정확하지 않다
def find_fibonacci_seq_form(n):
    sq5 = math.sqrt(5)
    phi = (1 + sq5) / 2
    return int(math.floor(phi ** n / sq5))

# 제네레이터 사용 Generator
def fibo_generator():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a+b

fg = fibo_generator()
for _ in range(10):
    print(next(fg), end=" ")

def test_find_fib():
    n = 10
    assert(find_fibonacci_seq_rec(n) == 55)
    assert(find_fibonacci_seq_iter(n) == 55)
    assert(find_fibonacci_seq_form(n) == 55)
    print("테스트 통과")
    
test_find_fib()