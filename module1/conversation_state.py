import os
from anthropic import Anthropic
from dotenv import load_dotenv

def choose_model():
    default_model = "claude-v1"
    choice = input(f"Enter model name or press Enter to use default ({default_model}): ")
    return choice.strip() if choice.strip() else default_model

def get_system_instruction(default="You are a helpful assistant."):
    instruction = input(f"Enter system instruction or press Enter to use default:\n{default}\n")
    return instruction.strip() if instruction.strip() else default

def run_stateless_example(client, model):
    print("\n--- Stateless Example ---")
    system_instruction = get_system_instruction()
    first_message = input("Enter first user message: ")
    response1 = client.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_instruction},
            {"role": "user", "content": first_message}
        ]
    )
    print("Claude:", response1.choices[0].message["content"])

    second_message = input("Enter second user message: ")
    response2 = client.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_instruction},
            {"role": "user", "content": second_message}
        ]
    )
    print("Claude:", response2.choices[0].message["content"])
    print("Note: Claude does not remember the first message in this stateless example.\n")

def run_stateful_chat_loop(client, model):
    print("\n--- Stateful Chat Loop ---")
    system_instruction = get_system_instruction("You are a helpful assistant who remembers previous messages.")
    conversation_history = [{"role": "system", "content": system_instruction}]

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Ending stateful chat.")
            break

        conversation_history.append({"role": "user", "content": user_input})

        response = client.completions.create(
            model=model,
            messages=conversation_history
        )
        assistant_message = response.choices[0].message["content"]
        print("Claude:", assistant_message)

        conversation_history.append({"role": "assistant", "content": assistant_message})

        print("\nConversation history so far:")
        for msg in conversation_history:
            print(f"{msg['role'].capitalize()}: {msg['content']}")
        print()

def main():
    load_dotenv()
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        print("Error: ANTHROPIC_API_KEY not found in environment variables.")
        return

    client = Anthropic(api_key=api_key)
    model = choose_model()

    run_stateless_example(client, model)
    run_stateful_chat_loop(client, model)

if __name__ == "__main__":
    main()