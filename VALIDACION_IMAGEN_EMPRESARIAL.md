# Validación: Imagen Empresarial Funcional

**Fecha**: 2025-01-31  
**Estado**: ✅ Contenedor RUNNING  
**Imagen**: `splunk/mltk-container-golden-cpu-empresa-arm:5.2.2`

---

## ✅ Estado Actual

- ✅ Contenedor iniciado exitosamente
- ✅ JupyterLab accesible en https://localhost:8888
- ✅ TensorBoard, MLflow, Spark UI disponibles
- ✅ Image configurada en DSDL

---

## 🧪 Tests de Validación

### 1️⃣ Abrir JupyterLab

1. En DSDL UI: Click **"JUPYTER LAB"**
2. Login con password configurado
3. Verificar que abre sin errores

### 2️⃣ Test Helpers en JupyterLab

**Crear nuevo notebook:**

```python
# Cell 1: Test imports
import sys
sys.path.append("/dltk/notebooks_custom/helpers")

# Test telemetry
try:
    from telemetry_helper import log_metrics, log_training_step
    print("✅ telemetry_helper importado")
except ImportError as e:
    print(f"❌ Error: {e}")

# Test metrics
try:
    from metrics_calculator import calculate_all_metrics
    print("✅ metrics_calculator importado")
except ImportError as e:
    print(f"❌ Error: {e}")

# Test preprocessor
try:
    from preprocessor import standard_preprocessing
    print("✅ preprocessor importado")
except ImportError as e:
    print(f"❌ Error: {e}")

# Test connector
try:
    from splunk_connector import validate_splunk_config
    print("✅ splunk_connector importado")
except ImportError as e:
    print(f"❌ Error: {e}")
```

**Resultado esperado:**
```
✅ telemetry_helper importado
✅ metrics_calculator importado
✅ preprocessor importado
✅ splunk_connector importado
```

### 3️⃣ Test aeon

**Nueva cell:**

```python
# Test aeon (librería custom agregada)
try:
    import aeon
    print(f"✅ aeon version: {aeon.__version__}")
    print(f"✅ aeon ubicación: {aeon.__file__}")
except ImportError as e:
    print(f"❌ Error importando aeon: {e}")
```

**Resultado esperado:**
```
✅ aeon version: 1.1.0
✅ aeon ubicación: /usr/local/lib/python3.9/site-packages/aeon/...
```

### 4️⃣ Test Otras Librerías

**Nueva cell:**

```python
# Test TensorFlow, PyTorch, sklearn
import tensorflow as tf
import torch
import sklearn
import statsmodels
import scipy
import pandas as pd
import numpy as np

print(f"✅ TensorFlow: {tf.__version__}")
print(f"✅ PyTorch: {torch.__version__}")
print(f"✅ sklearn: {sklearn.__version__}")
print(f"✅ statsmodels: {statsmodels.__version__}")
print(f"✅ scipy: {scipy.__version__}")
print(f"✅ pandas: {pd.__version__}")
print(f"✅ numpy: {np.__version__}")
```

### 5️⃣ Abrir Template Empresarial

1. En JupyterLab: File → Open
2. Navegar a `/dltk/notebooks_custom/`
3. Abrir `template_empresa_base.ipynb`
4. Verificar estructura con helpers

### 6️⃣ Test Template Completo

**Copiar template y ejecutar:**

