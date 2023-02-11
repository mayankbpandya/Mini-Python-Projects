print("Welcome to General Knowledge Quiz!")

play = input("Do you want to play? Y/N:")
score = 0

if play.lower() != "y":
    quit()
else:
    print("Welcome! Let's begin :)")
    pass


answer = int(input("How many days are there in a week?"))
if answer == 7:
    print('Correct!')
    score += 1
else:
    print("Incorrect!")
    print('Correct answer is: 7')

answer = int(input("How many days are there in a leap year? "))
if answer == 366:
    print('Correct!')
    score += 1
else:
    print("Incorrect!")
    print('Correct answer is: 366')

answer = input("Name the smallest continent? ")
if answer.lower() == "australia":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")
    print('Correct answer is: Australia')

answer = input("Name the planet nearest to the Earth? ")
if answer.lower() == "mercury":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")
    print('Correct answer is: Mercury')

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")
print("Thanks for playing!")