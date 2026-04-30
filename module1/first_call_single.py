from dataclasses import dataclass
from typing import List
import os
from dotenv import load_dotenv

from anthropic import Anthropic

load_dotenv()

@dataclass
class Settings:
    api_key: str
    model: str = "cloud-sonnet-45-2250929"

def get_settings() -> Settings:
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise ValueError("Missing ANTHROPIC_API_KEY in environment variables")
    return Settings(api_key=api_key)

def get_client() -> Anthropic:
    settings = get_settings()
    return Anthropic(api_key=settings.api_key)

def send_message_to_claude(message: str) -> str:
    client = get_client()
    settings = get_settings()
    response = client.completions.create(
        model=settings.model,
        prompt=message,
        max_tokens_to_sample=300,
    )
    text_parts: List[str] = [
    block.text for block in response.content
    if hasattr(block, "text")
]
    if not text_parts:
        return "<No text response>"
    return "".join(text_parts)

def main():
    print("Checking API key and testing connection...")
    try:
        client = get_client()
        test_message = "Hello, Claude! This is a test message."
        response = send_message_to_claude(test_message)
        print("API key loaded successfully.")
        print("Response from Claude API:")
        print(response)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

    