import tkinter as tk
from tkinter import messagebox
import os


# Files
LIST1_FILE = "List1.txt"
LIST2_FILE = "List2.txt"
SAME_FILE = "Same.txt"
DIFF_FILE = "Different.txt"


# Functions
def load_list(filename):
    if not os.path.exists(filename):
        return []
    with open(filename, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def save_list(filename, data):
    with open(filename, "w", encoding="utf-8") as f:
        for item in data:
            f.write(item + "\n")

def compare_lists():
    start_button.config(state="disabled")
    root.update()

    list1 = load_list(LIST1_FILE)
    list2 = load_list(LIST2_FILE)

    same = []
    different = []

    total = len(list1) + len(list2)
    processed = 0

    set2 = set(list2)

    # We check the elements from list1.
    for item in list1:
        if item in set2:
            same.append(item)
        else:
            different.append(item)

        processed += 1
        percent = int((processed / total) * 100)
        progress_text.set(f"Progress: {percent}%")
        root.update()

    set1 = set(list1)

    # We check only the elements from list2.
    for item in list2:
        if item not in set1:
            different.append(item)

        processed += 1
        percent = int((processed / total) * 100)
        progress_text.set(f"Progress: {percent}%")
        root.update()

    save_list(SAME_FILE, same)
    save_list(DIFF_FILE, different)

    log_text.set(f"Done! Same: {len(same)}, Different: {len(different)}")
    messagebox.showinfo("Result", f"Found {len(same)} common items and {len(different)} different items.")

    progress_text.set("Progress: 100%")
    start_button.config(state="normal")


# GUI
root = tk.Tk()
root.title("ListMaster")
root.geometry("250x150")

log_text = tk.StringVar()

progress_text = tk.StringVar()
progress_text.set("Progress: 0%")

tk.Label(root, text="Comparing List 1 and 2").pack(pady=10)
start_button = tk.Button(root, text="Start", command=compare_lists, width=20, height=2)
start_button.pack(pady=3)
tk.Label(root, textvariable=log_text).pack(pady=3)

tk.Label(root, textvariable=progress_text).pack()

root.mainloop()
