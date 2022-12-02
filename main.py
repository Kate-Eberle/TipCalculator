print("Welcome to the tip calculator")

bill = float(input("What was the total bill: $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill: "))

billAfterTip = (bill * (tip / 100)) + bill

final_amount = round(billAfterTip / people,2)
final_amount = "{:.2f}".format(final_amount)  # added new formatting code to still make 2 decimal places when there's a zero at end
print(f"Each person should pay: ${final_amount}")