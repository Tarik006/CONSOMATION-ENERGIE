from flask import Blueprint, render_template, request, flash
import pandas as pd
from app.forms import APIForm
import joblib
import numpy as np

main = Blueprint('main', __name__)


# Charger le modèle entraîné et le scaler
model = joblib.load('energy_model.pkl')
scaler = joblib.load('scaler.pkl')

# Fonction pour prédire la consommation d'énergie
def estimate_consumption(input_time, input_temp):
    # Convertir l'heure entrée en datetime
    hour =  pd.to_datetime(input_time, format='%H:%M').hour

    # Créer un vecteur de caractéristiques pour l'entrée
    features = np.array([[hour, input_temp]])

    # Normaliser les caractéristiques avec le même scaler utilisé pendant l'entraînement
    features_scaled = scaler.transform(features)

    # Faire une prédiction avec le modèle
    predicted_consumption = model.predict(features_scaled)
    return predicted_consumption[0]


@main.route('/', methods=['GET', 'POST'])
def home():
    form = APIForm()
    estimated_consumption = None  # Pour stocker la réponse 

    if form.validate_on_submit():
        hour = form.hour.data
        temperature = form.temperature.data

        estimated_consumption = estimate_consumption(hour, temperature)

    return render_template('form.html', form=form, response_data=estimated_consumption)