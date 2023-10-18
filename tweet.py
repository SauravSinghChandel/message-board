import tkinter as tk

def send_message():
    username = username_entry.get()
    message = message_entry.get()
    if username.strip() != "" and message.strip() != "":
        message_text = f"{username}: {message}"
        chat_display.insert(tk.END, message_text + "\n")
        username_entry.delete(0, tk.END)
        message_entry.delete(0, tk.END)

app = tk.Tk()
app.title("Forum")

chat_frame = tk.Frame(app)
chat_frame.pack(padx=10, pady=10)

chat_display = tk.Text(chat_frame, height=10, width=40)
chat_display.pack()

username_label = tk.Label(chat_frame, text="Your Name:")
username_label.pack()

username_entry = tk.Entry(chat_frame)
username_entry.pack()

message_label = tk.Label(chat_frame, text="What's happening?")
message_label.pack()

message_entry = tk.Entry(chat_frame)
message_entry.pack()

send_button = tk.Button(chat_frame, text="Post!", command=send_message)
send_button.pack()

app.mainloop()