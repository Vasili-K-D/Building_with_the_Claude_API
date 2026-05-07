import json

from tool_use_with_claude.tool_functions import (
    get_current_datetime,
    get_current_datetime_schema,
    add_duration_to_datetime_schema,
    set_reminder_schema,
    add_duration_to_datetime,
    set_reminder
)
from tool_use_with_claude.utils import chat, add_assistant_message, add_user_message, text_from_message


def run_tool(tool_name, tool_inputs):
    print(f"tool_request tool_name: {tool_name}")
    if tool_name == "get_current_datetime":
        return get_current_datetime(**tool_inputs)
    elif tool_name == "add_duration_to_datetime":
        return add_duration_to_datetime(**tool_inputs)
    elif tool_name == "set_reminder":
        return set_reminder(**tool_inputs)
    return None


def run_tools(messages):
    tool_requests = [
        tool_block for tool_block in messages.content if tool_block.type == "tool_use"
    ]
    tool_results = []

    for tool_request in tool_requests:
        try:
            tool_result = run_tool(tool_request.name, tool_request.input)
            tool_result_block = {
                "type": "tool_result",
                "tool_use_id": tool_request.id,
                "content": json.dumps(tool_result),
                "is_error": False
            }
        except Exception as e:
            tool_result_block = {
                "type": "tool_result",
                "tool_use_id": tool_request.id,
                "content": f"Error: {e}",
                "is_error": True
            }

        tool_results.append(tool_result_block)

    return tool_results


def run_conversation(messages):
    while True:
        chat_response = chat(
            messages,
            tools=[get_current_datetime_schema, add_duration_to_datetime_schema, set_reminder_schema]
        )
        add_assistant_message(messages, chat_response)
        print(text_from_message(chat_response))

        if chat_response.stop_reason != "tool_use":
            break

        tool_results = run_tools(chat_response)
        add_user_message(messages, tool_results)

    return messages


messages = []
messages.append({
    "role": "user",
    "content": "Set a reminder for my doctors appointment. Its 177 days after Jan 1st, 2050.",
})

response = run_conversation(messages)