from flask import Blueprint, render_template
from app.forms import APIForm
import joblib
import numpy as np

main = Blueprint('main', __name__)


# Charger le modèle entraîné et le scaler
model = joblib.load('energy_model.pkl')
scaler = joblib.load('scaler.pkl')

import numpy as np

# Fonction pour prédire la consommation d'énergie pour une zone spécifique
def estimate_consumption(input_humidity, input_temp, input_zone):
    # Créer un vecteur de caractéristiques pour l'entrée (humidité et température)
    features = np.array([[input_humidity, input_temp]])

    # Normaliser les caractéristiques avec le même scaler utilisé pendant l'entraînement
    features_scaled = scaler.transform(features)

    # Faire une prédiction avec le modèle (il va prédire pour toutes les zones)
    predicted_consumption = model.predict(features_scaled)
    print(predicted_consumption)
    
    # Convertir le nom de la zone en un index (Zone1 -> 0, Zone2 -> 1, etc.)
    zone_index = ['PowerConsumption_Zone1', 'PowerConsumption_Zone2', 'PowerConsumption_Zone3'].index(input_zone)

    # Retourner la prédiction de consommation d'énergie pour la zone spécifiée
    return predicted_consumption[0][zone_index]


@main.route('/', methods=['GET', 'POST'])
def home():
    form = APIForm()
    estimated_consumption = None 

    if form.validate_on_submit():
        humidity = form.humidity.data
        temperature = form.temperature.data
        zone = form.zone.data

        estimated_consumption = estimate_consumption(humidity, temperature, zone)

    return render_template('form.html', form=form, response_data=estimated_consumption)