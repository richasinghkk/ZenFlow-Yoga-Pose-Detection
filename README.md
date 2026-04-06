# 🧘 ZenFlow — AI Yoga Pose Detection System

## 📌 Project Title
**ZenFlow: Enlightened Yoga Pose Classification via Transfer Learning**

ZenFlow is an AI-powered yoga assistant that detects yoga poses from images or live webcam feeds using deep learning. It provides posture feedback, performance analytics, and progress tracking to assist yoga practitioners, instructors, and researchers.

---

# 🎯 Project Objective

The goal of ZenFlow is to build an intelligent yoga pose classification system that:

- Detects yoga poses from images or live video
- Provides posture suggestions
- Displays confidence-based accuracy
- Tracks daily and weekly progress
- Generates analytics and reports
- Supports yoga training and research

---

# 🧠 Technologies Used

## 🔹 Machine Learning & AI

- TensorFlow
- Keras
- Transfer Learning
- MobileNetV2 (Pre-trained CNN)

## 🔹 Computer Vision

- OpenCV (cv2)

## 🔹 Backend

- Flask (Python Web Framework)

## 🔹 Frontend

- HTML
- CSS
- Glass UI Design

## 🔹 Database

- SQLite

## 🔹 Visualization

- Matplotlib

## 🔹 Report Generation

- ReportLab

---

# 🏗️ Project Features

## 🧘 Pose Detection

- Upload yoga pose images
- Predict yoga posture
- Display confidence score

## 🎥 Live Webcam Detection

- Real-time pose detection
- Instant feedback
- Live posture suggestions

## 🧠 Pose Suggestions

- AI-generated posture corrections
- Helps improve yoga alignment

## 📊 Analytics Dashboard

- Pose frequency visualization
- Confidence trend analysis

## 📄 Report Generation

- Generates downloadable PDF reports
- Includes pose history and timestamps

## 📅 Daily Summary

Shows:

- Total poses today
- Most practiced pose
- Average confidence

## 📊 Weekly Summary

Shows:

- Weekly activity summary
- Most practiced pose
- Confidence trend

## 📈 Improvement Tracker

Compares:

- Previous confidence
- Latest confidence
- Improvement percentage

---

# 🧪 How the System Works

```text
User Uploads Image
        ↓
Flask Receives File
        ↓
Image Preprocessing
        ↓
Deep Learning Model Predicts Pose
        ↓
Confidence Calculated
        ↓
Suggestions Generated
        ↓
Data Saved to Database
        ↓
Results Displayed on UI
