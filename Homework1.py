# Найти сумму чисел в вещественном числе
n = int(input('Введите число: '))
sum = 0
while n != 0:
    #узнаем последнюю цифру числа
    p = n % 10
    sum += p
    # отсекаем последнюю цифру
    n = n//10
print(sum)
