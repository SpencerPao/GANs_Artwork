#!/usr/bin/env python
"""
    Executes utility scripts to ensure clean data for input.
"""
from util import data_processing


def main():
    """Converting JPGs to PNGs as input for stylegan2 on google colab."""
    # data_processing.file_to_png(source_directory='data/train/abstract/',
    #                             target_directory='data/cleaned_train/abstract/')
    """Use the results of the model training ouput for each 20th kimg -> GIF."""
    data_processing.jpg_to_gif(file_path_input='data/Abstract_Progression_Images/',
                               file_path_output='data/Abstract_GIF/',
                               genre='abstract',
                               extend_frames=True,
                               duration=0.5)


if __name__ == '__main__':
    main()
