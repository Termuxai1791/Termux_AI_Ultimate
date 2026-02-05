from rich.console import Console

console = Console()

console.print("\n💻 Code Helper")
console.print("Describe what you want, and I'll generate starter code.\n")

request = console.input("Task > ")

console.print("\n--- Suggested Python Starter Code ---\n")

print(f"""# Auto-generated starter code

def main():
    print("Task: {request}")
    # TODO: Implement logic here

if __name__ == "__main__":
    main()
""")
