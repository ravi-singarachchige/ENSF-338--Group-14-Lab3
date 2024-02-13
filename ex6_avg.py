#Question 1

import random
from typing import List

def linear_search(arr: List[int], target: int) -> int:
    for i, item in enumerate(arr):
        if item == target:
            return i
    return -1

def binary_search(arr: List[int], target: int) -> int:
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            return mid
    return -1

def quicksort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

#Question 2

import timeit

linear_times = []
binary_times = []

for _ in range(1000):
    arr = [random.randint(0, 1000) for _ in range(1000)]
    target = random.randint(0, 1000)

    start = timeit.default_timer()
    linear_search(arr, target)
    end = timeit.default_timer()
    linear_times.append(end - start)

    start = timeit.default_timer()
    sorted_arr = quicksort(arr)
    binary_search(sorted_arr, target)
    end = timeit.default_timer()
    binary_times.append(end - start)

print(f"Average time for linear search: {sum(linear_times) / len(linear_times)}")
print(f"Average time for binary search: {sum(binary_times) / len(binary_times)}")

#Question 3

import timeit
import random

sizes = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]
linear_times = []
binary_times = []

for size in sizes:
    arr = [random.randint(0, size) for _ in range(size)]
    target = random.randint(0, size)

    start = timeit.default_timer()
    linear_search(arr, target)
    end = timeit.default_timer()
    linear_times.append(end - start)

    start = timeit.default_timer()
    sorted_arr = quicksort(arr)
    binary_search(sorted_arr, target)
    end = timeit.default_timer()
    binary_times.append(end - start)

print("Size\tLinear\tBinary")
for size, linear, binary in zip(sizes, linear_times, binary_times):
    print(f"{size}\t{linear}\t{binary}")

#Question 4
    
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.plot(sizes, linear_times, label='Linear Search')
plt.plot(sizes, binary_times, label='Quicksort + Binary Search')
plt.legend(loc='best')
plt.xlabel('Input Size')
plt.ylabel('Time (seconds)')
plt.title('Performance Comparison')
plt.savefig('ex6_avg.png')
plt.show()

#Question 5

#For small input sizes, linear search can be faster because it doesn't have the overhead of sorting the array.

#For larger input sizes, binary search can be faster, despite the sorting overhead, because its search time complexity is O(log n), which is much better than the O(n) of linear search.