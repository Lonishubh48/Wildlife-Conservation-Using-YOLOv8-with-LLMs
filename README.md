# 🦓 Animal Detection with YOLO and LLM Integration 🌍

Welcome to the **Animal Detection and Conservation Insights** repository! This project leverages YOLOv8 for real-time animal detection and integrates advanced Language Learning Models (LLMs) to provide insightful descriptions and conservation strategies for detected wildlife.

---

## 📜 Table of Contents
- [Overview](#-overview)
- [Features](#-features)
- [Setup and Installation](#-setup-and-installation)
- [Usage](#-usage)
- [Streamlit Web App](#-streamlit-web-app)
- [Notebooks and Scripts](#-notebooks-and-scripts)
- [Future Enhancements](#-future-enhancements)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🌟 Overview

Wildlife conservation is vital for maintaining biodiversity and ecological balance. This project combines **YOLOv8** for precise animal detection with **Large Language Models (LLMs)** to generate enriched descriptions and actionable conservation strategies.

### Objectives:
1. **Detect Animals** in uploaded images using the YOLO model.
2. **Generate Conservation Insights** for detected species using Generative AI.
3. Enable **speech output** for detected classes and conservation descriptions.
4. Provide an interactive **Streamlit web app** for users.

---

## 🚀 Features

### Detection:
- YOLOv8 is used for detecting animals in images, trained to recognize species like **elephants, rhinos, zebras, and buffalos**.

### Enriched Insights:
- Integrates **Gemini Pro LLM** for generating species-specific descriptions, ecological roles, threats, and conservation strategies.

### Text-to-Speech:
- Uses `gTTS` to convert insights into audio for an enhanced user experience.

### Streamlit Web App:
- A responsive and interactive web interface where users can:
  - Upload images for detection.
  - View detected species with bounding boxes.
  - Listen to conservation strategies.

---

## 🛠 Setup and Installation

### Prerequisites:
- Python 3.8+
- GPU for YOLOv8 (recommended)
- Libraries: `ultralytics`, `streamlit`, `opencv-python`, `numpy`, `gTTS`

### Installation:
1. Clone the repository:
   ```bash
   git clone https://github.com/lonishubh48/animal-detection-yolo-llm.git
   cd animal-detection-yolo-llm

---
### 🖥 Usage
Once the application is running, follow these steps:

- Open the Streamlit web app in your browser.
- Upload an image of wildlife in the provided file uploader.
- Wait for the YOLO model to process the image.
- View detected animals and their respective bounding boxes in the image.
- Read or listen to the AI-generated conservation insights.
---

## 🎨 Streamlit Web App
![Animaldetection](https://github.com/user-attachments/assets/fe89ab15-ff1d-4393-b43b-e63e11fb3c20)
### Features:
- **Custom Interface**: Wildlife-themed interface for a rich user experience.
- **Upload Images**: Accepts images in JPG, JPEG, and PNG formats.
- **Real-Time Results**: Provides bounding boxes with species names and confidence levels.
- **Text-to-Speech**: Converts generated descriptions into audio.
- **LLM Integration**: Offers detailed insights about detected species.
---
### 📒 Notebooks and Scripts
- Jupyter Notebook (Animal_detection.ipynb):
  - Demonstrates the entire process, from creating data directories to evaluation and testing of the YOLO model.
  - Provides step-by-step guidance to replicate the model training and testing process.
- Streamlit App Script (animaldetection.py):
  - Implements the YOLO model for detection within a web application.
  - **Note:** After training your model, replace the placeholder weight (trainedweight.pt) with your trained YOLO model weights.

---
### 🌍 Future Enhancements
- Docker Deployment: Containerize the application for scalable deployment.
- Video Stream Integration: Extend detection capabilities to video streams.
- Mobile App: Develop a mobile version for real-time detection on the go.
- Multilingual Support: Add language options for diverse user groups.
- Advanced Analytics: Include graphical summContributions are welcome! Here's how you can contribute:

---
### 🤝 Contributing
Contributions are welcome! Here's how you can contribute:
Fork the repository.
1. Create a feature branch:
```bash
git checkout -b feature-name
```
2. Commit your changes and push them to your forked repository.
3. Create a pull request with a detailed explanation of your changes.
---

### 📄 License
This project is licensed under the MIT License. See the LICENSE file for more details.


