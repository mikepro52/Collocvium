def factorial_list(n):
    factorials = []
    fact = 1
    for i in range(1, n + 1):
        fact *= i
        factorials.append(fact)
    return factorials

if __name__ == "__main__":
    n = int(input("Введите натуральное число n: "))
    result = factorial_list(n)
    print(f"Первые {n} факториалов: {result}")