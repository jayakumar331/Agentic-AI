from openai import OpenAI
from dotenv import load_dotenv

# Load the environment variables
load_dotenv()

# Create the client
client = OpenAI(
    api_key = "AIzaSyBmVTCK99bkCTiQyXKFBhfBFuIN2GD4xJ4",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Zero-shot Prompt
System_ZeroShot = "You are a helpful assistant. only answer if question is realted to maths, otherwise simple roast the person"
User_ZeroShot = "What is the capital of France?"

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": System_ZeroShot}, # System message
        {"role": "user", "content": User_ZeroShot} # User message
    ]   
)

print(response.choices[0].message.content)
#Zero-shot Prompt => It is a simple way to provide context to the model without having to provide a large amount of data.