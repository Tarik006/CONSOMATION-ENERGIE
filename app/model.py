import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler
import joblib


# Charger les données
df = pd.read_csv('powerconsumption.csv')

# Convertir 'Datetime' en type datetime
df['Datetime'] = pd.to_datetime(df['Datetime'])

# Extraire des caractéristiques de la date/heure
df['Hour'] = df['Datetime'].dt.hour
df['DayOfWeek'] = df['Datetime'].dt.dayofweek  # 0 = Lundi, 6 = Dimanche
df['Month'] = df['Datetime'].dt.month

# Sélectionner les colonnes pertinentes pour l'entraînement
features = ['Hour','Temperature']
target = 'PowerConsumption_Zone1'

# Sélectionner les caractéristiques et la cible
X = df[features]
y = df[target]

# Normaliser les données pour que le modèle fonctionne mieux (optionnel)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Diviser les données en ensemble d'entraînement et ensemble de test
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Créer un modèle de régression linéaire (ou autre modèle)
model = LinearRegression()

# Entraîner le modèle
model.fit(X_train, y_train)

# Prédire la consommation d'énergie sur les données de test
y_pred = model.predict(X_test)

# Évaluer le modèle
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')

# Sauvegarder le modèle entraîné
joblib.dump(model, 'app/energy_model.pkl')
joblib.dump(scaler, 'app/scaler.pkl')