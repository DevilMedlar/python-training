message = input("Type your message here: ")
available_minutes = int(input("Available minutes: "))

print(bool(message), bool(available_minutes))

if message:
    print("Text entered")
else:
    print("No text entered")

if available_minutes:
    print("Some time available")
else:
    print("No time available")
