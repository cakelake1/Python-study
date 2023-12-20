import os
from PIL import Image, ImageDraw, ImageColor
# def convert_image(current_ext, new_ext):
#     for file in os.listdir(os.getcwd()):
#         if file.endswith(current_ext):
#             im = Image.open(file)
#             im.save(file.replace(current_ext, new_ext))
# convert_image('.jpg', '.jpeg')


def convert_image(current_ext, new_ext):
    for file in os.listdir(os.getcwd()):
        if file.endswith(current_ext):
            im = Image.open(file)
            #draw = ImageDraw.Draw(im)
            sz = im.size
            print(im.size)
            draw = ImageDraw.Draw(im)
            #rsz = im.resize((1920,1080))
            #draw = ImageDraw.Draw(rsz)
            draw.rectangle(((50, 50), (100, 100)), fill=128, width=4)
            #draw.multiline_text( 'Hello,\nWorld!', align='center', font_size=40)
            im.show()
            #rgb_im = im.convert('RGB')
            #rgb_im.save(file.replace(current_ext, new_ext))
convert_image('.jpeg', '.png')

