<!-- ========================================= -->
<!--  FLASK ML API - IRIS CLASSIFICATION -->
<!-- ========================================= -->

<h1 align="center"> Flask Machine Learning API</h1>

<p align="center">
  <b> Iris Classification using Flask + Scikit-learn</b><br>
  A complete end-to-end Machine Learning deployment project
</p>

---

##  Badges

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-API-black?logo=flask)
![Machine Learning](https://img.shields.io/badge/ML-RandomForest-green)
![Scikit-learn](https://img.shields.io/badge/Scikit--Learn-1.8-orange)
![Status](https://img.shields.io/badge/Status-Active-success)
![Tests](https://img.shields.io/badge/Tests-Passed-brightgreen)
![License](https://img.shields.io/badge/License-OpenSource-lightgrey)
![API](https://img.shields.io/badge/API-REST-red)
![Build](https://img.shields.io/badge/Build-Passing-success)

</p>

---

##  Project Overview

This project is a **REST API built with Flask** that serves a **Machine Learning model (RandomForestClassifier)** trained on the **Iris dataset**.

It allows users to send flower measurements via JSON and receive real-time predictions.

---

##  Machine Learning Pipeline


---

##  Project Architecture

ml_api_project/
│
├── app.py → Flask API
├── train_model.py → Model training pipeline
├── test_api.py → Automated API tests
├── model.pkl → Trained ML model
├── model_info.json → Model metadata
├── requirements.txt → Dependencies
└── report.docx → Full documentation


---

##  Features

✔ REST API with Flask  
✔ Machine Learning prediction  
✔ JSON input/output  
✔ Input validation  
✔ Error handling (400, 404, 405, 422, 415)  
✔ Automated testing  
✔ Model evaluation metrics  
✔ Production-ready structure  

---

## 📡 API Endpoints

### 🟢 Home
GET /


Response:
```json
{
  "status": "ok",
  "message": "API de Machine Learning – Classification Iris"
}
🔵 Prediction
POST /predict
Input Format 1:
{
  "features": [5.1, 3.5, 1.4, 0.2]
}
Input Format 2:
{
  "sepal length (cm)": 5.1,
  "sepal width (cm)": 3.5,
  "petal length (cm)": 1.4,
  "petal width (cm)": 0.2
}
Output:
{
  "prediction": "setosa",
  "confidence": 1.0
}
🟣 Model Info
GET /model-info

Returns:

Model type
Accuracy
Confusion matrix
Features list
 Error Handling
Error	Meaning
400	Bad JSON format
404	Route not found
405	Method not allowed
415	Wrong Content-Type
422	Invalid input data

 Installation
git clone https://github.com/your-username/ml-flask-api.git
cd ml-flask-api

pip install -r requirements.txt
 Run Project
1. Train model
python train_model.py
2. Start API
python app.py
3. Test API
python test_api.py
 Live Test (Local)
http://127.0.0.1:5000/

Author

Mouhamadou Mokhtar Thiam
Student in Embedded Systems & IoT / Cybersecurity

📜 License

This project is open-source for educational use.
