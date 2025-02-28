import tkinter as tk

def evaluate():
    global calculation
    calculation = str(eval(calculation))
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def clear():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")


# CONSTANTS
WIDTH = 400
HEIGHT = 300

window = tk.Tk()
window.geometry(f"{WIDTH}x{HEIGHT}")
window.title("Calculator")

calculation = ""

text_result = tk.Text(window, height=1, font=("Arial", 24), width=20)
text_result.insert(1.0, calculation)
text_result.grid(row=0, column=0, columnspan = 4, sticky="nsew")

btn1 = tk.Button(window, text="1", command= lambda:add_to_calculation(1))
btn1.grid(row=1, column=0, columnspan=1, sticky="nsew")

btn2 = tk.Button(window, text="2", command= lambda:add_to_calculation(2))
btn2.grid(row=1, column=1, columnspan=1, sticky="nsew")

btn3 = tk.Button(window, text="3", command= lambda:add_to_calculation(3))
btn3.grid(row=1, column=2, columnspan=1, sticky="nsew")

btn_plus = tk.Button(window, text="+", command= lambda:add_to_calculation("+"))
btn_plus.grid(row=1, column=3, sticky="nsew")

btn4 = tk.Button(window, text="4", command= lambda:add_to_calculation(4))
btn4.grid(row=2, column=0, columnspan=1, sticky="nsew")

btn5 = tk.Button(window, text="5", command= lambda:add_to_calculation(5))
btn5.grid(row=2, column=1, columnspan=1, sticky="nsew")

btn6 = tk.Button(window, text="6", command= lambda:add_to_calculation(6))
btn6.grid(row=2, column=2, columnspan=1, sticky="nsew")

btn_subtract = tk.Button(window, text="-", command= lambda:add_to_calculation("-"))
btn_subtract.grid(row=2, column=3, sticky="nsew")

btn7 = tk.Button(window, text="7", command= lambda:add_to_calculation(7))
btn7.grid(row=3, column=0, columnspan=1, sticky="nsew")

btn8 = tk.Button(window, text="8", command= lambda:add_to_calculation(8))
btn8.grid(row=3, column=1, columnspan=1, sticky="nsew")

btn9 = tk.Button(window, text="9", command= lambda:add_to_calculation(9))
btn9.grid(row=3, column=2, columnspan=1, sticky="nsew")

btn_multi = tk.Button(window, text="x", command= lambda:add_to_calculation("*"))
btn_multi.grid(row=3, column=3, sticky="nsew")

btnOP = tk.Button(window, text="(", command= lambda:add_to_calculation('('))
btnOP.grid(row=4, column=0, columnspan=1, sticky="nsew")

btn0 = tk.Button(window, text="0", command= lambda:add_to_calculation(0))
btn0.grid(row=4, column=1, columnspan=1, sticky="nsew")

btnCP = tk.Button(window, text=")", command= lambda:add_to_calculation(')'))
btnCP.grid(row=4, column=2, columnspan=1, sticky="nsew")

btn_div = tk.Button(window, text="/", command= lambda:add_to_calculation("/"))
btn_div.grid(row=4, column=3, sticky="nsew")

btn_equals = tk.Button(window, text="=", command=evaluate)
btn_equals.grid(row=5, column=2, columnspan=2, sticky="nsew")

btn_clear = tk.Button(window, text="CE", command=clear)
btn_clear.grid(row=5, column=0, columnspan=2, sticky="nsew")

window.mainloop()