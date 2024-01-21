import pandas as pd 
import tensorflow as tf 
import keras 
from tensorflow.keras.preprocessing import image_dataset_from_directory

def load_data():
    train = image_dataset_from_directory('data\part1')