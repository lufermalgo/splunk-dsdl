# Testing Helpers Localmente (Sin Contenedor)

## 🎯 Propósito

Probar helpers empresariales **localmente en tu Mac** antes de construir la imagen Docker.

---

## 📋 Prerequisitos

### Python 3.9+

```bash
python3 --version  # Debe ser >= 3.9
```

### Instalar Librerías

```bash
cd /Users/lufermalgo/Proyectos/Splunk-DSDL

# Crear entorno virtual
python3 -m venv venv_dsdl
source venv_dsdl/bin/activate

# Instalar librerías base
pip install numpy pandas scikit-learn tensorflow

# MOCK de dsdlsupport (para pruebas)
pip install requests  # Para HEC mock
```

---

## 🧪 Test 1: metrics_calculator

### Crear script de test

```bash
cd /Users/lufermalgo/Proyectos/Splunk-DSDL
cat > test_metrics.py << 'EOF'
# test_metrics.py
import sys
sys.path.append('splunk-mltk-container-docker/notebooks_custom/helpers')

from metrics_calculator import calculate_all_metrics, calculate_regression_metrics, calculate_classification_metrics
import numpy as np

print("🧪 Testing metrics_calculator...\n")

# Test 1: Clasificación
print("Test 1: Clasificación")
y_true_cls = np.array([0, 1, 1, 0, 1, 0, 0, 1])
y_pred_cls = np.array([0, 1, 1, 0, 1, 0, 1, 1])  # 1 error
metrics_cls = calculate_all_metrics(y_true_cls, y_pred_cls)
print(f"  Accuracy: {metrics_cls['accuracy']:.3f}")
print(f"  F1: {metrics_cls['f1']:.3f}")
print()

# Test 2: Regresión
print("Test 2: Regresión")
y_true_reg = np.array([10.5, 20.3, 15.7, 25.1, 12.4])
y_pred_reg = np.array([10.2, 20.5, 15.3, 25.4, 12.1])
metrics_reg = calculate_regression_metrics(y_true_reg, y_pred_reg)
print(f"  R²: {metrics_reg['r2']:.3f}")
print(f"  MAE: {metrics_reg['mae']:.3f}")
print(f"  RMSE: {metrics_reg['rmse']:.3f}")
print()

print("✅ metrics_calculator funciona correctamente")
EOF

python3 test_metrics.py
```

---

## 🧪 Test 2: preprocessor

```bash
cat > test_preprocessor.py << 'EOF'
# test_preprocessor.py
import sys
sys.path.append('splunk-mltk-container-docker/notebooks_custom/helpers')

from preprocessor import standard_preprocessing, apply_preprocessing
import pandas as pd
import numpy as np

print("🧪 Testing preprocessor...\n")

# Crear datos de prueba
df = pd.DataFrame({
    'feature1': [1, 2, 3, 4, 5, None, 7, 8],
    'feature2': [10, 20, 30, 40, 50, 60, 70, 80],
    'target': [100, 200, 300, 400, 500, 600, 700, 800]
})

print(f"Original shape: {df.shape}")
print(f"Nulls: {df.isnull().sum().sum()}")

# Preprocesar
X_processed, scaler = standard_preprocessing(df, scaler_type='standard')

print(f"Processed shape: {X_processed.shape}")
print(f"Nulls after: {X_processed.isnull().sum().sum()}")
print()

# Aplicar a nuevos datos
df_new = pd.DataFrame({
    'feature1': [6, 9],
    'feature2': [90, 100],
    'target': [900, 1000]
})
X_new = apply_preprocessing(df_new, scaler)
print(f"New data processed: {X_new.shape}")

print("✅ preprocessor funciona correctamente")
EOF

python3 test_preprocessor.py
```

---

## 🧪 Test 3: telemetry_helper (MOCK)

```bash
cat > test_telemetry.py << 'EOF'
# test_telemetry.py
import sys
import os

# MOCK dsdlsupport antes de importar helpers
class MockSplunkHEC:
    def __init__(self, url="", token=""):
        self.url = url or "http://localhost:8088/services/collector/event"
        self.token = token or "mock-token"
        self.sent_events = []
    
    def send(self, events):
        """Capturar eventos en memoria en vez de enviar a Splunk"""
        self.sent_events.append(events)
        print(f"  📤 Mock HEC: {len(events)} eventos capturados")
        return type('Response', (), {'status_code': 200, 'text': '{"text":"Success","code":0}'})()

# Crear módulo mock
import importlib.util
spec = importlib.util.spec_from_loader('dsdlsupport', loader=None)
dsdlsupport = importlib.util.module_from_spec(spec)

# Crear sub-módulo SplunkHEC
class SplunkHECMock:
    SplunkHEC = MockSplunkHEC

dsdlsupport.SplunkHEC = SplunkHECMock
sys.modules['dsdlsupport'] = dsdlsupport

# Ahora importar helper
sys.path.append('splunk-mltk-container-docker/notebooks_custom/helpers')

from telemetry_helper import log_metrics, log_training_step

print("🧪 Testing telemetry_helper (MOCK)...\n")

# Test 1: Métricas
print("Test 1: log_metrics")
log_metrics(
    model_name="test_model",
    r2=0.95,
    accuracy=0.92,
    mae=0.05
)

# Test 2: Training
print("\nTest 2: log_training_step")
log_training_step(
    model_name="test_model",
    epoch=50,
    loss=0.023
)

print("\n✅ telemetry_helper funciona correctamente (MOCK)")
EOF

python3 test_telemetry.py
```

---

## 🧪 Test 4: splunk_connector

