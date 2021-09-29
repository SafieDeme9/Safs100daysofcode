import tkinter as tk

cal = tk.Tk()

cal.title("Calculatrice")

buttons = [
    'C','()','%','/',
    '7','8','9','*',
    '4','5','6','-',
    '1','2','3','+',
    '+/-','0','.','='
]

row = 1
col =0

for i in buttons:
    button_style = 'raised'
    action = lambda x = i: click_event(x)
    tk.Button(cal, text = i, width = 7, height = 7, relief = button_style, command = action) \
		.grid(row = row, column = col, sticky = 'nesw', )
    col += 1
    if col > 3:
        col = 0
        row += 1

display = tk.Entry(cal, width = 40, bg = "white")
display.grid(row = 0, column = 0, columnspan = 4)

def click_event(key):

    if key == '=':
        if '/' in display.get() and '.' not in display.get():
            display.insert(tk.END, ".0")
        
        try:
            result = eval(display.get())
            display.insert(tk.END, " = " + str(result))
        except:
            display.insert(tk.END, " Erreur")

    elif key == 'C':
        display.delete(0, tk.END)

    elif key == '+/-':
        if '=' in display.get():
            display.delete(0, tk.END)
        try:
            if display.get()[0] == '-':
                display.delete(0)
            else:
                display.insert(0, '-')
        except IndexError:
            pass

	# clear display and start new input		
    else:
        if '=' in display.get():
            display.delete(0, tk.END)
        display.insert(tk.END, key)

cal.mainloop()