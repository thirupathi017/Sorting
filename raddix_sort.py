def count_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # Count increment
    for i in arr:
        index = (i // exp) % 10
        count[index] += 1

    # Cumulative
    for i in range(1, 10):
        count[i] = count[i] + count[i - 1]

    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        pos = count[index] - 1
        output[pos] = arr[i]
        count[index]-=1

    return output

def radix(arr):
    exp = 1
    max_val = max(arr)
    while max_val // exp > 0:
        arr=count_sort(arr, exp)
        exp *= 10
    print(arr)















original_array = []
n = int(input("Enter the range for the original array: "))
for i in range(n):
    original_array.append(int(input(f"original_array[{i}]: ")))

radix(original_array)
