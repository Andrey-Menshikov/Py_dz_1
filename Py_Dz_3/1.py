input_data = input("Введите элементы списка из целых чисел через запятую : ")
original_list = input_data.replace(" ", "").split(",")
summ = 0

for index in range(len(original_list)):
    if index % 2 != 0:
        summ += int(original_list[index])

print(f"Сумма чисел стоящих на нечетной позиции равна {summ}")
