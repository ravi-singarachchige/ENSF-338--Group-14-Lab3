#Question 1
import json
import time
import matplotlib.pyplot as plt

def binary_search(arr, low, high, x, first_mid):
    if high >= low:
        mid = first_mid if first_mid is not None else (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x, None)
        else:
            return binary_search(arr, mid + 1, high, x, None)
    else:
        return -1


# Load data from JSON files
with open('ex7data.json', 'r') as f:
    data = json.load(f)

with open('ex7tasks.json', 'r') as f:
    tasks = json.load(f)

#Question 2

# Perform binary search for each task with different midpoints
midpoints = [i for i in range(0, len(data), 1000)]  # Midpoints to test
best_midpoints = []


for task in tasks:
    best_time = float('inf')
    best_midpoint = None
    for midpoint in midpoints:
        start_time = time.time()
        binary_search(data, 0, len(data)-1, task, midpoint)
        end_time = time.time()
        elapsed_time = end_time - start_time
        if elapsed_time < best_time:
            best_time = elapsed_time
            best_midpoint = midpoint
    best_midpoints.append(best_midpoint)

print(best_midpoints)

#Question 4
plt.scatter(tasks, best_midpoints)
plt.xlabel('Tasks')
plt.ylabel('Best Midpoints')
plt.savefig('ex7_plot.png')
plt.show()