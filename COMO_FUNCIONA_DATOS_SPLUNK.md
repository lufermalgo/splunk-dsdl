# 🔄 Cómo Llegan los Datos de Splunk al Modelo

**Respuesta corta**: DSDL AUTOMÁTICAMENTE pasa los datos de Splunk a las funciones `fit()` y `apply()`

---

## 🔄 Flujo Completo

### 1️⃣ En Splunk Web (Tú ejecutas):

```spl
index=demo_anomalias_data
| fit MLTKContainer algo=demo_modelo_completo epochs=20
from feature_* into app:demo_v1
```

### 2️⃣ DSDL Internamente:

```
1. Splunk lee datos del index "demo_anomalias_data"
2. Extrae las features "feature_*" (feature_0, feature_1, etc.)
3. Crea un CSV y JSON con esos datos
4. Envía por HTTPS al contenedor
5. Llama a fit(df, param) donde:
   - df = DataFrame con tus datos de Splunk ✅
   - param = {'epochs': 20} ✅
```

### 3️⃣ Tu Función `fit(df, param)` Recibe:

```python
def fit(df, param):
    # df ya tiene TUS DATOS de Splunk index demo_anomalias_data
    # No necesitas consultar nada, DSDL ya lo hizo
    
    print(f"Datos de Splunk: {df.shape}")  # Verás tus datos reales
    X = df.values  # Ya procesado
    # entrenar modelo...
```

---

## 📊 Formato de los Datos

Cuando Splunk envía datos a `fit()`:

```python
# df contiene:
#   feature_0  feature_1  feature_2  feature_3  feature_4
# 0    1.23      -0.45       2.10       0.87      -1.34
# 1    0.95       1.23      -0.67       1.45       0.92
# ... más filas ...

# param contiene:
# {'epochs': '20', 'batch_size': '32', ...}
```

---

## 🧪 Opcional: Consultar Directamente

Si NECESITAS consultar Splunk desde el notebook (interactivo):

```python
from dsdlsupport import SplunkSearch

# Crear búsqueda
search = SplunkSearch.SplunkSearch(
    search='index=demo_anomalias_data | head 100 | table feature_*'
)

# Obtener datos como DataFrame
df = search.as_df()
```

**Pero NO es necesario** para el flujo normal. DSDL ya lo hace automáticamente.

---

## ✅ Resumen

**NO necesitas consultar Splunk manualmente**

- ✅ `fit(df, param)` recibe tus datos automáticamente
- ✅ `apply(df)` recibe nuevos datos automáticamente
- ✅ Solo define las funciones `init`, `fit`, `apply`, `summary`
- ✅ DSDL gestiona el transporte de datos

**Tu notebook es "pasivo"**: recibe datos, procesa, retorna resultados

