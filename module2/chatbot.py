import os
from anthropic import Anthropic, APIError, RateLimitError
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
API_KEY = os.getenv("ANTHROPIC_API_KEY")

# Initialize Anthropic client
client = Anthropic(api_key=API_KEY)

# Define model and system prompt
MODEL = "claude-v1"
SYSTEM_PROMPT = (
    "You are a friendly mentor chatbot. "
    "Guide the user, ask clarifying questions, and communicate naturally."
)

# Conversation history to maintain context
conversation_history = [
    {"role": "system", "content": SYSTEM_PROMPT}
]

# Function to trim conversation history to last 10 messages
def trim_history(history, max_length=10):
    if len(history) > max_length:
        return history[-max_length:]
    return history

def print_welcome():
    print("Welcome to the chatbot! Type your message or /exit to quit, /reset to start over.")

def main():
    print_welcome()
    while True:
        try:
            user_input = input("You: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye!")
            break

        if not user_input:
            print("Please enter a message.")
            continue

        if user_input.lower() == "/exit":
            print("Exiting chatbot. Goodbye!")
            break

        if user_input.lower() == "/reset":
            conversation_history.clear()
            conversation_history.append({"role": "system", "content": SYSTEM_PROMPT})
            print("Conversation history reset.")
            continue

        # Add user message to history
        conversation_history.append({"role": "user", "content": user_input})
        conversation_history = trim_history(conversation_history)

        try:
            response = client.completions.create(
                model=MODEL,
                prompt=conversation_history,
                max_tokens_to_sample=300,
                stop_sequences=["\n\nHuman:"]
            )
            assistant_reply = response.completion.strip()
            print(f"Bot: {assistant_reply}")

            # Add assistant reply to history
            conversation_history.append({"role": "assistant", "content": assistant_reply})

        except RateLimitError:
            print("Rate limit exceeded. Please wait and try again.")
        except APIError as e:
            print(f"API error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()