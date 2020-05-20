# 사칙연산 계산기 프로그램 만들기
# 사용자로부터 "숫자 연산자 숫자"를 입력받아 결과값 출력
# 사용자가 c를 입력하면 다시 입력받아야하고, e를 입력하면 계산기 종료
# e를 입력하기 전까지는 종료되면 안됨
# 숫자나 연산자를 잘못 입력하면 다시 입력받도록 하기
while(1):
    a, s, b = map(str, input('식 입력: ').split())
    a = int(a)
    b = int(b)

    if s == "+": print("%d"%(a + b))
    elif s == "-": print("%d"%(a - b))
    elif s == "*": print("%d"%(a * b))
    elif s == "/": print("%d"%(a / b))

    q = input("다시 입력: c, 종료: e >>> ")
    if q == 'c':
        continue;

    elif q == 'e':
        break;
