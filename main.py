'''
Build a QR Code Generator using Python that allows you to create QR codes for 
URLs, text, contact details, or any custom data in seconds.
'''
import qrcode

url = input("Enter your url: ") 
filename = input("Filename you want to save it as: ")
if not(filename.endswith(".png")):
    filename = filename + ".png"

img = qrcode.make(url)
img.save(filename)

''' https://github.com/shrishtigpt1101-wq '''