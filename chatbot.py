import time
import random

# Greet the user
print("Hi! I am ChatBot. Type 'help' to see what I can do!")

# Bot commands
def show_help():
    print("""
I can do the following:
1. 'time' - Show the current time.
2. 'joke' - Tell a random joke.
3. 'bye' - Exit the chatbot.
    """)

# Random jokes
jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "What do you call fake spaghetti? An impasta!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!"
]

# Main loop
while True:
    user_input = input("\nYou: ").strip().lower()
    
    if user_input == "help":
        show_help()
    elif user_input == "time":
        print("Bot: The current time is", time.strftime("%H:%M:%S"))
    elif user_input == "joke":
        print("Bot:", random.choice(jokes))
    elif user_input == "bye":
        print("Bot: Goodbye! Have a great day!")
        break
    else:
        print("Bot: Sorry, I don't understand. Type 'help' to see what I can do.")

