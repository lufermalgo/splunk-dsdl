# Aclaración: Telemetría HEC - Token, Index y Tipo

## 🎯 Preguntas

1. ✅ ¿Usa el token configurado en DSDL? **SÍ**
2. ❓ ¿A qué index lleva los datos? **El configurado en el HEC Token**
3. ❓ ¿Qué tipo de index (events o metrics)? **Depende de cómo configures el token**

---

## 📋 Respuesta Detallada

### 1️⃣ Token de DSDL

**SÍ, usa automáticamente el token configurado en DSDL.**

```python
# telemetry_helper.py
def init_hec():
    hec = None
    if not HEC_AVAILABLE:
        return None
    
    if _hec is None:
        try:
            _hec = SplunkHEC()  # ← Sin parámetros
        except Exception as e:
            print(f"⚠️  Error inicializando HEC: {e}")
            return None
    return _hec
```

**Cómo funciona internamente:**

```python
# dsdlsupport.SplunkHEC.SplunkHEC.__init__()
def __init__(self, url="", token=""):
    # ← Por defecto vacío
    
    # PERO si existe variable de entorno:
    if "splunk_hec_enabled" in os.environ:
        access_enabled = os.environ["splunk_hec_enabled"]
        if access_enabled == "1":
            # ← Lee de variables de entorno automáticamente
            self.url = os.environ["splunk_hec_url"] + "/services/collector/event"
            self.token = os.environ["splunk_hec_token"]
```

**DSDL configura estas variables de entorno** cuando configuras HEC en el Setup.

**Flujo:**
```
1. Tú configuras HEC en DSDL Setup
2. DSDL guarda en variables de entorno del contenedor
3. SplunkHEC() lee automáticamente esas variables
4. telemetry_helper usa SplunkHEC() sin parámetros
5. ✅ Todo funciona automáticamente
```

---

### 2️⃣ ¿A qué index lleva los datos?

**El index configurado en el HEC Token que creaste en Splunk.**

**Cuando creas el HEC Token** (Settings → Data Inputs → HTTP Event Collector → New Token):

```
Token Name: dsdl-hec-token
Source Type: _json (recomendado)
Index: ??? ← AQUÍ defines dónde van
```

**Opciones comunes:**

| Index | Uso | Ejemplo |
|-------|-----|---------|
| `ml_metrics` | Métricas de modelos | R², accuracy, loss |
| `ml_logs` | Logs de entrenamiento | Epochs, debugging |
| `ml_models` | Registro de modelos | Modelos entrenados |
| `main` | General (no recomendado) | Todo junto |

**Recomendación:**

```
Index: ml_metrics  ← Para métricas R², accuracy, etc.
        (crear antes en Settings → Indexes)
```

---

### 3️⃣ ¿Tipo de index: events o metrics?

**Depende de si especificas metadata en el evento.**

#### Opción A: Index tipo "Events" (por defecto)

```python
# telemetry_helper.py (actual)
event = {
    'event_type': 'model_metrics',
    'model_name': model_name,
    'timestamp': datetime.now().isoformat(),
    'r2_score': r2,
    'accuracy': accuracy,
    ...
}

hec.send({'event': event})  # ← Sin metadata
```

**Resultado:**
- ✅ Va al index configurado en el token
- ✅ Se almacena como evento normal
- ✅ Puedes buscar: `index=ml_metrics model_name="mi_modelo"`

#### Opción B: Index tipo "Metrics" (optimizado)

Para usar un **index de tipo "metrics"**, necesitas agregar metadata:

```python
# Mejora sugerida
event = {
    'event_type': 'model_metrics',
    'model_name': model_name,
    'r2_score': r2,
    'accuracy': accuracy,
    ...
}

# Enviar con metadata para index metrics
hec.send({
    'event': event,
    'fields': {
        '_metric_type': 'gauge',
        'model_name': model_name
    },
    'sourcetype': 'ml:metrics'
})
```

**Resultado:**
- ✅ Va a index tipo "metrics" (más eficiente para números)
- ✅ Optimizado para timecharts y agregaciones
- ⚠️ Requiere index de tipo "metrics"

---

## 🎯 Solución Recomendada

### Paso 1: Crear Index en Splunk

```bash
# Settings → Indexes → New Index
Name: ml_metrics
Index Type: "Metrics"  # ← Optimizado para métricas
```

### Paso 2: Crear HEC Token

```bash
# Settings → Data Inputs → HTTP Event Collector → New Token
Name: dsdl-hec-token
Source Type: _json
Index: ml_metrics  # ← El que acabas de crear
```

### Paso 3: Configurar DSDL

```bash
# DSDL Setup → Splunk HEC Settings
Enable Splunk HEC: Yes
Splunk HEC Token: [pegar token]
Splunk HEC Endpoint URL: http://localhost:8088
```

### Paso 4: (Opcional) Mejorar telemetry_helper.py

```python
def log_metrics(model_name, r2=None, accuracy=None, **kwargs):
    """Enviar métricas con metadata para index metrics"""
    hec = init_hec()
    if hec is None:
        return
    
    event = {
        'event_type': 'model_metrics',
        'model_name': model_name,
        'timestamp': datetime.now().isoformat(),
        'r2_score': r2,
        'accuracy': accuracy,
        **kwargs
    }
    
    # Si quieres index tipo "metrics":
    hec.send({
        'event': event,
        'sourcetype': 'ml:metrics',
        'index': 'ml_metrics'  # ← Especificar explícitamente
    })
```

---

## 📊 Comparación: Events vs Metrics

| Aspecto | Events | Metrics |
|---------|--------|---------|
| **Uso** | Logs, texto | Números, métricas |
| **Storage** | Más espacio | Optimizado |
| **Búsqueda** | `index=ml_logs` | `index=ml_metrics` |
| **Timechart** | Funciona | Más rápido |
| **Estructura** | Flexible | Estructurado |
| **Ejemplo** | Debug logs | R², accuracy, loss |

**Para nuestro caso** (R², accuracy, loss, etc.):
- ✅ **Recomendado: Index tipo "Metrics"**

---

## 🔍 Verificación

**Después de configurar, verifica que lleguen datos:**

```bash
# En Splunk
index=ml_metrics
| head 10
| table _time, model_name, r2_score, accuracy, event_type
```

**Si no ves datos:**
1. Verificar token correcto en DSDL
2. Verificar contenedor reiniciado después de configurar HEC
3. Verificar permisos del token al index
4. Ver logs: `index=_internal "hec"`

---

## ✅ Resumen

| Pregunta | Respuesta |
|----------|-----------|
| ¿Usa token de DSDL? | ✅ SÍ, automáticamente |
| ¿A qué index? | El configurado en el HEC Token |
| ¿Tipo de index? | Events (default) o Metrics (recomendado) |

**Recomendación final:**
1. Crear index tipo "Metrics": `ml_metrics`
2. Crear HEC Token apuntando a `ml_metrics`
3. Configurar en DSDL
4. Reiniciar contenedores
5. ✅ Telemetría fluye automáticamente

