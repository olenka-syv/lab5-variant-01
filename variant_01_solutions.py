"""
Лабораторна робота: Функції та декомпозиція задач
Студент: Сиваченко Олена
Група: 1, EIP 30
Варіант: 1
"""
import math
def target_function(x):
    y = math.acos(x*x) - x
    return (y)

e = 0.0001

def solve_bisection(a = 0, b = 1):
    while e < (b-a)/2:
        c = (a+b)/2
        if target_function(a)*target_function(b) < 0:
            a = a
            b = c
            c = (a+b)/2
        elif target_function(a)*target_function(b) > 0:
            a = c
            b = b
            c = (a+b)/2
        else:
            return c
    else:
        return c
print (solve_bisection())