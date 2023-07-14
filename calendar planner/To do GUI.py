import datetime
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from ttkthemes import ThemedStyle

tasks = []
completed_tasks = []

def add_task():
    title = title_entry.get()
    description = description_entry.get("1.0", tk.END).strip()
    start_time = start_entry.get()
    end_time = end_entry.get()

    current_time = datetime.datetime.now().strftime("%I:%M %p")

    if not start_time:
        start_time = current_time
    if not end_time:
        end_time = current_time

    try:
        if start_time:
            start_time = datetime.datetime.strptime(start_time, "%I:%M %p").strftime("%I:%M %p")
        if end_time:
            end_time = datetime.datetime.strptime(end_time, "%I:%M %p").strftime("%I:%M %p")
    except ValueError:
        messagebox.showerror("Invalid Time Format", "Please use the format: hh:mm AM/PM")
        return

    task = {
        "title": title,
        "description": description,
        "start_time": start_time,
        "end_time": end_time
    }
    tasks.append(task)
    title_entry.delete(0, tk.END)
    description_entry.delete("1.0", tk.END)
    start_entry.delete(0, tk.END)
    end_entry.delete(0, tk.END)
    start_check_var.set(False)
    toggle_entry_state()
    update_task_tree()

def view_tasks():
    if tasks:
        task_tree.delete(*task_tree.get_children())
        for index, task in enumerate(tasks, start=1):
            task_tree.insert("", tk.END, text=index, values=(task["title"], task["description"], task["start_time"], task["end_time"]))
    else:
        messagebox.showinfo("No Tasks", "No tasks found.")

def view_completed_tasks(filter_option):
    completed_tasks_window = tk.Toplevel(window)
    completed_tasks_window.title("Completed Tasks")

    if filter_option == "today":
        filtered_tasks = [task for task in completed_tasks if task["completion_date"] == datetime.datetime.now().strftime("%Y-%m-%d")]
    elif filter_option == "past_7_days":
        filtered_tasks = [task for task in completed_tasks if task["completion_date"] >= (datetime.datetime.now() - datetime.timedelta(days=7)).strftime("%Y-%m-%d")]
    else:
        filtered_tasks = completed_tasks

    if filtered_tasks:
        completed_task_tree = ttk.Treeview(completed_tasks_window, columns=("Title", "Description"), show="headings")
        completed_task_tree.heading("Title", text="Title")
        completed_task_tree.heading("Description", text="Description")
        completed_task_tree.pack(pady=10, fill=tk.BOTH, expand=True)
        for index, task in enumerate(filtered_tasks, start=1):
            completed_task_tree.insert("", tk.END, text=index, values=(task["title"], task["description"]))
    else:
        messagebox.showinfo("No Completed Tasks", "No completed tasks found.")

def mark_task_complete():
    selection = task_tree.focus()
    if selection:
        task_index = int(task_tree.item(selection, "text")) - 1
        completed_task = tasks.pop(task_index)
        completed_task["completion_date"] = datetime.datetime.now().strftime("%Y-%m-%d")
        completed_tasks.append(completed_task)
        update_task_tree()
    else:
        messagebox.showerror("Invalid Selection", "Please select a task to mark as complete.")

def delete_task():
    selection = task_tree.focus()
    if selection:
        task_index = int(task_tree.item(selection, "text")) - 1
        deleted_task = tasks.pop(task_index)
        update_task_tree()
    else:
        messagebox.showerror("Invalid Selection", "Please select a task to delete.")

def update_task_tree():
    task_tree.delete(*task_tree.get_children())
    for index, task in enumerate(tasks, start=1):
        task_tree.insert("", tk.END, text=index, values=(task["title"], task["description"], task["start_time"], task["end_time"]))

def toggle_entry_state():
    if start_check_var.get():
        start_entry.config(state=tk.NORMAL, foreground="white")
        end_entry.config(state=tk.NORMAL, foreground="white")
        start_label.config(foreground="white")
        end_label.config(foreground="white")
    else:
        start_entry.config(state=tk.DISABLED, foreground="gray")
        end_entry.config(state=tk.DISABLED, foreground="gray")
        start_label.config(foreground="gray")
        end_label.config(foreground="gray")

