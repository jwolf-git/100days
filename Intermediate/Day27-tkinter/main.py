from tkinter import *
FONT = ("Ariel", 10)

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20,  pady=20)

input_bar = Entry(width=8)
input_bar.grid(column=1, row=0)

miles_label = Label(text="Miles", font=FONT)
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to", font=FONT)
equal_label.grid(column=0, row=1)

out_label = Label(text="0", font=FONT)
out_label.grid(column=1, row=1)

km_label = Label(text="Km", font=FONT)
km_label.grid(column=2, row=1)


def calculate():
    result = round(float(input_bar.get()) * 1.609344, 2)
    out_label.config(text=result)


calc_button = Button(text="Calculate", font=FONT, command=calculate)
calc_button.grid(column=1, row=2)


window.mainloop()

