# Задача 14: Требуется вывести все целые степени двойки
# (т.е. числа вида 2k), не превосходящие числа N.


def DegreeOfTwo(n):
    result = ''
    for i in range(n):
        if pow(2,i) > n:
            break
        result += str(pow(2,i)) + ' '

    return result

n = int(input('Введите число, а программа выдаст все степени числа 2 до вашего числа: '))
print(DegreeOfTwo(n))