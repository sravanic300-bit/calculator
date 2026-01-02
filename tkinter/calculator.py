import tkinter as tk

# Function to update expression
def press(key):
    entry_var.set(entry_var.get() + str(key))

# Function to evaluate expression
def calculate():
    try:
        result = eval(entry_var.get())
        entry_var.set(result)
        entry.config(bg="#d4edda")   # green output for success
    except:
        entry_var.set("Error")
        entry.config(bg="#f8d7da")   # red output for error

# Function to clear screen
def clear():
    entry_var.set("")
    entry.config(bg="white")

# Main window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.configure(bg="#2c2f33")
root.resizable(False, False)

entry_var = tk.StringVar()

# Display
entry = tk.Entry(
    root,
    textvariable=entry_var,
    font=("Arial", 20),
    bd=10,
    relief=tk.RIDGE,
    justify="right",
    bg="white",
    fg="black"
)
entry.pack(fill="x", padx=10, pady=10)

# Button frame
frame = tk.Frame(root, bg="#2c2f33")
frame.pack()

# Button layout
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

row = 0
col = 0

for btn in buttons:
    # Operator colors
    if btn in ["+", "-", "*", "/"]:
        bg_color = "#7289da"
        fg_color = "white"
    elif btn == "=":
        bg_color = "#43b581"
        fg_color = "white"
    else:
        bg_color = "#99aab5"
        fg_color = "black"

    action = calculate if btn == "=" else lambda x=btn: press(x)

    tk.Button(
        frame,
        text=btn,
        width=5,
        height=2,
        font=("Arial", 14),
        bg=bg_color,
        fg=fg_color,
        activebackground="#ffffff",
        command=action
    ).grid(row=row, column=col, padx=5, pady=5)

    col += 1
    if col > 3:
        col = 0
        row += 1

# Clear button
tk.Button(
    root,
    text="Clear",
    font=("Arial", 14),
    bg="#f04747",
    fg="white",
    activebackground="#ff6b6b",
    command=clear
).pack(fill="x", padx=10, pady=10)

root.mainloop()
