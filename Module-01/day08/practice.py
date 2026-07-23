#Exerciese from module day08
# 1 
def total(nums):
    if len(nums) == 0:
        return 0
    return nums[0] + total(nums[1:])

numbers = [10, 20, 30, 40]
print("Total:", total(numbers))

def count_down(n):
    if n <= 0:
        return
    print(n)
    count_down(n - 1)

count_down(5)

print('\n')
#2
def binary_search(items, target):
    left = 0
    right = len(items) - 1

    while left <= right:
        mid = (left + right) // 2

        if items[mid] == target:
            return mid
        elif items[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

balances = [100, 200, 350, 400, 500, 750]

print(binary_search(balances, 400))
print(binary_search(balances, 900))

print('\n')
#3
def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def merge_sort(items):
    if len(items) <= 1:
        return items

    mid = len(items) // 2

    left = merge_sort(items[:mid])
    right = merge_sort(items[mid:])

    return merge(left, right)

numbers = [7, 3, 8, 1, 6, 9, 2, 5]

print("Merge Sort:", merge_sort(numbers))
print("Python Sort:", sorted(numbers))

print('\n')
#4
accounts = [
    ("Biruk", 500),
    ("Belete", 1200),
    ("Dani", 750),
    ("Melos", 300)
]

sorted_accounts = sorted(accounts, key=lambda account: account[1], reverse=True)

print(sorted_accounts)

print('\n')
#5
def has_pair(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        current_sum = nums[left] + nums[right]

        if current_sum == target:
            return True
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return False


numbers = [1, 2, 3, 4, 6, 8, 10]

print(has_pair(numbers, 10))
print(has_pair(numbers, 20))