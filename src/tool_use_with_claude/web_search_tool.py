from pprint import pprint

from tool_use_with_claude.tool_functions import web_search_schema
from tool_use_with_claude.utils import add_user_message, chat

messages = []
add_user_message(
    messages,
    """
    What's the best exercise for gaining leg muscle?
    """,
)
response = chat(messages, tools=[web_search_schema])

pprint(response)

# for block in response.content:
#     pprint(block)
