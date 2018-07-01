#list comprehension
my_list = [number for number in range(0,1000) if number % 2 == 0]

#for loop
my_list = []
for number in range(0, 1000):
    if number % 2 == 0:
        my_list.append(number)