#ex1
#Display the sum of two integers and one decimal
import datetime
import math
import random

a=1
b=2
c=3.4

print(a, " + ", b, " + ",c, " = ", a+b+c)

#ex2
#Ask the user for their birthplace and display it in a sentence
birthplace = input("Enter your birthplace: ")
print("you were born in", birthplace)

#ex3
#ask the user for their birth year, then calculate and display their current age
birth_year = int(input("Enter the year of your birth (xxxx): "))
current_year = datetime.datetime.now().year
print("you are", current_year - birth_year, "years old")

#ex4
#Ask the user for the length and width of a rectangle , then display the area
length = int(input("Enter the length of your rectangle (cm²): "))
width = int(input("Enter the width of your rectangle (cm²): "))
print("The area of your rectangle is", length * width, "cm²")

#ex5
#Ask the user to enter a temperature in degrees Celsius, then display the conversion to Fahrenheit
#Ask the user to enter a temperature in degrees Fahrenheit, convert this temperature to Celsius, add 5°, and then display the result
first_temp = float(input("Convert the temperature C° in F°: "))
print("Temperature is ", (first_temp*(9/5))+32, "F°")
second_temp = float(input("Convert the temperature F° in C° +5°: "))
print("Temperature is ", ((second_temp-32)*(5/9))+5, "C°")

#ex6
#Ask the user for the radius of a circle, then display its circumference
radius = float(input("Enter the radius of your circle: "))
circumference = (2 * math.pi) * radius
rounded_circumference = round(circumference, 2)
print("The circumference of your circle is", rounded_circumference, "cm")

#ex7
#Ask the user for their favorite color, then display a personalized message with that color
color = input("What is your favorite color? ").lower()

if color == "red":
    print("\033[31mI like red too <3\033[0m")
elif color == "green":
    print("\033[32mGreen is a very good color\033[0m")
elif color == "blue":
    print("\033[34mBlue like the sea ^_^ \033[0m")
elif color == "yellow":
    print("\033[33mLike a little chick\033[0m")
elif color == "magenta":
    print("\033[35mOh... Magenta? Okay...\033[0m")
elif color == "cyan":
    print("\033[36mIsn't cyan just like blue?\033[0m")
else:
    print("Sorry, I don't know that color :'(")

#ex8
#Ask the user to enter two numbers, then display their product
first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
print("The sum of your numbers is", first_number + second_number)

#9
#Ask The user to enter Three numbers, then display the average of these three numbers
third_number = int(input("Enter the first number: "))
forth_number = int(input("Enter the second number: "))
fifth_number = int(input("Enter the third number: "))

average = (third_number + forth_number + fifth_number) / 3
print("The average of your numbers is", average)

#10
#Elevator
top_floor = 13
bottom_floor = -2
total_floor = 16
employee_floor = int(input("Enter the floor your starting from: "))

if employee_floor > top_floor or employee_floor < bottom_floor:
    print("You have entered an invalid floor!")
else:
    going_up = top_floor - employee_floor
    print("you went from the", employee_floor, "th floor to the", top_floor, "th floor, traveling", going_up, "floors" )
    print("Then you went from the", top_floor, "th floor to the", bottom_floor, "th floor, traveling", total_floor, "floors" )
    print("You travelled a total of", going_up+total_floor, "floors" )

#11
#Word Mixer

word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")
word3 = input("Enter the third word: ")
words = [word1, word2, word3]
effect = random.choice([1,2])
if effect == 1:
    result = " ".join([word + " " + word for word in words])
    print("Repeat each word twice:", result)
else:
    result = " ".join([word[::-1].upper() for word in words])
    print("Reverse words:", result)

#12
#Funny Sequence
funny_name = input("Enter a name: ")
funny_object = input("Enter the name of an object: ")
funny_location = input("Enter a location: ")

print(funny_name, "found a", funny_object, "in", funny_location)

#13
#ID Card

first_name = input("Enter your first name: ").capitalize()
last_name = input("Enter your last name: ").upper()
age = int(input("Enter your age: "))
grade = input("Enter your grade: ").upper()

print("Last name:", last_name)
print("First name:", first_name)
print("Age:", age)
print("Grade:", grade)

#14
#Invert Values
a = float(input("Enter a value for a: "))
b = float(input("Enter a value for b: "))
a,b = b,a
print("After swap:")
print("a =", a)
print("b =", b)

#15
#Calculate time
total_second = int(input("Enter a number of seconds: "))
hours = total_second // 3600
remaining_seconds = total_second % 3600
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

print(hours, ":", minutes, ":", seconds)