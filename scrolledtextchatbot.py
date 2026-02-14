import tkinter as tk
from tkinter import scrolledtext
import time, threading

qa = {
    "courses": "UG: B.Sc (CS), B.Com, BA, BBA\nPG: M.Sc (CS), MBA, M.Com",
    "fees": "UG Fees: Rs. 45,000/year\nPG Fees: Rs. 65,000/year",
    "hostel": "Facilities: WiFi, Mess, Gym\nFees: Rs. 30,000/year",
    "library": "Timings: 9AM–6PM\nBooks: 20,000+\nDigital Access: Yes",
    "admission": "Process: Entrance Test + Interview\nStart: June"
}

def bot_reply(text):
    for char in text:
        chat.insert(tk.END, char, "bot")
        chat.update()
        time.sleep(0.02)
    chat.insert(tk.END, "\n\n")
    chat.see(tk.END)

def ask():
    question = entry.get().lower()
    entry.delete(0, tk.END)
    chat.insert(tk.END, f"🧑 You: {question}\n", "user")
    answer = qa.get(question, "Please ask about courses, fees, hostel, library, or admission.")
    threading.Thread(target=bot_reply, args=(f"🤖 Bot: {answer}",)).start()

root = tk.Tk()
root.title("College Chatbot - Module 5 (Final)")

chat = scrolledtext.ScrolledText(root, width=60, height=20, wrap=tk.WORD)
chat.pack(padx=5, pady=5)

chat.tag_config("user", foreground="blue")
chat.tag_config("bot", foreground="green")

entry = tk.Entry(root, width=40)
entry.pack(side=tk.LEFT, padx=5, pady=5)
tk.Button(root, text="Ask", command=ask).pack(side=tk.LEFT)

root.mainloop()

