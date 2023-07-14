import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from ttkthemes import ThemedStyle
import os 


def search_assets(event=None):
    asset_input = asset_entry.get().upper()

    result_text.delete(1.0, tk.END)

    try:
        # Load dataframes if not already loaded
        if 'df1' not in globals():
            globals()['df1'] = pd.read_excel('VSE_TOOL_KIT_REPORT.xlsx', usecols='A,B,E')
        if 'df2' not in globals():
            globals()['df2'] = pd.read_excel('VSE_TOOLS_REPORT.xlsx', usecols='A,B,E')

        # Search in df1
        df1_filtered = globals()['df1'][globals()['df1']['ASSET #'] == asset_input]

        if not df1_filtered.empty:
            result_text.insert(tk.END, "Tool Kit:\n")
            result_text.insert(tk.END, str(df1_filtered) + "\n")
        else:
            result_text.insert(tk.END, "No matching rows found in Excel file 1.\n")
            return  # Skip caching if no match found

        # Search in df2
        loc_input = asset_input.replace('F', '')
        df2_filtered = globals()['df2'][globals()['df2']['LOC'] == loc_input]

        if not df2_filtered.empty:
            result_text.insert(tk.END, "Tools:\n")
            result_text.insert(tk.END, str(df2_filtered) + "\n")
        else:
            result_text.insert(tk.END, "No matching rows found in Excel file 2.\n")
            return  # Skip caching if no match found

        # Add search to history
        add_to_history(asset_input)

        # Cache the dataframes
        cache_dataframes()

    except FileNotFoundError:
        messagebox.showerror("File Not Found", "Excel file not found. Please enter a valid file name.")

def add_to_history(asset_input):
    # Add search to history list
    if asset_input not in history_list:
        history_list.append(asset_input)
        if len(history_list) > 5:
            history_list.pop(0)
        update_history_menu()

def update_history_menu():
    # Clear history menu
    history_menu.delete(0, tk.END)

    # Add history items to menu
    for asset in history_list:
        history_menu.add_command(label=asset, command=lambda x=asset: perform_history_search(x))

def perform_history_search(asset):
    asset_entry.delete(0, tk.END)
    asset_entry.insert(tk.END, asset)
    search_assets()

def clear_history_menu():
    history_menu.delete(0, tk.END)
    history_list.clear()

def open_preferences():
    messagebox.showinfo("Preferences", "Here you can set your preferences.")

def change_theme(theme):
    if theme == "dark_mode":
        root.config(bg="#1E1E1E")
        style.configure("TLabel",
                        foreground="white",
                        background="#1E1E1E")
        style.configure("TButton",
                        foreground="white",
                        background="#1E1E1E")
        style.configure("TEntry",
                        foreground="white",
                        background="#1E1E1E")
        style.configure("TCombobox",
                        foreground="white",
                        background="#1E1E1E")
        style.configure("TMenubutton",
                        foreground="white",
                        background="#1E1E1E")
        style.configure("TText",
                        foreground="white",
                        background="#1E1E1E",
                        font=("TkDefaultFont", 10, "bold"))  # Set the font to bold
        result_text.configure(foreground="white", background="#1E1E1E", font=("TkDefaultFont", 10, "bold"))  # Set the font to bold
        asset_entry.configure(foreground="white")
        search_button.configure(foreground="white", background="#333333")
        quit_button.configure(foreground="white", background="#333333")
    else:
        style.set_theme(theme)
        root.config(bg="white")
        result_text.configure(foreground="black", background="white", font=("TkDefaultFont", 10))  # Set the font to default
        asset_entry.configure(foreground="black")
        search_button.configure(foreground="black", background="white")
        quit_button.configure(foreground="black", background="white")

    update_color_theme_checkmarks()


def update_color_theme_checkmarks():
    # Clear all checkmarks
    for i in range(color_themes_menu.index("end")):
        label = color_themes_menu.entrycget(i, "label")
        if label.startswith("✓ "):
            color_themes_menu.entryconfig(i, label=label[2:])

    # Add checkmark to selected theme
    selected_theme = style.theme_use()
    for i in range(color_themes_menu.index("end")):
        label = color_themes_menu.entrycget(i, "label")
        if label == selected_theme:
            color_themes_menu.entryconfig(i, label="✓ " + label)

def zoom_in():
    result_text.config(font=(current_font_family, current_font_size + 1, "bold"))


def zoom_out():
    result_text.config(font=(current_font_family, current_font_size - 1, "bold"))


def change_font(font_family):
    global current_font_family
    current_font_family = font_family
    result_text.config(font=(current_font_family, current_font_size, "bold" if dark_mode_var.get() else "normal"))


def on_key_press(event):
    if event.keysym == "plus" and (event.state & 0x4) != 0:
        zoom_in()
    elif event.keysym == "minus" and (event.state & 0x4) != 0:
        zoom_out()


