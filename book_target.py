target = 20
books = int(input("How many books do you have? "))
if books < target:
    print("Books still needed:", target - books)
elif books == target:
    print("Target reached.")
else:
    print("Extra books:", books - target)
