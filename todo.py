import tkinter as tk
from tkinter import simpledialog, messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.tasks = []
        self.load_tasks()

        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        self.listbox = tk.Listbox(self.frame, width=50, height=10)
        self.listbox.pack(side=tk.LEFT, padx=10)

        self.scrollbar = tk.Scrollbar(self.frame, orient=tk.VERTICAL)
        self.scrollbar.config(command=self.listbox.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox.config(yscrollcommand=self.scrollbar.set)

        self.entry = tk.Entry(root, width=50)
        self.entry.pack(pady=5)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack(side=tk.LEFT, padx=5)

        self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_task)
        self.remove_button.pack(side=tk.LEFT, padx=5)

        self.update_button = tk.Button(root, text="Update Task", command=self.update_task)
        self.update_button.pack(side=tk.LEFT, padx=5)

        self.populate_listbox()

    def load_tasks(self):
        try:
            with open('tasks.txt', 'r') as file:
                self.tasks = [task.strip() for task in file.readlines()]
        except FileNotFoundError:
            pass

    def save_tasks(self):
        with open('tasks.txt', 'w') as file:
            for task in self.tasks:
                file.write(f"{task}\n")

    def add_task(self):
        task = self.entry.get()
        if task:
            self.tasks.append(task)
            self.populate_listbox()
            self.save_tasks()
            self.entry.delete(0, tk.END)

    def remove_task(self):
        try:
            selected_index = self.listbox.curselection()[0]
            self.tasks.pop(selected_index)
            self.populate_listbox()
            self.save_tasks()
        except IndexError:
            messagebox.showwarning("Warning", "No task selected")

    def update_task(self):
        try:
            selected_index = self.listbox.curselection()[0]
            new_task = simpledialog.askstring("Update Task", "Enter the new task:", initialvalue=self.tasks[selected_index])
            if new_task:
                self.tasks[selected_index] = new_task
                self.populate_listbox()
                self.save_tasks()
        except IndexError:
            messagebox.showwarning("Warning", "No task selected")

    def populate_listbox(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            self.listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()