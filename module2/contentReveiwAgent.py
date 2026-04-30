import os
import sys
import json
import re
from dotenv import load_dotenv
from anthropic import Anthropic  # Assuming you have this client library

# Load environment variables
load_dotenv()
API_KEY = os.getenv("ANTHROPIC_API_KEY")
if not API_KEY:
    print("Error: API key missing.")
    sys.exit(1)

client = Anthropic(api_key=API_KEY)
MODEL_NAME = "claude-v1"  # Example model name

def read_user_content():
    print("Paste your content (end with Ctrl+D or Ctrl+Z):")
    content = sys.stdin.read().strip()
    if not content:
        print("No content provided.")
        sys.exit(0)
    return content

def extract_json(text):
    json_pattern = re.compile(r"\{.*?\}", re.DOTALL)
    matches = json_pattern.findall(text)
    for match in matches:
        try:
            return json.loads(match)
        except json.JSONDecodeError:
            continue
    return None

def check_pii(content):
    prompt = f"""
You are a PII checker. Identify if the following text contains personally identifiable information (PII) such as names, emails, phone numbers, addresses, IDs, credit cards, passwords.

Text:
\"\"\"{content}\"\"\"

Respond ONLY with JSON:
{{
  "pii_status": "pass" or "fail",
  "explanation": "Reason for the decision"
}}
"""
    response = client.completions.create(
        model=MODEL_NAME,
        prompt=prompt,
        max_tokens=200,
        stop=["\n\n"]
    )
    raw_text = response.completion
    result = None
    try:
        result = json.loads(raw_text)
    except json.JSONDecodeError:
        result = extract_json(raw_text)
    if not result:
        result = {"pii_status": "pass", "explanation": "No PII detected or unable to parse response."}
    return result

def main():
    content = read_user_content()
    print("Checking content for PII...")
    result = check_pii(content)
    if result["pii_status"] == "pass":
        print("Content passed PII check:", result["explanation"])
        # Further processing can be done here
    else:
        print("Content failed PII check:", result["explanation"])
        sys.exit(1)

if __name__ == "__main__":
    main()