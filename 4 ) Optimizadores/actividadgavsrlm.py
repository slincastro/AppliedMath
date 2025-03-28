# -*- coding: utf-8 -*-
"""ActividadGAvsRLM.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/15OLpSg9Bo4DwQZpIaE-XmpJBN1gk4TpM

**1. GA vs RLM**
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

# Generar datos ficticios para la predicción del precio de una casa
np.random.seed(42)
num_samples = 100

# Features (Tamaño, Número de habitaciones, Distancia al centro, Antigüedad)
size = np.random.randint(50, 300, num_samples)  # Tamaño en m²
rooms = np.random.randint(1, 6, num_samples)  # Número de habitaciones
distance = np.random.uniform(1, 20, num_samples)  # Distancia en km
age = np.random.randint(0, 50, num_samples)  # Años de antigüedad

# Precio de la casa (fórmula ficticia con ruido)
true_weights = np.array([3000, 10000, -5000, -1000])  # Pesos reales de cada feature
price = (true_weights[0] * size + true_weights[1] * rooms +
         true_weights[2] * distance + true_weights[3] * age +
         np.random.normal(0, 50000, num_samples))  # Se agrega ruido aleatorio

# Convertir en matriz de características X e y
X = np.column_stack((size, rooms, distance, age))
y = price

# Dividir datos en entrenamiento y prueba (80% entrenamiento, 20% prueba)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# --- MÉTODO 1: REGRESIÓN LINEAL CON SKLEARN ---
model = LinearRegression()
model.fit(X_train, y_train)
y_pred_lr = model.predict(X_test)
mse_lr = mean_squared_error(y_test, y_pred_lr)

print("\n--- Regresión Lineal ---")
print(f"Coeficientes: {model.coef_}")
print(f"Error Cuadrático Medio (MSE): {mse_lr:.2f}")

# --- MÉTODO 2: OPTIMIZACIÓN CON ALGORITMO GENÉTICO ---
from scipy.optimize import differential_evolution

# Definir la función de costo (MSE entre predicciones y valores reales)
def cost_function(weights):
    y_pred = np.dot(X_train, weights)
    return mean_squared_error(y_train, y_pred)

# Definir los límites de los coeficientes
bounds = [(-50000, 50000)] * 4  # Rango de búsqueda para cada coeficiente

# Aplicar Algoritmo Genético
result = differential_evolution(cost_function, bounds, strategy='best1bin',
                                mutation=(0.5, 1), recombination=0.7, popsize=20, maxiter=100)

# Evaluar el modelo genético
best_weights = result.x
y_pred_ga = np.dot(X_test, best_weights)
mse_ga = mean_squared_error(y_test, y_pred_ga)

print("\n--- Algoritmo Genético ---")
print(f"Mejores coeficientes encontrados: {best_weights}")
print(f"Error Cuadrático Medio (MSE): {mse_ga:.2f}")

# --- COMPARACIÓN VISUAL ---
labels = ['Regresión Lineal', 'Algoritmo Genético']
mse_values = [mse_lr, mse_ga]

plt.bar(labels, mse_values, color=['blue', 'orange'])
plt.ylabel("Error Cuadrático Medio (MSE)")
plt.title("Comparación de Métodos de Optimización")
plt.show()

"""2. Modificar los datos: Que pasa si se cambian los pesos reales de las features"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

# Generar datos ficticios para la predicción del precio de una casa
np.random.seed(42)
num_samples = 100

# Features (Tamaño, Número de habitaciones, Distancia al centro, Antigüedad)
size = np.random.randint(50, 300, num_samples)  # Tamaño en m²
rooms = np.random.randint(1, 6, num_samples)  # Número de habitaciones
distance = np.random.uniform(1, 20, num_samples)  # Distancia en km
age = np.random.randint(0, 50, num_samples)  # Años de antigüedad

# Precio de la casa (fórmula ficticia con ruido)
true_weights = np.array([3000, 10000, -5000, -1000])  # CAMBIAR AQUI LOS PESOS REALES
price = (true_weights[0] * size + true_weights[1] * rooms +
         true_weights[2] * distance + true_weights[3] * age +
         np.random.normal(0, 50000, num_samples))  # Se agrega ruido aleatorio

# Convertir en matriz de características X e y
X = np.column_stack((size, rooms, distance, age))
y = price

