import numpy as np
import cv2

def extract_features(img, size=(64, 64)):
    """
    Resize image and flatten into a 1D vector
    """
    img_resized = cv2.resize(img, size)
    return img_resized.flatten()

def extract_features_from_list(images, size=(64, 64)):
    """
    Apply extract_features on a list of images
    """
    return np.array([extract_features(img, size) for img in images])

def normalize_features(X):
    """
    Normalize features to range [0,1]
    """
    return X / 255.0
