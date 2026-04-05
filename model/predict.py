import tensorflow as tf
import numpy as np
import cv2
import os

# Load trained model
model = tf.keras.models.load_model("model/yoga_model.h5")

# Dataset path
train_dir = "dataset/train"

# Get class names
class_names = sorted(os.listdir(train_dir))

IMG_SIZE = 224

def predict_pose(image_path):

    # Read image
    img = cv2.imread(image_path)

    if img is None:
        print("Image not found ❌")
        return

    img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
    img = img / 255.0

    img = np.expand_dims(img, axis=0)

    prediction = model.predict(img)

    predicted_class = class_names[np.argmax(prediction)]

    confidence = np.max(prediction)

    print("Predicted Pose:", predicted_class)
    print("Confidence:", confidence)

# Test image path
test_image = "test.jpg"

predict_pose(test_image)