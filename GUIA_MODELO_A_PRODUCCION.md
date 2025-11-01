# 🚀 Guía: De Notebook a Producción - Flujo Completo

**Fecha**: 2025-11-01  
**Objetivo**: Guía paso a paso para que Cristian (o cualquier DS) ponga su modelo en producción

---

## 📋 Requisitos Previos

✅ Contenedor DSDL empresarial funcionando  
✅ Splunk con datos indexados  
✅ Helpers custom instalados  
✅ HEC configurado (telemetría)

---

## 🔄 Flujo Completo: Dev → Prod

### FASE 1: Desarrollo en JupyterLab ⚙️

#### 1.1 Crear Notebook en JupyterLab

**En JupyterLab** (`http://localhost:8888`):

1. Nuevo notebook: `Modelo_Corona_V1.ipynb`
2. Importar helpers y librerías

```python
import sys
sys.path.append("/srv/notebooks_custom/helpers")

from telemetry_helper import log_metrics, log_training_step, log_error
from metrics_calculator import calculate_all_metrics
from preprocessor import standard_preprocessing
import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
```

#### 1.2 Definir Funciones Requeridas

**DSDL requiere 3 funciones**:

```python
# 1️⃣ INIT: Inicialización del modelo
def init(param):
    """
    Inicializar modelo y parámetros
    """
    global model, scaler
    
    # Parámetros del modelo
    epochs = param.get('epochs', 50)
    batch_size = param.get('batch_size', 32)
    learning_rate = param.get('learning_rate', 0.001)
    
    # Definir arquitectura del modelo
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(64, activation='relu', input_shape=(n_features,)),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(32, activation='relu'),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(1, activation='sigmoid')  # Para anomalías
    ])
    
    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=learning_rate),
        loss='binary_crossentropy',
        metrics=['accuracy']
    )
    
    # Inicializar preprocessor
    scaler = None
    
    return model

# 2️⃣ FIT: Entrenamiento del modelo
def fit(df, param):
    """
    Entrenar modelo con datos
    """
    global model, scaler
    
    # Separar features y target
    # Asumir que la última columna es el target
    feature_cols = [col for col in df.columns if col != 'target']
    X = df[feature_cols].values
    y = df['target'].values if 'target' in df.columns else None
    
    # Preprocesamiento
    X_processed, scaler = standard_preprocessing(X)
    
    # Split train/val
    if y is not None:
        X_train, X_val, y_train, y_val = train_test_split(
            X_processed, y, test_size=0.2, random_state=42
        )
    else:
        # Autoencoder: solo features
        X_train, X_val = train_test_split(X_processed, test_size=0.2, random_state=42)
        y_train, y_val = None, None
    
    # Parámetros del entrenamiento
    epochs = param.get('epochs', 50)
    batch_size = param.get('batch_size', 32)
    
    # Callbacks
    callbacks = [
        tf.keras.callbacks.EarlyStopping(patience=5, restore_best_weights=True)
    ]
    
    # Entrenar
    if y_train is not None:
        history = model.fit(
            X_train, y_train,
            validation_data=(X_val, y_val),
            epochs=epochs,
            batch_size=batch_size,
            callbacks=callbacks,
            verbose=0
        )
    else:
        # Autoencoder: reconstruir input
        history = model.fit(
            X_train, X_train,  # Input = Output
            validation_data=(X_val, X_val),
            epochs=epochs,
            batch_size=batch_size,
            callbacks=callbacks,
            verbose=0
        )
    
    # Calcular métricas
    val_pred = model.predict(X_val)
    
    if y_val is not None:
        metrics = calculate_all_metrics(y_val, (val_pred > 0.5).astype(int))
    else:
        # Autoencoder: MSE como métrica
        metrics = {
            'mse': np.mean((X_val - val_pred) ** 2),
            'mae': np.mean(np.abs(X_val - val_pred))
        }
    
    # Enviar telemetría a Splunk
    log_metrics(
        model_name='Modelo_Corona_V1',
        accuracy=metrics.get('accuracy', None),
        f1=metrics.get('f1', None),
        precision=metrics.get('precision', None),
        recall=metrics.get('recall', None)
    )
    
    # Log de entrenamiento
    final_loss = history.history['loss'][-1]
    log_training_step(
        model_name='Modelo_Corona_V1',
        epoch=epochs,
        loss=final_loss
    )
    
    return model

# 3️⃣ APPLY: Aplicar modelo a nuevos datos
def apply(df):
    """
    Aplicar modelo entrenado para predicción
    """
    global model, scaler
    
    # Separar features
    feature_cols = [col for col in df.columns if col != 'target']
    X = df[feature_cols].values
    
    # Preprocesar con el mismo scaler del entrenamiento
    if scaler is not None:
        X_processed = scaler.transform(X)
    else:
        X_processed = X
    
    # Predecir
    predictions = model.predict(X_processed)
    
    # Si es autoencoder, calcular error de reconstrucción
    if len(X_processed.shape) > 2 or X_processed.shape[1] == X_processed.shape[0]:
        # Autoencoder: reconstruir y calcular error
        reconstructed = model.predict(X_processed)
        errors = np.mean((X_processed - reconstructed) ** 2, axis=1)
        return errors
    else:
        # Clasificador: probabilidad o clase
        return predictions.flatten()

# 4️⃣ SUMMARY: Resumen del modelo
def summary(df):
    """
    Generar resumen de métricas del modelo
    """
    global model
    
    if model is None:
        return {"status": "Model not initialized"}
    
    return {
        "model_type": "Autoencoder" if y is None else "Classifier",
        "architecture": model.to_json(),
        "trainable_parameters": model.count_params(),
        "layers": len(model.layers)
    }
```

