# """
# this is My Module
# to create Function
# to calculate age
# """

from calendar import month


age = input("Please write your age:").strip()
unit = input("Please choose Time Unit:Months, weeks, Days").strip().lower()

months = int(age) * 12
weeks= months * 4
days= int(age) * 365

if unit == 'months' or unit == 'm':
    print("your choosed The Unit Months")
    print(f"you Lived for {months:,} Months.")
elif unit == 'weeks':
    print("you choosed the Unit Weeks")
    print(f"you Lived for {weeks:,} weeks.")
elif unit == 'days':
    print("you choosed the unit days")
    print(f"you Lived for {days:,} days.")
else:
    print("choosed unit false.")