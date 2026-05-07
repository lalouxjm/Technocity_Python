from copy import deepcopy
import my_func

"""
#1
a = [1,2,3]
b = deepcopy(a)
b.append([4,5])
print(b)
print(a)

#2
squares = [x**2 for x in range(5)]
print(squares)

#numbers = [int(input("next number: ")) for x in range(10)]
numbers = [1,2,3,4,5,6,7,8,9,10]
print(numbers)

for item in numbers:
    evens = [i for i in numbers if i % 2 == 0]

print(evens)

#3
def list_sum(lst):
    total = 0
    for i in lst:
        total += i
    return total

def max_list(lst):
    return max([x for x in lst])

print(list_sum(numbers))
print(max_list(numbers))
"""
#4
"""
toolbox = ["Screwdriver", "Hammer", "Adjustable Wrench", "Saw", "Duck Tape", "Nails"]
print("Toolbox: ",toolbox)
while True:
    new_tool = input("What tool do you want to add? ")
    if new_tool not in toolbox:
        toolbox.append(new_tool)
        break
    else:
        print(my_func.red(f"{new_tool} is already in the toolbox"))
print("Toolbox: ",toolbox)
while True:
    remove_tool = input("What tool do you want to remove? ")
    if remove_tool not in toolbox:
        print(my_func.red(f"{remove_tool} is not in the toolbox"))
    else:
        toolbox.remove(remove_tool)
        break
print("Toolbox: ",toolbox)
print("Toolbox 3rd item: ",toolbox[2])
"""

#5
"""
result = tuple(int(input(f" {i+1}. Enter a value between 0 and 255:")) for i in range(3))
print(f"RGB({result[0]}, {result[1]}, {result[2]})", sep="")
print("Hexadecimal: #",f"{result[0]:02X}", f"{result[1]:02X}", f"{result[2]:02X}", sep="")
"""
"""
def get_color_input():
    while True:
        try:
            values = input("Enter 3 integers for R, G, B (0-255), separated by spaces: ").split()
            r, g, b = map(int, values)

            if not all(0 <= x <= 255 for x in (r, g, b)):
                raise ValueError(my_func.red("Values must be between 0 and 255"))

            return (r, g, b)
        except ValueError as e:
            print(my_func.red(f"Invalid input: {e}. Please try again.\n"))


color = get_color_input()

print(f"Decimal: RGB{color}")

hex_color = '#{:02X}{:02X}{:02X}'.format(*color)
print(f"Hexadecimal: {hex_color}")
"""
"""
#6
s = "AB"
res = {x: {y: x+y for y in s} for x in s}
print(res)

#7
keys = ["A", "B", "C"]
values = ["1","2","3"]
print("dict1")
d = dict(zip(keys, values))
print(d)
for k, v in zip(keys, values):
    print(k, v)

print("dict2")
d2 = {'A': '10', 'B': '20', 'C': '30'}
print(d2)
for k, v1, v2 in zip(d.keys(), d.values(), d2.values()):
    print(k, v1, v2)
"""
#7
#Cinema Seat Reservation

row = ["A","B","C","D"]
seat = ["1","2","3","4","5","6","7","8"]
reservations = {}

def init_reservation():
    #print("init")
    for i in range(4):
        for j in range(8):
            reservations[(row[i]+seat[j])] = ""

def display_seats():
    print("===SEATING DISPLAY===")
    for i in range(4):
        if i != 0:
            print("\n")
        for j in range(8):
            print(row[i]+seat[j], sep="", end="")
            if j != 7:
                print(":[ ] - ", end="")
            else:
                print(":[ ]", end="")

def display_reservations():
    for i in range(4):
        for j in range(8):
            seat_id = row[i] + seat[j]
            status = reservations[seat_id]

            if status == "":
                print(f"{seat_id}: Empty", end=" | ")
            else:
                print(my_func.blue(f"{seat_id}: {status}"), end=" | ")

        print()

def make_reservation():
    print(my_func.green("===Reservation==="))
    client_name = input("Please enter your name: ")
    for key in reservations:
        if reservations[key] == '':
            reservations[key] = client_name.capitalize()
            break

def cancel_reservation():
    print(my_func.green("===Cancellation==="))
    cancellation_name = input("Please enter the name for the cancellation: ")
    found = False
    for key in reservations:
        if reservations[key] == cancellation_name.capitalize():
            reservations[key] = ''
            found = True
            break
    if not found:
        print(my_func.red("You don't have a reservation yet."))

print(my_func.green("===MOVIE THEATER RESERVATION==="))
init_reservation()
while True:
    #print(reservations)

    try:
        menu_choice = int(input("\nPress 1 to create a reservation \nPress 2 to cancel a reservation \nPress 3 to see the seating display \nPress 4 to exit : "))
    except ValueError:
        print(my_func.red("Please enter a valid number"))
        continue


    if menu_choice == 1:
        make_reservation()
    if menu_choice == 2:
        cancel_reservation()
    if menu_choice == 3:
        #display_seats()
        display_reservations()
    if menu_choice == 4:
        print("Thank you for your time! Have a nice day!")
        break