import json
from datetime import datetime
from rich.console import Console

console = Console()
memory_file = "chat_memory.json"

console.print("\n🧠 Memory Chat (saved locally)")
console.print("Type exit to stop\n")

chatlog = []

while True:
    msg = console.input("You > ")
    if msg.lower() == "exit":
        break

    chatlog.append({
        "time": str(datetime.now()),
        "message": msg
    })

with open(memory_file, "w") as f:
    json.dump(chatlog, f, indent=2)

console.print(f"\n✅ Saved chat into {memory_file}\n")
