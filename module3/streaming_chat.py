import os
import asyncio
import sys
from dotenv import load_dotenv
from anthropic import AsyncAnthropic

load_dotenv()

MODEL_NAME = "claude-v1"

async def stream_once(client, user_prompt):
    print("Claude:", end=" ", flush=True)
    try:
        stream = await client.messages.stream(
            model=MODEL_NAME,
            max_tokens_to_sample=300,
            messages=[{"role": "user", "content": user_prompt}],
        )
        async for chunk in stream.text_stream:
            print(chunk, end="", flush=True)
        final_message = await stream.get_final_message()
        print()  # Newline after streaming finishes
    except Exception as e:
        print(f"\nError: {e}", file=sys.stderr)

async def chat_loop():
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        print("Error: ANTHROPIC_API_KEY not found in environment variables.")
        return

    client = AsyncAnthropic(api_key=api_key)
    print("Streaming chat demo. Type 'exit' or 'quit' to stop.")

    try:
        while True:
            user_input = input("You: ").strip()
            if user_input.lower() in ("exit", "quit"):
                break
            if not user_input:
                continue
            await stream_once(client, user_input)
    finally:
        await client.aclose()

if __name__ == "__main__":
    asyncio.run(chat_loop())