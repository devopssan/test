def two_sum(numbers, target):
    left, right = 0, len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == target:
            return [left + 1, right + 1]  # 1-indexed
        elif current_sum < target:
            left += 1
        else:
            right -= 1

# Example test case
print(two_sum([2,7,11,15], 9))  # Expected output: [1, 2]

# I have added few more test cases to check the function works for various inputs and constraints
print(two_sum([-10, -3, 4, 5, 9], 6))  # Expected output: [2, 5]
print(two_sum([1, 2, 3, 4, 4, 9, 56, 90], 8))  # Expected output: [4, 5]
print(two_sum([-1000, -999, 0, 3, 999], -1))  # Expected output: [1, 5]
print(two_sum([100, 200, 300, 400, 800], 700))  # Expected output: [3, 4]