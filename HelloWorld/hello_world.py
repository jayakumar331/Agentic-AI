from openai import OpenAI
from dotenv import load_dotenv

# Load the environment variables
load_dotenv()

# Create the client
client = OpenAI(
    api_key = "AIzaSyBmVTCK99bkCTiQyXKFBhfBFuIN2GD4xJ4",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)


response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."}, # System message
        {"role": "user", "content": "Hello, how are you?"} # User message
    ]   
)

print(response.choices[0].message.content)