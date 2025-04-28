secret_code = 7
chances = 5

while chances > 0:
    guess = int(input("Guess the secret code: "))
    
    if guess == secret_code:
        print("You found the secret code!")
        break
    elif guess > secret_code:
        print("Too High")
    else:
        print("Too Low")
    
    chances -= 1
    if chances == 0:
        print("Game Over! You ran out of chances")