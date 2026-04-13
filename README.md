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
