#imports qrcode library
import qrcode
from PIL import Image

#Creates barcode ushing QRcode library
#img = qrcode.make("http://192.168.0.5:5050")
img = qrcode.make("http://127.0.0.1:5000")
#img = qrcode.make("https://qrcodegentestversion1.000webhostapp.com/LoginPage.html")
#Saves Barcode locally
img.save("project/modules/data/Test.jpg")
img = Image.open("project/modules/data/Test.jpg")
img.show()
img.close()