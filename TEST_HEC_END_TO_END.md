# Test End-to-End: Validar Telemetría REAL en Splunk

**Objetivo**: Confirmar que HEC funciona y los datos llegan a Splunk

---

## 🔍 Estado Actual

- ✅ HEC configurado en DSDL
- ✅ Token presente en contenedor
- ⚠️ Error "Connection refused" al enviar

---

## 📋 Diagnóstico Paso a Paso

### 1️⃣ Verificar HEC Enabled en Splunk

**En Splunk Web:**
1. Settings → Data Inputs
2. Verificar que **"HTTP Event Collector"** dice **"Enabled"**
3. Si dice **"Disabled"**, click **"Enable"**

---

### 2️⃣ Verificar Token Existente

**El token configurado es:**
```
88af8cd6-1b92-48f5-86f6-f3f4445aa1f0
```

**Para verificar en Splunk:**
1. Settings → Data Inputs → HTTP Event Collector
2. Ver tokens existentes
3. Verificar que el token anterior aparece

---

### 3️⃣ Verificar Índices Asociados al Token

1. Click en el token `88af8cd6-1b92-48f5-86f6-f3f4445aa1f0`
2. Ver **"Allowed Indexes"**
3. Verificar que incluye índices donde quieres guardar datos

**Si NO existen ml_metrics ni ml_model_logs:**
- El token puede apuntar a `main`
- O no tiene índices asignados

---

### 4️⃣ Crear Índices (Si No Existen)

**A) En Splunk Web:**

1. Settings → Indexes → New Index
2. Crear primer índice:
   - **Name**: `ml_metrics`
   - **Type**: `Metrics` (o `Events` si no hay opción Metrics)
   - Click **"Save"**
3. Crear segundo índice:
   - **Name**: `ml_model_logs`
   - **Type**: `Events`
   - Click **"Save"**

**B) Vía CLI:**

```bash
# Conectar a Splunk CLI
/Applications/Splunk/bin/splunk cmd

# Crear índice metrics (si soportado)
./splunk add index ml_metrics -dataType metric

# Crear índice events
./splunk add index ml_model_logs

# Verificar
./splunk list indexes
```

---

### 5️⃣ Actualizar Token con Índices Correctos

1. Settings → Data Inputs → HTTP Event Collector
2. Click en token `88af8cd6-1b92-48f5-86f6-f3f4445aa1f0`
3. Click **"Edit"**
4. En **"Allowed Indexes"**, seleccionar:
   - `ml_metrics`
   - `ml_model_logs`
   - (o `main` si prefieres probar ahí primero)
5. Click **"Update"**

---

### 6️⃣ Reiniciar Contenedor DSDL

**Desde DSDL UI:**
1. Containers → **STOP**
2. Esperar 10 segundos
3. **START**

**O desde terminal:**
```bash
docker restart ad5dc0f16592
```

---

### 7️⃣ Test Simple desde JupyterLab

**En JupyterLab, crear cell:**

```python
import sys
sys.path.append("/srv/notebooks_custom/helpers")
from telemetry_helper import log_metrics

print("🧪 Test HEC simple\n")

# Enviar una métrica simple
log_metrics(
    model_name="test_hec_v1",
    r2_score=0.99,
    accuracy=0.98
)
```

**Resultado esperado:**
```
✅ Métricas enviadas para test_hec_v1
```

---

### 8️⃣ Verificar en Splunk

**Buscar datos:**

```spl
index=main model_name="test_hec_v1"
| head 10
| table _time, model_name, r2_score, accuracy, event_type
```

**O si usaste índices específicos:**

```spl
index=ml_metrics OR index=ml_model_logs
| head 10
```

---

## 🚨 Troubleshooting

### Error: "Connection refused"

**Causas posibles:**

1. **HEC no habilitado en Splunk**
   - Settings → Data Inputs → HTTP Event Collector → Enable

2. **Puerto 8088 no accesible**
   ```bash
   # Verificar que Splunk escucha en 8088
   lsof -i :8088
   
   # Debería mostrar splunkd escuchando
   ```

3. **Firewall bloqueando**
   - Para localhost, no debería ser problema

### Error: "Invalid token"

**Causa**: Token incorrecto o expirado

**Solución**: 
1. Verificar token en DSDL Setup
2. Comparar con token en Splunk
3. Si no coincide, volver a configurar

### Datos no aparecen en Splunk

**Posibles causas:**

1. **Token sin índice asignado**
   - Editar token y agregar índices

2. **Índice no existe**
   - Crear ml_metrics y ml_model_logs

3. **Permisos incorrectos**
   - Token debe tener permisos de escritura al índice

---

## 📊 Test Más Completo

**Una vez que el básico funciona:**

```python
import sys
sys.path.append("/srv/notebooks_custom/helpers")
from telemetry_helper import log_metrics, log_training_step, log_error
import numpy as np

print("🧪 Test HEC completo\n")

# Test 1: Métricas de modelo
log_metrics(
    model_name="app1_autoencoder_demo_v1",
    r2_score=0.95,
    accuracy=0.92,
    f1_score=0.90,
    precision=0.91,
    recall=0.89,
    mae=0.05,
    rmse=0.08
)

# Test 2: Paso de entrenamiento
log_training_step(
    model_name="app1_autoencoder_demo_v1",
    epoch=50,
    loss=0.023,
    val_loss=0.025,
    learning_rate=0.001
)

# Test 3: Error simulado
try:
    raise ValueError("Test error")
except Exception as e:
    log_error(
        model_name="app1_autoencoder_demo_v1",
        error_message=str(e),
        error_type=type(e).__name__
    )

print("\n✅ Todos los tests ejecutados")
print("📊 Verificar en Splunk:")
print("   index=ml_metrics OR index=ml_model_logs")
```

---

## ✅ Checklist Final

- [ ] HEC enabled en Splunk
- [ ] Token existe y es correcto
- [ ] Índices ml_metrics y ml_model_logs creados
- [ ] Token tiene permisos a índices
- [ ] Contenedor reiniciado después de cambios
- [ ] Test simple ejecutado
- [ ] Datos visibles en Splunk
- [ ] Timechart funcionando

---

## 🎯 Resultado Esperado

**Después de completar los pasos:**

```
✅ Métricas enviadas para test_hec_v1
✅ Datos en Splunk (index=main o index=ml_metrics)
✅ Dashboard funcionando
✅ Ecosistema 100% validado
```

