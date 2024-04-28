
import tkinter as tk

def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def delete_task():
    try:
        task_index = listbox.curselection()[0]
        listbox.delete(task_index)
    except IndexError:
        pass

def edit_task():
    try:
        task_index = listbox.curselection()[0]
        new_task = entry.get()
        listbox.delete(task_index)
        listbox.insert(task_index, new_task)
        entry.delete(0, tk.END)
    except IndexError:
        pass

root = tk.Tk()
root.title("To-Do List")
root.geometry("700x500")

header_label = tk.Label(root, text="To-Do List", font=("Comic Sans MS", 40), fg="cyan", bg="black")
header_label.pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=10)

listbox = tk.Listbox(frame, width=50, height=10, font=("Helvetica", 12))
listbox.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

entry = tk.Entry(root, font=("Helvetica", 12))
entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", width=15, command=add_task)
add_button.pack(side=tk.LEFT, padx=10)

edit_button = tk.Button(root, text="Edit Task", width=15, command=edit_task)
edit_button.pack(side=tk.LEFT, padx=10)

delete_button = tk.Button(root, text="Delete Task", width=15, command=delete_task)
delete_button.pack(side=tk.LEFT)

root.mainloop()
