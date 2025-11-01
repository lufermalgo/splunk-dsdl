# Test Telemetría Real en Splunk

## ❌ Estado Actual

**NO**, los tests locales NO enviaron datos a Splunk porque:
1. Usaron MOCK (simulación en memoria)
2. No hay comunicación real con Splunk
3. Son validaciones de código, no end-to-end

---

## ✅ Para Probar con Splunk Real

### Prerequisitos

1. **Splunk corriendo**
```bash
# Verificar
/Applications/Splunk/bin/splunk status

# Si no está corriendo
/Applications/Splunk/bin/splunk start
```

2. **Índices creados**
- ✅ `ml_metrics` (Metrics)
- ✅ `ml_model_logs` (Events)

3. **HEC Token creado**
- Settings → Data Inputs → HTTP Event Collector → New Token
- Name: `dsdl-ml-telemetry-hec`
- Index: `ml_metrics`
- **COPIAR token**

---

## 🧪 Test Real End-to-End

### Opción A: Usar Contenedor DSDL Activo

**En JupyterLab del contenedor:**

```python
# Importar helpers
import sys
sys.path.append("/dltk/notebooks/helpers")
from telemetry_helper import log_metrics
from metrics_calculator import calculate_all_metrics

# Test con datos sintéticos
import numpy as np
import pandas as pd

y_true = np.random.randint(0, 2, 100)
y_pred = np.random.randint(0, 2, 100)

metrics = calculate_all_metrics(y_true, y_pred)

# Enviar a Splunk REAL
log_metrics(
    model_name="app1_test_model_v1",
    app_name="app1",
    **metrics
)

print("✅ Datos enviados a Splunk")
```

**Verificar en Splunk:**
```spl
index=ml_metrics model_name="app1_test_model_v1"
| head 10
| table _time, model_name, accuracy, f1
```

---

### Opción B: Test desde Mac (sin contenedor)

**Nota**: Requiere Splunk corriendo y HEC configurado

```bash
cd /Users/lufermalgo/Proyectos/Splunk-DSDL

# Crear test con HEC real
cat > test_real_hec.py << 'EOF'
import requests
import json
from datetime import datetime

# Configuración
hec_url = "http://localhost:8088/services/collector/event"
hec_token = "YOUR_HEC_TOKEN_HERE"  # ← PEGAR TOKEN REAL

# Evento de prueba
event = {
    "event": {
        "event_type": "model_metrics",
        "model_name": "app1_test_local_v1",
        "app_name": "app1",
        "timestamp": datetime.now().isoformat(),
        "r2_score": 0.95,
        "accuracy": 0.92,
        "mae": 0.05
    },
    "sourcetype": "ml:metrics",
    "index": "ml_metrics"
}

# Enviar
headers = {
    "Authorization": f"Splunk {hec_token}",
    "Content-Type": "application/json"
}

response = requests.post(hec_url, json=event, headers=headers, verify=False)

print(f"Status: {response.status_code}")
print(f"Response: {response.text}")

if response.status_code == 200:
    print("✅ Evento enviado a Splunk")
else:
    print("❌ Error enviando evento")
EOF

python3 test_real_hec.py
```

**Verificar en Splunk:**
```spl
index=ml_metrics model_name="app1_test_local_v1"
| table _time, model_name, r2_score, accuracy
```

---

## 🎯 Flujo Completo con Template

### Usar template_empresa_base.ipynb

1. **Abrir contenedor DSDL**
   - DSDL → Containers → Start
   - Open JupyterLab

2. **Copiar template**
   - File → Open → `template_empresa_base.ipynb`
   - File → Save As → `MiTest_Autoencoder_v1.ipynb`

3. **Ejecutar cells de test**
   - Descomentar cell de testing
   - Ejecutar cells

4. **Verificar en Splunk**
   ```spl
   index=ml_metrics
   | head 20
   | table _time, model_name, event_type, r2_score, accuracy
   ```

---

## ✅ Checklist de Validación

- [ ] Splunk corriendo
- [ ] Índices creados (ml_metrics, ml_model_logs)
- [ ] HEC habilitado globalmente
- [ ] HEC Token creado y configurado
- [ ] DSDL configurado con HEC Token
- [ ] Contenedor iniciado (si usando JupyterLab)
- [ ] Test ejecutado
- [ ] Datos visibles en Splunk

---

## 🚨 Troubleshooting

### No se ven datos en Splunk

```spl
# Buscar errores HEC
index=_internal "hec" OR "HEC"
| head 50

# Verificar token
index=_internal sourcetype="splunk_health_check"
| head 20
```

### Error "HEC authentication failed"

- Verificar token correcto
- Verificar HEC habilitado globalmente
- Verificar permisos del token al index

### Error "Index not found"

- Crear índice `ml_metrics`
- Verificar nombre correcto
- Verificar permisos del token

---

## 📊 Resultado Esperado

Si todo funciona, en Splunk deberías ver:

```
index=ml_metrics
| head 10

_time                  model_name                      event_type      r2_score    accuracy
2025-01-31 21:30:00   app1_test_model_v1              model_metrics   0.95       0.92
2025-01-31 21:30:05   app1_test_model_v1              model_metrics   0.94       0.91
```

