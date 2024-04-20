from tkinter import *
from tkinter import ttk

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def mod(a, b):
    return a % b

def lcm(a, b):
    L = a if a > b else b
    while L <= a * b:
        if L % a == 0 and L % b == 0:
            return L
        L += 1

def hcf(a, b):
    H = a if a < b else b
    while H >= 1:
        if a % H == 0 and b % H == 0:
            return H
        H -= 1

def extract_from_text(text):
    l = []
    for t in text.split(' '):
        try:
            l.append(float(t))
        except ValueError:
            pass
    return l

def calculate():
    text = textin.get().strip()
    if not text:
        result.config(text="Please enter an expression")
        return
    for word in text.split(' '):
        if word.upper() in operations.keys():
            try:
                l = extract_from_text(text)
                r = operations[word.upper()](l[0], l[1])
                result.config(text=str(r))
            except Exception as e:
                result.config(text="Error: " + str(e))
            finally:
                break
        elif word.upper() not in operations.keys():
            result.config(text="Invalid expression")

def clear():
    textin.set("")
    result.config(text="Cleared")

def on_enter(event=None):
    calculate()

operations = {'ADD': add, 'ADDITION': add, 'SUM': add, 'PLUS': add,
              'SUB': sub, 'DIFFERENCE': sub, 'MINUS': sub, 'SUBTRACT': sub,
              'LCM': lcm, 'HCF': hcf, 'PRODUCT': mul, 'MULTIPLICATION': mul,
              'MULTIPLY': mul, 'DIVISION': div, 'DIV': div, 'DIVIDE': div, 'MOD': mod,
              'REMANDER': mod, 'MODULUS': mod}

win = Tk()
win.geometry('400x300')
win.title('Smart Calculator')

# Background Gradient
background_gradient = Canvas(win, width=400, height=300, bd=0, highlightthickness=0)
background_gradient.create_rectangle(0, 0, 400, 150, fill="#4CAF50", outline="")
background_gradient.create_rectangle(0, 150, 400, 300, fill="#333333", outline="")
background_gradient.pack()

style = ttk.Style()
style.configure('TButton', foreground='black', background='#ffffff', font=('Arial', 10, 'bold'))
style.configure('TEntry', foreground='black', background='#ffffff', font=('Arial', 10))

title_label = Label(win, text='Smart Calculator', font=('Arial', 16, 'bold'), bg='#4CAF50', fg='white', pady=10)
title_label.place(x=100, y=20, width=200)

input_frame = Frame(win, bg='#ffffff')
input_frame.place(x=50, y=80, width=300, height=40)

input_label = Label(input_frame, text='Enter expression:', bg='#ffffff', font=('Arial', 10))
input_label.place(x=10, y=10)

textin = StringVar()
entry = ttk.Entry(input_frame, width=30, textvariable=textin)
entry.place(x=130, y=10)
entry.bind('<Return>', on_enter)

calculate_button = ttk.Button(win, text='Calculate', command=calculate)
calculate_button.place(x=100, y=140, width=100)

result = Label(win, width=20, bg='#ffffff', relief='ridge', font=('Arial', 12), pady=5)
result.place(x=100, y=180)

clear_button = ttk.Button(win, text='Clear', command=clear)
clear_button.place(x=210, y=140, width=100)

win.mainloop()
