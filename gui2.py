import tkinter

import game
from settings import Colors, standart_button, font_main, font_big_text


class Button:
    def action(self):
        if data.check_answer(self.text):
            root['background'] = Colors.background_wins
            label_question['background'] = Colors.background_wins
        else:
            root['background'] = Colors.background_lose
            label_question['background'] = Colors.background_lose



    def __init__(self, text):
        self.text = text

    def create(self):
        obj = tkinter.Button(text=self.text, background=Colors.text_big, border=2, borderwidth=2,
                             width=standart_button.width,
                             height=standart_button.height, font=font_main, activebackground=Colors.text_big,
                             activeforeground="white", command=self.action)
        return obj


root = tkinter.Tk()
root.geometry("640x480")
root.resizable(width=False, height=False)
root.configure(background=Colors.background)

label_score = tkinter.Label(text="")

data = game.Game()
label_question = tkinter.Label(text=data.get_question(), font=font_big_text, background=Colors.background,
                               foreground=Colors.text_big)

but1 = Button(data.get_answers()[0][0]).create()
but2 = Button(data.get_answers()[1][0]).create()
but3 = Button(data.get_answers()[2][0]).create()
but4 = Button(data.get_answers()[3][0]).create()

but1.bind('<Button-1>')
but2.bind('<Button-1>')
but3.bind('<Button-1>')
but4.bind('<Button-1>')

label_question.place(anchor="n", relx=0.5, rely=0.3)
but1.place(relx=.27, rely=.6, anchor="center", relwidth=0.45, relheight=0.2)
but2.place(relx=.72, rely=.6, anchor="center", relwidth=0.45, relheight=0.2)
but3.place(relx=.27, rely=.8, anchor="center", relwidth=0.45, relheight=0.2)
but4.place(relx=.72, rely=.8, anchor="center", relwidth=0.45, relheight=0.2)

root.mainloop()
