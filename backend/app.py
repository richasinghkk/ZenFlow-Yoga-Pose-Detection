import os
import numpy as np
import cv2
import tensorflow as tf
import subprocess

from flask import Flask, render_template, request

from database import save_prediction
from suggestions import get_suggestions
from accuracy import get_accuracy_status


# Flask setup
app = Flask(
    __name__,
    template_folder="../frontend/templates",
    static_folder="../frontend/static"
)

# Ensure images folder exists
image_folder = os.path.join(app.static_folder, "images")
os.makedirs(image_folder, exist_ok=True)

# Load trained model
model = tf.keras.models.load_model("model/yoga_model.h5")

# Load class names
train_dir = "dataset/train"
class_names = sorted(os.listdir(train_dir))

IMG_SIZE = 224


# Prediction Function
def predict_pose(image_path):

    img = cv2.imread(image_path)

    if img is None:
        return "Image Error", 0

    img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
    img = img / 255.0

    img = np.expand_dims(img, axis=0)

    prediction = model.predict(img)

    predicted_class = class_names[np.argmax(prediction)]

    confidence = float(np.max(prediction))

    return predicted_class, confidence


# 🏠 Slide 1 — Welcome Page
@app.route("/")
def welcome():
    return render_template("welcome.html")


# 📤 Slide 2 — Upload Page
@app.route("/upload")
def upload_page():
    return render_template("upload.html")


# 📊 Prediction Route
@app.route("/predict", methods=["POST"])
def predict():

    prediction = None
    confidence = None
    filename = None
    suggestions = None
    accuracy_status = None

    file = request.files["file"]

    if file:

        filename = file.filename

        filepath = os.path.join(
            image_folder,
            filename
        )

        file.save(filepath)

        prediction, confidence = predict_pose(filepath)

        # Suggestions
        suggestions = get_suggestions(prediction)

        # Accuracy
        accuracy_status = get_accuracy_status(confidence)

        # Save to database
        save_prediction(prediction, confidence)

    return render_template(
        "result.html",
        prediction=prediction,
        confidence=confidence,
        filename=filename,
        suggestions=suggestions,
        accuracy_status=accuracy_status
    )


# 🎥 Slide 3 — Webcam Page
@app.route("/webcam_page")
def webcam_page():
    return render_template("webcam_page.html")


# 🎥 Start Webcam
@app.route("/webcam")
def start_webcam():

    try:

        python_path = os.path.join(
            os.getcwd(),
            "zenflow_env",
            "Scripts",
            "python.exe"
        )

        subprocess.Popen(
            [python_path, "backend/webcam.py"]
        )

        return "<h2>🎥 Webcam Started Successfully!</h2>"

    except Exception as e:

        return f"Error starting webcam: {e}"


# 📊 Slide 4 — Analytics
@app.route("/analytics")
def analytics():

    try:

        python_path = os.path.join(
            os.getcwd(),
            "zenflow_env",
            "Scripts",
            "python.exe"
        )

        subprocess.run(
            [python_path, "research/generate_chart.py"]
        )

        return render_template("analytics.html")

    except Exception as e:

        return f"Error loading analytics: {e}"


# 📄 Slide 5 — Report
@app.route("/report")
def generate_report():

    try:

        python_path = os.path.join(
            os.getcwd(),
            "zenflow_env",
            "Scripts",
            "python.exe"
        )

        subprocess.run(
            [python_path, "research/generate_report.py"]
        )

        return "<h2>📄 Yoga Report Generated Successfully!</h2>"

    except Exception as e:

        return f"Error generating report: {e}"


# 📅 Slide 6 — Daily Summary
@app.route("/daily")
def daily_summary():

    import sqlite3
    from datetime import datetime
    from collections import Counter

    conn = sqlite3.connect("pose_data.db")

    cursor = conn.cursor()

    today = datetime.now().strftime("%Y-%m-%d")

    cursor.execute(
        "SELECT pose, confidence, timestamp FROM predictions"
    )

    rows = cursor.fetchall()

    conn.close()

    today_poses = []
    today_conf = []

    for row in rows:

        if today in row[2]:

            today_poses.append(row[0])
            today_conf.append(row[1])

    if len(today_poses) == 0:

        total = 0
        most_pose = "None"
        avg_conf = 0

    else:

        pose_counts = Counter(today_poses)

        most_pose = pose_counts.most_common(1)[0][0]

        avg_conf = round(
            (sum(today_conf) / len(today_conf)) * 100,
            2
        )

        total = len(today_poses)

    return render_template(
        "daily.html",
        total=total,
        most_pose=most_pose,
        avg_conf=avg_conf
    )


# 📊 Slide 7 — Weekly Summary
@app.route("/weekly")
def weekly_summary():

    import sqlite3
    from datetime import datetime, timedelta
    from collections import Counter

    conn = sqlite3.connect("pose_data.db")

    cursor = conn.cursor()

    last_week = datetime.now() - timedelta(days=7)

    cursor.execute(
        "SELECT pose, confidence, timestamp FROM predictions"
    )

    rows = cursor.fetchall()

    conn.close()

    week_poses = []
    week_conf = []

    for row in rows:

        row_date = datetime.strptime(
            row[2],
            "%Y-%m-%d %H:%M:%S"
        )

        if row_date >= last_week:

            week_poses.append(row[0])
            week_conf.append(row[1])

    if len(week_poses) == 0:

        total = 0
        most_pose = "None"
        avg_conf = 0

    else:

        pose_counts = Counter(week_poses)

        most_pose = pose_counts.most_common(1)[0][0]

        avg_conf = round(
            (sum(week_conf) / len(week_conf)) * 100,
            2
        )

        total = len(week_poses)

    return render_template(
        "weekly.html",
        total=total,
        most_pose=most_pose,
        avg_conf=avg_conf
    )


# 📈 Slide 8 — Improvement Tracker
@app.route("/improvement")
def improvement_tracker():

    import sqlite3

    conn = sqlite3.connect("pose_data.db")

    cursor = conn.cursor()

    cursor.execute(
        "SELECT pose, confidence FROM predictions"
    )

    rows = cursor.fetchall()

    conn.close()

    if len(rows) < 2:

        previous = 0
        latest = 0
        improvement = 0
        pose = "No Data"

    else:

        pose = rows[-1][0]

        previous = round(rows[-2][1] * 100, 2)

        latest = round(rows[-1][1] * 100, 2)

        improvement = round(
            latest - previous,
            2
        )

    return render_template(
        "improvement.html",
        pose=pose,
        previous=previous,
        latest=latest,
        improvement=improvement
    )


# Run App
if __name__ == "__main__":
    app.run(debug=True)