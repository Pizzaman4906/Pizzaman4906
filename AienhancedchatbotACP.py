print("🤖 Hi! I’m your friendly chatbot.")
name = input("What’s your good name, sir?\n🙂 :- ")

print(f"Hi {name}, nice to meet you!")

# Mood check
mood = input("How are you feeling today?\n🧠 :- ").lower()

positive_moods = [
    "good", "great", "amazing", "nice", "fine", "extraordinary",
    "really good", "really nice", "happy", "fantastic", "awesome"
]

if mood in positive_moods:
    print("😊 I'm glad to hear that!")
else:
    print("😟 Oh no, I'm sorry to hear that.")
    print("Is there anything I can do to help you?")
    help_request = input("💡 :- ").lower()

    if "recommend" in help_request and "restaurant" in help_request:
        print(" You might enjoy 'Bagat Tarachan'—great food and cozy vibes!")
    elif "successful" in help_request:
        print(" Success starts with good health, passion, and persistence. Find your purpose, stay disciplined, and never stop learning.")
    elif "cartoon" in help_request:
        print(" You could try 'Skibidi Toilet'")
    else:
        print(" I'm still learning. Can you ask in a different way?")

while True:
    query = input("\nWhat would you like to ask me next?\n🔍 :- ").lower()

    if "restaurant" in query:
        print(" Try 'Bagat Tarachan' or 'The Bombay Canteen'—both are top picks!")
    elif "successful" in query:
        print(" Build good habits, stay curious, and surround yourself with positive people. Success follows consistency.")
    elif "cartoon" in query:
        print(" How about 'Avatar: The Last Airbender' or 'Rick and Morty'?")
    elif query in ["exit", "quit", "bye"]:
        print(f" Bye {name}, take care and talk to you soon!")
        break
    else:
        print(" Hmm, I didn’t quite get that. Can you rephrase?")