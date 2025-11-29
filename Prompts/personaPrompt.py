from openai import OpenAI
from dotenv import load_dotenv

# Load the environment variables
load_dotenv()

# Create the client
client = OpenAI(
    api_key = "AIzaSyBmVTCK99bkCTiQyXKFBhfBFuIN2GD4xJ4",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# personaPrompt
System_personaPrompt = """Role: You are a my best friend Abinesh who is 31 years old. he is currenlty working as devops engineer in beribot
Examples:

1. What is abinesh age => 31
2. What is abinesh job => devops engineer
3. What is abinesh company => beribot
4. is abinesh married => no
5. is abinesh single => yes
6. abinesh home location => coimbatore


Rules:
1. Answer the user's question ans assume you are abinesh.
"""

User_personaPrompt = "What is my name "


response = client.chat.completions.create(
    model = "gemini-2.5-flash",
    # response_format = {"type": "json_object"},
    messages = [
        {"role":"system","content":System_personaPrompt},
        {"role":"user","content":User_personaPrompt}
    ]
)

print(response.choices[0].message.content)