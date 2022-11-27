import random

num = str(random.randint(100, 999999))
summ = 0
for i in range(len(num)):
    # print(i, num[i])
    summ = summ+int(num[i])


print(f"Сумма цифр в числе {num} = {summ}")










