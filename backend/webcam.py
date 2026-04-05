import cv2
import numpy as np
import tensorflow as tf
import os

from suggestions import get_suggestions

# Load trained model
model = tf.keras.models.load_model("model/yoga_model.h5")

# Load class names
train_dir = "dataset/train"
class_names = sorted(os.listdir(train_dir))

IMG_SIZE = 224

# Start webcam
cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    if not ret:
        break

    # Resize frame for prediction
    img = cv2.resize(frame, (IMG_SIZE, IMG_SIZE))
    img = img / 255.0

    img = np.expand_dims(img, axis=0)

    prediction = model.predict(img)

    predicted_class = class_names[np.argmax(prediction)]

    confidence = float(np.max(prediction))

    # Get suggestions
    tips = get_suggestions(predicted_class)

    # Text 1 — Pose Name
    text1 = f"{predicted_class} ({confidence:.2f})"

    cv2.putText(
        frame,
        text1,
        (10, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    # Text 2 — Suggestion 1
    if len(tips) > 0:

        cv2.putText(
            frame,
            tips[0],
            (10, 80),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 255, 0),
            2
        )

    # Text 3 — Suggestion 2
    if len(tips) > 1:

        cv2.putText(
            frame,
            tips[1],
            (10, 110),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 255, 0),
            2
        )

    # Show frame
    cv2.imshow("ZenFlow Webcam", frame)

    # Press Q to stop webcam
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()