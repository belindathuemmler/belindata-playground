"""Card image for 'Measuring on Curved Surfaces': the belindata logo (the twisted band) centred on ivory,
in the 1376x768 card format. Usage: python logo_card.py path/to/logo.png out.jpg"""
import sys
from PIL import Image

logo, out = sys.argv[1], sys.argv[2]
W, H, IVORY = 1376, 768, (250, 248, 245)
card = Image.new('RGB', (W, H), IVORY)
im = Image.open(logo).convert('RGBA')
h = int(H * 0.84)
im = im.resize((int(im.width * h / im.height), h), Image.LANCZOS)
card.paste(im, ((W - im.width) // 2, (H - im.height) // 2), im)
card.save(out, quality=92)
print('ok')
