'''Para crear códic=gos QR usando el lenguaje de programacin Python, primero debe asegurardse de tener los módulos PyQRcode y pypng instalados en su entorno virtual
pip3 install PyQRCode
pip3 install pypng'''

import pyqrcode
import png

link = 'chttps://www.instagram.com/the.clever.programmer/'

qr_code = pyqrcode.create(link)
qr_code.png('instagram.png', scale=5)