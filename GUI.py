from tkinter import messagebox
import tkinter


def clickMe():
    messagebox.showinfo("Button Clicked", str.get())

window = tkinter.Tk()
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 200
X = window.winfo_screenwidth() // 2 - WINDOW_WIDTH // 2
Y = window.winfo_screenheight() // 2 - WINDOW_HEIGHT // 2

window.title('Client')
window.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{X}+{Y}')
window.resizable(False, False)




frame1=tkinter.Frame(window, bd=2)
frame1.pack(side="left", fill="both", expand=True)

frame2=tkinter.Frame(window, bd=2)
frame2.pack(side="right", fill="both", expand=True)


label = tkinter.Label(window, text='사번')
label.pack(side="left")

entry=tkinter.Entry(window, width=30)
entry.pack(side="right")

button = tkinter.Button(window, overrelief="solid", width=10, text='등록')
button.pack(side="bottom")

window.mainloop()