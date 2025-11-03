# 🌺 Chest X-ray Disease Classification using ResNet50, CBAM, and Grad-CAM

## 📌 Overview
This project involves building an AI system that classifies chest X-ray images to detect pneumonia. The system leverages a pre-trained ResNet50 model enhanced with **CBAM (Convolutional Block Attention Module)** for improved focus on relevant regions and integrates **Grad-CAM** for visual explainability.

This approach is valuable in medical applications where model transparency is essential. The project includes overfitting mitigation strategies and performance evaluation.

---

## 🚀 Features
- ✅ ResNet50-based image classification
- ✅ CBAM integration for channel and spatial attention
- ✅ Grad-CAM for heatmap-based explainability
- ✅ Data augmentation to improve generalization
- ✅ EarlyStopping and ReduceLROnPlateau callbacks
- ✅ High validation accuracy with clear visual insights

---

## 🛠️ Tech Stack
- **Language:** Python
- **Frameworks:** TensorFlow, Keras
- **Libraries:** OpenCV, NumPy, Matplotlib

---

## 🧐 Model Architecture
- Base: Pre-trained **ResNet50** (ImageNet weights, frozen during initial training)
- Attention: **CBAM** layer after the final convolutional block
- Classifier: GlobalAveragePooling + Dense(128, relu) + Dropout(0.5) + Dense(1, sigmoid)

---

## 🧪 Dataset
The dataset used is the publicly available [Chest X-ray dataset from Kaggle](https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia):
- Classes: **PNEUMONIA**, **NORMAL**
- Images are resized to 224x224 for model input

---

## 📈 Training Summary
- Batch Size: 32
- Epochs: 5–10
- Optimizer: Adam
- Loss: Binary Crossentropy
- Metrics: Accuracy

Overfitting mitigation:
- ✅ Data Augmentation (flip, rotate, zoom)
- ✅ Dropout (0.5)
- ✅ EarlyStopping (patience=3)
- ✅ ReduceLROnPlateau (factor=0.2, patience=2)

---

## 🔍 Grad-CAM Visualizations
Grad-CAM is used to overlay heatmaps on original X-rays, indicating regions that influenced the model’s prediction. This enhances interpretability for medical use.

![Grad-CAM Example](gradcam_example.png)
