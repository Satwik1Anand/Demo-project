import os
from anthropic import Anthropic
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Anthropic client with API key
client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

# Define the model to use
MODEL = "claude-v1"

# System prompt defining agent behavior and output formats
SYSTEM_PROMPT = """
You are a task planning agent. Ask clarifying questions to understand the user's goal.
Output the final plan in JSON or text format as requested.
"""

def main():
    print("Task Planning Agent (type 'exit' to quit)")
    while True:
        goal = input("Enter your goal: ")
        if goal.lower() == "exit":
            break
        output_format = input("Choose output format (1 for JSON, 2 for text): ")
        if output_format.lower() == "exit":
            break

        messages = [{"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": goal}]

        while True:
            response = client.chat.completions.create(
                model=MODEL,
                messages=messages
            )
            reply = response.choices[0].message["content"]
            print(reply)

            # Check if reply contains a plan (simplified check)
            if "plan" in reply.lower():
                break
            else:
                user_input = input("Your answer: ")
                if user_input.lower() == "exit":
                    return
                messages.append({"role": "assistant", "content": reply})
                messages.append({"role": "user", "content": user_input})

if __name__ == "__main__":
    main()