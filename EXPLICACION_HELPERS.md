# Explicación: Helpers Empresariales

## 📋 Propósito

Los helpers son **bibliotecas genéricas reutilizables** que el científico de datos simplemente **importa y usa**. No necesita modificarlos ni entender su implementación interna.

---

## 🎯 ¿Cómo funciona?

### Antes (sin helpers)
```python
# Científico de datos tiene que:
# 1. Importar sklearn manualmente
from sklearn.metrics import r2_score, accuracy_score, f1_score, precision_score, recall_score, mean_absolute_error, mean_squared_error
import numpy as np

# 2. Calcular cada métrica manualmente
r2 = r2_score(y_true, y_pred)
accuracy = accuracy_score(y_true, y_pred)
f1 = f1_score(y_true, y_pred, average='weighted')
precision = precision_score(y_true, y_pred, average='weighted')
recall = recall_score(y_true, y_pred, average='weighted')
mae = mean_absolute_error(y_true, y_pred)
rmse = np.sqrt(mean_squared_error(y_true, y_pred))

# 3. Decidir qué métricas usar según el problema
if regression:
    use r2, mae, rmse
elif classification:
    use accuracy, f1, precision, recall

# 4. Configurar logging a Splunk HEC manualmente
# (muchas líneas de código adicionales...)
```

### Ahora (con helpers)
```python
# Científico de datos solo importa:
from metrics_calculator import calculate_all_metrics
from telemetry_helper import log_metrics

# Y usa en UNA línea:
metrics = calculate_all_metrics(y_true, y_pred)

# Métricas disponibles según el tipo:
print(metrics)  # Retorna todas las que apliquen
# {
#   'r2': 0.95,              # Si es regresión
#   'accuracy': 0.92,        # Si es clasificación
#   'f1': 0.90,              # Si es clasificación
#   'precision': 0.89,       # Si es clasificación
#   'recall': 0.91,          # Si es clasificación
#   'mae': 0.05,             # Siempre
#   'rmse': 0.08             # Siempre
# }

# Y envía telemetría también en UNA línea:
log_metrics(model_name="mi_modelo", **metrics)
```

---

## 🔍 ¿Es genérico para cualquier modelo?

### ✅ SÍ - Ejemplos de uso:

**1. Autoencoder (Cristian)**
```python
from metrics_calculator import calculate_all_metrics

# El modelo predice probabilidad de anomalía
reconstruction_error = autoencoder.predict(X)
is_anomaly = (reconstruction_error > threshold).astype(int)

# Calcula métricas automáticamente
metrics = calculate_all_metrics(y_true_is_anomaly, is_anomaly)
# Retorna: accuracy, f1, precision, recall (porque is_anomaly es clasificación 0/1)
```

**2. Random Forest (predicción de precios)**
```python
from metrics_calculator import calculate_regression_metrics

# El modelo predice precio (valor continuo)
predicted_price = model.predict(features)

# Calcula métricas de regresión
metrics = calculate_regression_metrics(y_true_prices, predicted_price)
# Retorna: r2, mae, rmse, mse (porque price es regresión)
```

**3. SVM (clasificación de imágenes)**
```python
from metrics_calculator import calculate_classification_metrics

# El modelo predice clase (0=perro, 1=gato, 2=pájaro)
predicted_class = model.predict(image_features)

# Calcula métricas de clasificación
metrics = calculate_classification_metrics(y_true_classes, predicted_class)
# Retorna: accuracy, f1, precision, recall
```

**4. LSTM (forecasting)**
```python
from metrics_calculator import calculate_regression_metrics

# El modelo predice valor futuro (temperatura, stock, etc.)
predicted_value = lstm.predict(time_series)

# Calcula métricas de regresión
metrics = calculate_regression_metrics(y_true_values, predicted_value)
```

---

## 🧠 ¿Cómo decide qué métricas calcular?

El helper tiene lógica inteligente:

```python
def _is_classification(y):
    """Detectar si y es clasificación"""
    if isinstance(y, np.ndarray):
        # Si son enteros O pocos valores únicos (<20) → clasificación
        return y.dtype in [np.int32, np.int64] or len(np.unique(y)) <= 20
    return False

def _is_regression(y):
    """Detectar si y es regresión"""
    if isinstance(y, np.ndarray):
        # Si son flotantes O muchos valores únicos (>20) → regresión
        return y.dtype in [np.float32, np.float64] or len(np.unique(y)) > 20
    return False
```

**Ejemplos:**
- `y = [0, 1, 1, 0, 0, 1]` → Clasificación (enteros, 2 valores únicos)
- `y = [25.5, 30.2, 28.7, 35.1]` → Regresión (flotantes, muchos valores únicos)
- `y = [1, 2, 3, 4, 5]` (pocos únicos) → Clasificación
- `y = [1.0, 1.5, 2.0, 2.5, ...]` (muchos únicos) → Regresión

---

## 🎯 Ventajas para el Científico de Datos

| Antes | Ahora |
|-------|-------|
| ❌ 10+ líneas de código | ✅ 1 línea |
| ❌ Decidir manualmente qué métricas usar | ✅ Automático |
| ❌ Configurar logging manual | ✅ 1 línea `log_metrics()` |
| ❌ Implementación inconsistente entre proyectos | ✅ Estándar en toda la empresa |
| ❌ Olvidar alguna métrica importante | ✅ Calcula todas automáticamente |

---

## 📦 ¿Dónde está el código?

El científico de datos **NO VE** el código del helper. Solo lo importa:

```python
# En cualquier notebook:
import sys
sys.path.append("/dltk/notebooks/helpers")  # Esto lo hace una vez
from metrics_calculator import calculate_all_metrics  # Ya puede usar
```

Los helpers están **preinstalados en la imagen Docker** en `/dltk/notebooks/helpers/`

---

## 🚀 Flujo Real del Científico

1. **Abre JupyterLab** en contenedor DSDL
2. **Abre template** `template_empresa_base.ipynb`
3. **Copia a su proyecto**: `File → Save As → Cristian_Autoencoder_v1.ipynb`
4. **Desarrolla su modelo**: edita la función `fit()` y `apply()`
5. **Usa helpers**: simplemente llama funciones
6. **No se preocupa por**: métricas, logging, telemetría

---

## ✅ Conclusión

**SÍ, `metrics_calculator.py` es genérico** para:
- ✅ Cualquier modelo ML/DL
- ✅ Cualquier tipo de problema (clasificación, regresión, forecast, etc.)
- ✅ Cualquier framework (TensorFlow, PyTorch, sklearn, etc.)

El científico solo pasa `y_true` y `y_pred`, y el helper **automáticamente**:
1. Detecta si es clasificación o regresión
2. Calcula las métricas apropiadas
3. Retorna un dict estándar
4. Se puede enviar a Splunk con `log_metrics()`

**Es como usar una biblioteca estándar** (pandas, numpy), pero diseñada específicamente para las necesidades de la empresa.

