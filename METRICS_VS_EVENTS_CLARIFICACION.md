# Clarificación: Índices Metrics vs Events para Telemetría

## 🎯 Problema

Intentamos enviar datos a un índice tipo "Metrics" pero los datos no aparecen.

---

## 🔍 Análisis

### SplunkHEC Limitation

**SplunkHEC** (clase de DSDL) usa:
```python
# splunk-mltk-container-docker/package-dsdlsupport/src/dsdlsupport/SplunkHEC.py
self.url = os.environ["splunk_hec_url"] + "/services/collector/event"
```

**Endpoint**: `/services/collector/event`  
**Propósito**: Enviar EVENTOS JSON normales

---

### Formato Metrics Requerido

Para índices tipo "Metrics", Splunk requiere endpoint `/services/collector` con formato especial:

```json
{
  "time": 1638316800,
  "event": "metric",
  "fields": {
    "metric_name:r2_score": 0.95,
    "model_name": "my_model"
  }
}
```

**Nota**: El formato es completamente diferente.

---

## 📊 Comparación

| Aspecto | Endpoint /services/collector/event | Endpoint /services/collector |
|---------|-----------------------------------|------------------------------|
| **Uso** | Eventos normales JSON | Métricas estructuradas |
| **Formato** | `{'event': {...}}` | `{'event': 'metric', 'fields': {...}}` |
| **Index type** | Events, Main | Metrics |
| **Búsqueda** | `index=X | stats avg(field)` | `mstats avg(field)` |
| **SplunkHEC** | ✅ Soportado | ❌ NO soportado |

---

## ✅ Solución Recomendada

**Cambiar ml_metrics a tipo "Events"** es la solución más simple porque:

1. ✅ SplunkHEC ya funciona con eventos
2. ✅ No requiere cambios de código
3. ✅ Búsquedas normales (`stats`, `timechart`) funcionan
4. ✅ JSON flexible para cualquier estructura
5. ✅ Compatible con toda la telemetría actual

---

## 📋 Para que QUEDE Metrics

Si realmente queremos índices tipo "Metrics", necesitamos:

1. **Crear wrapper custom** para `/services/collector` endpoint
2. **Transformar datos** al formato de métricas
3. **Actualizar helpers** para usar el nuevo wrapper
4. **Cambiar búsquedas** a usar `mstats`

**Complejidad**: Alta  
**Beneficio**: Marginal (mejor compresión de almacenamiento)

---

## 🎯 Decisión

**Recomendación**: Mantener índices tipo "Events"

**Razones**:
- ✅ Más simple
- ✅ Flexibilidad
- ✅ Compatibilidad
- ✅ SplunkHEC funciona out-of-the-box

**Los índices "Events" manejan métricas numéricas perfectamente** con `stats`, `timechart`, etc.

---

## 📝 Acción

**Cambiar índices a tipo "Events"**:

1. Settings → Indexes → ml_metrics → Edit
2. Cambiar "Index type" a "Events"
3. Save
4. Repetir para ml_model_logs (si es necesario)
5. Ejecutar test de telemetría

---

## 🔍 Referencias

- Splunk HEC Event Format: https://docs.splunk.com/Documentation/Splunk/latest/Data/FormateventsforHTTPEventCollector
- Splunk Metrics Format: https://docs.splunk.com/Documentation/Splunk/latest/Data/Sendmetricstoametricsindex
- Difference: Metrics optimized for time-series numeric data, Events optimized for flexible JSON

