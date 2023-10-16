import qrcode
from PIL import Image, ImageDraw, ImageFont

with open('listl.txt', 'r') as fp:
    data = fp.read().split('\n')
    for i in range(0, len(data)-3, 4):
        s1 = data[i:i + 4]
        qrcode.QRCode(version=1, border=2, box_size=2)
        kkk = []
        for k1, k in enumerate(s1):
            z = k.split(',')
            kkk += [z[0]]
            img = qrcode.make(f'{z[1]}')
            img.save(f'myqr{k1}.png')

        img1 = Image.open('bhk-1.png')
        img2 = Image.open('myqr0.png')
        img3 = Image.open('myqr1.png')
        img4 = Image.open('myqr2.png')
        img5 = Image.open('myqr3.png')

        img2 = img2.resize((206, 206))
        img3 = img3.resize((206, 206))
        img4 = img4.resize((206, 206))
        img5 = img5.resize((206, 206))
        img1.paste(img2, (42, 1457), mask=img2)
        img1.paste(img3, (364, 1457), mask=img3)
        img1.paste(img4, (676, 1457), mask=img4)
        img1.paste(img5, (987, 1457), mask=img5)

        # img = img.convert('RGB')
        f = ImageDraw.Draw(img1)
        fnt = ImageFont.truetype("comicbd.ttf", 30)

        f.text((50, 1680), f'{kkk[0]}', font=fnt, fill=(0, 0, 0))
        f.text((372, 1680), f'{kkk[1]}', font=fnt, fill=(0, 0, 0))
        f.text((684, 1680), f'{kkk[2]}', font=fnt, fill=(0, 0, 0))
        f.text((995, 1680), f'{kkk[3]}', font=fnt, fill=(0, 0, 0))

        img1.save(f'qrfinal/index{i}AB.png')
