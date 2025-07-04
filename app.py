import nltk
from nltk.chat.util import Chat, reflections
nltk.download('punkt')

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?"]
    ],
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey!"]
    ],
    [
        r"what is your name?",
        ["I'm a chatbot you built!"]
    ],
    [
        r"how are you?",
        ["I'm good, thanks!", "Doing great. What about you?"]
    ],
    [
        r"sorry (.*)",
        ["It's okay!", "No worries!"]
    ],
    [
        r"quit",
        ["Bye! Take care.", "Goodbye!"]
    ]
]

def chatbot():
    print("Hi! I'm your chatbot. Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

chatbot()