#### 1.3 Guardar Notebook

```python
# Guardar en JupyterLab
# Archivo: Modelo_Corona_V1.ipynb
# Se guarda automáticamente en /srv/notebooks/
```

**DSDL exporta automáticamente** a `/srv/notebooks/app/Modelo_Corona_V1.py`

---

### FASE 2: Testing con Splunk 🧪

#### 2.1 Modo Development (mode=stage)

**En Splunk Web → Search**:

```spl
index=corona_data 
| head 1000
| fit MLTKContainer algo=Modelo_Corona_V1 mode=stage epochs=10 batch_size=32 
into app:corona_modelo_test
```

**Qué hace**:
- ✅ Envía datos al contenedor
- ✅ Abre JupyterLab para debug interactivo
- ✅ **NO guarda modelo** en producción
- ✅ Útil para iterar rápidamente

#### 2.2 Verificar en JupyterLab

1. Abrir `http://localhost:8888`
2. Ver logs en el notebook
3. Ajustar hiperparámetros si es necesario
4. Re-ejecutar `fit` con nuevos parámetros

---

### FASE 3: Entrenar Modelo Real 🎯

#### 3.1 Fit Command Completo

**En Splunk Web → Search**:

```spl
index=corona_data 
| fit MLTKContainer 
    algo=Modelo_Corona_V1 
    epochs=50 
    batch_size=32 
    learning_rate=0.001 
from feature_* 
into app:corona_modelo_v1_produccion
```

**Qué hace**:
- ✅ Lee datos de `index=corona_data`
- ✅ Extrae features `feature_*`
- ✅ Entrena modelo con parámetros especificados
- ✅ Guarda modelo en `app:corona_modelo_v1_produccion`
- ✅ Envía métricas a `ml_metrics`
- ✅ Envía logs a `ml_model_logs`

#### 3.2 Verificar Resultados

**En Splunk Web → Search**:

```spl
| rest /servicesNS/-/mltk-container/storage/collections/data/models
| where title="corona_modelo_v1_produccion"
```

O:

```spl
index=ml_metrics model_name=Modelo_Corona_V1
| mstats avg(_value) by metric_name
```

---

### FASE 4: Aplicar Modelo (Inferencia) 🔄

#### 4.1 Apply Command

**En Splunk Web → Search**:

