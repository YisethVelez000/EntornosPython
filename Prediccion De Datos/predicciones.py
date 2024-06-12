#importar las librerias
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Cargar el dataset
df = pd.read_excel('dataset_limpio.xlsx')

# Seleccionar las variables relevantes para la regresión
variables = ['matematicas', 'lecto_escritura', 'apoyo_economico']

X = df[variables]
y = df['riesgo']

# Dividir el conjunto de datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear el modelo de regresión lineal
model = LinearRegression()

# Entrenar el modelo
model.fit(X_train, y_train)

# Realizar predicciones en el conjunto de prueba
y_pred = model.predict(X_test)

def predecir (nmat,lecto, apoyo):
    pred = model.predict([[nmat, lecto, apoyo]])
    return pred[0]