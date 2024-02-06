#Question 1
import json

def binary_search(arr, target, first_midpoint):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = first_midpoint if start == 0 else (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1

# Load data from JSON files
with open('ex7data.json', 'r') as f:
    data = json.load(f)

with open('ex7tasks.json', 'r') as f:
    tasks = json.load(f)

# Perform binary search for each task
first_midpoint = len(data) // 2  # Default first midpoint
for target in tasks:
    index = binary_search(data, target, first_midpoint)
    print(f'Target: {target}, Index: {index}')

#Question 2
    
import json
import time

def binary_search(arr, target, first_midpoint):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = first_midpoint if start == 0 else (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1

# Load data from JSON files
with open('ex7data.json', 'r') as f:
    data = json.load(f)

with open('ex7tasks.json', 'r') as f:
    tasks = json.load(f)

# Perform binary search for each task with different midpoints
for target in tasks:
    best_time = float('inf')
    best_midpoint = None
    for first_midpoint in range(len(data)):
        start_time = time.time()
        binary_search(data, target, first_midpoint)
        end_time = time.time()
        elapsed_time = end_time - start_time
        if elapsed_time < best_time:
            best_time = elapsed_time
            best_midpoint = first_midpoint
    print(f'Target: {target}, Best Midpoint: {best_midpoint}, Best Time: {best_time}')

#Question 3
    
import json
import time
import matplotlib.pyplot as plt

def binary_search(arr, target, first_midpoint):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = first_midpoint if start == 0 else (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1

# Load data from JSON files
with open('ex7data.json', 'r') as f:
    data = json.load(f)

with open('ex7tasks.json', 'r') as f:
    tasks = json.load(f)

# Perform binary search for each task with different midpoints
targets = []
best_midpoints = []
for target in tasks:
    best_time = float('inf')
    best_midpoint = None
    for first_midpoint in range(len(data)):
        start_time = time.time()
        binary_search(data, target, first_midpoint)
        end_time = time.time()
        elapsed_time = end_time - start_time
        if elapsed_time < best_time:
            best_time = elapsed_time
            best_midpoint = first_midpoint
    targets.append(target)
    best_midpoints.append(best_midpoint)

# Plot targets vs best midpoints
plt.scatter(targets, best_midpoints)
plt.xlabel('Target')
plt.ylabel('Best Midpoint')
plt.title('Best Midpoint for Each Target')
plt.savefig('ex7_plot.png')
plt.show()