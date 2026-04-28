
from utils import add_user_message, chat, add_assistant_message


continue_chat = True
messages = []
system_prompt = """
You are a patient math tutor.
Do not directly answer a student's questions.
Guide them to a solution step by step.
"""


while continue_chat:
    user_input = input("Enter your message (or 'exit' to quit the chat): ")
    if user_input.lower() in ["exit", "quit"]:
        continue_chat = False
        print("Ending the chat. Goodbye!")
    else:
        add_user_message(messages, user_input)
        answer = chat(messages=messages, system_prompt=system_prompt)
        add_assistant_message(messages, answer)
        add_assistant_message(messages, answer)
        print(f"Claude answer: {answer}")