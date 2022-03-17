#!/usr/bin/env python
"""
    Used to preprocess data.
"""
from glob import glob
import cv2
import imageio


def file_to_png(source_directory: str,
                target_directory: str):
    """
        Convert all JPG's to PNG file types.
        Conversion of dimensions is also initiated. (299,299,3)->(256,256,3)
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
        img = cv2.resize(img, (256, 256), cv2.INTER_AREA)
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
    extend_frames:
        If you want to extend your frames by X seconds.
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
