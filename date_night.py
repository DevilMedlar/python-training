available = int(input("How long is the date? "))
num_candles = int(input("How many candles? "))
playlist_length = int(input("How long is the playlist? "))

mood_ready = 60 <= available and (2 <= num_candles or 30 <= playlist_length)

if mood_ready:
    print("Mood ready")
else:
    print("Needs more preparation")
    