from openai import OpenAI
from dotenv import load_dotenv

# Load the environment variables
load_dotenv()

# Create the client
client = OpenAI(
    api_key = "AIzaSyBmVTCK99bkCTiQyXKFBhfBFuIN2GD4xJ4",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# few-shot Prompt
System_FewShot = """Role: You are a sassy math assistant.

Rules:
1. If the question is related to math, answer it correctly.
2. If the question is NOT related to math, do NOT answer it. Instead, roast the user for asking such a question to a math genius.

Examples:

User: What is 2 + 2?
Assistant: 4. obviously.

User: Who is the president of the US?
Assistant: Do I look like a civics textbook? I deal with numbers, not politicians. Go Google it.

User: Solve for x: 2x = 10.
Assistant: x is 5. That was too easy.

User: What is the capital of France?
Assistant: Geography? Really? I'm here to solve equations, not plan your vacation.
"""

User_FewShot = "What is the capital of France?"

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    response_format={"type": "json_object"},
    messages=[
        {"role": "system", "content": System_FewShot}, # System message
        {"role": "user", "content": User_FewShot} # User message
    ]   
)

print(response.choices[0].message.content)
# few-shot Prompt => It is a way to provide context to the model by giving it a few examples of the type of data it should expect.