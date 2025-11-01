# Estrategia de Gobernanza: Indexación y Metadatos

## 🎯 Contexto

**Situación actual:**
- HEC Token sin index específico → datos van a `main`
- DSDL tiene logs propios (aún no identificados completamente)
- Necesitamos separar telemetría de modelos por aplicación

**Pregunta clave:**
> "¿Cómo garantizar que métricas de modelos de diferentes apps queden organizadas?"

---

## 📊 Análisis de Datos HEC en DSDL

### ¿Qué almacena DSDL actualmente?

Según documentación:

| Tipo de Dato | Index | Origen |
|--------------|-------|--------|
| **Container management logs** | `_internal` | DSDL startup/shutdown |
| **Training logs** | HEC (configurado) | `hec.send()` en notebooks |
| **Epoch metrics** | HEC (configurado) | Durante entrenamiento |
| **Inference logs** | HEC (configurado) | Durante scoring |

**Conclusión:** Si HEC no está configurado con index, todo cae en `main`. ⚠️

---

## 🏗️ Propuesta de Arquitectura

### Opción 1: Index por Aplicación (Recomendado)

```
ml_metrics_app1       → App 1 modelo 1, modelo 2, ...
ml_metrics_app2       → App 2 modelo 1, modelo 2, ...
ml_model_logs_app1    → App 1 logs de training
ml_model_logs_app2    → App 2 logs de training
```

**Ventajas:**
- ✅ Separación clara por app
- ✅ Permisos de acceso por app
- ✅ Retention diferente por app
- ✅ Búsqueda: `index=ml_metrics_app1 model_name="modelo_x"`

**Desventajas:**
- ❌ Muchos índices si hay muchas apps
- ❌ Configuración manual por app

### Opción 2: Index único con Metadatos

```
ml_metrics            → Todas las apps, todos los modelos
ml_model_logs         → Todos los logs
```

**Con metadatos:**
```json
{
  "event": {
    "app_name": "app1",
    "model_name": "autoencoder_horno4_v1",
    "model_version": "1.0.0",
    "r2_score": 0.95
  }
}
```

**Ventajas:**
- ✅ Una sola configuración
- ✅ Búsqueda: `index=ml_metrics app_name="app1"`
- ✅ Escalable

**Desventajas:**
- ❌ Depende de metadatos correctos
- ❌ Permisos más complejos

### Opción 3: Híbrida (RECOMENDADA)

```
ml_metrics            → Index tipo "Metrics" para TODAS las apps
ml_model_logs         → Index tipo "Events" para TODOS los logs

Metadatos en eventos:
{
  "app_name": "app1",
  "model_name": "app1_autoencoder_horno4_v1",  ← Con prefijo de app
  "model_version": "1.0.0",
  "owner": "cristian",
  "project": "horno4_anomalies"
}
```

**Ventajas:**
- ✅ Balance entre simplicidad y flexibilidad
- ✅ Fácil agregación cross-app: `index=ml_metrics | stats avg(r2_score) by app_name`
- ✅ Búsqueda específica: `index=ml_metrics app_name="app1" model_name="autoencoder*"`
- ✅ Index tipo "Metrics" optimizado

---

## ✅ Recomendación Final: Opción 3 (Híbrida)

### Estructura de Índices

```bash
# 1. Index para métricas (todas las apps)
Settings → Indexes → New Index
Name: ml_metrics
Type: Metrics
MaxDataSize: Auto

# 2. Index para logs (todas las apps)
Settings → Indexes → New Index  
Name: ml_model_logs
Type: Events
MaxDataSize: Auto
```

### Estructura de Naming

**Modelos:**
```
app_name + _ + tipo + _ + caso_uso + _ + version

Ejemplos:
  app1_autoencoder_horno4_v1
  app1_lstm_demand_forecast_v2
  app2_xgboost_anomaly_detection_v1
```

**Eventos:**
```json
{
  "event": {
    "app_name": "app1",
    "model_name": "app1_autoencoder_horno4_v1",
    "model_version": "1.0.0",
    "owner": "cristian",
    "project": "horno4_anomalies",
    "timestamp": "2025-01-31T20:00:00",
    "event_type": "model_metrics",
    "r2_score": 0.95,
    "accuracy": 0.92,
    "mae": 0.05
  }
}
```

---

## 🔧 Actualización de Helpers

### telemetry_helper.py Mejorado

```python
def log_metrics(model_name, app_name=None, model_version=None, owner=None, 
                project=None, r2=None, accuracy=None, **kwargs):
    """
    Enviar métricas de modelo con metadatos completos
    
    Args:
        model_name: Nombre completo del modelo (incluye app prefix)
        app_name: Nombre de la aplicación (opcional, extraído del nombre)
        model_version: Versión del modelo (opcional)
        owner: Dueño del modelo (opcional)
        project: Proyecto/caso de uso (opcional)
        r2, accuracy, etc.: Métricas
    """
    hec = init_hec()
    if hec is None:
        return
    
    # Extraer app_name del model_name si no se proporciona
    if app_name is None and model_name:
        parts = model_name.split('_')
        app_name = parts[0] if len(parts) > 0 else 'default'
    
    event = {
        'event_type': 'model_metrics',
        'app_name': app_name,
        'model_name': model_name,
        'model_version': model_version,
        'owner': owner,
        'project': project,
        'timestamp': datetime.now().isoformat(),
        'r2_score': r2,
        'accuracy': accuracy,
        **kwargs
    }
    
    try:
        hec.send({
            'event': event,
            'sourcetype': 'ml:metrics',
            'index': 'ml_metrics'
        })
        print(f"✅ Métricas enviadas para {model_name}")
    except Exception as e:
        print(f"⚠️  Error enviando métricas: {e}")
```

