# Script para Generar Datos Dummy en Splunk

**Objetivo**: Crear datos de prueba en un índice Splunk para testing del modelo demo

---

## 📊 Script SPL para Generar Datos

### Paso 1: Crear Índice (si no existe)

```spl
# En Splunk Web → Settings → Indexes
# Crear índice: demo_anomalias_data
# Tipo: Events
```

### Paso 2: Generar Datos con SPL

**Ejecutar este script en Splunk Web → Search**:

```spl
index=demo_anomalias_data
| delete

| makeresults count=1000
| eval feature_0=mvrange(0,1000)
| mvexpand feature_0
| eval feature_0=feature_0/100
| eval feature_1=random()/pow(2,31)*10 - 5
| eval feature_2=random()/pow(2,31)*8 - 4
| eval feature_3=random()/pow(2,31)*6 - 3
| eval feature_4=random()/pow(2,31)*12 - 6

| eval anomaly_type="normal"

| appendpipe [
    | head 100
    | eval feature_0=feature_0 + 5
    | eval feature_1=feature_1 + 8
    | eval feature_2=feature_2 + 10
    | eval feature_3=feature_3 + 12
    | eval feature_4=feature_4 + 15
    | eval anomaly_type="anomaly"
]

| eval _time=now() - random()%86400

| outputlookup demo_anomalias_data.csv
```

---

## 🔧 Script Alternativo (Más Controlado)

```spl
# Script para generar datos más controlados

index=demo_anomalias_data
| delete

| makeresults count=1000
| streamstats count as row_num

# Features normales (distribución normal)
| eval feature_0=random()/pow(2,31)*20 - 10
| eval feature_1=random()/pow(2,31)*15 - 7.5
| eval feature_2=random()/pow(2,31)*10 - 5
| eval feature_3=random()/pow(2,31)*25 - 12.5
| eval feature_4=random()/pow(2,31)*30 - 15

# Clasificación: 900 normales, 100 anómalos
| eval anomaly_type=if(row_num <= 100, "anomaly", "normal")
| eval cluster_id=floor(row_num/200)

# Agregar patrones a anomalías
| eval feature_0=if(anomaly_type="anomaly", feature_0 + random()/pow(2,31)*15 + 10, feature_0)
| eval feature_1=if(anomaly_type="anomaly", feature_1 + random()/pow(2,31)*12 + 8, feature_1)
| eval feature_2=if(anomaly_type="anomaly", feature_2 + random()/pow(2,31)*10 + 6, feature_2)
| eval feature_3=if(anomaly_type="anomaly", feature_3 + random()/pow(2,31)*20 + 15, feature_3)
| eval feature_4=if(anomaly_type="anomaly", feature_4 + random()/pow(2,31)*25 + 20, feature_4)

# Timestamp
| eval _time=now() - random()%86400
| fields - row_num

# Guardar
| outputlookup demo_anomalias_data.csv
```

---

## 📊 Verificar Datos Generados

```spl
index=demo_anomalias_data
| head 20
| stats count by anomaly_type
```

O:

```spl
index=demo_anomalias_data
| stats values(anomaly_type) as types, count by anomaly_type
| table types, count
```

---

## 🚀 Usar con el Modelo Demo

Una vez generados los datos, ejecutar en Splunk Web:

```spl
index=demo_anomalias_data
| fit MLTKContainer algo=demo_modelo_completo epochs=20 batch_size=32 
from feature_* 
into app:demo_modelo_v1
```

Luego aplicar:

```spl
index=demo_anomalias_data
| apply demo_modelo_v1 from feature_*
| eval anomaly_score=_value
| eval predicted_anomaly=if(anomaly_score > 0.5, 1, 0)
| stats count by anomaly_type, predicted_anomaly
```

---

## 📝 Notas

- Los datos se generan con `makeresults` (100% sintético)
- 1000 registros: 900 normales, 100 anómalos
- 5 features numéricas
- Campo `anomaly_type` para validación del modelo
- Usar `outputlookup` para persistir

