def fizzbuzz(num):
    lst = []

    for i in range(num):
        if (i + 1) % 3 == 0 and (i + 1) % 5 == 0:
            lst.append("FizzBuzz")
        elif (i + 1) % 5 == 0:
            lst.append("Buzz")
        elif (i + 1) % 3 == 0:
            lst.append("Fizz")
        else:
            lst.append(f"{i + 1}")
    return lst

print(fizzbuzz(3))
print(fizzbuzz(5))
print(fizzbuzz(15))

def fizzlaaabuzz(num) -> list:
    lst = []

    for i in range(num):
        if (i+1) % 3 == 0 and (i+1) % 5 == 0 and (i+1) % 4 == 0:
            lst.append("FizzLaaaBuzz")
        elif (i+1) % 4 == 0 and (i+1) % 5 == 0:
            lst.append("LaaaBuzz")
        elif (i + 1) % 3 == 0 and (i + 1) % 5 == 0:
            lst.append("FizzBuzz")
        elif (i+1) % 3 == 0 and (i+1) % 4 == 0:
            lst.append("FizzLaaa")
        elif (i + 1) % 5 == 0:
            lst.append("Buzz")
        elif (i + 1) % 4 == 0:
            lst.append("Laaa")
        elif (i + 1) % 3 == 0:
            lst.append("Fizz")
        else:
            lst.append(f"{i + 1}")
    return lst

print(fizzlaaabuzz(5))
print(fizzlaaabuzz(20))
print(fizzlaaabuzz(60))