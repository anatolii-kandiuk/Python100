import random

# print("Random number between 1 and 10:", random.randint(1, 10))
# print("Random number between 1 and 100:", random.uniform(1, 10))

# list_of_friends = ["Alice", "Bob", "Charlie", "David", "Eve"]
# random_friend = random.choice(list_of_friends)
# print("Random friend:", random_friend)

rock_paper_scissors_ascii = [
    """
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """,
    """
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    """,
    """
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """
]

user_choice = int(input("Choose rock (0), paper (1), or scissors (2): "))
computer_choice = random.randint(0, 2)

print("You chose:", rock_paper_scissors_ascii[user_choice])
print("Computer chose:", rock_paper_scissors_ascii[computer_choice])

if user_choice == computer_choice:
    print("It's a tie!")
elif (user_choice == 0 and computer_choice == 2) or \
     (user_choice == 1 and computer_choice == 0) or \
     (user_choice == 2 and computer_choice == 1):
    print("You win!")
else:
    print("You lose!")