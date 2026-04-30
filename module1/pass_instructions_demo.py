import os
from dotenv import load_dotenv
from anthropic import Anthropic

def main():
    load_dotenv()
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        print("Error: Anthropic API key not found.")
        return

    client = Anthropic(api_key)

    system_instruction = input("Enter system instruction: ")
    user_message = input("Enter user message: ")
    model_name = input("Enter model name (leave blank for default): ") or "claude-v1"

    print(f"Using model: {model_name}")

    response = client.messages.create(
        model=model_name,
        messages=[
            {"role": "system", "content": system_instruction},
            {"role": "user", "content": user_message}
        ]
    )

    print("Model Response:")
    print(response['choices'][0]['message']['content'])

if __name__ == "__main__":
    main()