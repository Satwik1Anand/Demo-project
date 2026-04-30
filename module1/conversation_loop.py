import os
from dotenv import load_dotenv
from anthropic import Anthropic

def main():
    load_dotenv()
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise ValueError("API key not found. Please set ANTHROPIC_API_KEY in your .env file.")
    
    client = Anthropic(api_key)
    print("Conversation loop started. Type 'exit' to stop.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Goodbye! Conversation ended.")
            break
        
        response = client.completions.create(
            model="claude-sonnet-4-5-2-0250929",
            prompt=user_input,
            max_tokens_to_sample=300
        )
        print("Claude:", response.completion)

if __name__ == "__main__":
    main()