from textblob import TextBlob
from colorama import Fore, Style, init


init(autoreset=True)

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0.2:
        return "Positive", Fore.GREEN
    elif polarity < -0.2:
        return "Negative", Fore.RED
    else:
        return "Neutral", Fore.YELLOW

def spy_chatbot():
    print(Fore.CYAN + "🕵️ Sentiment Spy Activated. Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print(Fore.MAGENTA + "Spy Chatbot signing off. Stay sharp! 🕶️")
            break

        sentiment, color = analyze_sentiment(user_input)
        print(color + f"Spy Analysis: {sentiment} sentiment detected.\n" + Style.RESET_ALL)


spy_chatbot()