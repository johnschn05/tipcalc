#!usr/bin/python3

# Tip Calculator
# printing app title
print(27 * "-")
print("Tip Calculator 2019")
print("Author: John E. Schneider")
print("Released: 22-May-2019")
print("v1.0")
print(27 * "-")

# defining variables with user's input
meal_total = float(input("Enter meal total: "))
tot_tippers = float(input("Enter number of tippers: "))
tip = float(input("Enter tip percent: "))

#moving decimal two spaces to the left
tip = (tip / 100)
tip_total = str(meal_total * tip / tot_tippers)

# display user inputs for varification
meal_total = str(meal_total)
tot_tippers = str(tot_tippers)
tip = int(tip * 100)
tip = str(tip)
print(27 * "-")
print("Your inputs are as follows:")
print(("Meal Total: ") + (meal_total))
print(("Total Tippers: ") + (tot_tippers))
print(("Tip Percent: ") + (tip) + "%")
# printing tip amount for each tipper
print(27 * "-")
print(("Tip Total per diner: ") + (tip_total))
print(27 * "-")
