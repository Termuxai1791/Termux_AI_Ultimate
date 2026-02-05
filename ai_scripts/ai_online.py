import os
from openai import OpenAI
from rich.console import Console

console = Console()

key = os.getenv("OPENAI_API_KEY")

if not key:
    console.print("\n❌ No API key found!", style="bold red")
    console.print("Set it like this:")
    console.print('export OPENAI_API_KEY="your_key_here"\n')
    exit()

client = OpenAI(api_key=key)

console.print("\n🌍 Online AI Chat started (type exit to quit)\n")

while True:
    user = console.input("You > ")

    if user.lower() in ["exit", "quit"]:
        break

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": user}]
    )

    console.print("\nAI >", style="bold yellow")
    console.print(response.choices[0].message.content)
    console.print("")

