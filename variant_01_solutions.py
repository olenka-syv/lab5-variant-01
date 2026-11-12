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

def solve_bisection(a, b, e):
    steps = []
    N = 0
    while e < (b-a)/2:
        c = (a+b)/2
        if target_function(a)*target_function(c) < 0:
            a = a
            b = c
            N = N + 1
            steps.append((N, c))
        elif target_function(a)*target_function(c) > 0:
            a = c
            b = b
            N = N + 1
            steps.append((N, c))
        else:
            return (c, N, steps)
    else:
        return (c, N, steps)

def save_results_to_file(results, filename = "results_variant_01.txt"):
    c, N, steps = results
    with open(filename, "w") as file:
        file.write("Result\n")
        file.write(f"Root:{c:.6f}\n")
        file.write("Table of iterations:\n")
        file.write(f"{"Iteration":>15} | {"Approximation":<15}\n")
        for step, value in steps:
            file.write(f"{step:>15} | {value:<15.6f}\n")

def main():
    a = 0
    b = 1
    e = 0.0001
    print(solve_bisection(a, b, e))
    save_results_to_file(solve_bisection(a, b, e))

main()


