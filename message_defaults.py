message = input("Type messaga: ")
available_minutes = int(input("Minutes: "))

display_message = message or "No message supplied"
timed_message = available_minutes and display_message

print(display_message, type(display_message))
print(timed_message, type(timed_message))
