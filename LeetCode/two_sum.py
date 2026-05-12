
list1 = [2, 7, 11, 15]
list2 = [3, 2, 4]
list3 = [3, 3]

def two_sum(nums: list, target: int) -> list | None:
    left, right = 0, len(nums) - 1

    while left < right:
        s = nums[left] + nums[right]
        if s == target:
            return [left, right]
        elif s < target:
            left += 1
        else:
            right -= 1
    return None

print("two_sum")
print(two_sum(list1, 9))
print(two_sum(list2, 6))
print(two_sum(list3, 6))

def two_sum2(nums: list, target: int) -> list | None:
    seen = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

    return None

print("two_sum2")
print(two_sum2(list1, 9))
print(two_sum2(list2, 6))
print(two_sum2(list3, 6))
