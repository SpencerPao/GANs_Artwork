# Creating Artwork with GAN's
This repository is meant to explore the random generation of artwork via the usage of GANs

### Requirements
Run the following:

```
conda create -n art_gans python=3.8
pip install -r requirements.txt
```
### Data
The abstract folder contains the data. This is representation of where the data exists on your local.
```
root
├───data
│   ├───cleaned_train
│   │   └───abstract
│   ├───cleaned_validation
│   │   └───abstract
│   ├───train
│   │   └───abstract
│   └───validation
│       └───abstract
└───util
```

### Notebook
Artwork_Creation_GANs.ipynb is the notebook where the work resides.

### Util folder
Keeps all the preprocessing scripts for images

### Executables
- clean_data.py converts and resizes specifically JPG images to PNG. Resized to (256,256,3)
