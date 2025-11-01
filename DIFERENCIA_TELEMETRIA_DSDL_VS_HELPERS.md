# Aclaración: Telemetría DSDL vs Helpers

## 🎯 Pregunta

> "DSDL ya captura logs y métricas. ¿Para qué sirven los helpers?"

---

## 📊 Lo que DSDL Captura Automáticamente

### Container Health (Infraestructura)

| Métrica | Fuente | Index | Qué Captura |
|---------|--------|-------|-------------|
| **CPU, Memory, GPU** | Observability Cloud / Kubernetes | Splunk Observability | Uso de recursos hardware |
| **Startup/Shutdown** | DSDL Container Manager | `_internal` | Eventos de contenedor |
| **stdout/stderr** | Container Logs | Container Logs API | Prints, errores Python |
| **Otel Traces** | Observability Cloud | Splunk Observability | Latencia endpoints, request/response |

**Ejemplos:**
- ❌ No captura: R², accuracy, precision, recall
- ❌ No captura: Training loss por epoch
- ❌ No captura: Métricas de negocio (MAE, RMSE)
- ❌ No captura: Model performance en inferencia

---

## 🎯 Lo que los Helpers Capturan

### Business Metrics (Modelo)

| Métrica | Fuente | Index | Qué Captura |
|---------|--------|-------|-------------|
| **R², Accuracy, F1** | `metrics_calculator.py` | `ml_metrics` | Rendimiento del modelo |
| **Training Loss** | Notebook `fit()` | `ml_model_logs` | Pérdida por epoch |
| **MAE, RMSE** | `metrics_calculator.py` | `ml_metrics` | Errores de predicción |
| **Model Drift** | `telemetry_helper.py` | `ml_metrics` | Decaída de performance |
| **Inference Stats** | `telemetry_helper.py` | `ml_model_logs` | Throughput, latencia |

**Ejemplos:**
- ✅ Captura: Accuracy del modelo
- ✅ Captura: Model performance metrics
- ✅ Captura: Training progression
- ✅ Captura: Business KPIs

---

## 🔍 Comparación Directa

### DSDL Automático: Container Health

```
DSDL Captura:
├── CPU: 45%
├── Memory: 2.5GB / 4GB
├── GPU: 67%
└── Latency: 200ms

Pregunta que responde:
"¿El contenedor está sano?"
```

### Helpers Custom: Model Performance

```
Helpers Capturan:
├── R²: 0.95
├── Accuracy: 92%
├── MAE: 0.05
└── Model Drift: No

Pregunta que responde:
"¿El modelo es bueno?"
```

---

## ❌ Confusión Común

### "DSDL ya captura métricas, no necesito helpers"

**FALSO.**

DSDL captura **infraestructura** (CPU, memoria).  
Helpers capturan **negocio** (R², accuracy).

**Son complementarios, no duplicados.**

---

## 📊 Ejemplo Real

### Escenario: Modelo autoencoder entrenando

**DSDL captura automáticamente:**
```json
{
  "timestamp": "2025-01-31T20:00:00",
  "container": "dev-cristian",
  "cpu_percent": 65,
  "memory_mb": 2048,
  "status": "running"
}
```

**Helpers capturan (manual pero estandarizado):**
```json
{
  "timestamp": "2025-01-31T20:00:00",
  "model_name": "app1_autoencoder_horno4_v1",
  "epoch": 50,
  "loss": 0.023,
  "r2_score": 0.95,
  "accuracy": 0.92
}
```

**Con ambos puedes responder:**
- ✅ ¿El contenedor está bien? (DSDL: CPU OK)
- ✅ ¿El modelo está bien? (Helpers: R² > 0.9)

---

## 🎯 ¿Es Manual?

### Helpers NO son manuales para el DS

**DS solo hace:**
```python
from metrics_calculator import calculate_all_metrics
from telemetry_helper import log_metrics

# En su función fit():
metrics = calculate_all_metrics(y_true, y_pred)
log_metrics(model_name="mi_modelo", **metrics)  # ← 1 línea
```

**Helpers hacen:**
- ✅ Cálculo de métricas (detecta clasificación vs regresión)
- ✅ Envío a Splunk HEC
- ✅ Formato correcto
- ✅ Manejo de errores

**Es 1 línea de código, no es "manual".**

---

## 🤔 Entonces ¿DSDL Captura Alguna Métrica de Modelo?

**SÍ, PERO SOLO SI TU LO ENVÍAS VÍA HEC.**

De la documentación:

> "If DSDL calls hec.send(...), partial training logs appear in the Splunk platform."

**Traducción:** DSDL NO captura métricas de modelo automáticamente.  
**TÚ DEBES enviarlas usando `hec.send()`**.  
Los helpers estandarizan esto.

---

## 📊 Tabla Comparativa

| Aspecto | DSDL Automático | Helpers Custom |
|---------|----------------|----------------|
| **CPU, Memory** | ✅ Captura | ❌ No |
| **Container logs** | ✅ Captura | ❌ No |
| **R², Accuracy** | ❌ No | ✅ Captura |
| **Training metrics** | ❌ No | ✅ Captura |
| **Model drift** | ❌ No | ✅ Captura |
| **Configuración** | Setup DSDL | Helpers preinstalados |
| **Código DS** | 0 líneas | 1 línea |
| **Estándar** | Splunk | Tu empresa |

---

## ✅ Conclusión

**Los helpers SÍ son necesarios porque:**

1. ✅ DSDL captura **infra**, helpers capturan **negocio**
2. ✅ DSDL NO captura métricas de modelo automáticamente
3. ✅ Helpers estandarizan cómo enviar métricas
4. ✅ Helpers agregan metadatos (app_name, owner, project)
5. ✅ Helpers son "one-liners" para el DS

**Sin helpers:**
- DS escribe métricas manualmente (inconsistente)
- Sin estándar de metadatos
- Código duplicado en cada proyecto

**Con helpers:**
- DS escribe 1 línea: `log_metrics(**metrics)`
- Métricas estandarizadas
- Metadatos automáticos
- Gobierno y auditoría

---

## 🎯 Analogía

**DSDL Automático** = Instrumentos del auto
- Velocímetro (CPU)
- Combustible (Memoria)
- Tacómetro (GPU)

**Helpers** = Desempeño del motor
- Caballos de fuerza (R²)
- Consumo (Accuracy)
- Eficiencia (MAE)

**Necesitas AMBOS para saber si el auto funciona bien.**

