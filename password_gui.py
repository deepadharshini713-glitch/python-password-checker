import tkinter as tk
import re

def check_password():
    password = entry.get()
    score = 0

    if len(password) >= 8:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[^A-Za-z0-9]", password):
        score += 1

    if score <= 2:
        result.config(text="WEAK ❌")
    elif score <= 4:
        result.config(text="MEDIUM ⚠️")
    else:
        result.config(text="STRONG ✅")

    score_label.config(text=f"Score: {score}/5")


window = tk.Tk()
window.title("Password Strength Checker")
window.geometry("400x300")

title = tk.Label(
    window,
    text="🔐 Password Strength Checker",
    font=("Arial", 18)
)
title.pack(pady=20)

entry = tk.Entry(window, show="*", width=30)
entry.pack(pady=10)

button = tk.Button(
    window,
    text="Check Password",
    command=check_password
)
button.pack(pady=10)

result = tk.Label(
    window,
    text="Enter a password",
    font=("Arial", 14)
)
result.pack(pady=10)

score_label = tk.Label(
    window,
    text="Score: 0/5",
    font=("Arial", 12)
)
score_label.pack(pady=10)

window.mainloop()