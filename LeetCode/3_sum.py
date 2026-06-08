nums = [-1,0,1,2,-1,-4]
pos = []
def three_sum(nums):
    result = []

    for i in range(len(nums)-1):
        pair = [nums[i], nums[i+1]]
        if pair not in pos:
            pos.append(pair)

        for j in range(len(nums)):
            possibility = [pair[0], pair[1], nums[j]]
            possibility.sort()
            if pair[0] + pair[1] + nums[j] == 0 and possibility not in result:
                result.append(possibility)
    return result
print(three_sum(nums))