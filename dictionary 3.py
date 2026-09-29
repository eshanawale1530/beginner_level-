your_expenses = {
    "Hotel": 1200,
    "Food": 800,
    "Transportation": 500,
    "Attractions": 300,
    "Miscellaneous": 200
}

partner_expenses = {
    "Hotel": 1000,
    "Food": 900,
    "Transportation": 400,
    "Attractions": 350,
    "Miscellaneous": 150
}

# Calculate total expenses
your_total = sum(your_expenses.values())
partner_total = sum(partner_expenses.values())

print("Your total expenses:", your_total)
print("Partner's total expenses:", partner_total)

# Determine who spent more
if your_total > partner_total:
    print("You spent more money.")
elif partner_total > your_total:
    print("Your partner spent more money.")
else:
    print("Both spent the same amount.")

# Find the category with the biggest difference
max_difference = 0
category = ""

for expense in your_expenses:
    difference = abs(your_expenses[expense] - partner_expenses[expense])

    if difference > max_difference:
        max_difference = difference
        category = expense

print("Category with the biggest difference:", category)
print("Difference:", max_difference)