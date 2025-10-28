# UE23CS352A - ML Mini Project

Project Overview

This project classifies driver activities (safe driving, texting, drinking, etc.) from images into 10 categories (c0–c9).
We built baseline models (Linear SVM, Softmax, Naive Bayes, Decision Tree, Two-Layer Neural Net) and achieved good validation performance.
The repo also supports single image classification for testing.

## Setup Instructions
**1. Clone the repository**
git clone https://github.com/AnaghaNagaraj/ue23cs352a-ML-067-086.git
cd ue23cs352a-ML-067-086

**2. Create a virtual environment (recommended)**
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows

**3. Install dependencies**
pip install -r requirements.txt

**4. Dataset**
Dataset is **not included in this repo** (too large for GitHub).  

1. Download the dataset from [Kaggle](https://www.kaggle.com/c/state-farm-distracted-driver-detection) or use the dataset provided by the course.  
2. Place it in the following folder structure:
data/
raw/
train/
c0/
c1/
...
c9/
test/

---
Each folder c0...c9 contains images for that class.

test/ contains unlabeled test images.

## How to Run
**Option A – Run the consolidated script**
python run_models.py


This will:

Load & preprocess data

Train all models (SVM, Softmax, Naive Bayes, Decision Tree, MLP)

Save the best model (best_mlp_model.pkl)

Allow you to classify any single image interactively:

Enter the FULL PATH to an image file (or type 'quit'):

**Option B – Run individual notebooks**

You can run each notebook directly in Google Colab:

- [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AnaghaNagaraj/ue23cs352a-ML-067-086/blob/main/LinearSVM.ipynb) Linear SVM  
- [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AnaghaNagaraj/ue23cs352a-ML-067-086/blob/main/Softmax.ipynb) Softmax Classifier  
- [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AnaghaNagaraj/ue23cs352a-ML-067-086/blob/main/NaiveBayes_DecisionTree.ipynb) Naive Bayes & Decision Tree  
- [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AnaghaNagaraj/ue23cs352a-ML-067-086/blob/main/TwoLayerNet.ipynb) Two Layer Neural Network  

---

## Example Single Image Prediction
Enter the FULL PATH to an image file (or type 'quit'): data/raw/train/c6/img_104.jpg
--- Two-Layer Net (MLP) Single Image Prediction ---
Input Image: img_104.jpg
Classification: Drinking (c6)

## Repo Structure
├── features.py                # Preprocessing functions
├── linear_classifier.py       # Linear SVM/Softmax implementation
├── linear_svm.py              # SVM loss functions
├── softmax.py                 # Softmax loss functions
├── neural_net.py              # Two-Layer Neural Net
├── run_models.py              # Main script (train + predict)
├── *.ipynb                    # Notebooks for each model
├── requirements.txt           # Dependencies
├── README.md                  # This file
└── data/
    └── raw/
        ├── train/c0...c9
        └── test/

## ✨ Team
- Anagha Nagaraj (UE23CS352A-PES1UG23CS067) --- Data preprocessing, repo setup, baseline models, evaluation
- Anusha Balamurali (UE23CS352A-PES1UG23CS086) --- Model training, experiments, documentation, analysis
