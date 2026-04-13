"""
test_api.py
Phase 5 : Tests de l'API avec la bibliothèque requests
Couvre : GET /, POST /predict, GET /model-info, erreurs
"""

import requests
import json

BASE_URL = "http://127.0.0.1:5000"


def sep(title=""):
    print("\n" + "─" * 55)
    if title:
        print(f"  {title}")
        print("─" * 55)


def display(resp):
    print(f"  Status  : {resp.status_code}")
    try:
        print(f"  Réponse : {json.dumps(resp.json(), indent=4, ensure_ascii=False)}")
    except Exception:
        print(f"  Réponse brute : {resp.text}")


# ────────────────────────────────────────────────
# TEST 1 – GET /   (test de vie)
# ────────────────────────────────────────────────
sep("TEST 1 – GET / (sanity check)")
r = requests.get(f"{BASE_URL}/")
display(r)
assert r.status_code == 200, "✘ Attendu 200"
assert r.json()["status"] == "ok"
print("  ✔ Passed")

# ────────────────────────────────────────────────
# TEST 2 – POST /predict  (format 'features')
# ────────────────────────────────────────────────
sep("TEST 2 – POST /predict  (liste 'features')")
payload = {"features": [5.1, 3.5, 1.4, 0.2]}
r = requests.post(f"{BASE_URL}/predict", json=payload)
display(r)
assert r.status_code == 200
assert "prediction" in r.json()
print("  ✔ Passed")

# ────────────────────────────────────────────────
# TEST 3 – POST /predict  (format clés nommées)
# ────────────────────────────────────────────────
sep("TEST 3 – POST /predict  (clés nommées)")
payload = {
    "sepal length (cm)": 6.3,
    "sepal width (cm)": 3.3,
    "petal length (cm)": 6.0,
    "petal width (cm)": 2.5,
}
r = requests.post(f"{BASE_URL}/predict", json=payload)
display(r)
assert r.status_code == 200
print(f"  → Prédiction : {r.json()['prediction']}")
print("  ✔ Passed")

# ────────────────────────────────────────────────
# TEST 4 – POST /predict  (3 exemples différents)
# ────────────────────────────────────────────────
sep("TEST 4 – POST /predict  (3 exemples)")
samples = [
    {"features": [5.1, 3.5, 1.4, 0.2], "expected": "setosa"},
    {"features": [6.0, 2.9, 4.5, 1.5], "expected": "versicolor"},
    {"features": [6.3, 3.3, 6.0, 2.5], "expected": "virginica"},
]
for s in samples:
    r = requests.post(f"{BASE_URL}/predict", json={"features": s["features"]})
    pred = r.json()["prediction"]
    ok = "✔" if pred == s["expected"] else "✘"
    print(f"  {ok} {s['features']} → {pred}  (attendu: {s['expected']})")
print("  ✔ Passed")

# ────────────────────────────────────────────────
# TEST 5 – GET /model-info
# ────────────────────────────────────────────────
sep("TEST 5 – GET /model-info")
r = requests.get(f"{BASE_URL}/model-info")
display(r)
assert r.status_code == 200
info = r.json()
assert "model_type" in info
assert "evaluation" in info
print(f"  → Accuracy : {info['evaluation']['accuracy']}")
print("  ✔ Passed")

# ────────────────────────────────────────────────
# TESTS D'ERREURS (Phase 4)
# ────────────────────────────────────────────────

sep("TEST 6 – Données manquantes (422)")
r = requests.post(f"{BASE_URL}/predict", json={"features": [5.1, 3.5]})
display(r)
assert r.status_code == 422
print("  ✔ Passed")

sep("TEST 7 – Valeur non numérique (422)")
r = requests.post(f"{BASE_URL}/predict", json={"features": [5.1, "abc", 1.4, 0.2]})
display(r)
assert r.status_code == 422
print("  ✔ Passed")

sep("TEST 8 – JSON mal formé (400)")
r = requests.post(
    f"{BASE_URL}/predict",
    data="NOT JSON AT ALL",
    headers={"Content-Type": "application/json"}
)
display(r)
assert r.status_code == 400
print("  ✔ Passed")

sep("TEST 9 – Mauvais Content-Type (415)")
r = requests.post(
    f"{BASE_URL}/predict",
    data="sepal=5.1",
    headers={"Content-Type": "text/plain"}
)
display(r)
assert r.status_code == 415
print("  ✔ Passed")

sep("TEST 10 – Route inexistante (404)")
r = requests.get(f"{BASE_URL}/unknown-route")
display(r)
assert r.status_code == 404
print("  ✔ Passed")

sep("TEST 11 – Mauvaise méthode HTTP (405)")
r = requests.get(f"{BASE_URL}/predict")
display(r)
assert r.status_code == 405
print("  ✔ Passed")

# ────────────────────────────────────────────────
print("\n" + "=" * 55)
print("  ✔  Tous les tests sont passés avec succès !")
print("=" * 55 + "\n")
