import os
import pandas as pd
from dotenv import load_dotenv
from anthropic import Anthropic

# Load environment variables and API key
load_dotenv()
API_KEY = os.getenv("ANTHROPIC_API_KEY")
if not API_KEY:
    raise ValueError("Missing Anthropic API key in .env file")

# Initialize Anthropic client
client = Anthropic(api_key=API_KEY)
model = "claude-1"

# Load dataset function with multiple encoding attempts
def load_dataset(file_path):
    encodings = ["utf-8", "latin1", "cp1252"]
    for enc in encodings:
        try:
            return pd.read_csv(file_path, encoding=enc)
        except Exception:
            continue
    raise ValueError("Failed to load dataset with supported encodings")

# Build dataset summary
def build_summary(df):
    summary = f"Rows: {len(df)}\n"
    summary += f"Columns: {list(df.columns)}\n"
    summary += f"Data Types:\n{df.dtypes}\n"
    summary += f"Missing Values:\n{df.isnull().sum()}\n"
    summary += f"Duplicate Rows: {df.duplicated().sum()}\n"
    summary += f"Sample Data:\n{df.head().to_string()}\n"
    return summary

# Ask agent a question
def ask_agent(summary, question):
    prompt = f"""
You are a data-checking assistant. Use only the following dataset summary to answer:

{summary}

Question: {question}
Answer:"""
    response = client.completions.create(
        model=model,
        prompt=prompt,
        max_tokens_to_sample=200,
        stop_sequences=["\n\n"]
    )
    return response.completion.strip()

def main():
    data_file = "your_dataset.csv"  # Place your CSV file in the project folder
    df = load_dataset(data_file)
    summary = build_summary(df)
    print("Data-checking agent ready. Type 'exit' to quit.")
    while True:
        user_question = input("What do you want to know? ")
        if user_question.lower() == "exit":
            break
        answer = ask_agent(summary, user_question)
        print(answer)

if __name__ == "__main__":
    main()