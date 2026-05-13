list1 = [3,2,3]
list2 = [2,2,1,1,1,1,1,2,2]

def majority_elements(nums: list) -> int:
    n = maj = 0
    nums.sort()
    n = len(nums)
    maj = nums[n // 2]

    return maj

print(majority_elements(list1))
print(majority_elements(list2))
