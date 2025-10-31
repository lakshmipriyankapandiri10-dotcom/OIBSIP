import calendar

year = int(input("Enter year: "))
month = int(input("Enter month (1-12): "))

print("\nYour calendar:\n")
print(calendar.month(year, month))

