list1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]
target = 17

def binary_search(arr, target):
  lo, hi = 0, len(arr) - 1

  while lo <= hi:
    mid = (lo + hi) // 2
    if   arr[mid] == target:
        return mid
    elif arr[mid] <  target:
        lo = mid + 1
    else:
        hi = mid - 1
  return -1


print(f"{target} is on index: {binary_search(list1, target)}")