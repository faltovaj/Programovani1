def fibonacci(N):
    print("N-te Fibonacciho cislo budeme pocitat pro N =", N)
    N1, N2 = 0, 1
    if N < 2:
        return N
    for i in range(2, N+1):
        N1, N2 = N2, N1 + N2
    return N2

def faktorial(N):
    print("Volame faktorial pro cislo", N)
    if N < 1:
        print("Faktorial pouze pro N >= 1!")
        return None
    factorial = 1
    while N > 1:
        factorial *= N
        N -= 1
    return factorial

print(fibonacci(5))
print()
print(fibonacci(0))
print()
print(fibonacci(1))
print()
print(fibonacci(50))

print()
print(faktorial(10))
print()
print(faktorial(1))
print()
print(faktorial(0))
