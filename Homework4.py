#Задать список из N элементов, заполненных числами из [-N, N]. Найти произведение элементов на указанных позициях. 
# Позиции хранятся в списке positions - создайте этот список (например: positions = [1, 3, 6]).

positions = [1, 3, 6]
n = int(input("Введите натуральное число n: "))
res = []
result = 1

for i in range(n*-1, n+1):
    res.append(i)
    
print(res[0:(len(res))])

for i in range(0, len(positions)):
    result *= res[positions[i]]

print(f'Произведение элементов: {result}')