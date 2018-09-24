# resize pokeGAN.py
import os
from PIL import Image
src = "./data"
dst = "./resizedData"

if not os.path.exists(dst):
    os.mkdir(dst)

for each in os.listdir(src):
    img = Image.open(os.path.join(src, each))
    img = img.resize((256, 256), Image.ANTIALIAS)
    img.save(os.path.join(dst,each))