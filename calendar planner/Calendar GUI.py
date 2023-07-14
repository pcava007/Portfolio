import datetime
import tkinter as tk
from tkinter import messagebox
from tkcalendar import Calendar, DateEntry
from tkinter import ttk

tasks = {}
completed_tasks = {}

def toggle_time_entry():
    if start_check_var.get():
        start_entry.config(state=tk.NORMAL)
        end_entry.config(state=tk.NORMAL)
    else:
        start_entry.config(state=tk.DISABLED)
        end_entry.config(state=tk.DISABLED)

def add_task():
    title = task_title.get()
    description = task_description.get("1.0", tk.END).strip()
    start_time = task_start_time.get() if start_check_var.get() else ""
    end_time = task_end_time.get() if start_check_var.get() else ""
    date = task_date.get_date().strftime("%m/%d/%Y")

    task = {
        "title": title,
        "description": description,
        "start_time": start_time,
        "end_time": end_time
    }

    if date in tasks:
        tasks[date].append(task)
    else:
        tasks[date] = [task]

    messagebox.showinfo("Success", "Task added: " + title)
    clear_task_fields()

def view_tasks():
    if tasks:
        task_text = ""
        for date, task_list in tasks.items():
            task_text += "Date: " + date + "\n"
            task_text += "Tasks:\n"
            for index, task in enumerate(task_list, start=1):
                task_text += f"{index}. Title: {task['title']}\n"
                task_text += f"   Description: {task['description']}\n"
                task_text += f"   Start Time: {task['start_time']}\n"
                task_text += f"   End Time: {task['end_time']}\n"
            task_text += "\n"
        messagebox.showinfo("Tasks", task_text)
    else:
        messagebox.showinfo("No Tasks", "No tasks found.")

def delete_task():
    selected_date = task_date.get_date().strftime("%m/%d/%Y")
    if selected_date in tasks:
        task_list = tasks[selected_date]
        if task_list:
            task_index = task_tree.focus()
            if task_index:
                task_index = int(task_index) - 1
                deleted_task = task_list.pop(task_index)
                messagebox.showinfo("Task Deleted", "Task deleted: " + deleted_task["title"])
                update_task_tree()
            else:
                messagebox.showerror("No Task Selected", "Please select a task to delete.")
        else:
            messagebox.showerror("No Tasks", "No tasks found on selected date.")
    else:
        messagebox.showerror("No Tasks", "No tasks found on selected date.")

def mark_task_complete():
    selected_date = task_date.get_date().strftime("%m/%d/%Y")
    if selected_date in tasks:
        task_list = tasks[selected_date]
        if task_list:
            task_index = task_tree.focus()
            if task_index:
                task_index = int(task_index) - 1
                completed_task = task_list.pop(task_index)
                completed_task_date = datetime.datetime.now().strftime("%m/%d/%Y")
                completed_task["completion_date"] = completed_task_date

                if completed_task_date in completed_tasks:
                    completed_tasks[completed_task_date].append(completed_task)
                else:
                    completed_tasks[completed_task_date] = [completed_task]

                messagebox.showinfo("Task Completed", "Task marked as complete: " + completed_task["title"])
                update_task_tree()
            else:
                messagebox.showerror("No Task Selected", "Please select a task to mark as complete.")
        else:
            messagebox.showerror("No Tasks", "No tasks found on selected date.")
    else:
        messagebox.showerror("No Tasks", "No tasks found on selected date.")

def clear_task_fields():
    task_title.set("")
    task_description.delete("1.0", tk.END)
    task_start_time.set("")
    task_end_time.set("")

def update_task_tree():
    task_tree.delete(*task_tree.get_children())
    selected_date = task_date.get_date().strftime("%m/%d/%Y")
    if selected_date in tasks:
        task_list = tasks[selected_date]
        for index, task in enumerate(task_list, start=1):
            task_tree.insert("", tk.END, index, values=(task["title"], task["description"], task["start_time"], task["end_time"]))

