# Creating Artwork with GAN's
This repository is meant to explore the random generation of artwork via the usage of GANs

### Requirements
Run the following:

```
conda create -n art_gans python=3.8
pip install -r requirements.txt
```
### Data
The abstract folder contains the data. This is a representation of where the data exists on your local.
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
StyleGan2_ADA_Custom_Abstract.ipynb is the notebook where the work resides. This notebook is google colab oriented. It seems that you need more than 12GB of RAM that is allocated for the free version unfortunatley.

### Util folder
Keeps all the preprocessing scripts for images

### Executables
- clean_data.py converts and resizes specifically JPG images to PNG. Resized to (256,256,3)
  - Use results of clean_data.py and send data to google colab in your drive. Directions on what to do next are noted in the StyleGan2_ADA_Custom_Abstract.ipynb notebook.
