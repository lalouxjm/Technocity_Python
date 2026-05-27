lst = [-1,0,3,5,9,12]
t1 = 9
t2 = 2


def binary_search(nums: list[int], target: int) -> int:
    for i, v in enumerate(nums):
        if v == target:
            return i
    return -1

print(f"is {t1} in {lst}? : {False if binary_search(lst, t1) == -1 else True }")
print(f"is {t2} in {lst}? : {False if binary_search(lst, t2) == -1 else True }")