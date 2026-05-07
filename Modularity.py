import math
import my_func
from datetime import datetime, timedelta, timezone


#1
def perimeter(n):
    return 2* math.pi * n

print(round(perimeter(5),2), "cm")

#2
def next_week(n):
    today = datetime.now()
    one_more_week = today + timedelta(weeks=n)
    formated = one_more_week.strftime("%d/%m/%Y")
    return formated

print("In one week, it will be", next_week(1))

#3
def offset(n):
    today = datetime.now(timezone.utc)
    local_time = today + timedelta(hours=n)
    return local_time.strftime("%d/%m/%Y - %H:%M:%S")
while True:
    try:
        hours = int((input("Enter an offset in hours: ")))
    except ValueError:
        print(my_func.red("Please enter a valid number"))
        continue
    else:
        print(my_func.blue(f"In GMT{hours:+}, the date and time is: ", offset(hours)))
        break


print(my_func.snake_case("Hello World"))
print(my_func.factorial(8))