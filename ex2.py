import random
import timeit
import matplotlib.pyplot as plt

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def test_algorithm(algorithm, input_size, case_type):
    if case_type == 'best':
        test_array = list(range(1, input_size + 1))  # Already sorted
    elif case_type == 'worst':
        test_array = list(range(input_size, 0, -1))  # Reverse order
    else:
        test_array = [random.randint(1, 1000) for _ in range(input_size)]  # Random order
    
    start_time = timeit.default_timer()
    algorithm(test_array.copy())
    elapsed_time = timeit.default_timer() - start_time
    
    return elapsed_time

# Test both algorithms on 20 different sizes and for best, worst, and average cases
input_sizes = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 150, 200, 250, 300, 400, 500, 750, 1000, 1500, 2000]
case_types = ['best', 'worst', 'average']

for case_type in case_types:
    for size in input_sizes:
        bubble_sort_time = test_algorithm(bubble_sort, size, case_type)
        quicksort_time = test_algorithm(quicksort, size, case_type)
        print(f"Case: {case_type.capitalize()}, Input Size: {size}, Bubble Sort Time: {bubble_sort_time}, Quicksort Time: {quicksort_time}")
