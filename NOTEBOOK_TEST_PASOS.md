# Pasos para Probar el Notebook en JupyterLab

**Objetivo**: Validar que helpers, aeon y template empresarial funcionan

---

## 📋 Checklist Pre-JupyterLab

- [x] notebooks_custom visible en JupyterLab
- [ ] Crear nuevo notebook o abrir template

---

## 🧪 Test 1: Verificar Helpers

**En JupyterLab, crear nueva cell:**

```python
# Test import helpers
import sys
sys.path.append("/srv/notebooks_custom/helpers")

print("🧪 Test 1: Importando helpers\n")

try:
    from telemetry_helper import log_metrics, log_training_step
    print("✅ telemetry_helper importado")
except ImportError as e:
    print(f"❌ Error telemetry: {e}")

try:
    from metrics_calculator import calculate_all_metrics
    print("✅ metrics_calculator importado")
except ImportError as e:
    print(f"❌ Error metrics: {e}")

try:
    from preprocessor import standard_preprocessing
    print("✅ preprocessor importado")
except ImportError as e:
    print(f"❌ Error preprocessor: {e}")

try:
    from splunk_connector import validate_splunk_config
    print("✅ splunk_connector importado")
except ImportError as e:
    print(f"❌ Error connector: {e}")
```

---

## 🧪 Test 2: Verificar aeon

**Nueva cell:**

```python
# Test aeon
print("\n🧪 Test 2: Verificando aeon\n")

try:
    import aeon
    print(f"✅ aeon version: {aeon.__version__}")
    print(f"✅ aeon ubicación: {aeon.__file__}")
except ImportError as e:
    print(f"❌ Error importando aeon: {e}")
```

---

## 🧪 Test 3: Test Métricas

**Nueva cell:**

```python
# Test cálculo de métricas
print("\n🧪 Test 3: Probando metrics_calculator\n")

from metrics_calculator import calculate_all_metrics
import numpy as np

# Datos de prueba
y_true = np.array([1, 1, 0, 0, 1])
y_pred = np.array([1, 0, 0, 0, 1])

metrics = calculate_all_metrics(y_true, y_pred)
print(f"Accuracy: {metrics['accuracy']:.3f}")
print(f"F1: {metrics['f1']:.3f}")
print(f"Precision: {metrics['precision']:.3f}")
print(f"Recall: {metrics['recall']:.3f}")
```

**Resultado esperado:**
```
Accuracy: 0.800
F1: 0.667
Precision: 1.000
Recall: 0.667
```

---

## 🧪 Test 4: Test Preprocesamiento

**Nueva cell:**

```python
# Test preprocesamiento
print("\n🧪 Test 4: Probando preprocessor\n")

from preprocessor import standard_preprocessing
import pandas as pd
import numpy as np

# Datos sintéticos
df = pd.DataFrame(np.random.rand(10, 5), columns=[f'feature_{i}' for i in range(5)])
print(f"Shape original: {df.shape}")

X_processed, scaler = standard_preprocessing(df)
print(f"Shape procesado: {X_processed.shape}")
print(f"✅ Preprocesamiento exitoso")
```

---

## 🧪 Test 5: Test Telemetría (MOCK)

**Nueva cell:**

```python
# Test telemetría (simulación)
print("\n🧪 Test 5: Probando telemetry_helper (MOCK)\n")

from telemetry_helper import log_metrics

# Simular envío de métricas (no enviará realmente a Splunk sin HEC)
log_metrics(
    model_name="test_mi_modelo_v1",
    r2_score=0.95,
    accuracy=0.92,
    f1_score=0.90,
    mae=0.05,
    rmse=0.08
)

print("✅ Telemetría mock ejecutada")
```

---

## 🎯 ¿Qué Esperar?

Si todos los tests pasan:

```
✅ Helpers importables
✅ aeon funcionando
✅ Métricas calculándose
✅ Preprocesamiento OK
✅ Telemetría simulada OK

🎉 Ecosistema empresarial 100% funcional
```

---

## 📝 Siguiente Paso

Una vez validado, puedes:
1. Abrir template_empresa_base.ipynb
2. Copiarlo para tu modelo
3. Personalizar init/fit/apply
4. Entrenar modelo real

