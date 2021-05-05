# Gerador de QR Code
import pyqrcode
link = 'https://twitter.com/gutossauros'
pyqrcode.create(link).svg('qrcodelink.svg', scale = 10)