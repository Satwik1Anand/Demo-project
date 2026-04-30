import os
import json
from dotenv import load_dotenv
from anthropic import AnthropicClient

def main():
    load_dotenv()
    api_key = os.getenv("AnthropicAPIKey")
    if not api_key:
        print("Error: AnthropicAPIKey not found in environment variables.")
        return

    client = AnthropicClient(api_key)

    print("JSON Response Demo")
    print("Describe a simple task or feature request (e.g., 'How to focus better while studying'):")
    user_description = input("> ").strip()
    if not user_description:
        print("No input provided. Exiting.")
        return

    system_instruction = (
        "You are a JSON-only service. Output only valid JSON following this schema: "
        "{title, category, priority, summary, steps}. Infer category and priority from the user's input. "
        "Do not add extra fields or explanations."
    )

    response = client.messages.create(
        model="cloudsony45-2250929",
        max_tokens=300,
        messages=[
            {"role": "system", "content": system_instruction},
            {"role": "user", "content": user_description}
        ]
    )

    if not response.content:
        print("No response content received.")
        return

    raw_json = None
    for block in response.content:
        if block.get("type") == "text":
            raw_json = block.get("text")
            break

    if not raw_json:
        print("No text block found in response.")
        return

    print("Raw JSON from Cloud:")
    print(raw_json)

    cleaned_json = raw_json.strip("```")

    try:
        data = json.loads(cleaned_json)
    except json.JSONDecodeError:
        print("Failed to parse JSON response.")
        return

    print("\nStructured Output:")
    print(f"Title: {data.get('title')}")
    print(f"Category: {data.get('category')}")
    print(f"Priority: {data.get('priority')}")
    print(f"Summary: {data.get('summary')}")
    print("Steps:")
    for i, step in enumerate(data.get("steps", []), 1):
        print(f"  {i}. {step}")

if __name__ == "__main__":
    main()