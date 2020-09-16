import math
import sys
str = "Ведьгун Е.A. ИУ5-54Б"
print(len(str)*'-')
print(str)
print(len(str)*'-')
try:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    c = int(sys.argv[3])
except:
    print("Неверный формат аргументов командной строки")
    while(True):
        print("Введите коэффициенты биквадратного уравнения")
        try:
            a = int(input())
            b = int(input())
            c = int(input())
        except:
            print("Неверный формат ввода данных")
        else:
            break
if(a == 0 or b == 0 or c == 0):
    if ((a == 0 and b == 0) or ((b == 0) and (-c / a < 0)) or ((a == 0) and (-c / b < 0))):
        print("Действительных корней нет")
    elif (( b == 0 and c == 0) or ( a == 0 and c == 0)):
        print("Уравнение имеет один корень: 0")
    else:
        if ((a != 0) and (-c / a > 0)):
            print("Уравнение имеет два корня: %f %f" %((-c / a)**(0.25),-((-c / a)**(0.25))))
        if ((b != 0) and (-c / b > 0)):
            print("Уравнение имеет два корня: %f %f" %((-c / b)**(0.25),-((-c / b)**(0.25))))
        if ((a != 0) and (-b / a > 0)):
            print("Уравнение имеет три корня: 0 %f %f" %((-b / a)**(0.25),-((-b / a)**(0.25))))
else:
    d = b**2 - 4*a*c
    if (d < 0):
        print("Действительных корней нет")
    elif (d == 0):
        x1 = -b / (2 * a)
        if (x1 < 0):
            print("Действительных корней нет")
        else:
            x1 = math.sqrt(x1)
            print("Уравнение имеет два корня: %f %f" %(x1,-x1))
    elif (d > 0):
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        if ((x1 < 0) and (x2 < 0)):
            print("Действительных корней нет")
        elif ((x1 < 0) or (x2 < 0)):
            if (x1 < 0):
                x2 = math.sqrt(x2)
                print("Уравнение имеет два корня: %f %f" %(x2,-x2))
            else:
                x1 = math.sqrt(x1)
                print("Уравнение имеет два корня: %f %f" %(x1,-x1))
        else:
            x1 = math.sqrt(x1)
            x2 = math.sqrt(x2)
            print("Уравнение имеет четыре корня: %f %f %f %f" %(x1,-x1,x2,-x2))