import os
import time
from dotenv import load_dotenv
import anthropic
from anthropic import APIError

def sendWithRetry(client, model, user_message, max_retries=3, delay=2):
    for attempt in range(1, max_retries + 1):
        print(f"Attempt {attempt} of {max_retries}")
        try:
            response = client.messages.create(
                model=model,
                messages=[{"role": "user", "content": user_message}]
            )
            return response['choices'][0]['message']['content']
        except APIError as e:
            print(f"API error: {e}")
            time.sleep(delay)
    return "All retry attempts failed."

def main():
    load_dotenv()
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        print("API key missing. Please set ANTHROPIC_API_KEY in your .env file.")
        return

    client = anthropic.Anthropic(api_key=api_key)
    print("Welcome! Type your question for Claude:")
    user_message = input()
    model = "claude-v1"  # example model name

    print("Sending request with retry logic...")
    result = sendWithRetry(client, model, user_message)
    print("Response from Claude:")
    print(result)

if __name__ == "__main__":
    main()