"""
Лабораторна робота: Функції та декомпозиція задач
Студент: Сиваченко Олена
Група: 1, EIP 30
Варіант: 1
"""
import math
def target_function(x):
    y = math.acos(x**2) - x
    return (y)

def solve_bisection(a = 0, b = 1, e = 0.0001):
    N = 0
    while e < (b-a)/2:
        c = (a+b)/2
        if target_function(a)*target_function(c) < 0:
            a = a
            b = c
            N = N + 1
        elif target_function(a)*target_function(c) > 0:
            a = c
            b = b
            N = N + 1
        else:
            return (c, N)
    else:
        return (c, N)
print (solve_bisection())