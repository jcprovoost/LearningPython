
import random  

print("You have 10 guesses to determine the number between 1 and 100")

chosenNumber = random.randint(1, 100)
guess = int(input("My guess is: "))
tries = 1

def main():
  while not tries > 10:
      if guess == the_number:
          print(chosenNumber, "was the correct number!")
          print("You did it in", tries, "tries")
          break
      if guess > chosenNumber:
          print("Wrong! The answer is lower")
      elif guess < the_number:
          print("Wrong! The asnwer is higher")
      guess = int(input("My", tries,"th guess is: "))
      tries += 1

# calling the main method from here constantly
main()

if tries > 10:
    print("You failed.")
