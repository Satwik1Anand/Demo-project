#enforce_output_format_demo.py 


import os
import json
from typing import List
from dotenv import load_dotenv
from anthropic import Anthropic, TextBlock

MODEL_NAME = "claude-sonne-4520250929"

def get_client() -> Anthropic:
    load_dotenv()
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise ValueError("ANTHROPIC_API_KEY not found in environment")
    return Anthropic(api_key=api_key)

def choose_format() -> str:
    options = {
        "1": "JSON",
        "2": "bullets",
        "3": "steps"
    }
    while True:
        print("Choose output format:")
        print("1. JSON")
        print("2. Bullet points")
        print("3. Numbered steps")
        choice = input("Enter choice (1/2/3): ").strip()
        if choice in options:
            return options[choice]
        print("Invalid choice, please try again.")

def build_system_instruction(output_name: str, format_choice: str) -> str:
    if format_choice == "JSON":
        return (
            f"Respond only with valid JSON in this schema:\n"
            f"{{\n"
            f'  "title": string,\n'
            f'  "summary": string,\n'
            f'  "severity": string,\n'
            f'  "steps": [string]\n'
            f"}}"
        )
    elif format_choice == "bullets":
        return "Respond using bullet points. Each line must start with a dash (-)."
    elif format_choice == "steps":
        return "Respond using numbered steps. Each line must start with a number followed by a period."
    else:
        return ""

def extract_text(response) -> str:
    texts = []
    for block in response.completions[0].completion.split("\n"):
        texts.append(block)
    return "\n".join(texts)

def strip_code_fences(text: str) -> str:
    if text.startswith("```") and text.endswith("```"):
        return "\n".join(text.strip("```").split("\n")[1:])
    return text

def main():
    print("Enforce Output Format Demo")
    client = get_client()
    format_choice = choose_format()
    system_instruction = build_system_instruction("Output", format_choice)
    user_prompt = input("Describe what you want Claude to generate: ")

    print(f"Using model: {MODEL_NAME}")
    print(f"Enforcing format: {format_choice}")

    response = client.completions.create(
        model=MODEL_NAME,
        prompt=f"{system_instruction}\n\n{user_prompt}",
        max_tokens_to_sample=1000,
        stop_sequences=["\n\n"]
    )

    raw_output = response.completions[0].completion
    print("Raw output:")
    print(raw_output)

    if format_choice == "JSON":
        try:
            clean_output = strip_code_fences(raw_output)
            parsed = json.loads(clean_output)
            print("Validated JSON output:")
            print(json.dumps(parsed, indent=2))
        except json.JSONDecodeError as e:
            print(f"JSON validation error: {e}")

if __name__ == "__main__":
    main()