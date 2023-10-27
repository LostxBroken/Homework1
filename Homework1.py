# Task

a, b = float(input()), float(input())
print(a * b, 2 * (a + b))

# Task2

n = int(input("Введите пятизначное число: "))

tot = n // 10000
th = (n // 1000) % 10
hun = (n // 100) % 10
tens = (n // 10) % 10
unit = n % 10

result = (tens ** unit) * hun / (tot - th)

print("Результат:", result)