---

## 📋 Cómo Usar

### Opción A: Científico especifica todo

```python
from telemetry_helper import log_metrics

log_metrics(
    model_name="app1_autoencoder_horno4_v1",
    app_name="app1",  # ← Especificado explícitamente
    model_version="1.0.0",
    owner="cristian",
    project="horno4_anomalies",
    r2=0.95,
    accuracy=0.92
)
```

### Opción B: Helper extrae automáticamente

```python
from telemetry_helper import log_metrics

# Si model_name sigue convención: app_tipo_caso_version
log_metrics(
    model_name="app1_autoencoder_horno4_v1",  # ← Helper extrae app_name
    model_version="1.0.0",
    owner="cristian",
    project="horno4_anomalies",
    r2=0.95
)
```

---

## 🔍 Consultas de Ejemplo

### Por App

```spl
index=ml_metrics app_name="app1"
| timechart span=1h avg(r2_score) by model_name
```

### Comparar Apps

```spl
index=ml_metrics 
| stats avg(r2_score) as avg_r2, avg(accuracy) as avg_acc by app_name
| sort -avg_r2
```

### Modelo Específico

```spl
index=ml_metrics model_name="app1_autoencoder_horno4_v1"
| head 100
| table _time, r2_score, accuracy, mae
```

### Alert: Drift Detection

```spl
index=ml_metrics event_type="model_metrics"
| stats latest(r2_score) as current_r2, latest(accuracy) as current_acc by model_name
| eval drift = if(current_r2 < 0.85 OR current_acc < 0.90, 1, 0)
| where drift=1
| eval alert="Model drift: " + model_name
```

### Dashboard: Performance por App

```spl
index=ml_metrics
| stats 
    avg(r2_score) as avg_r2,
    avg(accuracy) as avg_acc,
    count as num_samples
  by app_name, model_name
| sort app_name, -avg_r2
```

---

## 🛡️ Gobierno y Permisos

### Roles y Acceso

| Rol | Acceso |
|-----|--------|
| **Admin** | Todos los índices ml_* |
| **App Owner** | Solo su app: `app_name="app1"` |
| **Data Scientist** | Sus modelos: `owner="cristian"` |
| **Read-only** | Ver solo, no modificar |

### Configuración de Roles

```bash
# Settings → Users and Authentication → Roles
Role: ml_app1_owner
Indexes: ml_metrics, ml_model_logs
Search filters: app_name="app1"

Role: ml_scientist
Indexes: ml_metrics, ml_model_logs  
Search filters: owner=*session.USER*
```

---

## 📝 Convenciones de Naming

### Para Modelos

**Formato:**
```
{app_name}_{model_type}_{use_case}_{version}
```

**Ejemplos:**
- ✅ `app1_autoencoder_horno4_v1`
- ✅ `app2_lstm_demand_forecast_v2`
- ✅ `app1_xgboost_churn_prediction_v3`
- ❌ `modelo1` (no tiene contexto)
- ❌ `autoencoder` (conflicto entre apps)

### Para Variables en Eventos

```python
{
    "app_name": "app1",              # Corto, consistente
    "model_name": "app1_autoencoder_horno4_v1",  # Completo
    "model_version": "1.0.0",        # Semver
    "owner": "cristian",             # Usuario GitHub/SSO
    "project": "horno4_anomalies"    # Descripción proyecto
}
```

---

## ✅ Checklist de Implementación

### Para DevOps/Ingeniería de Datos

- [ ] Crear índices: `ml_metrics` (Metrics), `ml_model_logs` (Events)
- [ ] Crear HEC Token apuntando a `ml_metrics`
- [ ] Configurar DSDL con HEC Token
- [ ] Definir y documentar convenciones de naming
- [ ] Configurar roles y permisos por app
- [ ] Crear dashboards base por app
- [ ] Configurar alerts de drift

### Para Científicos de Datos

- [ ] Seguir convención de naming: `app_name_type_use_case_version`
- [ ] Usar helpers empresariales para telemetría
- [ ] Incluir metadatos: app_name, owner, project
- [ ] Documentar modelos en Git con metadata

### Para el Template

- [ ] Actualizar `template_empresa_base.ipynb` con convención
- [ ] Pre-poblar campos app_name, owner en helpers
- [ ] Crear ejemplos de uso en comments
- [ ] Documentar metadatos requeridos

---

## 🚀 Próximos Pasos

1. **Crear índices** `ml_metrics` y `ml_model_logs`
2. **Actualizar** `telemetry_helper.py` con metadatos mejorados
3. **Crear** HEC Token y configurar en DSDL
4. **Documentar** convención de naming en repo Git
5. **Probar** con un modelo real (Cristian autoencoder)
6. **Crear** dashboards y alerts base

---

## 📚 Referencias

- Splunk HEC: https://docs.splunk.com/Documentation/Splunk/latest/Data/UsetheHTTPEventCollector
- Index types: https://docs.splunk.com/Documentation/Splunk/latest/Indexer/Aboutindexesandindexers
- Splunk Metrics: https://docs.splunk.com/Documentation/Splunk/latest/Metrics/GetStartedinSplunkEnterprise

