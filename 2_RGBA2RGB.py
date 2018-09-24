from PIL import Image
import os
import scipy.misc

src = "./resizedData"
dst = "./resized_black/"

if not os.path.exists(dst):
    os.mkdir(dst)

for each in os.listdir(src):
    png = Image.open(os.path.join(src, each))
    #print(png.mode)
    # print each
    if png.mode == 'RGBA':
        png.load() # required for png.split()
        background = Image.new("RGB", png.size, (0,0,0))
        background.paste(png, mask=png.split()[3]) # 3 is the alpha channel
        background.save(os.path.join(dst,each.split('.')[0] + '.jpg'), 'JPEG')
    elif png.mode == 'P':
        # convert P to RGBA before convert background to black
        png = scipy.misc.imread(os.path.join(src, each), mode='RGBA')
        png = Image.fromarray(png)
        png.load()
        background = Image.new("RGB", png.size, (0,0,0))
        background.paste(png, mask=png.split()[3]) # 3 is the alpha channel
        background.save(os.path.join(dst,each.split('.')[0] + '.jpg'), 'JPEG')
    else:
        png.convert('RGB').save(os.path.join(dst, each.split('.')[0] + '.jpg'), 'JPEG')