import random
import string

def chatbot():
    print("\nAI Assistant Activated!")
    while True:
        user = input("You: ").lower()

        if "hello" in user:
            print("AI: Hello! How can I help you?")
        elif "python" in user:
            print("AI: Python is a powerful programming language for AI and web development.")
        elif "bye" in user:
            print("AI: Goodbye!")
            break
        else:
            print("AI: I'm still learning. Try another question.")

def password_generator():
    length = int(input("Enter password length: "))
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    password = "".join(random.choice(chars) for _ in range(length))
    print("Generated Password:", password)

def text_analyzer():
    text = input("Enter text: ")
    words = len(text.split())
    chars = len(text)
    print(f"Words: {words}")
    print(f"Characters: {chars}")

while True:
    print("\n===== AI HUB =====")
    print("1. AI Chatbot")
    print("2. Password Generator")
    print("3. Text Analyzer")
    print("4. Exit")

    choice = input("Select an option: ")

    if choice == "1":
        chatbot()

    elif choice == "2":
        password_generator()

    elif choice == "3":
        text_analyzer()

    elif choice == "4":
        print("Thank you for using AI Hub!")
        break

    else:
        print("Invalid choice. Try again.")
