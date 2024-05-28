import qrcode
img = qrcode.make('http://github.com/ArslanAshirov')
img.save("qrcode")