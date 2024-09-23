import textwrap
from PIL import Image, ImageDraw, ImageFont
from random import choice

with open('newd.txt', 'r') as fp:
    data = fp.read().split('\n')
    wrapper = textwrap.TextWrapper(width=20)

    for student in data:
        color = choice([(255, 0, 153), (22, 252, 236)])
        img = Image.open('fp-1.png') # replace fp-1.png with your template image 
        img = img.convert('RGB')
        f = ImageDraw.Draw(img)
        fnt = ImageFont.truetype("comicbd.ttf", 48)
        rollno, name = student.split(',')
        a = wrapper.fill(text=name)
        la = a.split('\n')

        if len(la) == 1:
            fnt = ImageFont.truetype("comicbd.ttf", 54)
            f.text((119, 687), f'{a: ^26}', font=fnt, fill=color)
        else:
            f.text((119, 680), f'{la[0]: ^29}', font=fnt, fill=color) 
            f.text((119, 740), f'{la[1]: ^39}', font=fnt, fill=color)
        img.save(f'freshers aim/{rollno}.png')

# (255, 0, 153), (22, 252, 236)
