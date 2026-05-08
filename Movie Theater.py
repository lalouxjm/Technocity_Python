#7
#Cinema Seat Reservation
import my_func

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