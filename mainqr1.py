import qrcode
from PIL import Image, ImageDraw, ImageFont

with open('listl.txt', 'r') as fp:
    data = fp.read().split('\n')
    cordinates = [(42, 1457), (364, 1457), (676, 1457), (987, 1457)]

    for i in range(0, len(data), 4):
        img1 = Image.open('bhk-1.png')
        s1 = data[i:i + 4]
        qrcode.QRCode(version=1, border=2, box_size=2)

        f = ImageDraw.Draw(img1)
        fnt = ImageFont.truetype("comicbd.ttf", 30)

        for k1, k in enumerate(s1):
            z = k.split(',')
            f.text((cordinates[k1][0] + 8, 1680), f'{z[0]}', font=fnt, fill=(0, 0, 0))
            img = qrcode.make(f'{z[1]}')
            img.save(f'myqr{k1}.png')

        imgs = [Image.open(f'myqr{ii}.png') for ii in range(4)]
        for r in range(4):
            imgs[r] = imgs[r].resize((206, 206))
            img1.paste(imgs[r], cordinates[r], mask=imgs[r])

        img1.save(f'qrfinal/index{i}abc.png')
