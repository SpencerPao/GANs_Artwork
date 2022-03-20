#!/usr/bin/env python
"""
    Used to preprocess data.
"""
from glob import glob
import cv2
import imageio
from PIL import Image
from typing import Tuple


def file_to_png(source_directory: str,
                target_directory: str):
    """
        Convert all JPG's to PNG file types.
        Conversion of dimensions is also initiated. (299,299,3)->(256,256,3) if you want. (line commented)
        Parameters:
            source_directory: str - folder path location to raw files.
            target_directory: str - folder path location to send cleaned files
        Return:
            None
    """
    print("Processing files...")
    jpgs = glob(f'{source_directory}*.jpg')
    for j in jpgs:
        img = cv2.imread(j)
        # img = cv2.resize(img, (256, 256), cv2.INTER_AREA)
        cv2.imwrite(f'{target_directory}/' + (j[:-3] + 'png').split('\\')[1], img)


def jpg_to_gif(file_path_input: str,
               file_path_output: str,
               genre: str,
               duration: int) -> None:
    """Converting the fake image output for each saved model iteration in google colab into
    GIF format. NOTE: This takes a while...

    Parameters:
    ----------
    file_path_path_input: str
        Address where the JPGs from the training iteration of GAN is located.
    file_path_output: str
        Address where the gif will be located.
    genre:
        what genre your gif is representing.
    duration:
        Length of time on how long you want to extend each frame.

    Return:
    ----------
    None.
    """
    print("Reading in files to convert for gif.")
    filenames = glob(f'{file_path_input}*.jpg')
    images = []
    for filename in filenames:
        images.append(imageio.imread(filename))
    imageio.mimsave(f'{file_path_output}{genre}.gif', images, duration=0.5)


def padd_resize_for_input(image_address: str,
                          dimension: int,
                          target_address: str) -> None:
    """Padd and resized PNG images for any specified dimensions
    Parameters:
    ----------
    image_address: str
        location of where all the pngs are located.
    dimension: int
        What square dimension you want to scale toward.
    target_address: str
        Where to save the resulting resized, padded image.
    Return:
    ----------
    None
    """
    filenames = glob(f'{image_address}*.png')
    print("Padding and resizing PNG images...")
    for f in filenames:
        res = _expand2square(f, (255, 255, 255)).resize((dimension, dimension))
        fi = f.split('\\')[1]
        res.save(f'{target_address}/{fi}', quality=95)


def _expand2square(image_path: str, background_color: Tuple[int, int, int]):
    """Helper function to padd_resize_for_input. This function resizes images to a square.
    Parameters:
    ----------
    image_path: str
        Location of where individual images are located.
    background color: [int,int,int]
        Color for padding. (Currently using white)
    Return:
    ----------
    None
    """
    pil_img = Image.open(image_path)
    width, height = pil_img.size
    if width == height:
        return pil_img
    elif width > height:
        result = Image.new(pil_img.mode, (width, width), background_color)
        result.paste(pil_img, (0, (width - height) // 2))
        return result
    else:
        result = Image.new(pil_img.mode, (height, height), background_color)
        result.paste(pil_img, ((height - width) // 2, 0))
        return result


def check_channels(file_path_address: str, image_type: str):
    """Manual verifier to determine which images to further clean or remove.
    This checks to see if there is a consistent third dimension in each of the images.

    Paramters:
    ---------
    file_path_address: str
        Address of where all jpgs are located.
    image_type: str
        image type as in .png or .jpg
    Return:
    ---------
    Array of name of jpgs to address.
    """
    imgs = glob(f'{file_path_address}*.{image_type}')
    arr_other = []
    for i, j in enumerate(imgs):
        print(f"Starting {i} for filename: {j}")
        im = cv2.imread(j)
        try:
            if im.shape[2] != 3:
                arr_other.append(j)
        except Exception as e:
            arr_other.append(j)
            print(e)
    return arr_other
