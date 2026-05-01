import os
from dotenv import load_dotenv
from google import genai
import argparse

load_dotenv()
# Retrieve the API key 
api_key = os.environ.get("GEMINI_API_KEY")
if api_key is None:
    raise RuntimeError("GEMINI_API_KEY is not set in the environment variables.")

# Getting prompt from the user from CLI
parser = argparse.ArgumentParser(description="Process a user prompt with an AI bot")
parser.add_argument("user_prompt", type=str, help="User prompt for AI agent")
args = parser.parse_args()

# Setting the client and generating content for AI
client = genai.Client(api_key=api_key)
response = client.models.generate_content(
    model='gemini-2.5-flash', contents=f"{args.user_prompt}")

# counting the amount of prompt and response tokens used
prompt_tokens = response.usage_metadata.prompt_token_count
response_tokens = response.usage_metadata.candidates_token_count

if response_tokens is None:
    raise RuntimeError("Potential failed API call, no response!")

def main():
    print(f"Prompt tokens: {prompt_tokens}")
    print(f"Response tokens: {response_tokens}")
    print(response.text)

if __name__ == "__main__":
    main()
