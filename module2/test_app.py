import os
from dotenv import load_dotenv
from anthropic import Anthropic

def askCloud(user_text, instruction):
    prompt = (
        "Human: <<START>>\n"
        f"{user_text}\n"
        "<<END>>\n"
        f"Instruction: {instruction}\n"
        "Assistant:"
    )
    response = client.messages.create(
        model=model,
        max_tokens_to_sample=1000,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.content.text

def main():
    print("Text Processing App using Claude API")
    print("Paste your content below. Press Ctrl-D (Mac/Linux) or Ctrl-Z (Windows) then Enter when done:")

    user_text = ""
    try:
        while True:
            line = input()
            user_text += line + "\n"
    except EOFError:
        pass

    print("\nContent received.")
    while True:
        instruction = input("What do you want to do with it? (type 'exit' to quit): ")
        if instruction.lower() in ("exit", "quit"):
            print("Exiting program.")
            break
        output = askCloud(user_text, instruction)
        print("\n--- Output ---")
        print(output)
        print("--------------\n")

if __name__ == "__main__":
    load_dotenv()
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        print("Error: ANTHROPIC_API_KEY not found in environment variables.")
        exit(1)

    client = Anthropic(api_key)
    model = "claude-v1"  # or your preferred model name

    main()