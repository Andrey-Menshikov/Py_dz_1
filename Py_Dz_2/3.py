import random

my_list = []
for i in range(random.randint(1, 100)):

      my_list.append(i)
print(my_list)
for i in range(len(my_list)):
    temp =0
    n = random.randint(0, len(my_list)-1)

    temp = my_list[n]
    my_list[n] = my_list[i]
    my_list[i] = temp

print(my_list)


