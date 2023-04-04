from PIL import Image, ImageEnhance, ImageFilter
import os

path = 'D:\Python\Projects\Python Projects\Photo_Editor- Python\imgs'
pathout = 'D:\Python\Projects\Python Projects\Photo_Editor- Python\edited_imgs'

for filename in os.listdir(path):
    img = Image.open(os.path.join(path, filename))

    edit = img.filter(ImageFilter.SHARPEN).convert('L')

    factor = 1.5
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(factor)

    clean_name = os.path.splitext(filename)[0]

    edit.save(os.path.join(pathout, f'{clean_name}_edited.jpg'))