import random
number = random.randint(1,9)
chances = 0
while chances<5:
    guess = int(input("Enter your guess : "))
    if guess == number:
        print("Congratulations")
    elif guess<number:
        print("you guess was too low: guess a number higher than",guess)
    else:
        print("your guess was too high: guess a number lower than this",guess)
    chances += 1
if not chances<5 :
    print("YOU LOOSE. the number is", number)