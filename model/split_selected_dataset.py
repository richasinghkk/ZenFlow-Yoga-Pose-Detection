import os
import shutil
import random

source_dir = "dataset"

train_dir = "dataset/train"
val_dir = "dataset/validation"
test_dir = "dataset/test"

os.makedirs(train_dir, exist_ok=True)
os.makedirs(val_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

# Read selected poses
with open("model/selected_poses.txt") as f:
    selected_poses = [line.strip() for line in f.readlines()]

train_ratio = 0.7
val_ratio = 0.15
test_ratio = 0.15

for pose in selected_poses:

    pose_path = os.path.join(source_dir, pose)

    if not os.path.exists(pose_path):
        print(f"{pose} not found ❌")
        continue

    images = os.listdir(pose_path)
    random.shuffle(images)

    total = len(images)

    train_count = int(total * train_ratio)
    val_count = int(total * val_ratio)

    train_images = images[:train_count]
    val_images = images[train_count:train_count+val_count]
    test_images = images[train_count+val_count:]

    os.makedirs(os.path.join(train_dir, pose), exist_ok=True)
    os.makedirs(os.path.join(val_dir, pose), exist_ok=True)
    os.makedirs(os.path.join(test_dir, pose), exist_ok=True)

    for img in train_images:
        shutil.copy(
            os.path.join(pose_path, img),
            os.path.join(train_dir, pose, img)
        )

    for img in val_images:
        shutil.copy(
            os.path.join(pose_path, img),
            os.path.join(val_dir, pose, img)
        )

    for img in test_images:
        shutil.copy(
            os.path.join(pose_path, img),
            os.path.join(test_dir, pose, img)
        )

    print(f"{pose} split done ✅")

print("Dataset splitting completed 🎉")