# Рефлексия:
# В эталонном решении, конечно по хитрому взят поиск из предыдущего решения. Но так как в предыдущей рефлексии я пообещал себе разобраться в своем решении и посмотреть, как можно его улучшить и упростить, глядя на эталонное решение. С уверенностью это сделал.
# Я думаю за счет текущей задачи у меня открывается понимание выполнения решений, стало немного проще на душе и в коде.

# Задания:
    # 3.1. Напишите программу, которая получает на вход два типа (расширения) графических форматов, находит в текущем каталоге все графические файлы, соответствующие первому расширению, и конвертирует их в графический формат по второму расширению:

import os
from PIL import Image, ImageDraw, ImageColor
def convert_image(current_ext, new_ext):
    for file in os.listdir(os.getcwd()):
        if file.endswith(current_ext):
            im = Image.open(file)
            im.save(file.replace(current_ext, new_ext))
convert_image('.jpg', '.jpeg')

    # 3.2. Дополните предыдущую функцию рисованием в центре изображения незаполненного квадрата, внутри которого будут написаны две строчки (вторая с новой строки):
def convert_image(current_ext, new_ext):
    for file in os.listdir(os.getcwd()):
        if file.endswith(current_ext):
            im = Image.open(file)
            draw = ImageDraw.Draw(im)
            square_size = 200
            square_left = (im.width - square_size) // 2
            square_top = (im.height - square_size) // 2
            draw.rectangle([square_left, square_top, square_left + square_size, square_top + square_size], width=10)
            draw.multiline_text((square_left + 40, square_top + 40), 'Hello,\nWorld!', align='center', font_size=40)
            rgb_im = im.convert('RGB')
            rgb_im.save(file.replace(current_ext, new_ext))
            del draw
convert_image('.png', '.jpg')

