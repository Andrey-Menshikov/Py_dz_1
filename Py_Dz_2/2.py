import random
n = random.randint(10, 99)

my_list = []
for i in range(1, n+1):
    my_list.append((1+1/i)**i)
print(f" Список из {n} чисел: {my_list}")

summ = sum(my_list)
print(f"Сумма:{round(summ)}")





