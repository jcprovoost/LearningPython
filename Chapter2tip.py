# LearningPython
# Jesper Provoost, 2017, CreaTe UT

print("What to tip the restaurant waiter or waitress?")

totalPrice = int(input("What is the total price of the meal?"))

fifteenPerc = int(totalPrice / 100 * 15)
twentyPerc = int(totalPrice / 100 * 15)

print("\nFeeling satisfied? With a total of €",totalPrice,", a 15% tip would be €" \
       ,fifteenPerc,"\nIn total this is €",totalPrice + fifteenPerc)

print("\nWant to be really generous? Give a tip of € \
       ,twentyPerc,"\nIn total this is €",totalPrice + twentyPerc)
