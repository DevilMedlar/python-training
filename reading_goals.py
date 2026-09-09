days = int(input("How many days did you spend reading? "))
completeed_books = int(input(f"How many books did you read in {days} day(s)? "))

if completeed_books >= 3 and days >= 5:
    print("Both goals reached")
elif completeed_books >= 3 or days >= 5:
    print("One goal reached")
else:
    print("Neither goal reached")
