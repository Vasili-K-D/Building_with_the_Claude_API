from api_client import claude_client, model


def add_user_message(messages, text):
    user_message = {"role": "user", "content": text}
    messages.append(user_message)


def add_assistant_message(messages, text):
    assistant_message = {"role": "assistant", "content": text}
    messages.append(assistant_message)


def chat(messages: list[dict], system_prompt: str | None = None):
    parameters = {
        "model": model,
        "max_tokens": 1000,
        "messages": messages,
    }
    if system_prompt:
        parameters["system"] = system_prompt

    message = claude_client.messages.create(**parameters)
    return message.content[0].text