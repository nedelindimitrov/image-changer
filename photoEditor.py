from PIL import Image, ImageEnhance, Image, ImageFilter
import os


def blackwhitefunc():
    path = './imgs'
    pathOut = '/editedImgs'

    for filename in os.listdir(path):
        img = Image.open(f"{path}/{filename}")

        edit = img.filter(ImageFilter.SHARPEN).convert("L").rotate(-360)

        factor = 1.5
        enhancer = ImageEnhance.Contrast(edit)
        edit = enhancer.enhance(factor)

        clean_name = os.path.splitext(filename)[0]

        edit.save(f'.{pathOut}/{clean_name}_edited.jpg')


def sharpening():
    path = './imgs'
    pathOut = '/editedImgs'

    for filename in os.listdir(path):
        img = Image.open(f"{path}/{filename}")

        edit = img.filter(ImageFilter.SHARPEN).convert("RGB").rotate(-360)

        factor = 1.5
        enhancer = ImageEnhance.Contrast(edit)
        edit = enhancer.enhance(factor)

        clean_name = os.path.splitext(filename)[0]

        edit.save(f'.{pathOut}/{clean_name}_edited.jpg')


user_input = input("Choose your photo change: (black&white or sharpening)")

if user_input == "black&white":
    blackwhitefunc()
elif user_input == "sharpening":
    sharpening()
