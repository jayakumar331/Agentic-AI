from openai import OpenAI
from dotenv import load_dotenv


# Load the environment variables
load_dotenv()

# Create the client
client = OpenAI(
    api_key = "AIzaSyBmVTCK99bkCTiQyXKFBhfBFuIN2GD4xJ4",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Chain of Thought Prompt
System_ChainOfThought = """Role: You are a helpful assistant that solves problems by thinking step-by-step.

Rules:
1. Read the user's question carefully.
2. Break down the problem into smaller, manageable steps.
3. Solve each step one by one, showing your reasoning.
4. Provide the final answer clearly after the steps.

Examples:

User: Roger has 5 tennis balls. He buys 2 more cans of tennis balls. Each can has 3 tennis balls. How many tennis balls does he have now?
Assistant:
Step 1: Roger starts with 5 tennis balls.
Step 2: He buys 2 cans of tennis balls.
Step 3: Each can has 3 tennis balls, so he buys 2 * 3 = 6 tennis balls.
Step 4: Total tennis balls = Initial balls + New balls = 5 + 6 = 11.
Answer: 11

User: The cafeteria had 23 apples. If they used 20 to make lunch and bought 6 more, how many apples do they have?
Assistant:
Step 1: The cafeteria started with 23 apples.
Step 2: They used 20 apples, so 23 - 20 = 3 apples remaining.
Step 3: They bought 6 more apples, so 3 + 6 = 9 apples.
Answer: 9
"""

User_ChainOfThought = "If it takes 5 machines 5 minutes to make 5 widgets, how long would it take 100 machines to make 100 widgets?"

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": System_ChainOfThought}, # System message
        {"role": "user", "content": User_ChainOfThought} # User message
    ]
)

print(response.choices[0].message.content)
# Chain of Thought Prompt => It encourages the model to explain its reasoning step-by-step.
