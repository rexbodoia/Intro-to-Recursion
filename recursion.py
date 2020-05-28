#!/anaconda3/bin/python
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(15):
    print(fibonacci(i), end = ' ')
print('')

import random
list = list(range(10))
random.shuffle(list)

def bubble_sort(list):
    for i in range(len(list)):
        for j in range(len(list)-1):
            curr = list[j]
            next = list[j+1]
            if curr > next:
                list[j] = next
                list[j+1] = curr
    return list

print(list)
print(bubble_sort(list))
random.shuffle(list)

def rec_sort_helper(list, n):
    if n == 1:
        return list
    for i in range(len(list) - 1):
        curr = list[i]
        next = list[i+1]
        if curr > next:
            list[i] = next
            list[i+1] = curr
    return rec_sort_helper(list, n - 1)

def rec_sort(list):
    return rec_sort_helper(list, len(list))

print(list)
print(rec_sort(list))
