#Question 1:

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
    return arr

def binary_search(arr, val, start, end):
    if start == end:
        if arr[start] > val:
            return start
        else:
            return start+1
    if start > end:
        return start

    mid = (start+end)//2
    if arr[mid] < val:
        return binary_search(arr, val, mid+1, end)
    elif arr[mid] > val:
        return binary_search(arr, val, start, mid-1)
    else:
        return mid

def binary_insertion_sort(arr):
    for i in range(1, len(arr)):
        val = arr[i]
        j = binary_search(arr, val, 0, i-1)
        arr = arr[:j] + [val] + arr[j:i] + arr[i+1:]
    return arr

#Question2:

import timeit
import random

lengths = [100, 1000, 5000, 10000]
times_insertion = []
times_binary_insertion = []

for length in lengths:
    arr = [random.random() for _ in range(length)]
    
    start = timeit.default_timer()
    insertion_sort(arr)
    end = timeit.default_timer()
    times_insertion.append(end - start)
    
    start = timeit.default_timer()
    binary_insertion_sort(arr)
    end = timeit.default_timer()
    times_binary_insertion.append(end - start)

print("Insertion sort times:", times_insertion)
print("Binary insertion sort times:", times_binary_insertion)

#Question3:

import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate

# Assuming times_insertion and times_binary_insertion are lists containing the time taken by each algorithm
lengths = [100, 1000, 5000, 10000]

# Interpolation
xnew = np.linspace(min(lengths), max(lengths), 500)
f_insertion = interpolate.interp1d(lengths, times_insertion, kind='quadratic')
f_binary_insertion = interpolate.interp1d(lengths, times_binary_insertion, kind='quadratic')

plt.figure(figsize=(10, 6))
plt.plot(lengths, times_insertion, 'o', xnew, f_insertion(xnew), '-')
plt.plot(lengths, times_binary_insertion, 'o', xnew, f_binary_insertion(xnew), '-')
plt.legend(['Insertion Sort', 'Interpolation of Insertion Sort', 'Binary Insertion Sort', 'Interpolation of Binary Insertion Sort'], loc='best')
plt.xlabel('Length of Array')
plt.ylabel('Time (seconds)')
plt.title('Time Complexity of Insertion Sort and Binary Insertion Sort')
plt.savefig('ex5_plot.png', dpi=300)
plt.show()

#Question4:

#The speed of the algorithms depends on the specific inputs and their initial order. However, in general, binary insertion sort can be faster than traditional insertion sort.

#Traditional insertion sort has a time complexity of O(n^2) because for each element in the array, it may have to compare and move it with every other element that came before it.

#Binary insertion sort, on the other hand, reduces the number of comparisons by using a binary search to find the correct position of the current element, which takes O(log n) time.

#However, it still has to move the remaining elements to make space for the current element, which takes O(n) time. So, the overall worst-case time complexity is still O(n^2), but on average, binary insertion sort will make fewer comparisons than traditional insertion sort.

#Therefore, if the cost of comparisons is significantly higher than the cost of swaps (such as with large records where comparison involves multiple fields or complex computations), binary insertion sort can be faster. 

#However, if the cost of swaps is high (such as with large records that take a lot of time to move), the advantage of binary insertion sort may be diminished, as it still makes the same number of swaps as traditional insertion sort.
