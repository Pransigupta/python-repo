import random

computer = random.choice([-1, 0, 1])

your = input("Enter your choice (s/w/G): ")

dict = {"s": -1, "w": 0, "G": 1}
reverseDict = {-1: "snake", 0: "water", 1: "gun"}

your = dict[your]

print(f"Your choice: {reverseDict[your]}")
print(f"Computer choice: {reverseDict[computer]}")

if computer == your:
    print("It's a draw!")

elif computer == -1 and your == 0:
    print("You lose!")

elif computer == 0 and your == -1:
    print("You win!")

elif computer == 0 and your == 1:
    print("You win!")

elif computer == 1 and your == 0:
    print("You lose!")

elif computer == -1 and your == 1:
    print("You win!")

elif computer == 1 and your == -1:
    print("You lose!")