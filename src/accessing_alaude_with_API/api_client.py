from dotenv import load_dotenv
load_dotenv()

from anthropic import Anthropic

claude_client = Anthropic()
model = "claude-sonnet-4-5"
