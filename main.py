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

game_images = [rock, paper, scissors]

user_choice= randint(0,2)#int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice >= 3 or user_choice < 0:
    print("You type invalid number")
else:
    print(game_images[user_choice])

    choice_pc = randint(0,2)
    print(f"Computer chose ")
    print(game_images[choice_pc])
# 0 ROCK - 1 PAPER - 2 SCISSORS
    if user_choice == 0 and choice_pc == 2:
        print("You win!")
    elif choice_pc == 0 and user_choice == 2:
        print("You lose")
    elif choice_pc > user_choice:
        print("You lose")
    elif user_choice > choice_pc:
        print("You win!")
    elif choice_pc == user_choice:
        print("It's a draw")












