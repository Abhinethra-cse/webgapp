import random
from datetime import datetime


greetings = ["hi","hello", "vanakkam", "hola"]
greet_responses = [
    "Hello! How can i assist you?",
    "Hi there!Ask me anything",
    "Hey!What do you want to know?"
]

about_responses = [
    "I am MiniGPT, your simple chatbot!",
    "I'm a small Python chatbot created to reply smartly.",
    "You can ask me general questions, and l'll try to answer!"
]

fallback = [
    "Interesting! Tell me more.",
    "Hmm... I don't fully understand that yet.",
    "I'm still learning! Ask me something else.",
    "Good question! Let's try another topic."
]

def get_response(user):
    text = user.lower()

    if any(word in text for word in greetings):
        return random.choice(greet_responses)
    
    if "who are you"in text or"about" in text or"name" in text:
        return random.choice(about_responses)
    
    if "time" in text:
        return "The current time is " + datetime.now().strftime("%H:%M:%S")
    
    if"date" in text:
        return "Today is " + datetime.now().strftime("%Y-%m-%d")
     
    if "python" in text:
        return "python is a powerful programming language used for AL ,ML,Web apps and more."

    if "creator"in text or "who created you" in text:
        return"I was created by you using python!" 
    
    return random.choice(fallback)

def main():
    print("MiniGPT Chatbot — type 'exit' to stop.\n")
    while True:
        user = input("You: ")

        if user.lower() == "exit":
            print("MiniGPT: Goodbye! Have a great day!")
            break

        reply = get_response(user)
        print("MiniGPT:", reply)

if __name__ == "__main__":
    main()


