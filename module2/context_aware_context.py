import os
import json
from typing import List
from dotenv import load_dotenv
from anthropic import Anthropic, TextBlock

MODEL_NAME = "claude-sonnet-4-5-2-0250929"

def get_client() -> Anthropic:
    load_dotenv()
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise ValueError("ANTHROPIC_API_KEY not found in environment")
    return Anthropic(api_key=api_key)

def get_combined_text(blocks: List[TextBlock]) -> str:
    texts = [block.text for block in blocks if block.type == "text"]
    return "".join(texts) if texts else "No text response from Claude."

def main():
    client = get_client()
    print("Context-Aware Response System")
    name = input("Enter your name (default: User): ") or "User"
    skill = input("Enter your skill level (default: beginner): ") or "beginner"
    mood = input("Enter your mood (default: neutral): ") or "neutral"
    question = input("Ask a simple question: ")
    if not question:
        print("No question provided. Exiting.")
        return

    context = {
        "user_profile": {
            "name": name,
            "skill_level": skill,
            "interests": ["technology", "AI", "programming"]
        },
        "session_context": {
            "mood": mood,
            "language": "en",
            "claude_role": "friendly and helpful assistant"
        }
    }
    print("Context to send:", json.dumps(context, indent=2))

    prompt_text = (
        f"Use the following JSON context to tailor your response:\n{json.dumps(context)}\n"
        f"Answer the question accordingly:\n{question}"
    )

    response = client.completions.create(
        model=MODEL_NAME,
        prompt=prompt_text,
        max_tokens_to_sample=300,
    )

    answer = get_combined_text(response.completion)
    print("\nClaude's response:")
    print(answer)

if __name__ == "__main__":
    main()