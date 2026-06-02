nums1 = [-2,1,-3,4,-1,2,1,-5,4]
nums2 = [5,4,-1,7,8]

def max_sub_array(nums: list) -> int:
    """
    result = 0
    max_result = 0
    for i in range(len(nums)):
        result += nums[i]
        if result < 0:
            result = 0
        if result > max_result:
            max_result = result

    return max_result
    """


print(max_sub_array(nums1))
print(max_sub_array(nums2))