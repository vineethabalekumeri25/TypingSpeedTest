import tkinter as tk
from tkinter import messagebox
import time
import random

# Sentences for the typing test
SENTENCES = [
    "The quick brown fox jumps over the lazy dog.",
    "Practice makes perfect when it comes to typing.",
    "A journey of a thousand miles begins with a single step.",
    "She sells seashells by the seashore.",
    "To be or not to be, that is the question.",
]

# Initialize variables
start_time = None
selected_sentence = random.choice(SENTENCES)

# Start the test
def start_test():
    global start_time, selected_sentence
    selected_sentence = random.choice(SENTENCES)
    sentence_label.config(text=selected_sentence)
    start_time = time.time()
    input_text.delete("1.0", tk.END)
    input_text.focus()
    check_button.config(state=tk.DISABLED)
    enable_check_button()  # Start monitoring for typing

# Dynamically enable the "Check Typing" button
def enable_check_button():
    typed_text = input_text.get("1.0", tk.END).strip()
    if typed_text:  # If there's any text, enable the button
        check_button.config(state=tk.NORMAL)
    else:
        check_button.config(state=tk.DISABLED)
    # Recheck in 100ms to dynamically monitor the text box
    root.after(100, enable_check_button)

# Check the typing result
def check_result():
    global start_time
    if not start_time:
        messagebox.showerror("Error", "You need to start the test first!")
        return

    elapsed_time = time.time() - start_time
    typed_text = input_text.get("1.0", tk.END).strip()

    # Calculate typing speed
    word_count = len(typed_text.split())
    wpm = round((word_count / elapsed_time) * 60, 2)

    # Check accuracy
    if typed_text == selected_sentence:
        messagebox.showinfo("Result", f"Great job! You typed correctly.\nSpeed: {wpm} WPM")
    else:
        messagebox.showwarning(
            "Result",
            f"Typing errors found.\nTry again.\nSpeed: {wpm} WPM\n\nExpected:\n{selected_sentence}\n\nTyped:\n{typed_text}",
        )
    check_button.config(state=tk.DISABLED)  # Disable button after checking

# Create the GUI window
root = tk.Tk()
root.title("Typing Speed Test")
root.geometry("700x400")
root.config(bg="lightblue")

# Title
title_label = tk.Label(root, text="Typing Speed Test", font=("Times New Roman", 24, "bold"), bg="lightblue", fg="darkblue")
title_label.pack(pady=10)

# Sentence to type
sentence_label = tk.Label(root, text=selected_sentence, font=("Times New Roman", 14), wraplength=600, bg="lightblue")
sentence_label.pack(pady=20)

# Input text box
input_text = tk.Text(root, height=5, width=60, font=("Times New Roman", 14))
input_text.pack(pady=10)

# Start and Check buttons
button_frame = tk.Frame(root, bg="lightblue")
button_frame.pack(pady=20)

start_button = tk.Button(button_frame, text="Start Test", font=("Times New Roman", 14), bg="lightgreen", command=start_test)
start_button.grid(row=0, column=0, padx=10)

check_button = tk.Button(button_frame, text="Check Typing", font=("Times New Roman", 14), bg="lightyellow", command=check_result, state=tk.DISABLED)
check_button.grid(row=0, column=1, padx=10)

# Run the app
root.mainloop()