#!/usr/bin/env python
"""
    Executes utility scripts to ensure clean data for input.
"""
from util import data_processing


def main():
    data_processing.file_to_png(source_directory='data/train/abstract/',
                                target_directory='data/cleaned_train/abstract/')


if __name__ == '__main__':
    main()
