from tkinter import filedialog

import tkinter as tk
import os

from PIL import Image


def choose_file_dialog():
    """
    This function open the file dialog and let the user choose the path of the folder.
    :return: the path
    :rtype: str
    """
    root = tk.Tk()
    root.withdraw()
    path = filedialog.askdirectory()
    root.destroy()
    return path


def resize_image(directory, resized_directory, image_name):
    """
    The function resize the image given.
    :param directory: directory path
    :type directory: str
    :param resized_directory: resized directory path
    :type resized_directory: str
    :param image_name: the name of the image.
    :type image_name: str
    :return: None
    :rtype: None
    """
    image = Image.open(f'{directory}/{image_name}')
    new_size = (1500, 1000) if image.width > image.height else (1000, 1500)
    image = image.resize(new_size, Image.ANTIALIAS)
    image.save(fp=f'{resized_directory}/{image_name[:-4]}_resize.jpg')


def main():
    directory = choose_file_dialog()
    print('Working on it! it may take some time...')

    resized_directory = f'{directory}/' + f'{directory.split("/")[-1]} - resized'
    images_len = len([image for image in os.listdir(directory) if image.endswith(".jpg")])
    os.mkdir(resized_directory)

    for index, image_name in enumerate(os.listdir(directory), start=1):
        if image_name.endswith(".jpg"):
            resize_image(directory, resized_directory, image_name)
            print(f'[{index}/{images_len}] - {image_name} - Done!')


if __name__ == "__main__":
    main()
