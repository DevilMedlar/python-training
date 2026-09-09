practice = int(input("How many minutes did you practice? "))

if practice < 0:
    print("Minutes cannot be negative.")
else:
    if 0 <= practice <= 19:
        print("Below target")
    elif 20 <= practice <=40:
        print("Within target")
    else:
        print("Above target")
