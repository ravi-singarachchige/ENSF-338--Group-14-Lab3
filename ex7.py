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

#Question 3
plt.scatter(tasks, best_midpoints)
plt.xlabel('Tasks')
plt.ylabel('Best Midpoints')
plt.savefig('ex7_plot.png')
plt.show()

#Question 4

#Question 4

#most of the time best midpoint is 0 and couple of time it's 1000.

#If the best midpoint is frequently at the extremes (0 or 1000), it suggests that the target values we're searching for are often located near the beginning or the end of your data array.

#The choice of initial midpoint does affect the performance of a binary search. Binary search works by repeatedly dividing the search space in half. 

#If the target value is near the beginning of the array, an initial midpoint of 0 would be more efficient because it reduces the search space more quickly. 

#Similarly, if the target value is near the end of the array, an initial midpoint of 1000 would be more efficient.
