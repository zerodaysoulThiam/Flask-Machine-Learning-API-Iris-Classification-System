"""
app.py
Phase 3 : API Flask – Phase 4 : Gestion des erreurs
"""

import json
import traceback
from flask import Flask, request, jsonify
import joblib
import numpy as np

# ── Initialisation ──────────────────────────────
app = Flask(__name__)

# ── Chargement du modèle ────────────────────────
try:
    model = joblib.load("model.pkl")
    label_encoder = joblib.load("label_encoder.pkl")
    with open("model_info.json", "r", encoding="utf-8") as f:
        MODEL_INFO = json.load(f)
    MODEL_LOADED = True
    print("✔  Modèle chargé avec succès.")
except Exception as e:
    MODEL_LOADED = False
    MODEL_INFO = {}
    print(f"✘  Erreur au chargement du modèle : {e}")

FEATURES = [
    "sepal length (cm)",
    "sepal width (cm)",
    "petal length (cm)",
    "petal width (cm)",
]

# ── Utilitaires ─────────────────────────────────

def error_response(message, status_code=400, details=None):
    body = {"error": True, "message": message}
    if details:
        body["details"] = details
    return jsonify(body), status_code


def validate_input(data):
    """Valide et extrait les features depuis le JSON reçu."""
    if not isinstance(data, dict):
        raise ValueError("Le corps de la requête doit être un objet JSON.")

    # Accepte 'features' (liste) ou les clés nommées
    if "features" in data:
        values = data["features"]
        if not isinstance(values, list):
            raise ValueError("'features' doit être une liste de 4 nombres.")
        if len(values) != 4:
            raise ValueError(f"'features' doit contenir 4 valeurs, {len(values)} reçues.")
        for v in values:
            if not isinstance(v, (int, float)):
                raise ValueError(f"Valeur invalide : '{v}' n'est pas un nombre.")
        return np.array(values, dtype=float).reshape(1, -1)

    # Clés nommées
    missing = [f for f in FEATURES if f not in data]
    if missing:
        raise ValueError(f"Champs manquants : {missing}")
    values = []
    for f in FEATURES:
        v = data[f]
        if not isinstance(v, (int, float)):
            raise ValueError(f"La valeur de '{f}' doit être un nombre, reçu : {type(v).__name__}.")
        values.append(float(v))
    return np.array(values, dtype=float).reshape(1, -1)


# ────────────────────────────────────────────────
# ROUTES
# ────────────────────────────────────────────────

# GET /  – Test de l'API
@app.route("/", methods=["GET"])
def index():
    return jsonify({
        "status": "ok",
        "message": "API de Machine Learning – Classification Iris",
        "model_loaded": MODEL_LOADED,
        "routes": {
            "GET  /": "Test de l'API",
            "POST /predict": "Prédiction (JSON requis)",
            "GET  /model-info": "Informations sur le modèle",
        },
        "example_payload": {
            "features": [5.1, 3.5, 1.4, 0.2]
        },
    }), 200


# POST /predict  – Prédiction
@app.route("/predict", methods=["POST"])
def predict():
    # Vérification modèle disponible
    if not MODEL_LOADED:
        return error_response(
            "Modèle non disponible. Lancez train_model.py d'abord.",
            status_code=503
        )

    # Vérification Content-Type
    if not request.is_json:
        return error_response(
            "Content-Type doit être 'application/json'.",
            status_code=415
        )

    # Lecture du JSON
    try:
        data = request.get_json(force=True, silent=False)
    except Exception:
        return error_response("Corps JSON invalide ou mal formé.", status_code=400)

    if data is None:
        return error_response("Corps JSON vide ou illisible.", status_code=400)

    # Validation des données
    try:
        X = validate_input(data)
    except ValueError as e:
        return error_response(
            str(e),
            status_code=422,
            details={
                "expected_format_option_1": {"features": [5.1, 3.5, 1.4, 0.2]},
                "expected_format_option_2": {
                    "sepal length (cm)": 5.1,
                    "sepal width (cm)": 3.5,
                    "petal length (cm)": 1.4,
                    "petal width (cm)": 0.2,
                },
            }
        )

    # Prédiction
    try:
        pred_encoded = model.predict(X)[0]
        pred_proba = model.predict_proba(X)[0]
        pred_label = label_encoder.inverse_transform([pred_encoded])[0]
        classes = list(label_encoder.classes_)
        probabilities = {
            cls: round(float(p), 4)
            for cls, p in zip(classes, pred_proba)
        }
    except Exception as e:
        return error_response(
            "Erreur interne lors de la prédiction.",
            status_code=500,
            details=str(e)
        )

    return jsonify({
        "prediction": pred_label,
        "class_index": int(pred_encoded),
        "probabilities": probabilities,
        "confidence": round(float(pred_proba.max()), 4),
        "input_received": {
            FEATURES[i]: float(X[0][i]) for i in range(4)
        },
    }), 200


# GET /model-info  – Informations du modèle
@app.route("/model-info", methods=["GET"])
def model_info():
    if not MODEL_LOADED:
        return error_response(
            "Modèle non disponible. Lancez train_model.py d'abord.",
            status_code=503
        )
    return jsonify(MODEL_INFO), 200


# ── Gestion globale des erreurs ──────────────────

@app.errorhandler(404)
def not_found(e):
    return error_response(
        f"Route introuvable.",
        status_code=404,
        details="Consultez GET / pour la liste des routes disponibles."
    )

@app.errorhandler(405)
def method_not_allowed(e):
    return error_response(
        "Méthode HTTP non autorisée sur cette route.",
        status_code=405
    )

@app.errorhandler(500)
def internal_error(e):
    return error_response(
        "Erreur interne du serveur.",
        status_code=500,
        details=traceback.format_exc()
    )


# ── Lancement ────────────────────────────────────

if __name__ == "__main__":
    print("\n" + "=" * 55)
    print("   API Flask – Machine Learning (Iris)")
    print("=" * 55)
    print("  http://127.0.0.1:5000/\n")
    app.run(debug=True, host="0.0.0.0", port=5000)
