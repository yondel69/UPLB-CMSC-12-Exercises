#Fuel Calculator
#the user inputs the fuel type, the amount of fuel they got in liters, and their payment amount in pesos
#if the payment is insufficient, then the program notifies the user how much they owe

fuel_type = str(input("What type of fuel do you use (DIESEL , PREMIUM, UNLEADED, KEROSENE)? : ").upper()) #to remove any case sensitive error we used .upper()
fuel_amount = float(input("How many liters did you get?: "))
payment = float(input("How much is your payment?: "))

if (fuel_type == "DIESEL"):
	if payment < (fuel_amount * 66.50):
		print("Insufficient Funds. You need to pay", (payment - (fuel_amount * 66.50)) * -1, "more.") 
		#the calculation is multiplied by -1 for the amount needed to be paid to print as positive 
	else:
		print("Your change is Php", payment - (fuel_amount * 66.50))

if (fuel_type == "PREMIUM"):
	if payment < (fuel_amount * 71.45):
		print("Insufficient Funds. You need to pay", (payment - (fuel_amount * 71.45)) * -1, "more.")
	else:
		print("Your change is Php", payment - (fuel_amount * 71.45))

if (fuel_type == "UNLEADED"):
	if payment < (fuel_amount * 69.36):
		print("Insufficient Funds. You need to pay", (payment - (fuel_amount * 69.36)) * -1, "more.")
	else:
		print("Your change is Php", payment - (fuel_amount * 69.36))

if (fuel_type == "KEROSENE"):
	if payment < (fuel_amount * 67.56):
		print("Insufficient Funds. You need to pay", (payment - (fuel_amount * 67.56)) * -1, "more.")
	else:
		print("Your change is Php", payment - (fuel_amount * 67.56))
