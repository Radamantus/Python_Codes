# Gerador de QR Code
import pyqrcode
link = 'https://twitter.com/CNPq_Oficial'
pyqrcode.create(link).svg('qrcodelink.svg', scale = 10)
