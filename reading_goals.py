days = int(input("How many days did you spend reading? "))
completed_books = int(input(f"How many books did you read in {days} day(s)? "))

if completed_books < 0 or days < 0:
    print("Counts cannot be negative.")
else:
    both_goals_reached = completed_books >= 3 and days >= 5
    if both_goals_reached:
        print("Both goals reached")
    elif completed_books >= 3 or days >= 5:
        print("One goal reached")
    else:
        print("Neither goal reached")
        
    if not both_goals_reached:
        print("Keep working on the remaining goals.")
        print(f"Progress: {completed_books} books over {days} day(s)")
