d1 = [1,2,3]
d2 = [2,5,5,6]
d3 = [9]

def plusOne(digits: list) -> list:
    numbers = "".join(map(str, digits))
    numbers = int(numbers) + 1
    result = []

    for num in str(numbers):
        result.append(int(num))

    return result

print(plusOne(d1))
print(plusOne(d2))
print(plusOne(d3))