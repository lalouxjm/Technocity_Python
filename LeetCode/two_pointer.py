list1 = [1,3,5,7,11]
target1 = 10

def two_pointer(arr, target):
  left, right = 0, len(arr) - 1

  while left < right:
    s = arr[left] + arr[right]
    if s == target:
        print(arr[left], arr[right])
        return True
    elif s < target:
        left += 1
    else:
        right -= 1
  return False

# arr must be sorted!
print(two_pointer(list1, target1))  # True (3+7)