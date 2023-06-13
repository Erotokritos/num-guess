import random 
upper_bound = input("Type the max number: ")

if upper_bound.isdigit():
    upper_bound = int(upper_bound)
    if upper_bound <=0:
        print("Insert a number larger than zero! ")
        quit()
else:
    print("Please insert a number!")
    quit()
    
random_num = random.randint(0,upper_bound)
guesses = 0
while True:
    guesses +=1
    guess = input("Guess my number: ")
    if guess.isdigit():
        guess = int(guess)
    else:
        print("Please type a number. ")
        continue

    if guess == random_num:
        print("Congrats ! You got it !")
        break
    else:
        print("Wroong!")
        if(abs(guess - random_num) > 10):
            print("Cold")
        elif(abs(guess-random_num)>5):
            print("Breeze")
        elif(abs(guess-random_num)<5 and abs(guess-random_num)>2):
            print("Warm")
        else:
            print("Hot")

print("You got it in", guesses,"guesses")