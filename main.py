from pywebio.input import *
from pywebio.output import *
from pywebio import start_server
import random

async def main():
    clear()
    min_num = await input("Введите минимальное число")
    max_num = await input("Введите максимальное число")
    tried = []
    num = random.randint(int(min_num),int(max_num))
    win = False
    while win == False:
        num_inp = await input("Угадайте число")
        if int(num_inp) > int(num):
            clear()
            put_text("Число меньше")
            tried.append(num_inp)
        elif int(num_inp) < int(num):
            clear()
            put_text("Число больше")
            tried.append(num_inp)
        if int(num_inp) == int(num):
            clear()
            put_text(f"Победа! число:{num}")
            put_text(f"Не удачные попытки:{tried}")
            put_text(f"Количество неудачных попыток:{len(tried)}")
            win = True
            put_button("Play again",onclick=main)
if __name__ == "__main__":
    start_server(main,port=8080,debug=True,cdn=False)