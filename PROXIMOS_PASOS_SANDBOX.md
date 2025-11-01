# Próximos Pasos - Sandbox DSDL Funcional

**Fecha**: 2025-01-31  
**Status**: ✅ Sandbox operacional

---

## 🎉 Estado Actual

### ✅ Completado

- [x] Splunk Enterprise 9.4.1 configurado
- [x] Apps MLTK, PSC, DSDL instaladas
- [x] Golden Image descargada (7.42 GB)
- [x] Errores OpenSSL y puerto 5000 resueltos
- [x] DSDL configurado y conectado
- [x] Contenedor DEV iniciado (`kind_hugle`)
- [x] JupyterLab accesible en https://localhost:8888

### 📊 Recursos Disponibles

**Contenedor**: `kind_hugle`  
**Imagen**: `splunk/mltk-container-golden-cpu:5.2.2`  
**Puertos**: 5000 (DSDL API), 8888 (JupyterLab), 6060 (MLflow), 4040 (Spark), 6006 (TensorBoard)

**Notebooks Disponibles**: 30+ notebooks predefinidos incluyendo:
- `barebone_template.ipynb` - Template base
- `autoencoder.ipynb` - Ejemplo de autoencoder
- `anomaly_detection_ecod.ipynb` - Detección de anomalías
- `binary_nn_classifier.ipynb` - Clasificador binario
- Y más...

---

## 🚀 Próximas Acciones

### 1. Explorar Notebooks Base

**Desde JupyterLab** (`https://localhost:8888`):

1. **Abrir `barebone_template.ipynb`**
   - Ver estructura base de DSDL
   - Entender funciones `fit`, `apply`, `summary`
   - Revisar imports y configuración

2. **Abrir `autoencoder.ipynb`**
   - Comparar con notebooks de Cristian
   - Identificar similitudes/diferencias
   - Evaluar librerías usadas

3. **Abrir `anomaly_detection_ecod.ipynb`**
   - Otra aproximación a detección de anomalías
   - Comparar algoritmos

---

### 2. Validar Librerías Disponibles

**Ejecutar en terminal JupyterLab o notebook**:

```python
import pandas as pd
import numpy as np
import tensorflow as tf
import torch

print(f"Pandas: {pd.__version__}")
print(f"NumPy: {np.__version__}")
print(f"TensorFlow: {tf.__version__}")
print(f"PyTorch: {torch.__version__}")

# Verificar librerías de Cristian
try:
    import aeon
    print(f"✓ aeon: {aeon.__version__}")
except ImportError:
    print("✗ aeon: NO disponible (requiere custom image)")

try:
    import statsmodels
    print(f"✓ statsmodels: {statsmodels.__version__}")
except ImportError:
    print("✗ statsmodels: NO disponible")

try:
    import scipy
    print(f"✓ scipy: {scipy.__version__}")
except ImportError:
    print("✗ scipy: NO disponible")
```

---

### 3. Preparar Datos de Prueba en Splunk

**Crear índice de prueba**:

```spl
# Desde Splunk Search
index=_internal | head 10000 | eval random_field=random()%100
  | stats count by random_field, sourcetype
  | outputlookup test_data.csv
```

**O usar datos sintéticos**:

```python
# En JupyterLab notebook
import pandas as pd
import numpy as np

# Generar datos sintéticos para prueba
np.random.seed(42)
data = {
    'timestamp': pd.date_range('2024-01-01', periods=1000, freq='5min'),
    'temperature': np.random.normal(75, 5, 1000),
    'pressure': np.random.normal(30, 2, 1000),
    'flow_rate': np.random.normal(100, 10, 1000)
}
df = pd.DataFrame(data)
print(df.head())
```

---

### 4. Ejecutar Ejemplo Predefinido

**Desde DSDL UI**:

1. Ir a **Examples**
2. Seleccionar **"Neural Network Classifier Example for Tensorflow"**
3. Click **"Run"**
4. Observar salida y métricas

**Desde JupyterLab**:

1. Abrir `autoencoder.ipynb`
2. Ejecutar celdas secuencialmente
3. Verificar que funciona sin errores

---

### 5. Adaptar Notebook de Cristian

**Workflow sugerido**:

1. **Copiar notebook de Cristian** a JupyterLab
   - Arrastrar archivo `.ipynb` a JupyterLab
   - O usar File → Upload

2. **Adaptar estructura DSDL**:
   - Agregar imports necesarios
   - Crear función `fit(df, **kwargs)` si no existe
   - Crear función `apply(df, **kwargs)` si no existe
   - Opcional: `summary(model)`

3. **Probar ejecución**:
   - Ejecutar celdas individuales
   - Verificar datos cargados
   - Validar entrenamiento

4. **Guardar**:
   - File → Save As
   - Nombre: `Cristian_Autoencoder_Horno4_v1.ipynb`
   - **NO usar espacios en nombres**

---

### 6. Validar Flujo End-to-End desde Splunk

**Ejecutar comando SPL de prueba**:

```spl
| makeresults count=100
| eval feature1=random()%100, feature2=random()%50, feature3=random()%200
| fit MLTKContainer algo=autoencoder mode=stage into app:my_test_model
| table *
```

**Verificar**:
- Datos enviados correctamente
- Modelo entrenado
- Resultados devueltos

