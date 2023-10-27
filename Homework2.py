# Task 1

number = int(input("Введите целое число: "))

if number == 0:
    print("нулевое число")
elif number > 0:
    if number % 2 == 0:
        print("положительное четное число")
    else:
        print("положительное нечетное число")
else:
    if number % 2 == 0:
        print("отрицательное четное число")
    else:
        print("отрицательное нечетное число")

# Task2

# Не получилось

# Task 3

X = int(input("Введите минимальную сумму инвестиций (X): "))
A = int(input("Введите сумму денег у Майкла (A): "))
B = int(input("Введите сумму денег у Ивана (B): "))

if A >= X and B >= X:
    print(2)  # Могут вложиться оба
elif A >= X:
    print("Mike")  # Только Майкл
elif B >= X:
    print("Ivan")  # Только Иван
elif A + B >= X:
    print(1)  # Вместе им хватает
else:
    print(0)  # Никто не может вложиться