# Dividir datos en entrenamiento y prueba (80% entrenamiento, 20% prueba)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# --- MÉTODO 1: REGRESIÓN LINEAL CON SKLEARN ---
model = LinearRegression()
model.fit(X_train, y_train)
y_pred_lr = model.predict(X_test)
mse_lr = mean_squared_error(y_test, y_pred_lr)

print("\n--- Regresión Lineal ---")
print(f"Coeficientes: {model.coef_}")
print(f"Error Cuadrático Medio (MSE): {mse_lr:.2f}")

# --- MÉTODO 2: OPTIMIZACIÓN CON ALGORITMO GENÉTICO ---
from scipy.optimize import differential_evolution

# Definir la función de costo (MSE entre predicciones y valores reales)
def cost_function(weights):
    y_pred = np.dot(X_train, weights)
    return mean_squared_error(y_train, y_pred)

# Definir los límites de los coeficientes
bounds = [(-50000, 50000)] * 4  # Rango de búsqueda para cada coeficiente

# Aplicar Algoritmo Genético
result = differential_evolution(cost_function, bounds, strategy='best1bin',
                                mutation=(0.5, 1), recombination=0.7, popsize=20, maxiter=100)

# Evaluar el modelo genético
best_weights = result.x
y_pred_ga = np.dot(X_test, best_weights)
mse_ga = mean_squared_error(y_test, y_pred_ga)

print("\n--- Algoritmo Genético ---")
print(f"Mejores coeficientes encontrados: {best_weights}")
print(f"Error Cuadrático Medio (MSE): {mse_ga:.2f}")

# --- COMPARACIÓN VISUAL ---
labels = ['Regresión Lineal', 'Algoritmo Genético']
mse_values = [mse_lr, mse_ga]

plt.bar(labels, mse_values, color=['blue', 'orange'])
plt.ylabel("Error Cuadrático Medio (MSE)")
plt.title("Comparación de Métodos de Optimización")
plt.show()

"""COLOCAR LA CONCLUSION AQUI:

3. Probar con una Funcion costo no lineal (cualquier feature elevar a una potencia)
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

# Generar datos ficticios para la predicción del precio de una casa
np.random.seed(42)
num_samples = 100

# Features (Tamaño, Número de habitaciones, Distancia al centro, Antigüedad)
size = np.random.randint(50, 300, num_samples)  # Tamaño en m²
rooms = np.random.randint(1, 6, num_samples)  # Número de habitaciones
distance = np.random.uniform(1, 20, num_samples)  # Distancia en km
age = np.random.randint(0, 50, num_samples)  # Años de antigüedad

# Precio de la casa (fórmula ficticia con ruido)
true_weights = np.array([3000, 10000, -5000, -1000])  # Pesos reales de cada feature
price = (true_weights[0] * size + true_weights[1] * rooms +
         true_weights[2] * distance + true_weights[3] * age +
         np.random.normal(0, 50000, num_samples))  # Se agrega ruido aleatorio

# Convertir en matriz de características X e y
X = np.column_stack((size, rooms, distance, age))
y = price

# Dividir datos en entrenamiento y prueba (80% entrenamiento, 20% prueba)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# --- MÉTODO 1: REGRESIÓN LINEAL CON SKLEARN ---
model = LinearRegression()
model.fit(X_train, y_train)
y_pred_lr = model.predict(X_test)
mse_lr = mean_squared_error(y_test, y_pred_lr)

print("\n--- Regresión Lineal ---")
print(f"Coeficientes: {model.coef_}")
print(f"Error Cuadrático Medio (MSE): {mse_lr:.2f}")

# --- MÉTODO 2: OPTIMIZACIÓN CON ALGORITMO GENÉTICO ---
from scipy.optimize import differential_evolution

# Definir la función de costo (MSE entre predicciones y valores reales)
def cost_function(weights):
    y_pred = np.dot(X_train, weights)
    return mean_squared_error(y_train, y_pred)

# Definir los límites de los coeficientes
bounds = [(-50000, 50000)] * 4  # Rango de búsqueda para cada coeficiente

# Aplicar Algoritmo Genético
result = differential_evolution(cost_function, bounds, strategy='best1bin',
                                mutation=(0.5, 1), recombination=0.7, popsize=20, maxiter=100)  # MODIFICAR EL CODIGO AQUI

# Evaluar el modelo genético
best_weights = result.x
y_pred_ga = np.dot(X_test, best_weights)
mse_ga = mean_squared_error(y_test, y_pred_ga)

print("\n--- Algoritmo Genético ---")
print(f"Mejores coeficientes encontrados: {best_weights}")
print(f"Error Cuadrático Medio (MSE): {mse_ga:.2f}")

# --- COMPARACIÓN VISUAL ---
labels = ['Regresión Lineal', 'Algoritmo Genético']
mse_values = [mse_lr, mse_ga]

plt.bar(labels, mse_values, color=['blue', 'orange'])
plt.ylabel("Error Cuadrático Medio (MSE)")
plt.title("Comparación de Métodos de Optimización")
plt.show()

"""COLOCAR LA CONCLUSION AQUI:

