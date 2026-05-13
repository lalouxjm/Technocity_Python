nums1 = [1,2,3,1]
nums2 = [1,2,3,4]
nums3 = [1,1,1,3,3,4,3,2,4,2]

def contains_duplicate(nums: list) -> bool:
    result = False
    new_set = set(nums)

    if len(nums) != len(new_set):
        result = True

    return result

print(contains_duplicate(nums1))
print(contains_duplicate(nums2))
print(contains_duplicate(nums3))