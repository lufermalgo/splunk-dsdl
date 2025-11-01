# Checklist DevOps: Instalación DSDL Empresarial

**Audiencia**: Ingenieros de Datos / DevOps  
**Propósito**: Checklist de despliegue completo de DSDL con configuración empresarial

---

## 📋 Prerequisitos de Sistema

### 1. Splunk
- [ ] Splunk instalado y corriendo
- [ ] Puerto web: 8000 (o configurado)
- [ ] Puerto admin: 8089
- [ ] Puerto HEC: 8088

### 2. Docker
- [ ] Docker Desktop instalado (local) o Kubernetes (producción)
- [ ] Docker corriendo: `docker ps`
- [ ] Espacio en disco: min 10GB libre

### 3. Apps Splunk
- [ ] Machine Learning Toolkit (MLTK) instalado
- [ ] Python Security Controller (PSC) instalado
- [ ] Data Science and Deep Learning (DSDL) instalado

Verificar:
```bash
ls /Applications/Splunk/etc/apps/ | grep -E "(MLTK|PSC|DSDL)"
```

---

## 📊 Creación de Índices

### 1. Index tipo "Metrics"

**Ruta**: Settings → Indexes → New Index

| Campo | Valor |
|-------|-------|
| **Index name** | `ml_metrics` |
| **Type** | **Metrics** ✅ |
| **App** | search |
| **Max Data Size** | 500 GB (o según política) |
| **Enable** | Yes |

**Justificación**: Optimizado para métricas numéricas (R², accuracy, loss)

### 2. Index tipo "Events"

**Ruta**: Settings → Indexes → New Index

| Campo | Valor |
|-------|-------|
| **Index name** | `ml_model_logs` |
| **Type** | **Events** ✅ |
| **App** | search |
| **Max Data Size** | 500 GB (o según política) |
| **Enable** | Yes |

**Justificación**: Para logs de debugging y tracking

---

## 🔐 Creación de Tokens

### 1. HEC Token

**Ruta**: Settings → Data Inputs → HTTP Event Collector

#### Paso 1: Habilitar HEC
- [ ] Settings → Data Inputs → HTTP Event Collector
- [ ] Click **"Global Settings"**
- [ ] **Enable** → `All Tokens: Enabled`
- [ ] Click **"Save"**

#### Paso 2: Crear Token
- [ ] Click **"New Token"**
- [ ] Configurar:

| Campo | Valor |
|-------|-------|
| **Token Name** | `dsdl-ml-telemetry-hec` |
| **Source Type** | `_json` (recomendado) |
| **Index** | **`ml_metrics`** ✅ |

- [ ] Click **"Review"**
- [ ] Click **"Submit"**
- [ ] **COPIAR el token generado** (no lo vuelves a ver)

#### Paso 3: Verificar Permisos
- [ ] Token debe tener acceso a:
  - ✅ `ml_metrics`
  - ✅ `ml_model_logs` (opcional, si se configuró)

### 2. Authentication Token (REST API)

**Ruta**: Settings → Tokens

- [ ] Click **"Create New Token"**
- [ ] Configurar:

| Campo | Valor |
|-------|-------|
| **Token Name** | `dsdl-api-token` |
| **Capability** | `Admin all objects` (o restringir según necesidad) |

- [ ] Click **"Create"**
- [ ] **COPIAR el token generado**

---

## ⚙️ Configuración DSDL

**Ruta**: Splunk Web → DSDL → Setup

### 1. Docker Settings

| Campo | Valor (Local) | Valor (Kubernetes) |
|-------|---------------|-------------------|
| **Docker Host** | `unix:///var/run/docker.sock` | `https://k8s-host:6443` |
| **Docker Registry** | (vacío o Docker Hub) | Registry privado |

- [ ] Click **"Test Connection"**
- [ ] Debe mostrar: ✅ Success

### 2. Certificate Settings

- [ ] Dejar **default** (self-signed para desarrollo)
- [ ] Para producción: subir certificados propios

### 3. Password Settings

- [ ] Crear password para JupyterLab:
  - Min 8 caracteres
  - Mezclar mayúsculas, minúsculas, números

### 4. Splunk Access

| Campo | Valor |
|-------|-------|
| **Splunk Host Address** | `localhost` (o IP/FQDN del splunk host) |
| **Splunk Management Port** | `8089` |
| **Splunk Access Token** | `[PEGAR AUTH TOKEN]` |

### 5. Splunk HEC

| Campo | Valor |
|-------|-------|
| **Enable Splunk HEC** | **Yes** ✅ |
| **Splunk HEC Token** | `[PEGAR HEC TOKEN]` |
| **Splunk HEC Endpoint URL** | `http://localhost:8088` |

> ⚠️ **IMPORTANTE**: Después de configurar HEC, **reiniciar contenedores** para que tome efecto.

### 6. Observability Settings

- [ ] Dejar en **No** para desarrollo
- [ ] Para producción: configurar Splunk Observability Cloud

### 7. Test & Save

- [ ] Click **"Test & Save"**
- [ ] Debe mostrar: ✅ Setup Completed

---

## 📦 Imagen Docker Personalizada

### 1. Opción A: Build Local

```bash
cd splunk-mltk-container-docker

# Build imagen
./build.sh golden-cpu-empresa splunk/ 5.2.2

# Verificar
docker images | grep golden-cpu-empresa

# Push a registry (si aplica)
docker tag splunk/golden-cpu-empresa:5.2.2 \
  registry.example.com/golden-cpu-empresa:5.2.2
docker push registry.example.com/golden-cpu-empresa:5.2.2
```

### 2. Opción B: Pull desde Registry

```bash
# Si ya existe en registry privado
docker pull registry.example.com/golden-cpu-empresa:5.2.2
```

