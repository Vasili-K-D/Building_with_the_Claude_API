
from utils import add_user_message, chat, add_assistant_message


continue_chat = True
messages = []

while continue_chat:
    user_input = input("Enter your message (or 'exit' to quit the chat): ")
    if user_input.lower() in ["exit", "quit"]:
        continue_chat = False
        print("Ending the chat. Goodbye!")
    else:
        add_user_message(messages, user_input)
        answer = chat(messages)
        add_assistant_message(messages, answer)
        print(f"Claude answer: {answer}")