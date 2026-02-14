import tkinter as tk
from tkinter import scrolledtext

qa = {
    "courses": "B.Sc (CS), B.Com, BA, BBA",
    "fees": "UG: 45k/year, PG: 65k/year",
    "hostel": "WiFi, Mess, Gym – Rs. 30k/year",
    "library": "Open 9AM–6PM, 20,000+ books",
    "admission": "Entrance + Interview from June"
}

def ask():
    question = entry.get().lower()
    entry.delete(0, tk.END)
    chat.insert(tk.END, f"🧑 You: {question}\n", "user")
    answer = qa.get(question, "Sorry, I only know about courses, fees, hostel, library, and admission.")
    chat.insert(tk.END, f"🤖 Bot: {answer}\n\n", "bot")
    chat.see(tk.END)

root = tk.Tk()
root.title("College Chatbot - Module 4")

chat = scrolledtext.ScrolledText(root, width=60, height=20, wrap=tk.WORD)
chat.pack(padx=5, pady=5)

chat.tag_config("user", foreground="blue")
chat.tag_config("bot", foreground="green")

entry = tk.Entry(root, width=40)
entry.pack(side=tk.LEFT, padx=5, pady=5)
tk.Button(root, text="Ask", command=ask).pack(side=tk.LEFT)

root.mainloop()

