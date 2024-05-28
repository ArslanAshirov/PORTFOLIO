import qrcode
img = qrcode.make('https://arslanashirov.github.io/PORTFOLIO/')
img.save("qrcode.png")