```bash
cat > test_splunk_connector.py << 'EOF'
# test_splunk_connector.py
import sys
sys.path.append('splunk-mltk-container-docker/notebooks_custom/helpers')

from splunk_connector import validate_splunk_config, get_splunk_config

print("🧪 Testing splunk_connector...\n")

# Test 1: Config actual
print("Test 1: get_splunk_config")
config = get_splunk_config()
print(f"  Host: {config['host']}")
print(f"  HEC URL: {config['hec_url']}")
print(f"  HEC Token: {config['hec_token']}")
print()

# Test 2: Validate (sin config)
print("Test 2: validate_splunk_config")
result = validate_splunk_config()
print(f"  Configurado: {result}")

print("\n✅ splunk_connector funciona correctamente")
EOF

python3 test_splunk_connector.py
```

---

## 🎯 Test Completo End-to-End

### Crear test completo

```bash
cat > test_all_helpers.py << 'EOF'
# test_all_helpers.py
"""
Test completo de helpers empresariales
Simula flujo de DS trabajando con autoencoder
"""

import sys
import os

# Setup MOCK
class MockSplunkHEC:
    def __init__(self, url="", token=""):
        self.sent_events = []
    
    def send(self, events):
        self.sent_events.append(events)
        print(f"✅ HEC Mock: {len(events)} eventos capturados")
        return type('Response', (), {'status_code': 200})()

import importlib.util
spec = importlib.util.spec_from_loader('dsdlsupport', loader=None)
dsdlsupport = importlib.util.module_from_spec(spec)

class SplunkHECMock:
    SplunkHEC = MockSplunkHEC
dsdlsupport.SplunkHEC = SplunkHECMock
sys.modules['dsdlsupport'] = dsdlsupport

# Importar helpers
sys.path.append('splunk-mltk-container-docker/notebooks_custom/helpers')

from telemetry_helper import log_metrics, log_training_step
from metrics_calculator import calculate_all_metrics
from preprocessor import standard_preprocessing
import pandas as pd
import numpy as np

print("🎯 Test End-to-End: Simulación Autoencoder\n")
print("=" * 60)

# Simular datos
np.random.seed(42)
X = np.random.rand(100, 10)
df = pd.DataFrame(X, columns=[f'feature_{i}' for i in range(10)])

# Preprocesar
print("\n1️⃣ Preprocesamiento")
X_processed, scaler = standard_preprocessing(df, scaler_type='standard')
print(f"   ✅ Shape: {df.shape} → {X_processed.shape}")

# Simular entrenamiento
print("\n2️⃣ Entrenamiento simulado")
epochs = 10
for epoch in range(1, epochs + 1):
    # Simular pérdida decreciente
    loss = 0.5 * (0.9 ** epoch)
    log_training_step(
        model_name="app1_autoencoder_horno4_v1",
        epoch=epoch,
        loss=loss
    )

# Simular predicciones
print("\n3️⃣ Evaluación")
y_true = np.random.randint(0, 2, 100)
y_pred = np.random.randint(0, 2, 100)
metrics = calculate_all_metrics(y_true, y_pred)

print(f"   ✅ Accuracy: {metrics['accuracy']:.3f}")
print(f"   ✅ F1: {metrics['f1']:.3f}")

# Loggear métricas
print("\n4️⃣ Envío de métricas")
log_metrics(
    model_name="app1_autoencoder_horno4_v1",
    app_name="app1",
    model_version="1.0.0",
    owner="cristian",
    project="horno4_anomalies",
    **metrics
)

print("\n" + "=" * 60)
print("✅ Test completo exitoso!")
print("\n📊 Resumen:")
print(f"   • Epochs loggeados: {epochs}")
print(f"   • Métricas calculadas: {len([k for k in metrics if metrics[k] is not None])}")
print(f"   • Helpers funcionando: ✅")
EOF

python3 test_all_helpers.py
```

---

## ✅ Verificación

### Ejecutar todos los tests

```bash
cd /Users/lufermalgo/Proyectos/Splunk-DSDL

echo "🧪 Ejecutando suite completa de tests..."
echo ""

python3 test_metrics.py && \
python3 test_preprocessor.py && \
python3 test_telemetry.py && \
python3 test_splunk_connector.py && \
python3 test_all_helpers.py

echo ""
echo "✅ Todos los tests pasaron!"
```

---

## 📋 Resultados Esperados

Si todo funciona, deberías ver:

```
🧪 Testing metrics_calculator...
Test 1: Clasificación
  Accuracy: 0.875
  F1: 0.857
Test 2: Regresión
  R²: 0.999
  MAE: 0.240
  RMSE: 0.265
✅ metrics_calculator funciona correctamente

🧪 Testing preprocessor...
✅ preprocessor funciona correctamente

🧪 Testing telemetry_helper (MOCK)...
✅ telemetry_helper funciona correctamente (MOCK)

✅ Todos los tests pasaron!
```

---

## 🚨 Troubleshooting

### Error: "No module named dsdlsupport"

**Solución**: El MOCK ya está incluido en los scripts de test.

### Error: "sklearn no installed"

```bash
pip install scikit-learn
```

### Error: "tensorflow no installed"

```bash
pip install tensorflow-cpu  # o tensorflow si tienes GPU
```

---

## 🎯 Ventajas de Testear Localmente

- ✅ Validar helpers antes del build
- ✅ Iteración rápida sin Docker
- ✅ Debugging más fácil
- ✅ Confirmar lógica independiente de Splunk

---

## 🚀 Siguiente Paso

Después de validar localmente:
1. Build imagen Docker
2. Test dentro del contenedor
3. Verificar que helpers siguen funcionando

