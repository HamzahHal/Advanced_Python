from tkinter import *

# Root Frame
root = Tk()
root.title("Test Interface")
UserLabel = Label(root, text="Username")
UserLabel.grid(row=0,column=2,)

# Entry Box
eUser = Entry(root, width=100, borderwidth=5)
eUser.grid(row=1, column=1, columnspan=3, padx=10, pady=10)


# Button Function
def DbInput():
    pass


# Button Initiation
EnterButton = Button(root, text="1", padx=40, pady=20, command=DbInput)


def myClick():
    pass


myButton = Button(root, text="Enter User", command=myClick)

root.mainloop()
