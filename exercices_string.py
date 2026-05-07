import random

#1
your_message = input("Enter your message: ")
max_length = 10

if len(your_message) > max_length:
    print(your_message[:max_length], "...", sep="")
else:
    print(your_message)

#2
sentence = "I have no idea what to say"
list_of_words = sentence.split(" ")
new_sentence = "-".join(list_of_words)
print(new_sentence)

#3
for i in range(5):
    print("Goodbye", i)

#4
total=0
for i in range(1,11):
    if i % 2 == 0:
        total+=i
print(total)

#5
sentence = "I have no idea what to say"
vowels = "aeiou"
space = " "
result = ""

for i in sentence:
    if i.lower() in vowels:
        result += i.upper()
    elif i == space:
        result += "_"
    else:
        result += i.lower()
print(result)

#6
my_list = ["apple", "banana", "cherry"]
for i, v in enumerate(my_list):
    print(i+1, v)
#7
count = 0
winner = random.randint(1,100)
while True:
    if count == 10:
        print("\033[32mYou lost! :'(\033[0m")
        break
    player = int(input("Enter your number: "))
    if player == winner:
        print("\033[32mYou Won!\033[0m")
        break
    if player < winner:
        print("\033[34mYour number is too low\033[0m")
    if player > winner:
        print("\033[31mYour number is too high\033[0m")
    count += 1

#8
#Rock Paper Scissor
player1_score = 0
player2_score = 0
player1_choice = ""

while True:
    if player1_score == 3:
        break
    if player2_score == 3:
        break

    player1_choice = input("Rock - Paper - Scissors (R,P,S): ")
    player2_choice = random.randint(1, 3)
    if player1_choice.upper() != "R" and player1_choice.upper() != "P" and player1_choice.upper() != "S":
        print("Wrong choice. Try again")
        break
    if player1_choice.upper() == "R":
        print("\nYou played ROCK")
    elif player1_choice.upper() == "P":
        print("You played PAPER")
    else:
        print("You played SCISSORS")

    if player2_choice == 1:
        print("Your adversary played ROCK")
    elif player2_choice == 2:
        print("Your adversary played PAPER")
    else:
        print("Your adversary played SCISSORS")


    if player1_choice.upper() == "R" and player2_choice == 1:
        print("\033[34mTie!\033[0m")
    if player1_choice.upper() == "P" and player2_choice == 2:
        print("\033[34mTie!\033[0m")
    if player1_choice.upper() == "S" and player2_choice == 3:
        print("\033[34mTie!\033[0m")

    if player1_choice.upper() == "R" and player2_choice == 3:
        print("\033[32mYou win! +1pt\033[0m")
        player1_score += 1
    if player1_choice.upper() == "P" and player2_choice == 1:
        print("\033[32mYou win! +1pt\033[0m")
        player1_score += 1
    if player1_choice.upper() == "S" and player2_choice == 2:
        print("\033[32mYou win! +1pt\033[0m")
        player1_score += 1

    if player1_choice.upper() == "R" and player2_choice == 2:
        print("\033[31mYou lose! P2 -> +1pt\033[0m")
        player2_score += 1
    if player1_choice.upper() == "P" and player2_choice == 3:
        print("\033[31mYou lose! P2 -> +1pt\033[0m")
        player2_score += 1
    if player1_choice.upper() == "S" and player2_choice == 1:
        print("\033[31mYou lose! P2 -> +1pt\033[0m")
        player2_score += 1
    print("\nTOTAL:\nPlayer 1 :",player1_score, "\nPlayer 2 :",player2_score,"\n")

if player1_score == 3:
    print("\033[32mYou won! Congratz!\033[0m")
else:
    print("\033[31mYou Lost! T_T\033[0m\n")


