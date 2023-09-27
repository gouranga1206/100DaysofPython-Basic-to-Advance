import random
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

User_Choice = int(input("What do you want to choice?\nChoose 0 for Rock.\nChoose 1 for Paper.\nChoose 2 for Scissor.\nchoice: "))

Computer_Choice = random.randint(0,2)

if not User_Choice:
    print("You have entered invalid input!")
else :
    def Cases(random_choice):
        match random_choice:
            case 0:
                if User_Choice == 1 :
                    print("User Wins")
                elif User_Choice ==2:
                    print("System Wins")
                else:
                    print("Draw")
            case 1:
                if User_Choice == 2 :
                    print("User Wins")
                elif User_Choice ==0:
                    print("System Wins")
                else:
                    print("Draw")
            case 2:
                if User_Choice == 0 :
                    print("User Wins")
                elif User_Choice ==1:
                    print("System Wins")
                else:
                    print("Draw")
            case default:
                print("Invalid input try again!")

random_choice = Cases(int(Computer_Choice))