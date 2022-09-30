# Задать список из n чисел последовательности  (1 + 1/n)^n и вывести на экран их сумму.
n = int(input("Введите натуральное число n "))
num = []
res =0
for i in range(1, n+1):
    
    res= ((1+1/i)**i)
    num.append (res)
      
print(sum(num))