import tkinter as tk

bg_colour = '#3d6466'

root = tk.Tk()
root.title("Calculator")
root.eval("tk::PlaceWindow . center")

frame = tk.Frame(root, width=300, height=400, bg='#3d6466')
frame.grid(row=0, column=0, columnspan=4)

#widgets
tk.Label(frame, text="Standard Calculator",
        bg=bg_colour,
        fg='white',
        font = ("TkMenuFont", 20)
        ).grid(row=0, column=0, columnspan=4)

input_var = tk.StringVar()
entry = tk.Entry(frame, textvariable=input_var, fg='white', bg = '#4a7074', width=45, justify='right', borderwidth=5)
entry.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

def button_clear():
    input_var.set('')

def button_click(number):
    current = input_var.get()
    input_var.set(current + str(number))

def calculate_result():
    try:
        result = eval(entry.get())
        entry.delete(0, 'end')
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, 'end')
        entry.insert(0, "Error")

buttons = [
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('+', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('*', 4, 3),
    ('0', 5, 1), ('CE', 5, 2), ('=', 5, 3), ('/', 5, 0)
]

for (text, row, column) in buttons:
    if text == 'CE':
        button = tk.Button(root, text=text, padx=10, pady=10, width=5, height=2, command=button_clear)
    elif text == '=':
        button = tk.Button(root, text=text, padx=10, pady=10, width=5, height=2, command=calculate_result)
    else:
        button = tk.Button(root, text=text, padx=10, pady=10, width=5, height=2, command=lambda t=text: button_click(t))
    button.grid(row=row, column=column, padx=5, pady=5) 

root.mainloop()