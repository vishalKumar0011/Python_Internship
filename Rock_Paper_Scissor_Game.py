#Rock Paper Scissors Game
import random
choices = ["Rock","Paper","Scissor"]
print("Choices:")
print("1. Rock")
print("2. Paper")
print("3. Scissor")
print("4. Quit")
user_wincount = 0
computer_wincount = 0
tie = 0
while True:
    user_choice = input("Enter your choice: ")
    if user_choice == "Quit":
        print("GoodBye!")
        break

    computer_choice = random.choice(choices)
    print(f"\nUser choice: {user_choice} \nComputer Choice: {computer_choice}")

    if user_choice == computer_choice:
        tie = tie + 1
        print("It's a tie")
    elif (user_choice == "Rock" and computer_choice == "Scissor") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissor" and computer_choice == "Paper"):
        user_wincount = user_wincount + 1
        print("You win!")
    else:
        computer_wincount = computer_wincount + 1
        print("Computer wins!")    

print(f"User Win: {user_wincount}")
print(f"Computer Win: {computer_wincount}")
print(f"Tie : {tie}")
