import tkinter as tk
 
# Simple Q&A data
qa = {
    "courses": "We offer B.Sc (CS), B.Com, BA, and BBA.",
    "fees": "Average yearly fees: Rs. 45,000.",
    "hostel": "Separate hostels for boys and girls, capacity 200 each.",
    "library": "Library has 20,000+ books and e-resources.",
    "admission": "Admissions start from June every year."
}
 
def ask():
    q = entry.get().lower()
    entry.delete(0, tk.END)
    a = qa.get(q, "Sorry, I don't know about that.")
    chat.insert(tk.END, f"You: {q}\nBot: {a}\n\n")
 
root = tk.Tk()
root.title("Simple College Chatbot")
 
chat = tk.Text(root, width=50, height=15)
chat.pack()
 
entry = tk.Entry(root, width=35)
entry.pack(side=tk.LEFT, padx=5, pady=5)
 
tk.Button(root, text="Ask", command=ask).pack(side=tk.LEFT)
 
root.mainloop()
