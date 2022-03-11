#!/usr/bin/env python
"""
    Used to preprocess data.
"""
from glob import glob
import cv2


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
