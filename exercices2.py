#1
#Finding the absolute value of a number
import datetime
import random


number = float(input("Enter a number: "))
print("Absolute Value: ", abs(number))

#2
#Younger & Older
current_year = datetime.datetime.now().year
my_age = current_year - 1982
your_age = int(input("Enter your age: "))

if your_age < my_age:
    print("You are younger than me")
else:
    print("You are older than me")

#3
#Cold or Hot?
temperature = int(input("Enter a temperature (C°): "))

match temperature:
    case t if t < 10:
        print("It's cold")
    case t if 10 <= t <= 15:
        print("That's cool")
    case t if 16 <= t <= 20:
        print("It's pleasant")
    case t if t >= 21:
        print("It's hot")
    case _:
        print("Wrong temperature")

#4
#Check if a number is even or odd
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("Your number is even")
else:
    print("Your number is odd")

#5
#Agricultural Cooperative
weather = random.choice([1,2,3])

match weather:
    case 1:
        print("The weather is good. Employees work on schedule 1.")
    case 2:
        print("The weather is bad. Employees work on schedule 2.")
    case 3:
        print("The weather is moderate. Employees work on schedule 3.")

#6
#Museum Admission Fees
standard_price = 8.50
customer_age = int(input("Enter your age: "))

if customer_age < 12:
    print("Children under 12yo are admitted for free")
elif 12 >= customer_age < 18:
    print("Young people under 18yo have a 12% discount. Price =", standard_price - ((standard_price/100)*12))
else:
    print("Adult price is €", standard_price,sep="")

#7
#Age-based category
user_age = int(input("Enter your age (6-12): "))
match user_age:
    case u if u < 6:
        print("You are too young")
    case u if 6 >= u <= 7:
        print("You are a child")
    case u if 8 >= u <= 9:
        print("You are a pupil")
    case u if 10 >= u <= 11:
        print("You are a youth")
    case u if u >= 12:
        print("You are a cadet")
    case _:
        print("Wrong age")

#8
#BMI Calculation
your_height = float(input("Enter your height (in meters): "))
your_weight = float(input("Enter your weight (in kg): "))

your_bmi = your_weight / (your_height ** 2)

if your_bmi < 18.5:
    print("You are underweight")
elif 18.5 <= your_bmi < 25:
    print("You are healthy")
elif 25 <= your_bmi < 30:
    print("You have excess weight")
else:
    print("You are obese")

#9
#Calculating Student Grade Averages

number_of_quizzes = int(input("How many quizzes?: "))
grades = []
for i in range(number_of_quizzes):
    grade = float(input(f"Enter a grade {i+1}: "))
    grades.append(grade)

average = sum(grades) / number_of_quizzes
print(f"The average grade is {average:.2f}")
if average > 18:
    print("Very good!")
elif 16 <= average <= 18:
    print("Good")
elif 13 <= average <= 15:
    print("Satisfactory")
elif 10 <= average <= 12:
    print("Pass")
else:
    print("Fail!")