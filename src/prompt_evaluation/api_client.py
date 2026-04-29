from dotenv import load_dotenv
load_dotenv()

from anthropic import Anthropic

claude_client = Anthropic()
model = "claude-haiku-4-5"
