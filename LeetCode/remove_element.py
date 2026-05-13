nums1 = [3,2,2,3]
val1 = 3
nums2 = [0,1,2,2,3,0,4,2]
val2 = 2


def remove_element(nums: list, val: int) -> int:
    k = 0

    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1

    return k

print(remove_element(nums1, val1))
print(remove_element(nums2, val2))

