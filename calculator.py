import tkinter as tk

def click(button_text):
    if button_text == "=":
        try:
            result = str(eval(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

root = tk.Tk()
root.title("Python Calculator")

entry = tk.Entry(root, width=20, font=("Times New Roman", 16))
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    "7", "8", "9", "+",
    "4", "5", "6", "-",
    "1", "2", "3", "*",
    "C", "0", "=", "/"
]

row, col = 1, 0
for b in buttons:
    tk.Button(root, text=b, width=5, height=2, font=("Times New Roman", 14),
              command=lambda x=b: click(x)).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
