from api_client import claude_client, model


message = claude_client.messages.create(
    model=model,
    max_tokens=1000,
    messages=[
        {
            "role": "user",
            "content": "What is quantum computing? Answer in one sentence"
        }
    ]
)

answer = message.content[0].text

print(answer)