root = tk.Tk()
root.title("Asset Search")

# Use Visual Studio Code-like theme
style = ThemedStyle(root)
style.set_theme("equilux")

# Menubar
menubar = tk.Menu(root)
root.config(menu=menubar)

# Preferences Menu
preferences_menu = tk.Menu(menubar, tearoff=0)

# Color Themes Submenu
color_themes_menu = tk.Menu(preferences_menu, tearoff=0)
color_themes_menu.add_command(label="Default", command=lambda: change_theme("default"))
color_themes_menu.add_command(label="Equilux", command=lambda: change_theme("equilux"))
color_themes_menu.add_command(label="Arc", command=lambda: change_theme("arc"))
color_themes_menu.add_command(label="Plastik", command=lambda: change_theme("plastik"))
color_themes_menu.add_command(label="Adapta", command=lambda: change_theme("adapta"))
color_themes_menu.add_command(label="Black", command=lambda: change_theme("black"))
color_themes_menu.add_command(label="Blue", command=lambda: change_theme("blue"))
color_themes_menu.add_command(label="Clearlooks", command=lambda: change_theme("clearlooks"))
color_themes_menu.add_command(label="Winxpblue", command=lambda: change_theme("winxpblue"))
color_themes_menu.add_command(label="Radiance", command=lambda: change_theme("radiance"))
color_themes_menu.add_command(label="Dark Mode", command=lambda: change_theme("dark_mode"))
preferences_menu.add_cascade(label="Color Themes", menu=color_themes_menu)

# Fonts Submenu
fonts_menu = tk.Menu(preferences_menu, tearoff=0)
fonts_menu.add_command(label="Arial", command=lambda: change_font("Arial"))
fonts_menu.add_command(label="Times New Roman", command=lambda: change_font("Times New Roman"))
fonts_menu.add_command(label="Courier New", command=lambda: change_font("Courier New"))
fonts_menu.add_command(label="Calibri", command=lambda: change_font("Calibri"))
preferences_menu.add_cascade(label="Fonts", menu=fonts_menu)

# Zoom Submenu
zoom_menu = tk.Menu(preferences_menu, tearoff=0)
zoom_menu.add_command(label="Zoom In", command=zoom_in)
zoom_menu.add_command(label="Zoom Out", command=zoom_out)
preferences_menu.add_cascade(label="Zoom", menu=zoom_menu)

menubar.add_cascade(label="Preferences", menu=preferences_menu)

# Asset Entry
asset_label = ttk.Label(root, text="Asset #:")
asset_label.pack()
asset_entry = ttk.Entry(root)
asset_entry.pack()

# Bind Enter key press event to search_assets function
root.bind('<Return>', search_assets)

# Search Button
search_button = ttk.Button(root, text="Search", command=search_assets)
search_button.pack()

# Result Text
result_text = tk.Text(root, height=20)
result_text.pack()

# Set initial font values
current_font_family = "Arial"
current_font_size = 10

# Configure initial font
result_text.config(font=(current_font_family, current_font_size, "bold"))

# Dark Mode Variable
dark_mode_var = tk.BooleanVar(value=False)


def toggle_dark_mode():
    dark_mode_enabled = dark_mode_var.get()

    if dark_mode_enabled:
        style.configure("TLabel", foreground="white", background="#1E1E1E", font="bold")
        style.configure("TButton", foreground="white", background="#1E1E1E", font="bold")
        style.configure("TEntry", foreground="white", background="#1E1E1E", font="bold")
        style.configure("TCombobox", foreground="white", background="#1E1E1E", font="bold")
        style.configure("TMenubutton", foreground="white", background="#1E1E1E", font="bold")
        style.configure("TText", foreground="white", background="#1E1E1E", font="bold")
        result_text.config(foreground="white", background="#1E1E1E", font=(current_font_family, current_font_size, "bold"))
    else:
        style.configure("TLabel", font="")
        style.configure("TButton", font="")
        style.configure("TEntry", font="")
        style.configure("TCombobox", font="")
        style.configure("TMenubutton", font="")
        style.configure("TText", font="")
        result_text.config(foreground="black", background="white", font=(current_font_family, current_font_size, "normal"))


# Dark Mode Checkbutton
dark_mode_checkbutton = ttk.Checkbutton(root, text="Dark Mode", variable=dark_mode_var, command=toggle_dark_mode)
dark_mode_checkbutton.pack()

# History Menu
history_list = []
history_menu = tk.Menu(menubar, tearoff=0)
history_menu.add_command(label="Clear History", command=clear_history_menu)
menubar.add_cascade(label="History", menu=history_menu)

# Quit Button
quit_button = ttk.Button(root, text="Quit", command=root.quit)
quit_button.pack(side=tk.BOTTOM, pady=10)

# Update color theme checkmarks
update_color_theme_checkmarks()

root.bind('<KeyPress>', on_key_press)
root.mainloop()

