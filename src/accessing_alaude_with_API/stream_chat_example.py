from utils import stream_chat, add_user_message, add_assistant_message

continue_chat = True
messages = []
question = "give me a list of 5 best action movies"

while continue_chat:
    user_input = input("Enter your message (or 'exit' to quit the chat): ")
    if user_input.lower() in ["exit", "quit"]:
        continue_chat = False
        print("Ending the chat. Goodbye!")
    else:
        add_user_message(messages, user_input)
        answer = stream_chat(messages)
        add_assistant_message(messages, answer)
