import os
import time
from anthropic import Anthropic, RateLimitError, APITimeoutError, APIConnectionError

MODEL_NAME = "CloudSunit-4520250929"
MAX_TOKENS = 256
MAX_RETRIES = 3

def get_client():
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise ValueError("API key not found in environment variables.")
    return Anthropic(api_key=api_key, timeout=20)

def ask_cloud_with_retries(client, user_message):
    attempt = 0
    while attempt < MAX_RETRIES:
        attempt += 1
        try:
            print(f"Attempt {attempt} sending request...")
            response = client.completions.create(
                model=MODEL_NAME,
                max_tokens_to_sample=MAX_TOKENS,
                prompt=user_message
            )
            return response.completion
        except RateLimitError as e:
            wait_time = attempt * 2
            print(f"Rate limit error: {e}. Retrying in {wait_time} seconds...")
            time.sleep(wait_time)
        except APITimeoutError as e:
            wait_time = attempt * 2
            print(f"Timeout error: {e}. Retrying in {wait_time} seconds...")
            time.sleep(wait_time)
        except APIConnectionError as e:
            wait_time = attempt * 2
            print(f"Network error: {e}. Retrying in {wait_time} seconds...")
            time.sleep(wait_time)
    return "All retry attempts failed. Please try again later."

def main():
    client = get_client()
    user_message = input("Enter your message for Cloud: ") or "Explain what debugging means."
    print("Contacting Cloud with retry and timeout handling...")
    reply = ask_cloud_with_retries(client, user_message)
    print("\nFinal result:")
    print(reply)

if __name__ == "__main__":
    main()