Selection = (input("Welcome to the console vending machine\n"
             "Choose a snack (Chips, Candy, Pastry)..."))

Chips = ["Doritos", "Lays", "Fritos"]
Candy = ["Skittles", "Twix", "Butterfinger"]
Pastry = ["Cupcake", "Danish","Barclaw"]

while True:
    if Selection.lower == "chips":
        snack = Chips.pop()

    elif Selection.lower == "candy":
        snack = Candy.pop()

    elif Selection.lower == "pastry":
        snack = Pastry.pop()
    else:
        raise ValueError:
            except(print("Sorry, enter chips, candy, or pastry for a snack"))

        continue

    print("Thanks for using the console vending machine, here's you {}, {} enjoy".format(snack, Selection))