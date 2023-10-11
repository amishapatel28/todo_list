import tkinter as tk

def add_task():
    task = task_entry.get()
    if task:
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def remove_task():
    selected_task = task_list.curselection()
    if selected_task:
        task_list.delete(selected_task)

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Create and configure the task list
task_list = tk.Listbox(root)
task_list.pack(pady=10)

# Create a text entry for new tasks
task_entry = tk.Entry(root)
task_entry.pack(pady=10)

# Create buttons to add and remove tasks
add_button = tk.Button(root, text="Add Task", command=add_task)
remove_button = tk.Button(root, text="Remove Task", command=remove_task)
add_button.pack()
remove_button.pack()

# The GUI application
root.mainloop()
