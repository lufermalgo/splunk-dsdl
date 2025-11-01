# Solución: HEC Connection Refused en macOS

**Problema**: `Connection refused` al enviar telemetría desde contenedor

**Error**: 
```
HTTPConnectionPool(host='localhost', port=8088): Max retries exceeded
```

---

## 🔍 Análisis

### Test realizado
```bash
docker exec ad5dc0f16592 curl -s http://host.docker.internal:8088/services/collector/event \
  -H "Authorization: Splunk 88af8cd6-1b92-48f5-86f6-f3f4445aa1f0" \
  -d '{"event": {"test": "hello"}}'

Resultado: {"text":"Success","code":0}
```

✅ **host.docker.internal:8088 funciona**  
❌ **localhost:8088 NO funciona** desde contenedor

---

## 📋 Causa Raíz

**DSDL configura HEC con URL**: `http://localhost:8088`

**En contenedores Docker**:
- `localhost` = dentro del contenedor mismo ❌
- `host.docker.internal` = host real de macOS ✅
- `172.17.0.1` = Docker bridge gateway (también funcionaría)

**DSDL no detecta automáticamente que debe usar host.docker.internal en macOS/Docker Desktop.**

---

## ✅ Soluciones

### Solución 1: Cambiar URL de HEC en DSDL Setup

**En Splunk Web**:
1. Ir a: **DSDL → Setup → Splunk HEC Settings**
2. Cambiar:
   - **Splunk HEC Endpoint URL**: `http://localhost:8088` 
   - **A**: `http://host.docker.internal:8088`
3. Click **"Test & Save"**
4. **Reiniciar contenedor**

**Ventajas**: Solución correcta y permanente  
**Desventajas**: Requiere config manual por usuario

---

### Solución 2: Modificar helpers para detectar Docker

**En `telemetry_helper.py`**:

```python
import os

def get_hec_url():
    """Detectar URL correcta según entorno"""
    base_url = os.getenv('splunk_hec_url', 'http://localhost:8088')
    
    # Si estamos en Docker, reemplazar localhost
    if 'container' in os.getenv('HOSTNAME', '').lower():
        base_url = base_url.replace('localhost', 'host.docker.internal')
    
    return base_url

def log_metrics(...):
    hec = init_hec()
    if hec is None:
        return
    
    # Obtener URL corregida
    hec.url = get_hec_url()
    
    # ... resto del código
```

**Problema**: `SplunkHEC()` se inicializa automáticamente con URL de env vars.

---

### Solución 3: Modificar variable de entorno en contenedor

**Intentar en runtime**:

```python
import os
os.environ['splunk_hec_url'] = 'http://host.docker.internal:8088'

# Luego importar
from telemetry_helper import log_metrics
```

**Problema**: Variables de entorno ya leídas por SplunkHEC al importar.

---

### Solución 4: Reconfigure Splunk HEC Endpoint via UI

**La más práctica**:

**Pasos**:
1. Abrir Splunk Web: https://localhost:9000
2. Ir a: **DSDL App → Configuration → Setup**
3. Scroll a **"Splunk HEC Settings"**
4. Editar campo **"Splunk HEC Endpoint URL"**:
   - De: `http://localhost:8088`
   - A: `http://host.docker.internal:8088`
5. Click **"Test & Save"**
6. **Volver a Containers UI** → **STOP** → Esperar → **START**

---

## 🧪 Test Post-Fix

```python
import sys
sys.path.append("/srv/notebooks_custom/helpers")
from telemetry_helper import log_metrics

log_metrics(
    model_name="test_hec_v3",
    r2_score=0.99,
    accuracy=0.98
)
```

**Resultado esperado**:
```
✅ Métricas enviadas para test_hec_v3
```

---

## 🚨 Si sigue sin funcionar

### Verificar HEC Enabled en Splunk

```bash
# Abrir Splunk Web
https://localhost:9000

# Settings → Data Inputs → HTTP Event Collector
# Verificar que dice "Enabled"
# Si dice "Disabled", click "Enable"
```

### Verificar que puerto 8088 escucha

```bash
lsof -i :8088 | grep splunk
```

Debería mostrar `splunkd` escuchando.

### Ver logs de HEC

```bash
# En Splunk
index=_internal sourcetype=splunk_httpinput
| head 20
```

---

## 📊 Resumen

| Solución | Efectividad | Permanencia | Complejidad |
|----------|-------------|-------------|-------------|
| Cambiar URL en DSDL UI | ✅ Alta | ✅ Permanente | ⭐ Fácil |
| Modificar helpers | ⚠️ Media | ⚠️ Re-querido rebuild | ⭐⭐⭐ Complejo |
| Override env vars | ❌ No funciona | ❌ | ⭐⭐ |
| Usar IP Docker bridge | ⚠️ Media | ⚠️ Depende de red | ⭐⭐ |

**Recomendación**: **Solución 4** (Cambiar URL en DSDL UI)

---

## ✅ Checklist Post-Solución

- [ ] URL HEC cambiada a `host.docker.internal:8088`
- [ ] Contenedor reiniciado
- [ ] Test ejecutado
- [ ] "✅ Métricas enviadas" recibido
- [ ] Datos visibles en Splunk: `index=ml_metrics`

