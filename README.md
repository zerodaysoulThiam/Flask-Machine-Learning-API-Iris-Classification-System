<!---------------------------------------------------------------------
  🎓 PROJET ACADÉMIQUE | FLASK ML API - IRIS CLASSIFICATION
  Création et Déploiement d'une API de Machine Learning avec Flask
  ONE MAGICAL BLOCK — RIGOUREUX & PROFESSIONNEL
---------------------------------------------------------------------->

<div align="center">

<!-- GLOW TITLE & BADGES GALORE -->
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=800&size=28&duration=3000&pause=500&color=F7B42C&center=true&vCenter=true&width=700&lines=🎓+PROJET+ACADÉMIQUE;🚀+FLASK+ML+API;🌸+CLASSIFICATION+IRIS;✨+MISE+EN+PRODUCTION+REST" alt="Typing SVG" />

<p>
  <b>⚡ Création et Déploiement d'une API de Machine Learning avec Flask</b><br>
  Institut Supérieur d'Informatique • Projet API ML • Mise en production réelle
</p>

<!-- ========== SUPERNOVA BADGES SECTION (NO SEPARATION) ========== -->
<p align="center">
  <img src="https://img.shields.io/badge/Statut-Terminé-00C853?style=for-the-badge&logo=checkmarx" />
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Flask-API-black?style=for-the-badge&logo=flask&logoColor=white" />
  <img src="https://img.shields.io/badge/ML-RandomForest-228B22?style=for-the-badge&logo=scikit-learn&logoColor=white" />
  <img src="https://img.shields.io/badge/Scikit--Learn-1.8-F7931E?style=for-the-badge&logo=scikit-learn" />
  <img src="https://img.shields.io/badge/JSON-Entrée%2FSortie-000000?style=for-the-badge&logo=json" />
  <img src="https://img.shields.io/badge/Modèle-Pickle-FF6F00?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Tests-Postman%20%7C%20cURL-FF6C37?style=for-the-badge&logo=postman" />
  <img src="https://img.shields.io/badge/Note-Évaluation%20sur%20100-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Version-1.0-9400D3?style=for-the-badge" />
</p>

<!-- ANIMATED DIVIDER -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=100&section=header&text=🎯%20Contexte%20Réel%20-%20Production%20ML%20🎯&fontSize=25&fontAlignY=40" width="100%" />

</div>

## 📌 **Contexte du Projet**

> Dans les systèmes modernes, les modèles de Machine Learning sont intégrés dans des applications via des **API REST**. Ce projet vise à reproduire un **cas réel de mise en production** en utilisant **Flask** — framework imposé (FastAPI, Django interdits).

**Domaine choisi** : 🌸 **Classification** — Dataset Iris (classification de fleurs en 3 espèces)

---

## 🎯 **Objectifs**

### Objectif Général
> Développer une solution complète intégrant un modèle de Machine Learning dans une **API REST fonctionnelle**

### Objectifs Spécifiques

| # | Objectif | Statut |
|---|----------|--------|
| 1 | Préparer un dataset (chargement, nettoyage, encodage, split) | ✅ |
| 2 | Construire un modèle de Machine Learning (entraînement, évaluation) | ✅ |
| 3 | Déployer le modèle via une API Flask | ✅ |
| 4 | Manipuler HTTP et JSON (requêtes/réponses) | ✅ |

---
🏗️ Architecture du Projet
ml_api_project/
├── 🐍 app.py                 # API Flask (routes, chargement modèle, erreurs)
├── 🧠 train_model.py         # Script d'entraînement + sauvegarde
├── 🧪 test_api.py            # Tests automatisés (requests, unittest)
├── 🤖 model.pkl              # Modèle sérialisé (pickle/joblib)
├── 📄 model_info.json        # Métadonnées (accuracy, classes, features)
├── 📦 requirements.txt       # Dépendances Python
├── 📁 data/
│   └── iris.csv              # Dataset utilisé
└── 📑 rapport.docx           # Rapport académique complet

🔮 Exemple Requête/Réponse
json
// POST /predict
// Content-Type: application/json

{
  "features": [5.1, 3.5, 1.4, 0.2]
}

// RÉPONSE (200 OK)
{
  "prediction": "setosa",
  "confidence": 1.0,
  "class_index": 0,
  "features_used": [5.1, 3.5, 1.4, 0.2]
}
📊 Exemple GET /model-info
json
{
  "model_type": "RandomForestClassifier",
  "accuracy": 0.9333333333333333,
  "classes": ["setosa", "versicolor", "virginica"],
  "n_features": 4,
  "feature_names": ["sepal_length", "sepal_width", "petal_length", "petal_width"]
}
❌ Gestion des Erreurs (Robustesse)
Code	Signification	Exemple
400	Bad JSON / champ manquant	{"feat": [1,2,3,4]} au lieu de features
404	Route non trouvée	/predic (faute de frappe)
405	Méthode non autorisée	PUT /predict
415	Wrong Content-Type	XML au lieu de JSON
422	Données invalides	[5.1, 3.5] (4 features requises)
⚙️ Installation & Exécution
bash
# 1. Cloner le dépôt
git clone https://github.com/votre-username/ml-flask-api.git
cd ml-flask-api

# 2. Créer un environnement virtuel (recommandé)
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# 3. Installer les dépendances
pip install -r requirements.txt

# 4. Entraîner le modèle et générer model.pkl
python train_model.py

# 5. Lancer l'API Flask
python app.py

# 6. (Nouveau terminal) Lancer les tests
python test_api.py
🌐 URL locale après lancement : http://127.0.0.1:5000/

Critères d'Évaluation
Critère	Pourcentage	Statut
📊 Prétraitement	15%	✅
🧠 Modèle	20%	✅
🐍 API Flask	30%	✅
🛡️ Robustesse	15%	✅
🧪 Tests	10%	✅
📝 Documentation	10%	✅
Total	100%	✅

Auteur
<div align="center">
Mouhamadou Mokhtar Thiam
🎓 Institut Supérieur d'Informatique
📚 Embedded Systems & IoT / Cybersecurity Student
🔗 GitHub • LinkedIn

</div>

## 🧠 **Pipeline Machine Learning** — *De la donnée à l'API*

```mermaid
graph LR
    A[📊 Dataset Iris] --> B[🧹 Nettoyage]
    B --> C[🔢 Encodage]
    C --> D[📊 Train/Test Split]
    D --> E[🌲 RandomForestClassifier]
    E --> F[📈 Évaluation ~93%]
    F --> G[💾 Sauvegarde model.pkl]
    G --> H[🐍 Flask API]
    H --> I[🌐 Routes REST]
    I --> J[✨ Prédictions JSON]
