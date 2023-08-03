'''Decodificar un código significa encontrar el valor, número, texto o enlace detrás del código QR. Hay muchas formas de decodificar un código QR utilizando por las camaras de su teléfono inteligente, para decodificar swe instala dos bibliotecas
pip3 install pyzbar
pip3 install pillow'''

from pyzbar.pyzbar import decode
from PIL import Image

decocdeQR = decode(Image.open('./instagram.png'))
print(decocdeQR[0].data.decode('ascii'))