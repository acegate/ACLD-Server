from tkinter import messagebox
import tkinter


def clickMe():
    messagebox.showinfo("Button Clicked", str.get())

window = tkinter.Tk()
WINDOW_WIDTH = 720
WINDOW_HEIGHT = 500
X = window.winfo_screenwidth() // 2 - WINDOW_WIDTH // 2
Y = window.winfo_screenheight() // 2 - WINDOW_HEIGHT // 2

window.title('Client')
window.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{X}+{Y}')
window.resizable(False, False)

label = tkinter.Label(window, text='HOST', justify='left')
label.pack()

label = tkinter.Label(window, text='포트번호', anchor='ne')
label.pack()


button = tkinter.Button(window, overrelief="solid", width=15, text='버튼', repeatdelay=1000, repeatinterval=100)
button.pack()


window.mainloop()