```python
# En JupyterLab, abrir template y descomentar cell de testing
# O crear nuevo notebook con este contenido:

import sys
sys.path.append("/dltk/notebooks_custom/helpers")

from telemetry_helper import log_metrics, log_training_step
from metrics_calculator import calculate_all_metrics
from preprocessor import standard_preprocessing
import pandas as pd
import numpy as np

print("🧪 Test template empresarial completo\n")

# Test 1: Preprocesamiento
print("1️⃣ Preprocesamiento")
df = pd.DataFrame(np.random.rand(100, 10), columns=[f'f{i}' for i in range(10)])
X_processed, scaler = standard_preprocessing(df)
print(f"   ✅ Shape: {df.shape} → {X_processed.shape}")

# Test 2: Métricas
print("\n2️⃣ Cálculo de métricas")
y_true = np.random.randint(0, 2, 100)
y_pred = np.random.randint(0, 2, 100)
metrics = calculate_all_metrics(y_true, y_pred)
print(f"   ✅ Accuracy: {metrics['accuracy']:.3f}")
print(f"   ✅ F1: {metrics['f1']:.3f}")

# Test 3: Telemetría (MOCK)
print("\n3️⃣ Telemetría (MOCK - no enviará a Splunk)")
print("   ⚠️  HEC no configurado, simulando...")
log_metrics(model_name="test_template", r2=0.95, accuracy=0.92)

# Test 4: aeon
print("\n4️⃣ aeon")
import aeon
print(f"   ✅ aeon {aeon.__version__} disponible")

print("\n" + "="*60)
print("✅ Template empresarial FUNCIONANDO")
```

**Resultado esperado:**
```
🧪 Test template empresarial completo

1️⃣ Preprocesamiento
   ✅ Shape: (100, 10) → (100, 10)

2️⃣ Cálculo de métricas
   ✅ Accuracy: 0.550
   ✅ F1: 0.550

3️⃣ Telemetría (MOCK - no enviará a Splunk)
   ⚠️  HEC no configurado, simulando...

4️⃣ aeon
   ✅ aeon 1.1.0 disponible

============================================================
✅ Template empresarial FUNCIONANDO
```

---

## 🧪 Test Datos Real desde Splunk (Opcional)

Si tienes datos en Splunk:

**En Splunk (ejemplo):**

```spl
index=main sourcetype=access_combined | head 1000
| fit MLTKContainer algo=test_template mode=stage _time IP into app:test_data
```

**En JupyterLab:**

```python
df, param = stage("test_data")
print(f"Datos cargados: {df.shape}")
print(df.head())
```

---

## ✅ Checklist de Validación

### Helpers
- [ ] telemetry_helper importa sin errores
- [ ] metrics_calculator importa sin errores
- [ ] preprocessor importa sin errores
- [ ] splunk_connector importa sin errores

### Librerías
- [ ] aeon instalado (1.1.0)
- [ ] TensorFlow instalado (2.20.0)
- [ ] PyTorch instalado (2.8.0)
- [ ] sklearn instalado (1.6.1)
- [ ] statsmodels instalado
- [ ] scipy instalado

### Template
- [ ] template_empresa_base.ipynb existe
- [ ] Template tiene estructura correcta
- [ ] Funciones init/fit/apply presentes
- [ ] Testing cells funcionan

### Funcionalidad
- [ ] Preprocesamiento funciona
- [ ] Métricas se calculan
- [ ] Telemetría (MOCK) se ejecuta
- [ ] Sin errores durante ejecución

---

## 🚨 Troubleshooting

### Error: "No module named telemetry_helper"

**Causa**: Path incorrecto  
**Solución**:
```python
import sys
print(sys.path)
# Agregar correcto
sys.path.append("/dltk/notebooks_custom/helpers")  # ← Verificar path real
```

### Error: "ImportError: cannot import name SplunkHEC"

**Causa**: dsdlsupport no disponible  
**Solución**: Normal en desarrollo. Helpers detectan y usan MOCK automático

### Error: "aeon module not found"

**Causa**: aeon no instalado  
**Solución**: Rebuild imagen o verificar requirements

### Error: "Permission denied en /dltk/notebooks_custom"

**Causa**: Permisos incorrectos  
**Solución**: Rebuild con Dockerfile correcto

---

## 📊 Resultado Esperado

Si todas las validaciones pasan:

**✅ Imagen empresarial 100% funcional**

- Helpers operativos
- aeon disponible
- Template listo
- Científicos de datos pueden comenzar

---

## 🎯 Siguiente Paso: Trabajar con Cristian

Con imagen validada:
1. Compartir acceso a JupyterLab
2. Entregar template empresarial
3. Documentar convención de naming
4. Ejecutar notebook de autoencoder de Cristian

