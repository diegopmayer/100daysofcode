from random import randint

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 forr Scissors\n"))
computer_choise = randint(0, 2)

dic = {0:rock, 1:paper, 2:scissors}
print("you chose:")
print(dic[user_choice])

print("Computer Chose:")
print(dic[computer_choise])

if user_choice == computer_choise:
    print("It's a draw")
elif user_choice == 0:
    if computer_choise == 1:
        print("you lose")
    elif computer_choise == 2:
        print("You win")
elif user_choice == 1:
    if computer_choise == 0:
        print("You win")
    elif computer_choise == 2:
        print("you lose")
elif user_choice == 2:
    if computer_choise == 0:
        print("You lose")
    elif computer_choise == 1:
        print("You win")