4. Agregar más features

**Número de baños:** entre 1 - 3, con su correspondiente valor real de theta=500

**Tiene garaje** (0 = No, 1 = Sí), con su correspondiente valor real de theta=15000
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

# Generar datos ficticios para la predicción del precio de una casa
np.random.seed(42)
num_samples = 100

# Features (Tamaño, Número de habitaciones, Distancia al centro, Antigüedad)
size = np.random.randint(50, 300, num_samples)  # Tamaño en m²
rooms = np.random.randint(1, 6, num_samples)  # Número de habitaciones
distance = np.random.uniform(1, 20, num_samples)  # Distancia en km
age = np.random.randint(0, 50, num_samples)  # Años de antigüedad
#INSERTAR AQUI LAS DOS NUEVAS FEATURES
banos = np.random.randint(0, 4, num_samples)  # Años de antigüedad

garaje = np.random.randint(0, 2, num_samples)  # Años de antigüedad

# Precio de la casa (fórmula ficticia con ruido)
true_weights = np.array([3000, 10000, -5000, -1000, 5000, 3000])  # Pesos reales de cada feature: INSERTAR AQUI LOS DOS NUEVOS THETAS REALES DE LAS DOS NUEVAS FEATURES
price = (true_weights[0] * size + true_weights[1] * rooms +
         true_weights[2] * distance + true_weights[3] * age + true_weights[4] * banos +garaje*true_weights[5]+
         np.random.normal(0, 50000, num_samples))  # Se agrega ruido aleatorio  # AGREGAR AQUI LAS CONTRIBUCIONES DE LAS DOS NUEVAS FEASTURES

# Convertir en matriz de características X e y
X = np.column_stack((size, rooms, distance, age,banos,garaje))
y = price

# Dividir datos en entrenamiento y prueba (80% entrenamiento, 20% prueba)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# --- MÉTODO 1: REGRESIÓN LINEAL CON SKLEARN ---
model = LinearRegression()
model.fit(X_train, y_train)
y_pred_lr = model.predict(X_test)
mse_lr = mean_squared_error(y_test, y_pred_lr)

print("\n--- Regresión Lineal ---")
print(f"Coeficientes: {model.coef_}")
print(f"Error Cuadrático Medio (MSE): {mse_lr:.2f}")

# --- MÉTODO 2: OPTIMIZACIÓN CON ALGORITMO GENÉTICO ---
from scipy.optimize import differential_evolution

# Definir la función de costo (MSE entre predicciones y valores reales)
def cost_function(weights):
    y_pred = np.dot(X_train, weights)
    return mean_squared_error(y_train, y_pred)

# Definir los límites de los coeficientes
bounds = [(-50000, 50000)] * 6  # Rango de búsqueda para cada coeficiente

# Aplicar Algoritmo Genético
result = differential_evolution(cost_function, bounds, strategy='best1bin',
                                mutation=(0.5, 1), recombination=0.7, popsize=20, maxiter=100)  # MODIFICAR EL CODIGO AQUI

# Evaluar el modelo genético
best_weights = result.x
y_pred_ga = np.dot(X_test, best_weights)
mse_ga = mean_squared_error(y_test, y_pred_ga)

print("\n--- Algoritmo Genético ---")
print(f"Mejores coeficientes encontrados: {best_weights}")
print(f"Error Cuadrático Medio (MSE): {mse_ga:.2f}")

# --- COMPARACIÓN VISUAL ---
labels = ['Regresión Lineal', 'Algoritmo Genético']
mse_values = [mse_lr, mse_ga]

plt.bar(labels, mse_values, color=['blue', 'orange'])
plt.ylabel("Error Cuadrático Medio (MSE)")
plt.title("Comparación de Métodos de Optimización")
plt.show()

"""COLOCAR AQUI SUS CONCLUSIONES:

5. Comparar los coeficientes obtenidos por cada approach

**Aquí comente sobras las actividad 2 a la 4.** Los coeficientes de ajuste han sido los mismos?

**Su Comentario:**
"""