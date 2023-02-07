import tkinter

class Colors:
    background = "#2d0087"
    background_wins = "#12674A"
    background_lose = "#BB2649"
    text_big = "#fac739"
    text_small = "#0A2647"
    contrast_low = "#144272"
    contrast_high = "fac739"

class Fonts:
    def __init__(self, font_type, font_size):
        self.ft = font_type
        self.fs = font_size

    def __str__(self):
        return f"{self.ft} {self.fs}"

class ButtonSize:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # def __int__(self):
    #     return self.size

standart_button = ButtonSize(12, 3)
font_main = Fonts('Arial', 20)
font_big_text = Fonts('Arial', 28)