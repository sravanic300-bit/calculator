import tkinter as tk
import math

# ---------------- Window ----------------
root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("430x600")
root.configure(bg="#eae7dc")  # nude background
root.resizable(False, False)

# ---------------- Display ----------------
display = tk.Entry(
    root,
    font=("Arial", 20),
    bg="#fdfcf9",
    fg="#1f2933",
    bd=8,
    relief="sunken",
    justify="right"
)
display.grid(row=0, column=0, columnspan=5, padx=10, pady=15, sticky="nsew")

# ---------------- Functions ----------------
def press(val):
    display.insert(tk.END, val)

def clear():
    display.delete(0, tk.END)

def delete():
    text = display.get()
    display.delete(0, tk.END)
    display.insert(0, text[:-1])

def calculate():
    try:
        expr = display.get()
        expr = expr.replace("×", "*").replace("÷", "/").replace("^", "**")
        result = eval(expr, {
            "__builtins__": None,
            "sin": math.sin,
            "cos": math.cos,
            "tan": math.tan,
            "log": math.log10,
            "ln": math.log,
            "sqrt": math.sqrt,
            "pi": math.pi,
            "e": math.e,
            "abs": abs,
            "factorial": math.factorial
        })
        display.delete(0, tk.END)
        display.insert(0, result)
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

# ---------------- Button Creator ----------------
def btn(txt, r, c, bg, cmd=None, cs=1):
    tk.Button(
        root,
        text=txt,
        font=("Arial", 12, "bold"),
        bg=bg,
        fg="#1f2933",
        relief="raised",
        activebackground="#d6ccc2",
        command=cmd
    ).grid(row=r, column=c, columnspan=cs, padx=4, pady=4, sticky="nsew")

# ---------------- Nude Color Palette ----------------
NUM  = "#f5f1ea"   # numbers
SCI  = "#dbe4e8"   # scientific
OP   = "#e3dac9"   # operators
CTRL = "#e6cfc1"   # control buttons
EQ   = "#cfe1b9"   # equals

# ---------------- Scientific Rows ----------------
btn("abs",1,0,SCI,lambda:press("abs("))
btn("mod",1,1,SCI,lambda:press("%"))
btn("div",1,2,SCI,lambda:press("÷"))
btn("x!",1,3,SCI,lambda:press("factorial("))
btn("e",1,4,SCI,lambda:press("e"))

btn("sin",2,0,SCI,lambda:press("sin("))
btn("cos",2,1,SCI,lambda:press("cos("))
btn("tan",2,2,SCI,lambda:press("tan("))
btn("cot",2,3,SCI,lambda:press("1/tan("))
btn("π",2,4,SCI,lambda:press("pi"))

btn("x²",3,0,SCI,lambda:press("^2"))
btn("x³",3,1,SCI,lambda:press("^3"))
btn("xⁿ",3,2,SCI,lambda:press("^"))
btn("x⁻¹",3,3,SCI,lambda:press("**-1"))
btn("10ˣ",3,4,SCI,lambda:press("10^"))

btn("√",4,0,SCI,lambda:press("sqrt("))
btn("³√",4,1,SCI,lambda:press("**(1/3)"))
btn("y√",4,2,SCI,lambda:press("**(1/"))
btn("log₁₀",4,3,SCI,lambda:press("log("))
btn("ln",4,4,SCI,lambda:press("ln("))

btn("(",5,0,SCI,lambda:press("("))
btn(")",5,1,SCI,lambda:press(")"))
btn("±",5,2,SCI,lambda:press("-"))
btn("%",5,3,SCI,lambda:press("%"))
btn("eˣ",5,4,SCI,lambda:press("e^"))

# ---------------- Numbers & Operators ----------------
btn("7",6,0,NUM,lambda:press("7"))
btn("8",6,1,NUM,lambda:press("8"))
btn("9",6,2,NUM,lambda:press("9"))
btn("DEL",6,3,CTRL,delete)
btn("AC",6,4,CTRL,clear)

btn("4",7,0,NUM,lambda:press("4"))
btn("5",7,1,NUM,lambda:press("5"))
btn("6",7,2,NUM,lambda:press("6"))
btn("×",7,3,OP,lambda:press("×"))
btn("÷",7,4,OP,lambda:press("÷"))

btn("1",8,0,NUM,lambda:press("1"))
btn("2",8,1,NUM,lambda:press("2"))
btn("3",8,2,NUM,lambda:press("3"))
btn("+",8,3,OP,lambda:press("+"))
btn("-",8,4,OP,lambda:press("-"))

btn("0",9,0,NUM,lambda:press("0"))
btn(".",9,1,NUM,lambda:press("."))
btn("EXP",9,2,NUM,lambda:press("e"))
btn("=",9,3,EQ,calculate,cs=2)

# ---------------- Grid Scaling ----------------
for i in range(10):
    root.grid_rowconfigure(i, weight=1)
for j in range(5):
    root.grid_columnconfigure(j, weight=1)

# ---------------- Run ----------------
root.mainloop()