def show_calendar():
    selected_date = None

    def select_date():
        nonlocal selected_date
        selected_date = cal.get_date()
        top.destroy()

    def configure_date_style(date):
        current_date = datetime.datetime.now().date()
        if date.month == cal._date.month:
            # Weekdays of the current month displayed in white
            if date.weekday() < 5:
                return {"foreground": "white"}
            # Weekends of the current month displayed in light grey
            else:
                return {"foreground": "lightgrey"}
        else:
            # Dates from overlapping months displayed in black
            return {"foreground": "black"}

    def update_selected_date(event):
        selected_date_label["text"] = "Selected Date: " + cal.selection_get().strftime("%m/%d/%Y")

    top = tk.Toplevel(root)
    top.title("Select Date")

    cal = Calendar(
        top,
        selectmode="day",
        year=datetime.datetime.now().year,
        month=datetime.datetime.now().month,
        foreground="white",
        headersforeground="white",
        normalforeground="white",
        weekendforeground="lightgrey",
        othermonthforeground="black",
        selectbackground="darkblue",
        selectforeground="white",
        headersbackground="white",
        normalbackground="white",
        weekendbackground="white",
        othermonthbackground="white"
    )
    cal.pack(padx=20, pady=20)

    ok_button = ttk.Button(top, text="OK", command=select_date)
    ok_button.pack(pady=10)

    style = ttk.Style(top)
    style.map("Calendar.Treeview", fieldbackground=[("selected", "darkblue")])
    style.map("Calendar.Treeview", foreground=[("selected", "white")])

    cal.bind("<<CalendarMonthChanged>>", lambda event: cal._update())
    cal.bind("<<CalendarSelected>>", update_selected_date)

    # Configure date style on every redraw
    cal._calendar["daynames"] = cal._calendar["daynames"].copy()
    cal._calendar["daynames"].update(configure_date_style)

    selected_date_label = ttk.Label(top, text="Selected Date: " + cal.get_date().strftime("%m/%d/%Y"))
    selected_date_label.pack(pady=10)

    top.mainloop()

    return selected_date

root = tk.Tk()
root.title("To-Do List Manager")

# Create a frame for the main content
main_frame = ttk.Frame(root, padding="20")
main_frame.pack()

# Task Title
task_title_label = ttk.Label(main_frame, text="Task Title:")
task_title_label.grid(row=0, column=0, sticky=tk.W, padx=10)
task_title = tk.StringVar()
task_title_entry = ttk.Entry(main_frame, textvariable=task_title)
task_title_entry.grid(row=0, column=1, sticky=tk.W, padx=10)

# Task Description
task_description_label = ttk.Label(main_frame, text="Task Description:")
task_description_label.grid(row=1, column=0, sticky=tk.W, padx=10)
task_description = tk.Text(main_frame, width=30, height=4)
task_description.grid(row=1, column=1, sticky=tk.W, padx=10)

# Task Date
task_date_label = ttk.Label(main_frame, text="Task Date:")
task_date_label.grid(row=2, column=0, sticky=tk.W, padx=10)
task_date = DateEntry(main_frame, width=12, background="darkblue", foreground="white", borderwidth=2)
task_date.grid(row=2, column=1, sticky=tk.W, padx=10)

# Task Time
start_check_var = tk.BooleanVar()
start_check_var.set(False)
start_check = ttk.Checkbutton(main_frame, text="Set Start Time", variable=start_check_var, command=toggle_time_entry)
start_check.grid(row=3, column=0, sticky=tk.W, padx=10)

task_start_time = tk.StringVar()
start_entry = ttk.Entry(main_frame, textvariable=task_start_time, state=tk.DISABLED)
start_entry.grid(row=3, column=1, sticky=tk.W, padx=10)

task_end_time = tk.StringVar()
end_entry = ttk.Entry(main_frame, textvariable=task_end_time, state=tk.DISABLED)
end_entry.grid(row=4, column=1, sticky=tk.W, padx=10)

# Task Buttons
add_button = ttk.Button(main_frame, text="Add Task", command=add_task)
add_button.grid(row=5, column=0, padx=10, pady=10)

view_button = ttk.Button(main_frame, text="View Tasks", command=view_tasks)
view_button.grid(row=5, column=1, padx=10, pady=10)

# Task Treeview
task_tree_frame = ttk.Frame(main_frame)
task_tree_frame.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

task_tree = ttk.Treeview(task_tree_frame)
task_tree.pack(side=tk.LEFT)

task_tree_scroll = ttk.Scrollbar(task_tree_frame, orient=tk.VERTICAL, command=task_tree.yview)
task_tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)

task_tree.configure(yscrollcommand=task_tree_scroll.set)

task_tree["columns"] = ("Title", "Description", "Start Time", "End Time")
task_tree.column("#0", width=0, stretch=tk.NO)
task_tree.column("Title", anchor=tk.W, width=150)
task_tree.column("Description", anchor=tk.W, width=200)
task_tree.column("Start Time", anchor=tk.W, width=100)
task_tree.column("End Time", anchor=tk.W, width=100)

task_tree.heading("#0", text="", anchor=tk.W)
task_tree.heading("Title", text="Title", anchor=tk.W)
task_tree.heading("Description", text="Description", anchor=tk.W)
task_tree.heading("Start Time", text="Start Time", anchor=tk.W)
task_tree.heading("End Time", text="End Time", anchor=tk.W)

# Task Buttons
delete_button = ttk.Button(main_frame, text="Delete Task", command=delete_task)
delete_button.grid(row=7, column=0, padx=10, pady=10)

complete_button = ttk.Button(main_frame, text="Mark Complete", command=mark_task_complete)
complete_button.grid(row=7, column=1, padx=10, pady=10)

# Show Calendar Button
calendar_button = ttk.Button(main_frame, text="Select Date", command=show_calendar)
calendar_button.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
