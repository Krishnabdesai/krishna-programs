# This code is Currency Converter Program.
print("Welcome to the Currency Converter!")

currency = input("Enter your Currency code: ").lower()
convert_currency = input("Enter the currency (code) you want to convert to: ").lower()
amount = float(input("Enter the amount you want to convert: "))

# first converting all currencies into usd
convert_usd={
"inr": 0.012,
"usd": 1.00,
"rub": 0.013,
"eur": 1.17,
"aud": 0.66,
"cad": 0.73,
"cny": 0.14,
"jpy": 0.0068,
"gbp": 1.34
}
# Now converting the amount to usd
amount_in_usd = amount * convert_usd[currency]

# Now converting the amount from usd to the desired currency
converted_amount = amount_in_usd / convert_usd[convert_currency]

print(f"converted amount is: {converted_amount:.2f} {convert_currency.upper()}")
