
print("==================================================")
print("           SMART EXPENSE TRACKER                  ")
print("==================================================")

day1 = int(input("Enter expense for Day 1 (₹): "))
day2 = int(input("Enter expense for Day 2 (₹): "))
day3 = int(input("Enter expense for Day 3 (₹): "))

total_expense = day1 + day2 + day3
average_expense = total_expense / 3

print("\n")
print("=" * 50)
print("                EXPENSE REPORT                    ")
print("=" * 50)
print(" Day 1 Expense : ₹", day1)
print(" Day 2 Expense : ₹", day2)
print(" Day 3 Expense : ₹", day3)
print("-" * 50)
print(" Total Expense   : ₹", total_expense)
print(" Average Expense : ₹", average_expense)
print("=" * 50)
print("         Keep tracking your money wisely      ")
print("=" * 50)