from collections import Counter

list1 = [3,2,3]
list2 = [2,2,1,2,2,1,1,2,2,1,1]

def majority_elements(nums: list) -> int:
    """
    nums.sort()
    return nums[len(nums) // 2]
    """


def majority_elements2(nums: list):
    """
    count = Counter(nums)
    return count.most_common(1)[0][0]
    """


print(majority_elements(list1))
print(majority_elements(list2))
print(majority_elements2(list1))
print(majority_elements2(list2))
