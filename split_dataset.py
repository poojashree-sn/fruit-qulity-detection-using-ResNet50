import os
import shutil
import random

# Paths
dataset_dir = 'dataset'
train_dir = os.path.join(dataset_dir, 'train')
test_dir = os.path.join(dataset_dir, 'test')

# Split ratio
train_ratio = 0.7
test_ratio = 0.3

# Create directories if they don't exist
for folder in ['train', 'test']:
    for class_name in ['fresh', 'rotten']:
        path = os.path.join(dataset_dir, folder, class_name)
        os.makedirs(path, exist_ok=True)

# Function to split and move images
def split_and_move(source_folder, class_name):
    # Get all images
    images = [img for img in os.listdir(source_folder) if img.lower().endswith(('png', 'jpg', 'jpeg'))]

    # Shuffle and split
    random.shuffle(images)
    split_index = int(len(images) * train_ratio)

    train_images = images[:split_index]
    test_images = images[split_index:]

    # Move images to respective folders
    for img in train_images:
        shutil.move(os.path.join(source_folder, img), os.path.join(train_dir, class_name, img))

    for img in test_images:
        shutil.move(os.path.join(source_folder, img), os.path.join(test_dir, class_name, img))

# Apply the split for each class
for class_folder in ['fresh', 'rotten']:
    source_folder = os.path.join(dataset_dir, class_folder)
    split_and_move(source_folder, class_folder)

print("Dataset split completed: 70% training, 30% testing.")
