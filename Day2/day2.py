print("Welcome to Tip Calculator!")

bill = float(input("What is the total bill amount?\nbill: "))
tip = int(input("How much tip would you want to give?\ntip: "))
split= int(input("How many split do you want to do?\nsplit: "))

total = ("{:.2f}".format((((tip/100) * bill) + bill) / split))

print(f"Each person have to pay: ${total}")