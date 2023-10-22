import os
import shutil

# Paths for the dataset
base_path_no = "no"
base_path_yes = "yes"
images_no=[file for file in os.listdir(base_path_no)]
images_yes=[file for file in os.listdir(base_path_yes)]

train_ratio = 0.7
valid_ratio = 0.15
test_ratio = 0.15

num_yes=len(images_yes)
num_no=len(images_no)

def move(files, source, destination):
    for file in files:
        shutil.move(os.path.join(source, file), os.path.join(destination, file))

move(images_no[:int(train_ratio*(num_no))],base_path_no, 'training/no')
move(images_no[int(train_ratio*(num_no)):int((train_ratio+valid_ratio)*(num_no))],base_path_no, 'validating/no')
move(images_no[int((train_ratio+valid_ratio)*(num_no)):],base_path_no, 'testing/no')

move(images_yes[:int(train_ratio*(num_yes))],base_path_yes, 'training/yes')
move(images_yes[int(train_ratio*(num_yes)):int((train_ratio+valid_ratio)*(num_yes))],base_path_yes, 'validating/yes')
move(images_yes[int((train_ratio+valid_ratio)*(num_yes)):],base_path_yes, 'testing/yes')