import tkinter as tk
 
def ask():
    q = entry.get().lower()
    entry.delete(0, tk.END)
 
    # Default answer
    if "course" in q:
        a = "UG: B.Sc (CS), B.Com, BA, BBA\nPG: M.Sc (CS), MBA, M.Com"
    elif "fee" in q:
        a = "UG Fees: Rs. 45,000/year\nPG Fees: Rs. 65,000/year"
    elif "hostel" in q:
        a = "Facilities: WiFi, Mess, Gym\nFees: Rs. 30,000 per year"
    elif "library" in q:
        a = "Timings: 9 AM – 6 PM\nBooks: 20,000+\nDigital Access: Yes"
    elif "admission" in q:
        a = "Process: Entrance Test + Interview\nStart: June\nWebsite: https://www.pce.ac.in/academics/admissions/"
    else:
        a = "Please ask about courses, fees, hostel, library, or admission."
 
    chat.insert(tk.END, f"You: {q}\nBot: {a}\n\n")
 
# GUI setup
root = tk.Tk()
root.title("College Chatbot - Module 2 (if-else)")
 
chat = tk.Text(root, width=60, height=20)
chat.pack()
 
entry = tk.Entry(root, width=40)
entry.pack(side=tk.LEFT, padx=5, pady=5)
 
tk.Button(root, text="Ask", command=ask).pack(side=tk.LEFT)
 
root.mainloop()