---

## 📋 Tareas para Sesión con Cristian

### Demostración (30 min)

1. ✅ Mostrar JupyterLab funcionando (5 min)
2. ✅ Ejecutar ejemplo predefinido (10 min)
3. ✅ Revisar notebooks de Cristian (10 min)
4. ✅ Identificar gaps y soluciones (5 min)

### Desarrollo Conjunto (60 min)

1. **Seleccionar notebook de Cristian**
   - Quizás: `anomalias_ej_corona.ipynb` (Conv1D + IsolationForest)
2. **Adaptar a DSDL**
   - Agregar estructura `fit`/`apply`
   - Testear librerías disponibles
3. **Probar flujo end-to-end**
   - Datos desde Splunk → Training → Inference

---

## 🔍 Validaciones Pendientes

### Librerías

| Librería | Estado Esperado | Acción Si Falta |
|----------|----------------|-----------------|
| TensorFlow | ✅ Incluida | - |
| Keras | ✅ Incluida | - |
| scikit-learn | ✅ Incluida | - |
| Pandas, NumPy | ✅ Incluida | - |
| Matplotlib, Seaborn | ✅ Incluida | - |
| aeon | ❌ Faltante | Crear custom image |
| statsmodels | ✅ Incluida | - |
| scipy | ✅ Incluida | - |

---

### Funcionalidades DSDL

| Feature | Verificar |
|---------|-----------|
| Mode=stage (push data to notebook) | ✅ Probar |
| SplunkSearch (pull data from Splunk) | ⚠️ Configurar token |
| SplunkHEC (send results back) | ⚠️ Configurar HEC |
| Auto-export .py from .ipynb | ✅ Probar guardar |
| ML-SPL fit/apply/summary | ✅ Probar comando |

---

## 📚 Documentación de Referencia

### Guías Disponibles

- `ANALISIS_COMPARATIVO_DSDL.md` - Análisis completo
- `CONFIGURACION_DSDL.md` - Configuración detallada
- `LANZAMIENTO_CONTENEDOR.md` - Iniciar contenedores
- `SANDBOX_FUNCIONAL.md` - Estado actual
- `SOLUCION_OPENSSL_ERROR.md` - Fix OpenSSL
- `SOLUCION_PUERTO_5000.md` - Fix AirPlay

### Notebooks de Cristian

- `Cristian-Autoencoder-Ejemplos/` - 13 notebooks
- Notebooks clave identificados:
  - `anomalias_ej_corona.ipynb`
  - `autoencoder_corona_esfuerzo_ejemplo`
  - Otros con Conv1D, IsolationForest, etc.

---

## 🎯 Objetivos Corto Plazo

### Esta Semana

- [ ] Validar todas las librerías disponibles
- [ ] Ejecutar 1-2 ejemplos predefinidos
- [ ] Adaptar 1 notebook de Cristian básico
- [ ] Probar `mode=stage` con datos reales

### Próxima Semana

- [ ] Sesión con Cristian: demostración + desarrollo
- [ ] Evaluar necesidad de custom image con `aeon`
- [ ] Documentar template base para empresa
- [ ] Planear migración a GCP/Azure

---

## ⚠️ Problemas Conocidos y Soluciones

### AirPlay Puerto 5000

**Problema**: Se reactiva al reiniciar macOS  
**Solución temporal**: Ejecutar script al iniciar Mac
```bash
#!/bin/bash
# ~/bin/disable-airplay.sh
defaults write com.apple.controlcenter.plist AirplayRecieverEnabled -bool false
killall ControlCenter 2>/dev/null
```

**Agregar a login items**:
- System Settings → General → Login Items
- Agregar script

### Persistencia de Notebooks

**Problema**: Notebooks en contenedor ephemeral  
**Solución**: 
- Usar Git desde JupyterLab (terminal)
- O montar volumen persistente en Docker

### Custom Image con `aeon`

**Cuando**: Si Cristian requiere `aeon` y no está en golden image  
**Cómo**: Seguir guía en `ANALISIS_COMPARATIVO_DSDL.md` sección 9.4

---

## 📊 Métricas de Éxito

### Sandbox Local ✅

- Contenedor iniciado exitosamente
- JupyterLab accesible
- Sin errores de configuración

### Próximos Hitos

- [ ] Primer ejemplo ejecutado end-to-end
- [ ] Primer notebook de Cristian adaptado
- [ ] Datos reales procesados
- [ ] Modelo producido consumido desde Splunk

---

## 🔗 Enlaces Útiles

### Splunk DSDL

- **JupyterLab**: https://localhost:8888
- **DSDL API**: https://localhost:5000
- **MLflow**: http://localhost:6060
- **TensorBoard**: http://localhost:6006
- **Spark**: http://localhost:4040

### Documentación

- **Repositorio**: https://github.com/lufermalgo/splunk-dsdl
- **Splunkbase MLTK**: https://splunkbase.splunk.com/app/2890/
- **Splunkbase DSDL**: https://splunkbase.splunk.com/app/4607/
- **GitHub DSDL**: https://github.com/splunk/splunk-mltk-container-docker

---

**Estado**: ✅ Sandbox listo para desarrollo  
**Próximo**: Explorar notebooks y validar librerías

