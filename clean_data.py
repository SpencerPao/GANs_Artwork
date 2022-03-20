#!/usr/bin/env python
"""
    Executes utility scripts to ensure clean data for input.
    This is done iteratively. Not automated.
"""
from util import data_processing


def main():
    """Converting JPGs to PNGs as input for stylegan2 on google colab."""
    # data_processing.file_to_png(source_directory='data/train/',
    #                             target_directory='data/cleaned_train/')
    """Padding images to square shape and resize if appropriate."""
    # data_processing.padd_resize_for_input(
    #     image_address='data/cleaned_train/',
    #     dimension=1024, # for stylegan2, the dimensions should be (128,256,512,1024)
    #     target_address='data/cleaned_train_resized/')  # cleaned_train_resized
    """Checking number of channels."""
    # arr = data_processing.check_channels(file_path_address='data/cleaned_train_resized',
    #                                      image_type='png')
    # print(arr)  # if empty, go ahead and upload data to google cloud. Else address images.

    """Use the results of the model training ouput for each 20th kimg -> GIF."""
    # data_processing.jpg_to_gif(file_path_input='data/Abstract_Progression_Images/',
    #                            file_path_output='data/Abstract_GIF/',
    #                            genre='abstract',
    #                            extend_frames=True,
    #                            duration=0.5)


if __name__ == '__main__':
    main()
