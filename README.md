# Domain-Adaptation-Using-Convolutional-AutoEncoder
In this repository, I implemented the domain Adaptation problem in Manet Dataset using Convolutional Autoencoder.
The basline borrows heavily from the following Github Link(https://bit.ly/3evvN9U) and youtube page(https://bit.ly/3bzUvEn).

## Table of contents
* [Task Description](#TaskDescription)
* [Installation](#Installation)
* [Usage](#Usage)
## Task Description
The dataset consist of Paired landscape and Monet-Stylized image from kaggle-set A(https://bit.ly/3l33Wiy) training image pairs.
The image pairs consists of image and the landscape paintings
The task is to adapt images from one domain to another.

Hyperparameter Optimisation was done using Optuna(https://optuna.org/)

Folder structure
--------------
```
Monet-styled-dataset
├──  Original_A       - this folder contains landscapes images.
│   ├── image1.jpeg
│   └── image10.jpeg
│   └── --------------------
│
├── Original_B      - this folder contains monet styled painting images.
│   ├── image2.jpeg
│   └── image123.jpeg
│   └── --------------------  
│   
│── Autoencoder-Baseline-mit-optuna.ipynb      - this notebook contains  python scripts with visualisation(can be run driectly in Jupyter notebook/IDE)
│   
├──  autoencoder_best_model.h5       - this model can be used directly for converting landscape image to paintings.


```
## Installation

Use the package manager [conda](https://anaconda.org/anaconda/conda) to install requirements.

```bash
conda env create --file requirements.yml
```
