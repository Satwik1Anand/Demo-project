import os
from dotenv import load_dotenv
from anthropic import Anthropic

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv("ANTHROPIC_API_KEY")

if not api_key:
    print("Error: API key not found.")
    exit(1)

client = Anthropic(api_key=api_key)
model = "claude-v1"

def run_variant(variant_name, system_prompt, user_task, max_tokens):
    print(f"Running variant: {variant_name}")
    response = client.messages.create(
        model=model,
        max_tokens_to_sample=max_tokens,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_task}
        ]
    )
    # Extract text content from response
    output = "".join(
        block["text"] for block in response.content if block["type"] == "text"
    )
    print(output[:800])  # Print first 800 characters for comparison
    usage = response.usage
    print(f"Tokens used - Input: {usage['input_tokens']}, Output: {usage['output_tokens']}, Total: {usage['total_tokens']}")
    return usage

def main():
    user_task = "Generate a six-month data engineering roadmap."

    # Naive verbose prompt (uses more tokens)
    naive_prompt = (
        "Write a long, detailed, multi-section roadmap with explanations, alternatives, and motivation. No limits."
    )

    # Optimized concise prompt (uses fewer tokens)
    optimized_prompt = (
        "Create a concise six-month data engineering roadmap with no more than six main bullets, "
        "each with up to three sub-bullets, and about 250 words total."
    )

    # Run naive variant with higher token limit
    run_variant("Naive", naive_prompt, user_task, max_tokens=800)

    # Run optimized variant with lower token limit
    run_variant("Optimized", optimized_prompt, user_task, max_tokens=300)

if __name__ == "__main__":
    main()