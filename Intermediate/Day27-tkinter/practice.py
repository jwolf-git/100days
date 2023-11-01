from tkinter import *

window = Tk()

window.title("My First GUI Program")
window.minsize(width=500, height=300)

my_label = Label(text="I am a label", font=("Arial", 24))
my_label.grid(row=0, column=0)

def button_clicked():
    print("I got clicked")
    my_label.config(text=input.get())


# Label


button = Button(text="Click Me", command=button_clicked)
button.grid(row=1, column=1)

button_new = Button(text="Don't Click me")
button.grid(row=0, column=2)

input = Entry(width=10)
input.grid(row=2, column=3)
input.get()

window.mainloop()

# def add(*args):
#     result = 0
#     for n in args:
#         result += n
#     return result
#
# print(add(3, 5, 6))
