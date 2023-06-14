# Bill calculator

print("Wlecome to the tip calculator!")

total = input("What is the total bill amount?\n> $")
tip = input("What % tip would you like to give?\n% = ")
people = input("How many people will split the bill?\n>")

price_per = ("{:.2f}".format(((float(total) * (float(tip) / float(100)) + float(total)) / float(people))))

print(f"Each person should pay ${price_per}")
