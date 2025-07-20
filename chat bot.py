from nltk.chat.util import Chat, reflections

# Define response pairs
pairs = [
    [r'hi|hello', ['Hello!', 'Hi there!', 'Hey! How can I assist you?']],
    [r'how are you\??', ['I am good, thank you!', 'Doing well. How about you?', 'Feeling great! 😊']],
    [r'thank you|thanks|thankyou', ['My pleasure!', 'You are welcome!', 'Anytime! 😊']],
    [r'bye+|goodbye', ['See you again!', 'Goodbye! Have a great day!', 'Take care! 👋']],
    [r'fine+|good+', ['I’m glad to hear that! 😊']],
    [r'yes|yup', ['Go ahead, I’m listening! 🎧']],
    [r'who are you|tell me about yourself', ['I am a chatbot developed by Samuel.', 'I’m your virtual assistant. 😊']],
    [r'who is your boss', ['Samuel is my creator.']],
    [r'any advice', ['You can do it!', 'Never give up! 💪', 'Stay positive and keep learning!']],
    [r'what is your name\??', ['You can call me ChatBot!', 'I am a chatbot created by Samuel.']],
    [r'what can you do\??', ['I can chat with you, answer questions, and assist you with tasks.']],
    [r'are you human\??', ['Nope, I am an AI chatbot — but I’m here to help! 🤖']],
    [r'tell me a joke', [
        'Why don’t programmers like nature? It has too many bugs. 😂',
        'I told my WiFi it was being slow… now it won’t talk to me. 😆'
    ]],
    [r'love you', ['Aww! That’s sweet! ❤️', 'I appreciate that! 😊']],
    [r'what is your favorite color\??', ['I like blue… because I live in the cloud! ☁️']],
    [r'how old are you\??', ['I am as young as the latest code update!']],
    [r'who made you\??', ['Samuel built me with Python! 🐍']]
]

chatbot = Chat(pairs, reflections)

def start_chat():
    print("Welcome to the ChatBot! 🤖 (Type 'bye' to exit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['bye', 'goodbye', 'exit', 'quit']:
            print("ChatBot: See you again! 👋")
            break
        response = chatbot.respond(user_input)
        if response:
            print("ChatBot:", response)
        else:
            print("ChatBot: I'm not sure how to respond to that. 🤔")

if __name__ == "__main__":
    start_chat()
