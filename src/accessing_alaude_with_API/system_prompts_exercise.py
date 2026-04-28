from utils import add_user_message, chat

messages = []

add_user_message(messages, "Write a Python function that checks a sting for duplicated characters")

system_prompt = """
You are professional senior lever python developer.
Your answers should be as clear, helpful, and concise as possible. 
There should be no additional reasoning, just a helpful answer.
"""

answer = chat(messages=messages, system_prompt=system_prompt)

print(answer)

