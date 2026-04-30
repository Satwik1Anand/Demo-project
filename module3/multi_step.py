import os
import re
from dotenv import load_dotenv
from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT

load_dotenv()
client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
model = "claude-v1"

def extractPointLimit(user_input):
    match = re.search(r'(\d+)\s*points?', user_input)
    return int(match.group(1)) if match else 5

def wantsPoints(user_input):
    return bool(re.search(r'\b(point|bullet|list)\b', user_input, re.I))

def isElaborationRequest(user_input):
    return bool(re.search(r'\b(explain more|continue)\b', user_input, re.I))

def buildSystemPrompt(usePoints, pointLimit):
    if usePoints:
        return f"Answer in exactly {pointLimit} bullet points. Each point must be short and concise."
    else:
        return "Answer in 2-3 sentences, be concise."

def callAPI(system_prompt, message_history, max_tokens=1000):
    messages = [{"role": "system", "content": system_prompt}] + message_history
    response = client.completions.create(
        model=model,
        prompt=system_prompt + "\n" + "\n".join([m["content"] for m in message_history]),
        max_tokens_to_sample=max_tokens,
        stop_sequences=[HUMAN_PROMPT]
    )
    return response.completion.strip()

def main():
    message_history = []
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        usePoints = wantsPoints(user_input)
        pointLimit = extractPointLimit(user_input) if usePoints else 0
        system_prompt = buildSystemPrompt(usePoints, pointLimit)
        message_history.append({"role": "user", "content": user_input})
        reply = callAPI(system_prompt, message_history)
        message_history.append({"role": "assistant", "content": reply})
        print("Claude:", reply)

if __name__ == "__main__":
    main()