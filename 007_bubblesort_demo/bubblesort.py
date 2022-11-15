'''
bubblesort.py

Demonstrate bubblesort

'''
my_list = [8, 10, 6, 2, 4]  # list to sort
swapped = True  # It's a little fake, we need it to enter the while loop.
count = 0
limit =len(my_list)
while swapped:
    swapped = False  # no swaps so far
    for i in range(limit - 1):
        count+=1
        if my_list[i] > my_list[i + 1]:
            swapped = True  # a swap occurred!
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
    limit -= 1

print(my_list)
print('count', count)
