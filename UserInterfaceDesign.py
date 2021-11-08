# from tkinter import *
#
#
# def LoginPage():
#     # Root Frame
#     root.title("Test Interface")
#     canvas = root()
#     UserLabel = Label(root, text="Username")
#     UserLabel.grid(row=0, column=2)
#     # Username Entry Box
#     eUser = Entry(root, width=100, borderwidth=5)
#     eUser.grid(row=1, column=1, columnspan=3, padx=10, pady=10)
#     # Username Entry Box
#     ePass = Entry(root, width=100, borderwidth=5)
#     ePass.grid(row=1, column=1, columnspan=3, padx=10, pady=10)
#     # Button Initiation
#     EnterButton = Button(root, text="Login", padx=40, pady=20, command=AuthUser)
#
# def DevPage():
#     # Root Frame
#     root.title("Test Interface")
#     UserLabel = Label(root, text="Username")
#     UserLabel.grid(row=0, column=2)
#     # Username Entry Box
#     eUser = Entry(root, width=100, borderwidth=5)
#     eUser.grid(row=1, column=1, columnspan=3, padx=10, pady=10)
#     # Username Entry Box
#     ePass = Entry(root, width=100, borderwidth=5)
#     ePass.grid(row=1, column=1, columnspan=3, padx=10, pady=10)
#     # Button Initiation
#     EnterButton = Button(root, text="Login", padx=40, pady=20, command=AuthUser)
#
#
# # Button Function
def AuthUser():
    Label1 = tk.Label(root, text="Login Accepted")
    Label2 = tk.Label(root, text="Login Denied")
    Label1.grid(row=7,column=3)
    Label2.grid(row=8,column=3)

#
#
# def changepage():
#     global pagenum, root
#     for widget in root.winfo_children():
#         widget.destroy()
#     if pagenum == 1:
#         DevPage(root)
#         pagenum = 2
#     else:
#         LoginPage()
#         pagenum = 1
#
#
# pagenum = 1
# # Root Frame
# root = Tk()
# LoginPage()
#
# root.mainloop()


import tkinter as tk


def LoginPage(root):
    # Username Label
    UserLabel = tk.Label(root, text="Username")
    UserLabel.grid(row=0, column=3)
    # Username Entry Box
    eUser = tk.Entry(root, width=100, borderwidth=5)
    eUser.grid(row=1, column=2, columnspan=3, padx=10, pady=10)
    # Password Label
    PassLabel = tk.Label(root, text="Password")
    PassLabel.grid(row=2, column=3)
    # Password Entry Box
    ePass = tk.Entry(root, width=100, borderwidth=5)
    ePass.grid(row=3, column=2, columnspan=3, padx=10, pady=10)
    # Button Initiation
    EnterButton = tk.Button(root, text="Login", padx=40, pady=20, command=AuthUser)
    EnterButton.grid(row=4, column=3)



def page2(root):
    page = tk.Frame(root)
    page.grid()
    tk.Label(page, text='This is page 2').grid(row=0)
    tk.Button(page, text='To page 1', command=changepage).grid(row=1)


def changepage():
    global PageNum, root
    for widget in root.winfo_children():
        widget.destroy()
    if PageNum == 1:
        page2(root)
        PageNum = 2
    else:
        LoginPage(root)
        PageNum = 1


PageNum = 1
root = tk.Tk()
root.title("Test Interface")
root.geometry("700x300")
LoginPage(root)
root.mainloop()
