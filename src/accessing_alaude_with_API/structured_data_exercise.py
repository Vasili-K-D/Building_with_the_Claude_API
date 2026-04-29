from utils import add_user_message, chat, add_assistant_message

messages = []

prompt = "Generate three different sample AWS commands. Each should be a very short"

add_user_message(messages, prompt)

add_assistant_message(messages, "Here are all three commands without any comments:\n```bash")
answer = chat(messages, stop_sequences=["```"])

print(answer)
