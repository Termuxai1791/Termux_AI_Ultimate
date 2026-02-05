from rich.console import Console
import os

console = Console()

def menu():
    console.print("\n🤖 Termux AI Assistant", style="bold green")
    console.print("1. Online Chat AI")
    console.print("2. Memory Chat (saved)")
    console.print("3. Code Helper")
    console.print("0. Exit\n")

while True:
    menu()
    choice = console.input("Choose > ")

    if choice == "1":
        os.system("python ~/Termux_AI_Ultimate/ai_scripts/ai_online.py")

    elif choice == "2":
        os.system("python ~/Termux_AI_Ultimate/ai_scripts/ai_memory.py")

    elif choice == "3":
        os.system("python ~/Termux_AI_Ultimate/ai_scripts/ai_code_writer.py")

    elif choice == "0":
        console.print("Bye 👋")
        break
