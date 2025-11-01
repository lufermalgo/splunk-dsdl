# Configurar HEC para Validar Telemetría

**Objetivo**: Hacer que los helpers envíen datos reales a Splunk para validar que la telemetría funciona.

---

## 🔍 Estado Actual

```
⚠️  Error enviando métricas: HTTPConnectionPool(host='localhost', port=8088): 
Max retries exceeded with url: /services/collector/event 
(Caused by NewConnectionError(...))
```

**Causa**: HEC no configurado en DSDL Setup

---

## ✅ Pasos para Configurar HEC

### Paso 1: Crear HEC Token en Splunk

1. **Abrir Splunk Web** (https://localhost:9000)
2. Ir a: **Settings** → **Data Inputs** → **HTTP Event Collector**
3. Click **"New Token"**
4. Configurar:
   - **Name**: `dsdl-ml-hec-token`
   - **App context**: `Search & Reporting`
   - Click **"Next"**
5. Configurar índices:
   - **Indexes**: Seleccionar `ml_metrics` y `ml_model_logs`
   - Click **"Review"**
6. **Copiar el token generado** (guardarlo, no lo verás de nuevo)

**Token va a lucir así:**
```
abcd1234-5678-90ef-ghij-klmnopqrstuv
```

---

### Paso 2: Configurar HEC en DSDL

1. **Abrir DSDL UI** (https://localhost:9000/en-US/app/dsdlt-app/)
2. Ir a: **Setup** → **Splunk HEC Settings**
3. Configurar:
   - **Enable Splunk HEC**: `Yes`
   - **Splunk HEC Token**: Pegar token del Paso 1
   - **Splunk HEC Endpoint URL**: `http://localhost:8088`
4. Click **"Test & Save"**

---

### Paso 3: Reiniciar Contenedor

**⚠️ IMPORTANTE**: DSDL configura HEC en variables de entorno cuando inicia el contenedor.

**Opciones:**

**A) Stop/Start desde DSDL UI:**
1. DSDL → **Containers**
2. Click **"STOP"** en el contenedor activo
3. Esperar 10 segundos
4. Click **"START"**

**B) Restart desde terminal:**
```bash
docker ps | grep empresa-arm
docker restart <CONTAINER_ID>
```

---

### Paso 4: Probar Telemetría

**En JupyterLab, nueva cell:**

```python
import sys
sys.path.append("/srv/notebooks_custom/helpers")
from telemetry_helper import log_metrics

print("🧪 Test telemetría REAL con HEC\n")

log_metrics(
    model_name="test_mi_modelo_v1",
    r2_score=0.95,
    accuracy=0.92,
    f1_score=0.90,
    mae=0.05,
    rmse=0.08
)
```

**Resultado esperado:**
```
✅ Métricas enviadas para test_mi_modelo_v1
```

**Si ves esto**: ✅ HEC funcionando

---

### Paso 5: Verificar en Splunk

**Buscar datos en Splunk:**

```spl
index=ml_metrics
| head 10
| table _time, model_name, r2_score, accuracy, f1_score, event_type
```

**O buscar solo tus métricas:**

```spl
index=ml_metrics model_name="test_mi_modelo_v1"
| table _time, r2_score, accuracy, f1_score
```

---

## 🧪 Test Más Completo

**Enviar múltiples métricas:**

```python
import sys
sys.path.append("/srv/notebooks_custom/helpers")
from telemetry_helper import log_metrics, log_training_step

print("🧪 Test telemetría completa\n")

# Test 1: Métricas de modelo
log_metrics(
    model_name="app1_autoencoder_horno4_v1",
    r2_score=0.95,
    accuracy=0.92,
    f1_score=0.90,
    mae=0.05,
    rmse=0.08
)

# Test 2: Paso de entrenamiento
log_training_step(
    model_name="app1_autoencoder_horno4_v1",
    epoch=50,
    loss=0.023,
    val_loss=0.025
)

# Test 3: Métricas de prueba
log_metrics(
    model_name="app1_autoencoder_horno4_v1",
    test_accuracy=0.93,
    test_f1=0.91,
    test_mae=0.04
)

print("\n✅ Telemetría enviada. Verificar en Splunk:")
print("   index=ml_metrics model_name=\"app1_autoencoder_horno4_v1\"")
```

---

## 📊 Búsquedas Útiles en Splunk

### Ver todas las métricas de un modelo
```spl
index=ml_metrics model_name="app1_autoencoder_horno4_v1"
| timechart latest(r2_score) as r2, latest(accuracy) as accuracy, latest(f1_score) as f1
```

### Ver pasos de entrenamiento
```spl
index=ml_model_logs event_type="training_step"
| timechart avg(loss) as avg_loss, avg(val_loss) as avg_val_loss by model_name
```

### Ver errores
```spl
index=ml_model_logs event_type="error"
| table _time, model_name, error_message, error_traceback
```

### Dashboard de modelos
```spl
index=ml_metrics
| stats latest(*) by model_name
| table model_name, r2_score, accuracy, f1_score, mae, rmse
```

---

## 🚨 Troubleshooting

### Error: "Connection refused"

**Causa**: HEC no configurado o contenedor no reiniciado

**Solución**:
1. Verificar DSDL Setup → HEC enabled
2. Reiniciar contenedor
3. Verificar token correcto

### No aparecen datos en Splunk

**Causa**: Token con permisos incorrectos o índice incorrecto

**Solución**:
1. Settings → Data Inputs → HTTP Event Collector
2. Editar token `dsdl-ml-hec-token`
3. Verificar índices permitidos incluyen `ml_metrics` y `ml_model_logs`

### Error: "Invalid token"

**Causa**: Token incorrecto copiado

**Solución**:
1. Verificar token en DSDL Setup
2. Volver a copiar desde Data Inputs
3. Reconfigurar DSDL

---

## ✅ Checklist Post-Configuración

- [ ] HEC Token creado en Splunk
- [ ] Token configurado en DSDL Setup
- [ ] Contenedor reiniciado
- [ ] Test telemetry_helper ejecutado
- [ ] Datos visibles en `index=ml_metrics`
- [ ] Dashboard básico funcionando

---

## 🎯 Resultado Esperado

**Después de configurar HEC:**

```
✅ Métricas enviadas para test_mi_modelo_v1
✅ Datos visibles en Splunk
✅ Timechart funcionando
✅ Dashboard operativo
```

**El ecosistema está 100% funcional.**