def update_current_datetime():
    current_datetime = datetime.datetime.now()
    current_date = current_datetime.strftime("%A, %B %d, %Y")
    current_time = current_datetime.strftime("%I:%M:%S %p")
    datetime_label.config(text=f"Current Date and Time: {current_date} {current_time}")
    window.after(1000, update_current_datetime)

# Create the main window
window = tk.Tk()
window.title("To-Do List Application")

# Apply the themed style for macOS look and feel
style = ThemedStyle(window)
style.set_theme("aqua")

# Configure button style
style.configure("TButton", background="#c8d7e1", foreground="white", relief="raised", font=("Helvetica", 12))

# Create a frame for date and time
datetime_frame = ttk.Frame(window)
datetime_frame.pack(pady=10)

# Create a label for date and time
datetime_label = ttk.Label(datetime_frame, text="Current Date and Time:")
datetime_label.pack()

# Update the current date and time label periodically
update_current_datetime()

# Create a menu button for completed tasks
completed_menu = ttk.Button(window, text="Completed Tasks", command=lambda: view_completed_tasks("all_time"))
completed_menu.pack(anchor=tk.NW)

# Create labels and entry fields
ttk.Label(window, text="Task Title:").pack()
title_entry = ttk.Entry(window)
title_entry.pack()
ttk.Label(window, text="Task Description:").pack()
description_entry = tk.Text(window, height=5, width=30)  # Adjusted height and width
description_entry.pack()

# Create a checkbox and associated variable
start_check_var = tk.BooleanVar()
start_check = ttk.Checkbutton(window, text="Set Start/End Time", variable=start_check_var, command=toggle_entry_state)
start_check.pack(pady=10)

# Create entry fields for start and end time
entry_frame = ttk.Frame(window)
entry_frame.pack()

start_label = ttk.Label(entry_frame, text="Start Time:", foreground="gray")
start_label.pack(side=tk.LEFT, padx=5)
start_entry = ttk.Entry(entry_frame, state=tk.DISABLED, foreground="gray")
start_entry.pack(side=tk.LEFT, padx=5)

end_label = ttk.Label(entry_frame, text="End Time:", foreground="gray")
end_label.pack(side=tk.LEFT, padx=5)
end_entry = ttk.Entry(entry_frame, state=tk.DISABLED, foreground="gray")
end_entry.pack(side=tk.LEFT, padx=5)

# Create buttons
button_frame = ttk.Frame(window)
button_frame.pack(pady=10)

add_button = ttk.Button(button_frame, text="Add Task", command=add_task)
add_button.pack(side=tk.LEFT, padx=5)
view_button = ttk.Button(button_frame, text="View Tasks", command=view_tasks)
view_button.pack(side=tk.LEFT, padx=5)
mark_button = ttk.Button(button_frame, text="Mark as Complete", command=mark_task_complete)
mark_button.pack(side=tk.LEFT, padx=5)
delete_button = ttk.Button(button_frame, text="Delete Task", command=delete_task)
delete_button.pack(side=tk.LEFT, padx=5)

# Create a treeview for task display
columns = ("Title", "Description", "Start Time", "End Time")
task_tree = ttk.Treeview(window, columns=columns, show="headings", selectmode="browse")
task_tree.heading("Title", text="Title")
task_tree.heading("Description", text="Description")
task_tree.heading("Start Time", text="Start Time")
task_tree.heading("End Time", text="End Time")
task_tree.column("Title", width=150)
task_tree.column("Description", width=200)
task_tree.column("Start Time", width=100)
task_tree.column("End Time", width=100)
task_tree.pack(pady=10, fill=tk.BOTH, expand=True)

# Create an exit button
exit_button = ttk.Button(window, text="Exit", command=window.quit)
exit_button.pack(side=tk.BOTTOM, pady=10)

# Start the main loop
window.mainloop()
