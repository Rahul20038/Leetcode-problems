def count_pairs_with_sum_less_than_target(arr, target):
    arr.sort()
    left = 0
    right = len(arr) - 1
    count = 0
    while left < right:
        if arr[left] + arr[right] < target:
            count += (right - left)
            left += 1
        else:
            right -= 1
    return count

# Example Usage
arr = [1, 3, 5, 7, 9]
target = 10
result = count_pairs_with_sum_less_than_target(arr, target)
print("Number of pairs:", result)