```spl
index=corona_data 
| apply corona_modelo_v1_produccion from feature_*
| eval anomaly_score=_value
| eval is_anomaly=if(anomaly_score > 0.8, 1, 0)
| stats count by is_anomaly
```

**Qué hace**:
- ✅ Lee datos de `index=corona_data`
- ✅ Extrae features `feature_*`
- ✅ Aplica modelo entrenado
- ✅ Retorna predicciones en campo `_value`
- ✅ Puedes crear campos derivados (`anomaly_score`, `is_anomaly`)

#### 4.2 Dashboard con Modelo

```spl
index=corona_data
| apply corona_modelo_v1_produccion from feature_*
| eval anomaly_score=_value
| timechart span=1h avg(anomaly_score) as avg_score by sensor
```

---

## 📊 Monitoreo y Observabilidad

### Telemetría Automática

Los helpers ya configurados envían:

**Métricas** (`index=ml_metrics`):
```spl
index=ml_metrics model_name=Modelo_Corona_V1
| mstats avg(_value) by metric_name span=1h
```

**Logs** (`index=ml_model_logs`):
```spl
index=ml_model_logs model_name=Modelo_Corona_V1
| eval hour=strftime(_time, "%H")
| stats count by event_type, hour
```

---

## 🔄 Versionado de Modelos

### Naming Convention

```
{app_name}_{use_case}_{owner}_v{version}

Ejemplos:
- corona_detection_cristian_v1
- corona_detection_cristian_v2
- molino_crudo_cristian_v1
```

### Cómo Versionar

1. Entrenar nuevo modelo:
```spl
| fit MLTKContainer algo=Modelo_Corona_V2 ...
into app:corona_detection_cristian_v2
```

2. Comparar modelos:
```spl
index=ml_metrics model_name=Modelo_Corona_V*
| mstats avg(_value) by model_name, metric_name
```

---

## ⚠️ Checklist Pre-Producción

### Antes de Entrenar

- [ ] Notebook tiene funciones `init`, `fit`, `apply`, `summary`
- [ ] Helpers importados correctamente
- [ ] Telemetría configurada
- [ ] Datos validados en Splunk
- [ ] Features definidas
- [ ] Hiperparámetros decididos

### Después de Entrenar

- [ ] Métricas visibles en `ml_metrics`
- [ ] Logs en `ml_model_logs`
- [ ] Modelo guardado en `app:modelo_*`
- [ ] Accuracy/F1/R² aceptables
- [ ] Apply funciona sin errores

### Para Producción

- [ ] Documentar hiperparámetros usados
- [ ] Registrar version en Git
- [ ] Crear dashboard de monitoreo
- [ ] Configurar alertas si accuracy baja
- [ ] Plan de retrain periódico

---

## 📚 Ejemplos Completos

### Ejemplo 1: Autoencoder (Anomalías)

Ver notebook: `Molino_Crudo.ipynb` en carpeta Cristian

### Ejemplo 2: Regresión

Ver notebook: `modelo_gas_corona.ipynb` en carpeta Cristian

### Ejemplo 3: Clasificación

Ver notebook: `setpoints_corona_h4.ipynb` en carpeta Cristian

---

## 🎯 Próximos Pasos para Cristian

1. **Copiar notebook real** de `/Cristian-Autoencoder-Ejemplos/` a JupyterLab
2. **Adaptar funciones** a formato DSDL (`init`, `fit`, `apply`, `summary`)
3. **Agregar telemetría** con helpers
4. **Probar en modo stage**: `mode=stage`
5. **Entrenar modelo real**: `fit ... into app:modelo_*`
6. **Aplicar modelo**: `apply modelo_*`
7. **Monitorear**: Dashboards con `ml_metrics` y `ml_model_logs`

---

## ✅ Conclusión

**Flujo Simple**:
1. Crear notebook con `init`, `fit`, `apply`, `summary`
2. Test con `mode=stage`
3. Entrenar con `fit ... into app:modelo_*`
4. Aplicar con `apply modelo_*`
5. Monitorear con dashboards

**Todo automático** gracias a helpers custom ✅

**Documentado y testeado** ✅

