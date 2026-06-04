array1 = [2,4,6,8]
array2 = [2,6,18,54]
array3 = [-9,-4,1,6,11]
array4 = [120,60,30,15]

def ArrayChallenge(arr):
    diff = arr[1] - arr[0]
    ratio = arr[1] / arr[0]

    is_arithmetic = True
    is_geometric = True

    for i in range(1, len(arr)):
        if arr[i] - arr[i - 1] != diff:
            is_arithmetic = False

        if arr[i] / arr[i - 1] != ratio:
            is_geometric = False

    if is_arithmetic:
        return "Arithmetic"

    if is_geometric:
        return "Geometric"

    return -1

print(f"{array1} is",ArrayChallenge(array1))
print(f"{array2} is",ArrayChallenge(array2))
print(f"{array3} is",ArrayChallenge(array3))
print(f"{array4} is",ArrayChallenge(array4))