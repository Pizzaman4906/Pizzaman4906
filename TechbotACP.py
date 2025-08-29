import re, random
from colorama import Fore, init

init(autoreset=True)

tools = {
    "downloads": ["Internet Download Manager", "Free Download Manager", "JDownloader"],
    "customization": ["Rainmeter", "PowerToys", "Wallpaper Engine"],
    "gaming": ["Steam", "Epic Games", "Roblox"]
}

jokes = [
    "Why did the gamer bring string to the match? To tie up loose ends!",
    "Why don't computers ever panic? They have great processors!",
    "Why did the download break up with the Wi-Fi? Too many dropped connections."
]

def normalize_input(text):
    return re.sub(r"\s+", "", text.strip().lower())

def suggest_tool():
    print(Fore.CYAN + "TechPal: Looking for downloads, customization, or gaming tools?")
    category = input(Fore.YELLOW + "You: ")
    category = normalize_input(category)

    if category in tools:
        suggestion = random.choice(tools[category])
        print(Fore.GREEN + f"TechPal: Try out {suggestion}. It's pretty slick.")
        print(Fore.CYAN + "TechPal: Want another suggestion? (yes/no)")
        answer = input(Fore.YELLOW + "You: ").lower()

        if answer == "yes":
            suggest_tool()
        elif answer == "no":
            print(Fore.GREEN + "TechPal: Cool. Let me know if you want more.")
        else:
            print(Fore.RED + "TechPal: Didn't catch that. Let's try again.")
            suggest_tool()
    else:
        print(Fore.RED + "TechPal: Hmm, I don't have tools for that category.")

    show_help()

def optimization_tips():
    print(Fore.CYAN + "TechPal: What are you optimizing—downloads, desktop, or gaming?")
    focus = normalize_input(input(Fore.YELLOW + "You: "))
    print(Fore.CYAN + "TechPal: How many minutes you got to spare?")
    time = input(Fore.YELLOW + "You: ")

    print(Fore.GREEN + f"TechPal: Quick tips for {focus} in {time} minutes:")
    print(Fore.GREEN + "- Close background apps.")
    print(Fore.GREEN + "- Use Task Manager to spot resource hogs.")
    print(Fore.GREEN + "- Tweak settings for performance over visuals.")

def tell_joke():
    print(Fore.YELLOW + f"TechPal: {random.choice(jokes)}")

def show_help():
    print(Fore.MAGENTA + "\nI can:")
    print(Fore.GREEN + "- Suggest tools (say 'suggestion')")
    print(Fore.GREEN + "- Offer optimization tips (say 'optimize')")
    print(Fore.GREEN + "- Tell a joke (say 'joke')")
    print(Fore.CYAN + "Type 'exit' or 'bye' to end.\n")

def chat():
    print(Fore.CYAN + "Yo! I'm TechPal, your digital wingman.")
    name = input(Fore.YELLOW + "Your name? ")
    print(Fore.GREEN + f"Nice to meet you, {name}. Let’s geek out!")

    show_help()

    while True:
        user_input = input(Fore.YELLOW + f"{name}: ")
        user_input = normalize_input(user_input)

        if "suggest" in user_input or "recommend" in user_input:
            suggest_tool()
        elif "optimize" in user_input or "tips" in user_input:
            optimization_tips()
        elif "joke" in user_input or "funny" in user_input:
            tell_joke()
        elif "help" in user_input:
            show_help()
        elif "exit" in user_input or "bye" in user_input:
            print(Fore.CYAN + "TechPal: Catch you later, legend!")
            break
        else:
            print(Fore.RED + "TechPal: Hmm, didn’t get that. Try again.")

if __name__ == "__main__":
    chat()
