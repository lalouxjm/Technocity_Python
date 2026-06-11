from collections import Counter

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in nums:
    print(num)

for i, num in enumerate(nums):
    print(i, num)

for i in range(len(nums)):
    print(i, nums[i])

for i, num in enumerate(nums, 1):
    print(i, num)

nums = [5,9,3,7]

for i, num in enumerate(nums):
    if num == 3:
        print(i)

d = {}

for i, num in enumerate(nums):
    d[i] = num
print(d)

for i, (k, v) in enumerate(d.items(), 1):
    print(i, k, v)

d = {
    "name": "Jamie",
    "age": 30,
    "city": "Brussels"
}

for key in d.keys():
    print(key)
for value in d.values():
    print(value)

for key, value in d.items():
    print(key, value)

for i, (key, value) in enumerate(d.items(), 1):
    print(i, key, value)

for i, key in enumerate(d.keys(), 1):
    print(i, d[key])

for i, key in enumerate(sorted(d.keys()), 1):
    print(i, key, d[key])

count = Counter("banana")
print(count.most_common(3)[1][0])

for i, v in enumerate(count.most_common(3)):
    print(i, v)

seen = set()
for char in "banana":
    if char not in seen:
        seen.add(char)
print(seen)

for i in sorted(seen):
    print(i)


d = dict(zip("123", "abcd"))
print(d)

for k, v in d.items():
    print(k, v)