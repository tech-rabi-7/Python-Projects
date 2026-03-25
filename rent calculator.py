#rent calculator in python - @tech-rabi-7

## Inputs we need from the user
# Total rent
# Total food ordered for snacking
# Electricity units spend
# Charge per unit 
# Persons living in room/flat

## Output
# Total amount you've to pay is

rent_charge = int(input("Enter your rent : "))    # receive input from the user
food_charge = int(input("Enter your food snaks charges : "))     # receive food charges from the user
electricity_unit = int(input("Enter how much unit you spend in the month : "))  # receive input from the user
electric_charge_per_unit = int(input("Enter the Electric Charge per Unit : "))     # receive Elelecric charges per unit from the user
persons=int(input("How many persons live in the Appartment : ")) ## receive no. of persons from the user

electric_bill = electricity_unit * electric_charge_per_unit

total = (rent_charge +food_charge + electric_bill)/persons

print(f" Each person should pay:  {total}")