### 3. Configurar en DSDL

**Ruta**: DSDL → Configuration → Container Images

- [ ] Verificar que `golden-cpu-empresa:5.2.2` esté disponible
- [ ] Si no está, agregar manualmente en:
  - `$SPLUNK_HOME/etc/apps/mltk-container/local/images.conf`

---

## ✅ Validación

### 1. Verificar Contenedor

- [ ] DSDL → Containers
- [ ] Click **"Start"** en cualquier imagen
- [ ] Debe iniciar sin errores
- [ ] Click **"Open JupyterLab"**
- [ ] Debe abrir en navegador

### 2. Verificar Helpers

En JupyterLab, crear nuevo notebook:

```python
# Test import de helpers
import sys
sys.path.append("/dltk/notebooks/helpers")

try:
    from telemetry_helper import log_metrics
    from metrics_calculator import calculate_all_metrics
    print("✅ Helpers disponibles")
except ImportError as e:
    print(f"❌ Error: {e}")
```

### 3. Verificar HEC

En JupyterLab:

```python
from dsdlsupport import SplunkHEC
hec = SplunkHEC.SplunkHEC()

# Test send
response = hec.send({
    'event': {
        'test': True,
        'message': 'Validation test from DevOps'
    }
})
print(response.status_code)  # Debe ser 200
```

### 4. Verificar Datos en Splunk

```spl
index=ml_metrics test=*
| head 10
| table _time, test, message
```

Debe mostrar el evento de prueba.

---

## 🚨 Troubleshooting

### Error: "Cannot connect to Docker"
```bash
# Verificar Docker corriendo
docker ps

# Si no está, iniciar Docker Desktop
open -a Docker
```

### Error: "HEC authentication failed"
- [ ] Verificar token correcto
- [ ] Verificar HEC habilitado globalmente
- [ ] Verificar index `ml_metrics` existe
- [ ] Verificar permisos del token

### Error: "Helpers no encontrados"
- [ ] Verificar imagen personalizada fue usada
- [ ] Verificar `/dltk/notebooks/helpers/` existe en contenedor
- [ ] Revisar logs: `docker logs <container-id>`

### Error: "Container starts but JupyterLab not accessible"
- [ ] Verificar puerto 8888 libre: `lsof -i :8888`
- [ ] Verificar firewall
- [ ] Revisar logs: DSDL → Configuration → Containers → <container> → Logs

---

## 📝 Estructura de Datos Esperada

### Evento de Métricas (ml_metrics)

```json
{
  "event": {
    "event_type": "model_metrics",
    "app_name": "app1",
    "model_name": "app1_autoencoder_horno4_v1",
    "model_version": "1.0.0",
    "owner": "cristian",
    "project": "horno4_anomalies",
    "timestamp": "2025-01-31T20:00:00",
    "r2_score": 0.95,
    "accuracy": 0.92,
    "f1_score": 0.90,
    "precision": 0.89,
    "recall": 0.91,
    "mae": 0.05,
    "rmse": 0.08
  },
  "sourcetype": "ml:metrics",
  "index": "ml_metrics"
}
```

### Evento de Logs (ml_model_logs)

```json
{
  "event": {
    "event_type": "training_step",
    "app_name": "app1",
    "model_name": "app1_autoencoder_horno4_v1",
    "epoch": 50,
    "loss": 0.023,
    "timestamp": "2025-01-31T20:00:00"
  },
  "sourcetype": "ml:training",
  "index": "ml_model_logs"
}
```

---

## 📊 Consultas de Validación

### Verificar métricas recibidas

```spl
index=ml_metrics
| head 20
| table _time, model_name, r2_score, accuracy, event_type
```

### Verificar logs recibidos

```spl
index=ml_model_logs
| head 20
| table _time, model_name, epoch, loss, event_type
```

### Estadísticas por modelo

```spl
index=ml_metrics event_type="model_metrics"
| stats 
    avg(r2_score) as avg_r2,
    avg(accuracy) as avg_acc,
    count as samples
  by model_name
| sort -avg_r2
```

---

## 🎯 Entrega al Equipo de Ciencia de Datos

### Documentación a Entregar

1. ✅ Acceso a JupyterLab (URL)
2. ✅ Credenciales (username/password)
3. ✅ Convención de naming de modelos
4. ✅ Template de notebook empresarial
5. ✅ Ejemplos de uso de helpers
6. ✅ Dashboard base en Splunk

### Información de Configuración

| Item | Detalle |
|------|---------|
| **Splunk URL** | http://localhost:8000 |
| **JupyterLab URL** | http://localhost:8888 (o dinámico) |
| **Index Métricas** | `ml_metrics` |
| **Index Logs** | `ml_model_logs` |
| **Naming Convention** | `app_name_type_use_case_version` |
| **Template** | `/dltk/notebooks_custom/template_empresa_base.ipynb` |

---

## ✅ Checklist Final

- [ ] Splunk corriendo
- [ ] DSDL instalado y configurado
- [ ] Docker/Kubernetes funcionando
- [ ] Índices creados (`ml_metrics`, `ml_model_logs`)
- [ ] HEC Token creado y configurado
- [ ] Auth Token creado y configurado
- [ ] Contenedor inicia correctamente
- [ ] JupyterLab accesible
- [ ] Helpers importables
- [ ] Test HEC funciona
- [ ] Datos llegan a índices correctos
- [ ] Documentación entregada a DS

---

## 📚 Referencias

- Análisis comparativo: `ANALISIS_COMPARATIVO_DSDL.md`
- Estrategia de gobierno: `ESTRATEGIA_GOVERNANCE_INDEXING.md`
- Scope imagen empresarial: `IMAGEN_EMPRESARIAL_SCOPE.md`

