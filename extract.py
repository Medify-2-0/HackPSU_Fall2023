Certainly! You want to create a Python script to organize the dataset into training, validation, and testing sets with separate folders for "cancer" and "tumor". Each set should contain only `.jpg` files.

Here's a Python script that uses the `os` and `shutil` libraries to organize the dataset as per your requirements:

```python
import os
import shutil
import random

# Paths for the dataset
base_path = "."  # Current directory
data = [
    # ... (your data here)
]

# Ratio for splitting the data
train_ratio = 0.7
valid_ratio = 0.15
test_ratio = 0.15

# Create directories
if not os.path.exists(os.path.join(base_path, 'train')):
    os.makedirs(os.path.join(base_path, 'train', 'tumor'))
    os.makedirs(os.path.join(base_path, 'train', 'cancer'))

if not os.path.exists(os.path.join(base_path, 'valid')):
    os.makedirs(os.path.join(base_path, 'valid', 'tumor'))
    os.makedirs(os.path.join(base_path, 'valid', 'cancer'))

if not os.path.exists(os.path.join(base_path, 'test')):
    os.makedirs(os.path.join(base_path, 'test', 'tumor'))
    os.makedirs(os.path.join(base_path, 'test', 'cancer'))

# Shuffle the data
random.shuffle(data)

# Split the data into training, validation, and testing sets
train_data = data[:int(len(data) * train_ratio)]
valid_data = data[int(len(data) * train_ratio):int(len(data) * (train_ratio + valid_ratio))]
test_data = data[int(len(data) * (train_ratio + valid_ratio)):]


def move(data_list, subset):
    for dcm_path, jpg_path, label in data_list:
        dest_path = os.path.join(base_path, subset, label, os.path.basename(jpg_path))
        shutil.copy(jpg_path, dest_path)

move(train_data, 'train')
move(valid_data, 'valid')
move(test_data, 'test')

print("Dataset organized successfully!")