def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

# Step 1: Generate a vector of 16 elements for worst-case complexity
worst_case_vector = list(range(16, 0, -1))

# Step 2: Manually show the workings of the algorithm until the vector is sorted
sorted_vector = quicksort(worst_case_vector)
print("Original Vector:", worst_case_vector)
print("Sorted Vector:", sorted_vector)

# Step 3: Run quicksort on inputs of increasing size which incur worst-case complexity
for size in range(10, 101, 10):
    input_vector = list(range(size, 0, -1))
    sorted_result = quicksort(input_vector)
    print(f"\nInput Size: {size}")
    print("Sorted Result:", sorted_result)
