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
        print(f"✅ HEC Mock: Capturado evento")
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

