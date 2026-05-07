import my_func
#1
#Discount function
"""
def discount(p:float, d:float) -> float:
    return (p/100)*d

try:
    price_original = float(input("Enter the price of the product: "))
    discount_amount = float(input("Enter the discount percentage: "))
except ValueError:
    print("Please enter a numeric float value")
else:
    print("The discounted price is €", round(price_original - discount(price_original, discount_amount),2))

"""

#2
#MAP
string_of_number = ['1', '2', '3', '4', '5']
res = map(int, string_of_number)
print(list(res))

"""
def double(value: int) -> int:
    return value * 2
def half(value: float) -> float:
    return value / 2
def expose(value: int) -> int:
    return pow(value,2)
"""

numbers = [1,2,3,4,5]
result = list(map(my_func.double, numbers))
print(result)
result1 = list(map(my_func.half, numbers))
print(result)
result2 = list(map(my_func.expose, numbers))
print(result2)

#3
#Lambda
multiply = lambda a,b: a*b
print("Multiply:", multiply(3,2))

sum_of_3 = lambda a,b,c: a+b+c
print("Sum:",sum_of_3(3,4,5))

power_of_2 = map(lambda num: pow(num,2), numbers)
print("List of power",list(power_of_2))

celsius = [0,10,20,30,40,50,100]
c_to_f = list(map(lambda cel: (cel * 9/5)+32, celsius))
print("Celsius to fahr",c_to_f)

fahrenheit = [0,32,40,70,80,90,100,110]
f_to_c = list(map(lambda fahr : round((fahr - 32) * 5/9,2), fahrenheit))
print("fahr to Celsius",f_to_c)


"""
##FUNCTIONS

#filter()
#Keeps only elements from an iterable that satisfy a condition
numbers = [1,2,3,4,5,6,7,8,9,10]
result = filter(lambda x: x % 2 == 0, numbers)
print("filter",list(result))

words = ["cat", "dog", "elephant"]
result = filter(lambda w: len(w) > 3, words)
print("filter",list(result))

#useful when you want to clean or select data.

#format()
#Format a value into a string ith a specific layout
text = "Hello {}"
print("format -",text.format("Steff"))

number = 3.14159
print("format -","{:.2f}".format(number))

#useful when you need a clean output for a text or numbers,...

#type()
#Returns the type of a specified object

a = ("apple", "banana", "cherry")
b = "Hello me"
c = 42

x = type(a)
y = type(b)
z = type(c)
print("type -", x,y,z, sep=" - ")

#useful when débugging or checking what kind of data you're dealing with

#all()
#Returns 'True' if all elements are true

numbers = [2,4,6,8,10]
print("Test ALL -",all(n % 2 == 0 for n in numbers))
#true if all numbers are even

values = [True, True, False]
print("Test ALL -",all(values))
#return 'false' since at least one value is not 'true'.

#useful when you need to check if everything meets a condition

#any()
#Returns 'True' if at least one element is true

numbers = [1,2,3,4,5]
print("Test ANY -",any(n % 2 == 0 for n in numbers))
#true since 2 numbers are even

values = [False, False, False]
print("Test ANY -",any(values))
#false since all values are false

#useful when you want to check if something exists
"""