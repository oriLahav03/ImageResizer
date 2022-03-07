from tkinter import filedialog

import tkinter as tk
import os

from PIL import Image


def choose_file_dialog():
    root = tk.Tk()
    root.withdraw()
    file = filedialog.askdirectory()
    root.destroy()
    return file


def resize_image(directory, resized_directory, image_name):
    image = Image.open(f'{directory}/{image_name}')
    new_size = (1500, 1000) if image.width > image.height else (1000, 1500)
    image = image.resize(new_size, Image.ANTIALIAS)
    image.save(fp=f'{resized_directory}/{image_name[:-4]}_resize.jpg')


def main():
    directory = choose_file_dialog()
    resized_directory = f'{directory}/' + f'{directory.split("/")[-1]} - resized'
    os.mkdir(resized_directory)
    print('Working on it! it may take some time...')
    images_len = len([image for image in os.listdir(directory) if image.endswith(".jpg")])
    for index, image_name in enumerate(os.listdir(directory), start=1):
        if image_name.endswith(".jpg"):
            resize_image(directory, resized_directory, image_name)
            print(f'[{index}/{images_len}] - {image_name} - Done!')


if __name__ == "__main__":
    main()
