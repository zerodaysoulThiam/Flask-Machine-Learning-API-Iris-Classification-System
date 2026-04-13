<a name="top"></a>
# 🚀 Flask Machine Learning API – Iris Classification

[![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-API-black?logo=flask)](https://flask.palletsprojects.com/)
[![Machine Learning](https://img.shields.io/badge/ML-RandomForest-green)](https://scikit-learn.org/)
[![Scikit-learn](https://img.shields.io/badge/Scikit--Learn-1.8-orange)](https://scikit-learn.org/)
[![Status](https://img.shields.io/badge/Status-Active-success)]()
[![Tests](https://img.shields.io/badge/Tests-Passed-brightgreen)]()
[![API](https://img.shields.io/badge/API-REST-red)]()
[![Build](https://img.shields.io/badge/Build-Passing-success)]()
[![License](https://img.shields.io/badge/License-OpenSource-lightgrey)]()

<p align="center"><b>Flask Machine Learning API – Iris Classification</b><br>API REST de Machine Learning avec Flask et Scikit-learn</p>

## Description
Ce projet est une API REST Flask permettant de faire des prédictions sur le dataset Iris grâce à un modèle RandomForestClassifier. L'utilisateur envoie des données JSON et reçoit une prédiction en temps réel.

## Pipeline Machine Learning
Dataset Iris → Prétraitement → Split train/test → RandomForestClassifier → Évaluation (~93%) → Sauvegarde model.pkl → API Flask

## Architecture
ml_api_project/
app.py
train_model.py
test_api.py
model.pkl
model_info.json
requirements.txt
report.docx

## Installation
git clone https://github.com/your-username/flask-ml-iris-api.git
cd flask-ml-iris-api
pip install -r requirements.txt

## Lancement
python train_model.py
python app.py
python test_api.py

## API
GET /
Retour :
{
"status": "ok",
"message": "API de Machine Learning – Classification Iris"
}

POST /predict
URL Postman :
http://127.0.0.1:5000/predict

Format 1 :
{
"features": [5.1, 3.5, 1.4, 0.2]
}

Format 2 :
{
"sepal length (cm)": 5.1,
"sepal width (cm)": 3.5,
"petal length (cm)": 1.4,
"petal width (cm)": 0.2
}

Réponse :
{
"prediction": "setosa",
"confidence": 1.0,
"class_index": 0
}

GET /model-info
Retourne accuracy, confusion matrix, features, modèle, classes.

## Erreurs
400 JSON invalide
404 route inexistante
405 méthode non autorisée
415 content-type incorrect
422 données invalides

## Tests
Postman
curl
python test_api.py

Exemple curl :
curl -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d "{\"features\": [5.1, 3.5, 1.4, 0.2]}"

## Résultats
Accuracy: 93.3%
Modèle: RandomForestClassifier
Dataset: Iris
Classes: 3
Features: 4

## Auteur
Mouhamadou Mokhtar Thiam
Étudiant IoT & Cybersécurité
Développeur Python / IA / Web / IoT

## Conclusion
Projet complet de déploiement d’un modèle Machine Learning en API REST avec Flask, prêt pour production et GitHub.
