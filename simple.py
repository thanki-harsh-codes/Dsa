import random

def bubble_sort(arr):
    print("\nBubble Sort:")
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            print(f"Step {i}.{j}: {arr}")
    return arr

def insertion_sort(arr):
    print("\nInsertion Sort:")
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            print(f"Insert {key} at position {j + 1}: {arr}")
        arr[j + 1] = key
    return arr

def selection_sort(arr):
    print("\nSelection Sort:")
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print(f"Swap index {i} with min index {min_idx}: {arr}")
    return arr

# Main Program
if __name__ == "_main_":
    original_data = random.sample(range(10, 100), 8)  # Generate 8 random numbers between 10–99
    print("Original List:", original_data)

    bubble_sort(original_data.copy())
    insertion_sort(original_data.copy())
    selection_sort(original_data.copy())