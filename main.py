import random
from tkinter import *


# кнопка Отправить
def asked():
    get_question = question.get()
    if is_valid(get_question):
        # система генерирует ответ
        n = random.randint(0, 20)
        print('Рандом-', n)
        answers = ['Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определённо да', 'Можешь быть уверен в этом',
                   'Мне кажется - да', 'Вероятнее всего', 'Хорошие перспективы', 'Знаки говорят - да', 'Да',
                   'Пока неясно, попробуй снова', 'Спроси позже', 'Не стоит', 'Сейчас нельзя предсказать',
                   'Спроси опять', 'Даже не думай', 'Мой ответ - нет', 'По моим данным - нет', 'Перспективы не очень '
                   'хорошие', 'Весьма сомнительно']
        lbl.configure(
            text="Ответ на твой вопрос:\n\n" + answers[n] + '\n\n\n\nВы можете задать другой вопрос\n или выйти'
                                                            ' из игры', padx="50", pady="8")
        btn_cancel.grid(column=1, row=7)
    else:
        lbl.configure(text="Вы ввели некорректный вопрос.\nВведите вопрос корректно")


def is_valid(phrase):
    if len(phrase) > 1:
        return True
    else:
        return False


def leave():
    window.quit()


window = Tk()
window.title("Приложение Magic Ball")
window.config(bg='bisque')
window.geometry('350x250')
lbl = Label(window, text="Привет,меня зовут Юля!\nПредлагаю тебе окунуться в мир магии и волшебства.\n\n"
                         " Эта программа предсказывает будущее! \n\n"
                         " Задай мне любой вопрос", font=("Arial", 10), bg='bisque', padx="10", pady="18")
lbl.grid(column=1, row=1)
question = Entry(window)
question.grid(column=1, row=2)
btn_ask = Button(window, text="Отправить", bg="light blue", fg="grey26", command=asked)
btn_ask.grid(column=1, row=3, padx="5", pady="5")
btn_cancel = Button(window, text="Выйти из игры", bg="light blue", fg="grey26", command=leave)
window.mainloop()
