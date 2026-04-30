import os
import json
from datetime import datetime
from dotenv import load_dotenv
from anthropic import Anthropic, TextBlock

MODEL_NAME = "claude-sene-45-2250-929"

def get_client():
    load_dotenv()
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise ValueError("API key not found in environment variables")
    return Anthropic(api_key=api_key)

def build_runtime_context(user_name):
    return {
        "user_name": user_name,
        "user_id": "user-" + str(hash(user_name)),
        "timestamp": datetime.utcnow().isoformat(),
        "channel": "cli",
        "request_id": "req-" + str(datetime.utcnow().timestamp()).replace('.', '')
    }

def main():
    print("Hands-on: Adding Runtime Context to API Requests")
    user_name = input("Enter your name: ")
    user_question = input("Describe your issue or question for Claude: ")

    context = build_runtime_context(user_name)
    context_json = json.dumps(context, indent=2)
    print("Runtime context to be sent:")
    print(context_json)

    client = get_client()

    message = (
        f"Claude will receive two things: the user's question and the runtime context.\n"
        f"Use the context, especially the user's name, to personalize your reply.\n\n"
        f"User question: {user_question}\n"
        f"Runtime context (JSON): {context_json}"
    )

    response = client.completions.create(
        model=MODEL_NAME,
        prompt=message,
        max_tokens_to_sample=300,
    )

    # Extract text blocks from response
    answer = "".join(
        block.text for block in TextBlock.from_response(response)
    )

    print("\nClaude's reply:")
    print(answer)
    print("\n--- End of run ---")

if __name__ == "__main__":
    main()