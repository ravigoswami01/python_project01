import tkinter as tk
from tkinter import messagebox


# Functions
def add_task():
    task = task_entry.get()

    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")


def remove_task():
    try:
        selected_task = task_listbox.curselection()[0]
        task_listbox.delete(selected_task)
    except:
        messagebox.showwarning("Warning", "Please select a task to remove!")


def view_tasks():
    tasks = task_listbox.get(0, tk.END)

    if tasks:
        task_text = "\n".join(tasks)
        messagebox.showinfo("Current Tasks", task_text)
    else:
        messagebox.showinfo("Current Tasks", "No tasks available.")


# Main Window
root = tk.Tk()
root.title("To-Do List App")
root.geometry("500x500")

# Heading
title_label = tk.Label(
    root,
    text="To-Do List Application",
    font=("Arial", 18, "bold")
)
title_label.pack(pady=10)

# Entry
task_entry = tk.Entry(root, width=40, font=("Arial", 12))
task_entry.pack(pady=10)

# Add Button
add_btn = tk.Button(
    root,
    text="Add Task",
    width=20,
    command=add_task
)
add_btn.pack(pady=5)

# Remove Button
remove_btn = tk.Button(
    root,
    text="Remove Selected Task",
    width=20,
    command=remove_task
)
remove_btn.pack(pady=5)

# View Button
view_btn = tk.Button(
    root,
    text="View Tasks",
    width=20,
    command=view_tasks
)
view_btn.pack(pady=5)

# Task List
task_listbox = tk.Listbox(
    root,
    width=50,
    height=15,
    font=("Arial", 12)
)
task_listbox.pack(pady=10)

# Exit Button
exit_btn = tk.Button(
    root,
    text="Exit",
    width=20,
    command=root.destroy
)
exit_btn.pack(pady=5)

root.mainloop()