from copy import deepcopy
import my_func


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
#tuple exercise
students = [
    (101, "Alex"),
    (102, "Bob"),
    (103, "Charlie")
]
def print_students():
    print(my_func.blue("print student names"))
    for student in students:
        print(f"{student[0]} : {student[1]}")

print(my_func.blue("unpack and print names"))
for student_id, name in students:
    print(name)

print(my_func.blue("find student"))
def find_student(search_id):

    for student_id, name in students:

        if student_id == search_id:
            return name

    return my_func.red("Student not found!")

print("student id: 101 -> ",find_student(101))
print("student id: 102 -> ",find_student(102))
print("student id: 103 -> ",find_student(103))
print("student id: 104 -> ",find_student(104))

def add_student():
    new_student = input("Name of new student: ")
    new_id = max(student[0] for student in students)
    new_input = new_id + 1, new_student
    students.append(new_input)
    print_students()

add_student()

def get_all_ids():
    list_of_ids = []
    for student in students:
        list_of_ids.append(student[0])
    print("list of ids ->",list_of_ids)

get_all_ids()

def tuple_to_dict(tuple_obj):
    dict_of_obj = {}

    dict_of_obj[tuple_obj[0]] = tuple_obj[1]
    return dict_of_obj

a = (101, "Alex")
b = (102, "Bob")
c = (103, "Charlie")

d = tuple_to_dict(a)
e = tuple_to_dict(b)
f = tuple_to_dict(c)

print(d)

#GET DICT
students = [
    {'id': 101, 'firstname': 'Alex', 'lastname' : 'Mercer'},
    {'id': 102, 'firstname': 'Bob', 'lastname' : 'Henderson'},
    {'id': 103, 'firstname': 'Charlie', 'lastname' : 'Johnson'}
]
for student in students:
    print(student.get('firstname'), student.get('lastname'))

list_of_students = [
    (101, 'Alex', 'Mercer'),
    (102, 'Bob', 'Henderson'),
    (103, 'Charlie', 'Johnson')
]
dict_of_students = {
     student[0]: {'id':  student[0], 'firstname': student[1], 'lastname': student[2]}
     for student in list_of_students
}

for k, v in dict_of_students.items():
    print(f"The student id number {k} is {v.get('firstname')}")