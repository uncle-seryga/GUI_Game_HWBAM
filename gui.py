import tkinter

class Colors:
    background = "#b20000"
    text_big = "#0096FF"
    text_small = "#0A2647"
    contrast_low = "#144272"
    contrast_high = "#2C74B3"


class Fonts:
    def __init__(self, font_type, font_size):
        self.ft = font_type
        self.fs = font_size

    def __str__(self):
        return f"{self.ft} {self.fs}"

title = Fonts('Arial', '22')
subtitle = Fonts('Arial', '18')

window = tkinter.Tk()
window.configure(bg=Colors.background)
label0 = tkinter.Label(text="My little password", foreground=Colors.text_big, background=Colors.background, font=title)
label1 = tkinter.Label(text="Login", foreground=Colors.text_big, background=Colors.background, font=subtitle)
label2 = tkinter.Label(text="Password", foreground=Colors.text_big, background=Colors.background, font=subtitle)
entry1 = tkinter.Entry(background="green", border=0)
entry2 = tkinter.Entry(background="green", border=0)
button = tkinter.Button(background="yellow", foreground=Colors.text_big, font=subtitle, text="Submit", border=0, borderwidth=0)

label0.pack()
label1.pack()
entry1.pack()
label2.pack()
entry2.pack()
button.pack()
window.mainloop()