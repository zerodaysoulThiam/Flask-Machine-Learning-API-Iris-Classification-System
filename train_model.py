"""
train_model.py
Phase 1 : Préparation des données + Phase 2 : Modélisation
Dataset : Iris (classification multi-classes)
"""

import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score, classification_report, confusion_matrix
)
import joblib
import json
import os

# ────────────────────────────────────────────────
# PHASE 1 : Préparation des données
# ────────────────────────────────────────────────

print("=" * 55)
print("   PHASE 1 : PRÉPARATION DES DONNÉES")
print("=" * 55)

# 1.1 Chargement
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df["species"] = iris.target
df["species_name"] = df["species"].map(
    dict(enumerate(iris.target_names))
)

# Sauvegarde du dataset brut
os.makedirs("data", exist_ok=True)
df.to_csv("data/iris_dataset.csv", index=False)
print(f"\n✔  Dataset chargé  : {df.shape[0]} lignes, {df.shape[1]} colonnes")
print(f"   Colonnes        : {list(df.columns)}")

# 1.2 Nettoyage
print(f"\n   Valeurs manquantes : {df.isnull().sum().sum()}")
df_clean = df.dropna()
print(f"   Lignes après nettoyage : {len(df_clean)}")

# 1.3 Encodage
le = LabelEncoder()
df_clean = df_clean.copy()
df_clean["species_encoded"] = le.fit_transform(df_clean["species_name"])

feature_names = [
    "sepal length (cm)",
    "sepal width (cm)",
    "petal length (cm)",
    "petal width (cm)",
]
X = df_clean[feature_names].values
y = df_clean["species_encoded"].values

print(f"\n   Classes : {list(le.classes_)}")
print(f"   Distribution :\n{df_clean['species_name'].value_counts().to_string()}")

# 1.4 Split train/test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
print(f"\n   Train : {X_train.shape[0]} exemples")
print(f"   Test  : {X_test.shape[0]} exemples")

# ────────────────────────────────────────────────
# PHASE 2 : Modélisation
# ────────────────────────────────────────────────

print("\n" + "=" * 55)
print("   PHASE 2 : MODÉLISATION")
print("=" * 55)

# 2.1 Choix & entraînement
model = RandomForestClassifier(
    n_estimators=100,
    max_depth=5,
    random_state=42
)
model.fit(X_train, y_train)
print("\n✔  Modèle entraîné : RandomForestClassifier")
print(f"   n_estimators = {model.n_estimators}, max_depth = {model.max_depth}")

# 2.2 Évaluation
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(
    y_test, y_pred,
    target_names=le.classes_,
    output_dict=True
)
cm = confusion_matrix(y_test, y_pred).tolist()

print(f"\n   Accuracy : {accuracy:.4f}  ({accuracy*100:.2f} %)")
print("\n   Rapport de classification :")
print(
    classification_report(y_test, y_pred, target_names=le.classes_)
)
print("   Matrice de confusion :")
print(np.array(cm))

# 2.3 Sauvegarde modèle + métadonnées
joblib.dump(model, "model.pkl")
joblib.dump(le, "label_encoder.pkl")

model_info = {
    "model_type": "RandomForestClassifier",
    "library": "scikit-learn",
    "task": "Classification multi-classes",
    "dataset": "Iris",
    "n_classes": int(len(le.classes_)),
    "classes": list(le.classes_),
    "features": feature_names,
    "n_features": len(feature_names),
    "hyperparameters": {
        "n_estimators": model.n_estimators,
        "max_depth": model.max_depth,
        "random_state": 42,
    },
    "evaluation": {
        "accuracy": round(accuracy, 4),
        "train_size": int(X_train.shape[0]),
        "test_size": int(X_test.shape[0]),
        "classification_report": {
            k: v for k, v in report.items()
            if k not in ["accuracy"]
        },
        "confusion_matrix": cm,
    },
}

with open("model_info.json", "w", encoding="utf-8") as f:
    json.dump(model_info, f, indent=2, ensure_ascii=False)

print("\n✔  Fichiers sauvegardés :")
print("     model.pkl")
print("     label_encoder.pkl")
print("     model_info.json")
print("     data/iris_dataset.csv")
print("\n" + "=" * 55)
print("   Entraînement terminé avec succès !")
print("=" * 55)
