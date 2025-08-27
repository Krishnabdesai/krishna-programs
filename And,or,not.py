jee_main = float(input("Enter JEE Main score: "))

gen_category = True if input("Are you from the General category? (yes/no): ") == "yes" else False
obc_category = True if input("Are you from the OBC category? (yes/no): ") == "yes" else False and not gen_category


if jee_main >= 93.10 and gen_category:
    print("You are eligible for JEE Advanced.")

elif jee_main >= 88.30 and obc_category:
    print("You are eligible for JEE Advanced.")

elif jee_main >= 45.00 and not gen_category and not obc_category:
    print("You are eligible for JEE Advanced.")

else:
    print("You are not eligible for JEE Advanced.")