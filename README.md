# Creating Artwork with GAN's
This repository is meant to explore the random generation of artwork via the usage of GANs

### Requirements
Run the following:

```
conda create -n art_gans python=3.7
pip install -r requirements.txt
```
### Data
The abstract folder contains the data. This is a representation of where the data exists on your local.
```
root
├───data
|   ├───Abstract_GIF
|   ├───Abstract_Progression_Images
│   ├───cleaned_train
│   │   └───genre_of_art
│   ├───cleaned_validation
│   │   └───genre_of_art
│   ├───train
│   │   └───genre_of_art
│   └───validation
│       └───genre_of_art
├───model
│   └───model_name
└───util
```

### Notebook
StyleGan2-ADA_Custom_Edited.ipynb is the notebook where the work resides. This notebook is google colab oriented. It seems that you need more than 12GB of RAM that is allocated for the free version unfortunately.

### Util folder
Keeps all the preprocessing scripts for images

### Executables
- clean_data.py converts and resizes specifically JPG images to PNG.
  - Can convert JPG's to PNG's
  - Padd images to square shape and resize if appropriate
  - Check number of channels to see if there is an inappropriate shape
  - Convert images to GIF
