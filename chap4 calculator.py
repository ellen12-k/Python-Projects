def Plus(x, y):
    return x + y

def Minus(x, y):
    return x - y

def Multi(x, y):
    return x * y

def Divi(x, y):
    return x / y

while True:
    x, s, y = map(str, input('계산식을 입력해주세요>>> ').split())
    x = int(x)
    y = int(y)

    if s == '+':
        result = Plus(x, y)
    elif s == '-':
        result = Minus(x, y)
    elif s == '*':
        result = Multi(x, y)
    elif s == '/':
        result = Divi(x, y)
    else:
        continue

    q = input("다시 입력: c, 종료: e >>> ")
    if q == 'c':
        continue;

    elif q == 'e':
        break;

    f = open("result.txt",'r')
    result = "%d \n" %result
    f.write(result)
    f.close()