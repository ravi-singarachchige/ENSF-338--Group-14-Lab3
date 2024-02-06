import random

#2
def bubble_sort(arr):
    comparisons = 0
    swaps = 0
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            comparisons += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swaps += 1
                swapped = True
        if not swapped:
            break
    return comparisons, swaps

#3 (running with inputs of increasing sizes)
input_sizes = [100, 500, 1000, 5000, 10000]  # Input sizes to test
min_val = 0  # Minimum value for input integers
max_val = 10000  # Maximum value for input integers
num_runs = 10  # Number of runs for each input size

for size in input_sizes:
    total_comparisons = 0
    total_swaps = 0
    for _ in range(num_runs):
        arr = [random.randint(min_val, max_val) for _ in range(size)]
        comparisons, swaps = bubble_sort(arr)
        total_comparisons += comparisons
        total_swaps += swaps
    avg_comparisons = total_comparisons / num_runs
    avg_swaps = total_swaps / num_runs
    print(f"Input Size: {size}")
    print(f"Average Comparisons: {avg_comparisons}")
    print(f"Average Swaps: {avg_swaps}")
    print("------------------------------")
