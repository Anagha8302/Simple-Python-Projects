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

#Write your code below this line 👇
game_images=[rock,paper,scissors]
your_choice=int(input("What do you choose?Type 0 for Rock,1 for Paper and 2 for Scissors:\n"))
if your_choice>=3 or your_choice<0:
  print("You typed an invalid number.You lose:(")
else:
  print(game_images[your_choice])
  comp_choice=random.randint(0,2)
  print(f"Computer chose:")
  print(game_images[comp_choice])

  if your_choice==0 and comp_choice==2:
    print("you win!!")
  elif comp_choice==0 and your_choice==2:
    print("You lose:(")
  elif comp_choice>your_choice:
    print("You lose:(")
  elif your_choice>comp_choice:
    print("You win!!")
  elif comp_choice==your_choice:
    print("It's a Draw.")
  
