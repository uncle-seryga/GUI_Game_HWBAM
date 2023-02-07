import codecs
import random


class Game:
    def __init__(self):
        with codecs.open("base.json", 'r', "UTF-8") as file:
            self.__data: dict = eval(file.read())
            self.__question = random.choice(list(self.__data.keys()))
            self.__answers = self.__data[self.__question]

    def get_question(self):
        return self.__question

    def get_answers(self):
        return self.__answers

    def check_answer(self, text):
        print(text)
        for answer in self.__answers:
            if answer[0] == str(text):
                return answer[1]
            else:
                pass


