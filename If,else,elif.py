# This program suggests an outfit based on the occasion input by the user.
print("Welcome to the Outfit Suggestion Program!")
print(" Choose one! - Diwali, Wedding, Birthday, Casual")

occasion = str(input("What is the occasion?- "))

if occasion == "Diwali":
    print("Wear a traditional dress.")

elif occasion == "Wedding":
    print("Wear a Choli.")

elif occasion == "Birthday":
    print("Wear a flower dress.")

elif occasion == "Casual":
    print("Wear a Jeans.")
else:
    print("Sorry, I don't have a suggestion for that occasion.")    