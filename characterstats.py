import tkinter as tk

def increase():
    value = int(lbl_value["text"])
    value = value + 1
    lbl_value["text"] = str(value)

def decrease():
    value = int(lbl_value["text"])
    value = value - 1
    lbl_value["text"] = str(value)

window = tk.Tk()
window.rowconfigure([0, 1], minsize=50, weight=1)
window.columnconfigure([0, 1, 2], minsize=100, weight=1)

lbl_title = tk.Label(master=window, text="Character Strength:")
lbl_title.grid(row=0, column=0, columnspan=3)

btn_drecrease = tk.Button(master=window, text="-", command=decrease)
btn_drecrease.grid(row=1, column=0)

lbl_value = tk.Label(master=window, text="0")
lbl_value.grid(row=1, column=1)

btn_increase = tk.Button(master=window, text="+", command=increase)
btn_increase.grid(row=1, column=2)




window.mainloop()

