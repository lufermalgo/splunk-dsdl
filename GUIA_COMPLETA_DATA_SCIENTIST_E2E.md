# Guía Completa Data Scientist: Workflow End-to-End DSDL

**Objetivo**: Guía paso a paso para que un Data Scientist cree, desarrolle y publique un modelo de autoencoder para detección de anomalías usando Splunk DSDL.

**Duración estimada**: 2-3 horas  
**Nivel**: Intermedio  
**Requisitos**: Acceso a JupyterLab, datos indexados en Splunk (`demo_anomalias_data`)

---

## 🎯 Contexto del Proyecto

### Objetivo del Modelo
Crear un **autoencoder** para detectar anomalías en datos industriales indexados en Splunk.

### Datos
- **Index**: `demo_anomalias_data`
- **Campos**: `feature_*` (feature_0, feature_1, feature_2, etc.)
- **Formato**: Series temporales de sensores industriales

### Naming Estándar
Seguiremos la convención: `{app_name}_{model_type}_{use_case}_{version}`

**Ejemplo**: `app1_autoencoder_demo_anomalias_v1`

### Qué Obtendremos al Final
Al guardar el notebook en JupyterLab, DSDL **automáticamente**:
1. Exporta las funciones `init`, `fit`, `apply`, `summary` a un módulo Python
2. Publica el modelo en `/srv/app/model/`
3. Hace disponible el modelo para usar desde SPL con `| fit` y `| apply`

---

## 📋 Checklist Pre-Workflow

Antes de comenzar, verifica que tienes:

- [ ] Acceso a JupyterLab (desde DSDL → Containers → Open JupyterLab)
- [ ] Contenedor DEV iniciado y corriendo
- [ ] Datos indexados en `demo_anomalias_data`
- [ ] Permisos para usar los helpers empresariales
- [ ] Template empresarial base disponible

### ⚠️ Nota Importante: Cómo Copiar Código

**Cuando copies código de esta guía a JupyterLab**:
- ✅ Copia SOLO el código dentro de los bloques ```python
- ❌ NO copies los triple backticks ``` ni el ``` al final
- ✅ Pega directamente en una nueva célula de código
- ✅ Ejecuta la célula con Shift+Enter

**Ejemplo correcto**:
```python
# Esto es lo que debes copiar
print("Hola mundo")
```

**Ejemplo incorrecto** (NO copies esto):
```
```python
print("Hola mundo")
```
```

---

## 📝 Paso 1: Preparar el Notebook Base

### 1.1 Abrir JupyterLab

1. En Splunk Web, navega a: **DSDL → Containers**
2. Si no hay contenedor DEV activo, haz clic en **"Start Development Container"**
3. Espera a que el contenedor inicie (1-2 minutos)
4. Haz clic en **"Open JupyterLab"**
5. Se abre JupyterLab en una nueva pestaña del navegador

### 1.2 Cargar Template Empresarial

1. En JupyterLab, navega a: `/dltk/notebooks_custom/`
2. Abre el archivo: `template_empresa_base.ipynb`
3. Haz clic en: **File → Save As...**
4. Guarda como: `app1_autoencoder_demo_anomalias_v1.ipynb`
5. **IMPORTANTE**: Este nombre sigue la convención estándar

**Ubicación final**: `/dltk/notebooks_custom/app1_autoencoder_demo_anomalias_v1.ipynb`

### 1.3 Verificar Estructura del Template

El template debería tener estas secciones base:
- Células de importación
- Función `init(df, param)`
- Función `fit(model, df, param)`
- Función `apply(model, df, param)`
- Función `summary(model)`

**Si no tiene estas funciones, las agregaremos en los siguientes pasos.**

---

## 🔍 Paso 2: Exploración de Datos (EDA)

### 2.1 Obtener Muestra de Datos de Splunk

En una nueva célula al inicio del notebook (después de las importaciones), agrega:

```python
# THIS CELL IS NOT EXPORTED - EDA: Exploración de datos
from dsdlsupport import SplunkSearch

# Obtener muestra de datos para exploración
print("🔍 Obteniendo muestra de datos de Splunk...")
search = SplunkSearch.SplunkSearch(
    search='index=demo_anomalias_data | head 1000 | table feature_*'
)

df_eda = search.as_df()
print(f"✅ Datos obtenidos: {df_eda.shape[0]} filas, {df_eda.shape[1]} columnas")
df_eda.head()
```

**Ejecuta esta célula** y verifica que obtienes datos.

### 2.2 Información Básica del Dataset

```python
# THIS CELL IS NOT EXPORTED - EDA: Información básica
print("=" * 60)
print("INFORMACIÓN BÁSICA DEL DATASET")
print("=" * 60)
print(f"\n📊 Dimensiones: {df_eda.shape}")
print(f"\n📋 Columnas: {list(df_eda.columns)}")
print(f"\n📈 Tipos de datos:\n{df_eda.dtypes}")
print(f"\n📉 Información completa:")
df_eda.info()
```

### 2.3 Estadísticas Descriptivas

```python
# THIS CELL IS NOT EXPORTED - EDA: Estadísticas descriptivas
print("=" * 60)
print("ESTADÍSTICAS DESCRIPTIVAS")
print("=" * 60)
print(df_eda.describe())
```

### 2.4 Detección de Valores Faltantes

```python
# THIS CELL IS NOT EXPORTED - EDA: Valores faltantes
print("=" * 60)
print("VALORES FALTANTES")
print("=" * 60)
missing = df_eda.isnull().sum()
if missing.sum() > 0:
    print("⚠️ Se encontraron valores faltantes:")
    print(missing[missing > 0])
else:
    print("✅ No hay valores faltantes")
```

### 2.5 Visualizaciones Básicas

```python
# THIS CELL IS NOT EXPORTED - EDA: Visualizaciones
import matplotlib.pyplot as plt
import seaborn as sns

# Configurar estilo
plt.style.use('seaborn-v0_8-darkgrid')
fig, axes = plt.subplots(2, 2, figsize=(15, 10))
fig.suptitle('Análisis Exploratorio de Datos - demo_anomalias_data', fontsize=16)

# Histogramas de las primeras 4 features
for i, col in enumerate(df_eda.columns[:4]):
    ax = axes[i // 2, i % 2]
    df_eda[col].hist(bins=50, ax=ax, alpha=0.7)
    ax.set_title(f'Distribución de {col}')
    ax.set_xlabel('Valor')
    ax.set_ylabel('Frecuencia')

plt.tight_layout()
plt.show()
```

### 2.6 Matriz de Correlación

```python
# THIS CELL IS NOT EXPORTED - EDA: Correlaciones
import numpy as np

# Calcular matriz de correlación
corr_matrix = df_eda.corr()

# Visualizar
plt.figure(figsize=(12, 10))
sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='coolwarm', center=0,
            square=True, linewidths=1, cbar_kws={"shrink": 0.8})
plt.title('Matriz de Correlación - Features')
plt.tight_layout()
plt.show()
```

### 2.7 Conclusiones del EDA

**Objetivo de esta sección**: Resumir los hallazgos clave del análisis exploratorio para tomar decisiones informadas sobre el modelo.

**Conclusiones que queremos obtener**:

1. **Dimensiones del dataset**: ¿Cuántas muestras y features tenemos?
   - Define si necesitamos muestreo o si tenemos suficientes datos
   - Determina la arquitectura del modelo (input dimension)

2. **Tipos de datos**: ¿Qué tipos de datos tenemos?
   - Determina qué features usar (solo numéricas para autoencoder)
   - Identifica si hay columnas categóricas que necesiten encoding

3. **Valores faltantes**: ¿Hay datos faltantes?
   - Determina estrategia de preprocesamiento (imputación, eliminación)
   - Afecta la calidad del modelo

4. **Rangos de valores**: ¿Qué rangos tienen nuestras features?
   - Determina si necesitamos normalización (valores en escalas muy diferentes)
   - Autoencoders funcionan mejor con datos normalizados

5. **Distribuciones**: ¿Cómo están distribuidas las features?
   - Identifica outliers (afectan el entrenamiento del autoencoder)
   - Determina si necesitamos transformaciones (log, etc.)

6. **Correlaciones**: ¿Hay features altamente correlacionadas?
   - Puede indicar redundancia (puede simplificar el modelo)
   - Afecta la interpretación del modelo

**Código para conclusiones**:

```python
# THIS CELL IS NOT EXPORTED - EDA: Conclusiones
print("=" * 60)
print("CONCLUSIONES DEL EDA")
print("=" * 60)

# Obtener solo columnas numéricas para análisis
numeric_cols = df_eda.select_dtypes(include=[np.number]).columns
df_numeric = df_eda[numeric_cols]

print("✅ Dimensiones del dataset:", df_eda.shape)
print("   - Filas (muestras):", df_eda.shape[0])
print("   - Columnas (features):", df_eda.shape[1])
print("   - Features numéricas:", len(df_numeric.columns))

print("\n✅ Valores faltantes:", df_eda.isnull().sum().sum())
if df_eda.isnull().sum().sum() > 0:
    print("   ⚠️  Hay valores faltantes que necesitamos manejar")

# Rango de valores (solo para columnas numéricas)
if len(df_numeric.columns) > 0:
    min_val = df_numeric.min().min()
    max_val = df_numeric.max().max()
    print(f"\n✅ Rango de valores (numéricos):")
    print(f"   - Mínimo: {min_val:.2f}")
    print(f"   - Máximo: {max_val:.2f}")
    print(f"   - Rango total: {max_val - min_val:.2f}")
    
    # Verificar si necesitamos normalización
    std_values = df_numeric.std()
    if std_values.max() / std_values.min() > 10:
        print("   ⚠️  Hay features con escalas muy diferentes → Normalización REQUERIDA")
    else:
        print("   ✅ Escalas similares → Normalización recomendada")
else:
    print("\n⚠️  No se encontraron columnas numéricas")

print("\n📝 Decisiones para el modelo basadas en EDA:")
print("   - Features a usar: Todas las numéricas disponibles")
print("   - Preprocesamiento: Normalización (StandardScaler)")
print("   - Arquitectura: Autoencoder simple (input → encoding → output)")
print("   - Encoding dimension: ~10% del input dimension (ajustable)")
```

**✅ Validación**: Asegúrate de haber ejecutado todas las células EDA y haber entendido tus datos antes de continuar.

---

## 🏗️ Paso 3: Configurar Imports y Helpers Empresariales

### 3.1 Actualizar Célula de Imports

En la primera célula marcada con `# mltkc_import`, reemplaza o agrega:

```python
# mltkc_import
# this definition exposes all python module imports that should be available in all subsequent commands

import json
import os
import datetime
import numpy as np
import pandas as pd
import tensorflow as tf
import keras
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error

# Importar helpers empresariales
import sys
sys.path.append('/dltk/notebooks_custom/helpers')

from telemetry_helper import log_metrics, log_training_step, log_error
from metrics_calculator import calculate_all_metrics
from preprocessor import standard_preprocessing, apply_preprocessing

# Global constants
MODEL_DIRECTORY = "/srv/app/model/data/"

# Configuración del modelo (usando naming estándar)
APP_NAME = "app1"
MODEL_TYPE = "autoencoder"
USE_CASE = "demo_anomalias"
VERSION = "v1"
MODEL_NAME = f"{APP_NAME}_{MODEL_TYPE}_{USE_CASE}_{VERSION}"

print(f"📦 Modelo configurado: {MODEL_NAME}")
print(f"✅ Helpers empresariales importados correctamente")
```

**Ejecuta esta célula** y verifica que no hay errores de importación.

### 3.2 Verificar Helpers Disponibles

```python
# THIS CELL IS NOT EXPORTED - Verificar helpers
print("🔍 Verificando helpers empresariales...")

try:
    from telemetry_helper import log_metrics
    print("✅ telemetry_helper importado")
except ImportError as e:
    print(f"❌ Error importando telemetry_helper: {e}")

try:
    from metrics_calculator import calculate_all_metrics
    print("✅ metrics_calculator importado")
except ImportError as e:
    print(f"❌ Error importando metrics_calculator: {e}")

try:
    from preprocessor import standard_preprocessing
    print("✅ preprocessor importado")
except ImportError as e:
    print(f"❌ Error importando preprocessor: {e}")

print("\n✅ Todos los helpers están disponibles")
```

---

## 📋 Paso 3.5: Entender el Metadata de Celdas (Importante para Exportación)

### ¿Qué es el Metadata de Celdas?

El **metadata de celdas** es información adicional que se almacena en cada celda de un notebook Jupyter. Esta información le dice a DSDL:

1. **Qué funciones exportar**: DSDL escanea el metadata para identificar qué celdas contienen funciones que deben exportarse al archivo `.py`
2. **Cómo identificar las funciones**: El campo `"name"` en el metadata indica el tipo de función (ej: `"mltkc_init"`, `"mltkc_fit"`, etc.)
3. **Protección de celdas**: El campo `"deletable": false` previene que se eliminen accidentalmente celdas críticas

### ¿Por qué es Importante?

**Sin el metadata correcto**, DSDL **NO exportará** las funciones al archivo `.py`, y cuando intentes usar el modelo desde Splunk, obtendrás errores como:

```
AttributeError: module 'app.model.mi_modelo' has no attribute 'fit'
```

**Con el metadata correcto**, DSDL automáticamente:
- ✅ Identifica las funciones requeridas (`init`, `fit`, `apply`, `summary`, `save`, `load`)
- ✅ Las exporta al archivo `.py` cuando guardas el notebook
- ✅ Permite que Splunk las llame desde ML-SPL

### ¿Cómo Funciona el Proceso de Exportación?

```
1. DS escribe código en celda: def fit(model, df, param): ...
2. DS agrega metadata a la celda: {"name": "mltkc_fit", ...}
3. DS guarda el notebook (.ipynb)
   ↓
4. DSDL escanea el notebook
5. DSDL encuentra celdas con metadata "mltkc_*"
6. DSDL extrae el código de esas celdas
7. DSDL crea/actualiza: /srv/app/model/mi_modelo.py
   ↓
8. Splunk ejecuta: | fit MLTKContainer algo=mi_modelo ...
9. DSDL importa mi_modelo.py y ejecuta fit()
```

### Metadata Completo para Cada Función

A continuación, el metadata completo que debes agregar a cada celda de código que contiene una función requerida:

#### 1. Metadata para `init()` - Función Requerida

```json
{
    "deletable": false,
    "name": "mltkc_init",
    "trusted": true,
    "editable": true,
    "slideshow": {
        "slide_type": ""
    },
    "tags": []
}
```

**Dónde agregarlo**: En la celda de código que contiene `def init(df, param):`

#### 2. Metadata para `fit()` - Función Requerida

```json
{
    "deletable": false,
    "name": "mltkc_fit",
    "trusted": true,
    "editable": true,
    "slideshow": {
        "slide_type": ""
    },
    "tags": []
}
```

**Dónde agregarlo**: En la celda de código que contiene `def fit(model, df, param):`

#### 3. Metadata para `apply()` - Función Requerida

```json
{
    "deletable": false,
    "name": "mltkc_apply",
    "trusted": true,
    "editable": true,
    "slideshow": {
        "slide_type": ""
    },
    "tags": []
}
```

**Dónde agregarlo**: En la celda de código que contiene `def apply(model, df, param):`

#### 4. Metadata para `summary()` - Función Requerida

```json
{
    "deletable": false,
    "name": "mltkc_summary",
    "trusted": true,
    "editable": true,
    "slideshow": {
        "slide_type": ""
    },
    "tags": []
}
```

**Dónde agregarlo**: En la celda de código que contiene `def summary(model=None):`

#### 5. Metadata para `save()` - Función Requerida

```json
{
    "editable": true,
    "slideshow": {
        "slide_type": ""
    },
    "tags": [],
    "deletable": false,
    "name": "mltkc_save"
}
```

**Dónde agregarlo**: En la celda de código que contiene `def save(model, name):`

**⚠️ IMPORTANTE**: Esta función es llamada automáticamente por DSDL después de `fit()`. Asegúrate de que:
- La firma sea: `def save(model, name):`
- Retorne el modelo: `return model`

#### 6. Metadata para `load()` - Función Opcional

```json
{
    "editable": true,
    "slideshow": {
        "slide_type": ""
    },
    "tags": [],
    "deletable": false,
    "name": "mltkc_load"
}
```

**Dónde agregarlo**: En la celda de código que contiene `def load(name):`

**⚠️ NOTA**: Esta función es opcional. DSDL NO la llama automáticamente, pero es útil para desarrollo local.

### ¿Qué Hace Cada Campo del Metadata?

| Campo | Valor | Propósito |
|-------|-------|-----------|
| `"name"` | `"mltkc_init"`, `"mltkc_fit"`, etc. | **CRÍTICO**: Identifica la función para DSDL. Sin esto, DSDL no exportará la función. |
| `"deletable"` | `false` | Previene que se elimine accidentalmente la celda (importante para funciones requeridas) |
| `"trusted"` | `true` | Indica que la celda es confiable y puede ejecutarse sin restricciones de seguridad |
| `"editable"` | `true` | Permite editar la celda (siempre `true` para desarrollo) |
| `"slideshow"` | `{"slide_type": ""}` | Configuración para presentaciones (no relevante para DSDL, pero parte del formato estándar) |
| `"tags"` | `[]` | Etiquetas opcionales para organizar celdas (vacío por defecto) |

### Cómo Agregar el Metadata en JupyterLab (Método Visual)

1. **Selecciona la celda de código** que contiene la función (ej: `def init(df, param):`)
   - ⚠️ **IMPORTANTE**: Debe ser la celda de CÓDIGO, NO la celda markdown (ej: "### Stage 1 - init")

2. **Activa el editor de metadata**:
   - Ve a: **View → Cell Toolbar → Edit Metadata**
   - O haz clic derecho en la celda → **Edit Metadata**

3. **Copia y pega el metadata completo**:
   - Se abrirá un editor JSON en la parte inferior de la celda
   - Borra cualquier contenido existente
   - Pega el metadata correspondiente (ej: para `init()`, usa el metadata de `mltkc_init`)

4. **Aplica los cambios**:
   - Haz clic en **"Apply"** o **"Save"**
   - El metadata se guardará en la celda

5. **Guarda el notebook**:
   - Presiona **Cmd+S** (Mac) o **Ctrl+S** (Windows/Linux)
   - DSDL automáticamente exportará las funciones al archivo `.py`

### Verificación del Metadata

Después de agregar el metadata, verifica que:

1. **El metadata está en la celda correcta**:
   - ✅ Celda de código con `def init(...):` → metadata `"name": "mltkc_init"`
   - ❌ Celda markdown "### Stage 1 - init" → NO debe tener este metadata

2. **El archivo `.py` exportado contiene las funciones**:
   ```python
   # En JupyterLab, ejecuta:
   import os
   py_file = f"/srv/app/model/{MODEL_NAME}.py"
   if os.path.exists(py_file):
       with open(py_file, 'r') as f:
           content = f.read()
           required_functions = ['def init(', 'def fit(', 'def apply(', 'def summary(', 'def save(']
           for func in required_functions:
               if func in content:
                   print(f"✅ {func} encontrada")
               else:
                   print(f"❌ {func} NO encontrada")
   ```

3. **No hay celdas markdown vacías con metadata**:
   - Si encuentras celdas markdown con metadata `"name": "mltkc_*"`, puedes eliminarlas o dejarlas (no afectan)

### Errores Comunes y Soluciones

| Error | Causa | Solución |
|-------|-------|----------|
| `AttributeError: module has no attribute 'fit'` | El metadata no está en la celda de código | Mueve el metadata a la celda de código que contiene `def fit()` |
| El archivo `.py` no tiene las funciones | El metadata está mal formado o falta el campo `"name"` | Verifica que el JSON sea válido y tenga `"name": "mltkc_*"` |
| No puedo borrar una celda | Tiene `"deletable": false` | Esto es intencional. Si necesitas borrarla, primero quita el metadata |
| Funciones duplicadas en `.py` | Hay múltiples celdas con el mismo metadata | Asegúrate de tener solo UNA celda con cada `"name": "mltkc_*"` |

### Orden de las Funciones en el Notebook

El orden recomendado de las funciones en el notebook es:

1. `init()` - Inicialización del modelo
2. `fit()` - Entrenamiento del modelo
3. `apply()` - Inferencia/predicción
4. `save()` - Guardado del modelo (requerido)
5. `load()` - Carga del modelo (opcional)
6. `summary()` - Metadatos del modelo

**Nota**: DSDL no requiere un orden específico, pero este orden facilita la lectura y el mantenimiento.

---

## 🎨 Paso 4: Definir Función `init()` - Inicialización del Modelo

### 4.1 Crear Función `init()` con Arquitectura de Autoencoder

En la célula marcada con `# mltkc_init`, reemplaza con:

```python
# mltkc_init
# initialize the model
# params: data and parameters
# returns the model object which will be used as a reference to call fit, apply and summary subsequently

def init(df, param):
    """
    Inicializar autoencoder para detección de anomalías.
    
    Args:
        df: DataFrame con datos de Splunk
        param: Diccionario con parámetros del modelo
    
    Returns:
        model: Modelo Keras compilado
    """
    print(f"🔧 Inicializando modelo: {MODEL_NAME}")
    
    # Obtener features del DataFrame
    if 'feature_variables' in param:
        feature_cols = param['feature_variables']
    else:
        # Si no hay feature_variables definidas, usar todas las numéricas
        feature_cols = [col for col in df.columns if df[col].dtype in ['float64', 'int64']]
        if not feature_cols:
            # Fallback: buscar columnas que empiecen con 'feature_'
            feature_cols = [col for col in df.columns if col.startswith('feature_')]
    
    X = df[feature_cols] if feature_cols else df.select_dtypes(include=[np.number])
    
    print(f"📊 Shape de los datos: {X.shape}")
    print(f"📋 Features seleccionadas: {len(X.columns)}")
    
    input_dim = X.shape[1]
    
    # Parámetros del modelo (con valores por defecto)
    encoding_dim = 10  # Dimensión de la capa oculta (bottleneck)
    if 'options' in param and 'params' in param['options']:
        if 'encoding_dim' in param['options']['params']:
            encoding_dim = int(param['options']['params']['encoding_dim'])
        if 'components' in param['options']['params']:
            encoding_dim = int(param['options']['params']['components'])
    
    activation = 'relu'
    if 'options' in param and 'params' in param['options']:
        if 'activation' in param['options']['params']:
            activation = param['options']['params']['activation']
    
    print(f"⚙️  Parámetros del modelo:")
    print(f"   - Input dimension: {input_dim}")
    print(f"   - Encoding dimension: {encoding_dim}")
    print(f"   - Activation: {activation}")
    
    # Construir autoencoder
    # Encoder
    encoder = keras.layers.Dense(
        encoding_dim, 
        activation=activation,
        input_shape=(input_dim,),
        name='encoder'
    )
    
    # Decoder
    decoder = keras.layers.Dense(
        input_dim,
        activation=activation,
        name='decoder'
    )
    
    # Modelo completo
    model = keras.Sequential([
        encoder,
        decoder
    ], name='Autoencoder')
    
    # Compilar modelo
    model.compile(
        optimizer='adam',
        loss='mse',  # Mean Squared Error para autoencoder
        metrics=['mae']  # Mean Absolute Error como métrica adicional
    )
    
    print(f"✅ Modelo compilado exitosamente")
    print(f"📐 Arquitectura: {input_dim} → {encoding_dim} → {input_dim}")
    
    return model
```

### 4.2 Probar Función `init()` Localmente

```python
# THIS CELL IS NOT EXPORTED - Test init localmente
# Crear datos dummy para probar
test_df = pd.DataFrame({
    'feature_0': np.random.randn(100),
    'feature_1': np.random.randn(100),
    'feature_2': np.random.randn(100),
    'feature_3': np.random.randn(100),
    'feature_4': np.random.randn(100)
})

test_param = {
    'feature_variables': ['feature_0', 'feature_1', 'feature_2', 'feature_3', 'feature_4'],
    'options': {
        'params': {
            'encoding_dim': 10
        }
    }
}

test_model = init(test_df, test_param)
print("\n📊 Resumen del modelo:")
test_model.summary()
```

**✅ Validación**: Verifica que el modelo se inicializa correctamente sin errores.

---

## 🏋️ Paso 5: Definir Función `fit()` - Entrenamiento con Telemetría

### 5.1 Crear Función `fit()` con Helpers Empresariales

En la célula marcada con `# mltkc_stage_create_model_fit`, reemplaza con:

```python
# mltkc_stage_create_model_fit
# returns a fit info json object

def fit(model, df, param):
    """
    Entrenar autoencoder con telemetría automática.
    
    Args:
        model: Modelo Keras inicializado
        df: DataFrame con datos de entrenamiento
        param: Diccionario con parámetros de entrenamiento
    
    Returns:
        dict: Información del entrenamiento (historial, métricas, etc.)
    """
    print(f"🚀 Iniciando entrenamiento del modelo: {MODEL_NAME}")
    
    returns = {}
    
    # Obtener features
    if 'feature_variables' in param:
        feature_cols = param['feature_variables']
    else:
        feature_cols = [col for col in df.columns if col.startswith('feature_')]
        if not feature_cols:
            feature_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    
    X = df[feature_cols] if feature_cols else df.select_dtypes(include=[np.number])
    
    print(f"📊 Datos de entrenamiento: {X.shape[0]} muestras, {X.shape[1]} features")
    
    # Preprocesamiento: Normalización
    print("🔧 Aplicando preprocesamiento (normalización)...")
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    X_scaled_df = pd.DataFrame(X_scaled, columns=X.columns, index=X.index)
    
    # Guardar scaler en returns para uso posterior
    returns['scaler'] = scaler
    
    # Parámetros de entrenamiento
    epochs = 50
    batch_size = 32
    validation_split = 0.2
    
    if 'options' in param and 'params' in param['options']:
        if 'epochs' in param['options']['params']:
            epochs = int(param['options']['params']['epochs'])
        if 'batch_size' in param['options']['params']:
            batch_size = int(param['options']['params']['batch_size'])
        if 'validation_split' in param['options']['params']:
            validation_split = float(param['options']['params']['validation_split'])
    
    print(f"⚙️  Parámetros de entrenamiento:")
    print(f"   - Epochs: {epochs}")
    print(f"   - Batch size: {batch_size}")
    print(f"   - Validation split: {validation_split}")
    
    # Callback para TensorBoard (opcional)
    log_dir = f"/srv/notebooks/logs/fit/{MODEL_NAME}_{datetime.datetime.now().strftime('%Y%m%d-%H%M%S')}"
    tensorboard_callback = tf.keras.callbacks.TensorBoard(
        log_dir=log_dir,
        histogram_freq=1
    )
    
    # Callback personalizado para logging de telemetría
    class TelemetryCallback(tf.keras.callbacks.Callback):
        def on_epoch_end(self, epoch, logs=None):
            """Enviar métricas de cada época a Splunk"""
            logs = logs or {}
            try:
                # ⚠️ CRÍTICO: Convertir valores NumPy/Pandas a tipos nativos de Python para JSON serialization
                # Los valores int64/float64 de NumPy no son serializables a JSON directamente
                epoch_value = int(epoch + 1)  # Convertir a int nativo
                loss_value = float(logs.get('loss', 0)) if logs.get('loss') is not None else 0.0
                val_loss_value = float(logs.get('val_loss', 0)) if logs.get('val_loss') is not None else 0.0
                mae_value = float(logs.get('mae', 0)) if logs.get('mae') is not None else 0.0
                val_mae_value = float(logs.get('val_mae', 0)) if logs.get('val_mae') is not None else 0.0
                
                log_training_step(
                    model_name=MODEL_NAME,
                    epoch=epoch_value,
                    loss=loss_value,
                    val_loss=val_loss_value,
                    mae=mae_value,
                    val_mae=val_mae_value
                )
            except Exception as e:
                print(f"⚠️  Error enviando telemetría en época {epoch + 1}: {e}")
                import traceback
                print(f"   Traceback completo: {traceback.format_exc()}")
    
    telemetry_callback = TelemetryCallback()
    
    # Entrenar modelo
    print("\n🏋️  Iniciando entrenamiento...")
    history = model.fit(
        x=X_scaled_df,
        y=X_scaled_df,  # Autoencoder: input = output
        epochs=epochs,
        batch_size=batch_size,
        validation_split=validation_split,
        verbose=1,
        callbacks=[tensorboard_callback, telemetry_callback]
    )
    
    returns['fit_history'] = history
    returns['model_epochs'] = epochs
    returns['model_batch_size'] = batch_size
    returns['scaler'] = scaler  # Guardar scaler para uso en apply
    
    # Evaluar modelo en datos completos
    print("\n📊 Evaluando modelo en datos completos...")
    test_results = model.evaluate(X_scaled_df, X_scaled_df, verbose=0)
    returns['model_loss'] = test_results[0]
    returns['model_mae'] = test_results[1] if len(test_results) > 1 else None
    
    print(f"✅ Entrenamiento completado")
    print(f"   - Loss final: {test_results[0]:.6f}")
    if len(test_results) > 1:
        print(f"   - MAE final: {test_results[1]:.6f}")
    
    # Calcular métricas de reconstrucción
    print("\n📈 Calculando métricas de reconstrucción...")
    X_pred = model.predict(X_scaled_df, verbose=0)
    
    # Calcular MSE y RMSE
    mse = mean_squared_error(X_scaled_df.values, X_pred)
    rmse = np.sqrt(mse)
    
    returns['mse'] = float(mse)
    returns['rmse'] = float(rmse)
    
    print(f"   - MSE: {mse:.6f}")
    print(f"   - RMSE: {rmse:.6f}")
    
    # Enviar métricas finales a Splunk (telemetría)
    try:
        # ⚠️ CRÍTICO: Convertir valores NumPy/Pandas a tipos nativos de Python para JSON serialization
        # Los valores int64/float64 de NumPy no son serializables a JSON directamente
        mae_value = float(returns['model_mae']) if returns['model_mae'] is not None else None
        rmse_value = float(rmse) if rmse is not None else None
        mse_value = float(mse) if mse is not None else None
        loss_value = float(test_results[0]) if test_results[0] is not None else None
        
        log_metrics(
            model_name=MODEL_NAME,
            r2_score=None,  # Autoencoder no tiene R² tradicional
            mae=mae_value,
            rmse=rmse_value,
            mse=mse_value,
            loss=loss_value,
            app_name=APP_NAME,
            model_version=VERSION,
            project=USE_CASE
        )
        print("✅ Métricas enviadas a Splunk")
    except Exception as e:
        print(f"⚠️  Error enviando métricas a Splunk: {e}")
        import traceback
        print(f"   Traceback completo: {traceback.format_exc()}")
    
    return returns
```

### 5.2 Probar Función `fit()` Localmente

```python
# THIS CELL IS NOT EXPORTED - Test fit localmente
# Usar datos dummy más grandes
test_df_fit = pd.DataFrame({
    'feature_0': np.random.randn(500),
    'feature_1': np.random.randn(500),
    'feature_2': np.random.randn(500),
    'feature_3': np.random.randn(500),
    'feature_4': np.random.randn(500)
})

test_param_fit = {
    'feature_variables': ['feature_0', 'feature_1', 'feature_2', 'feature_3', 'feature_4'],
    'options': {
        'params': {
            'epochs': '10',  # Pocas épocas para prueba rápida
            'batch_size': '32',
            'validation_split': '0.2'
        }
    }
}

# Crear modelo de prueba
test_model_fit = init(test_df_fit, test_param_fit)

# Entrenar (esto puede tomar unos minutos)
print("⏳ Entrenando modelo de prueba (esto tomará unos minutos)...")
fit_results = fit(test_model_fit, test_df_fit, test_param_fit)

print("\n✅ Test de fit completado exitosamente")
print(f"   - Loss: {fit_results.get('model_loss', 'N/A')}")
print(f"   - MSE: {fit_results.get('mse', 'N/A')}")
```

**✅ Validación**: Verifica que el entrenamiento se ejecuta sin errores y que las métricas se calculan correctamente.

---

## 🔮 Paso 6: Definir Función `apply()` - Inferencia con Detección de Anomalías

### 6.1 Crear Función `apply()` con Cálculo de Anomalías

En la célula marcada con `# mltkc_stage_create_model_apply`, reemplaza con:

```python
# mltkc_stage_create_model_apply

def apply(model, df, param):
    """
    Aplicar autoencoder para detección de anomalías.
    
    Args:
        model: Modelo Keras entrenado
        df: DataFrame con datos nuevos para inferencia
        param: Diccionario con parámetros (debe contener scaler de fit)
    
    Returns:
        DataFrame: DataFrame con reconstrucciones y scores de anomalía
    """
    print(f"🔮 Aplicando modelo: {MODEL_NAME}")
    
    # Obtener features (debe coincidir con las usadas en fit)
    if 'feature_variables' in param:
        feature_cols = param['feature_variables']
    else:
        feature_cols = [col for col in df.columns if col.startswith('feature_')]
        if not feature_cols:
            feature_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    
    X = df[feature_cols] if feature_cols else df.select_dtypes(include=[np.number])
    
    print(f"📊 Datos de inferencia: {X.shape[0]} muestras, {X.shape[1]} features")
    
    # Obtener scaler del entrenamiento (desde param o fit_results)
    scaler = None
    if 'scaler' in param:
        scaler = param['scaler']
    elif hasattr(model, 'scaler'):
        scaler = model.scaler
    
    # Aplicar normalización
    if scaler is not None:
        # Usar scaler del entrenamiento
        X_scaled = scaler.transform(X)
        print("✅ Usando scaler del entrenamiento")
    else:
        # Crear nuevo scaler si no está disponible (fallback)
        print("⚠️  Scaler no encontrado en param. Aplicando normalización nueva...")
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
    
    X_scaled_df = pd.DataFrame(X_scaled, columns=X.columns, index=X.index)
    
    # Predecir reconstrucciones
    print("🔄 Calculando reconstrucciones...")
    X_reconstructed = model.predict(X_scaled_df, verbose=0)
    X_reconstructed_df = pd.DataFrame(X_reconstructed, columns=X.columns, index=X.index)
    
    # Calcular error de reconstrucción (MSE por muestra)
    reconstruction_error = np.mean((X_scaled_df.values - X_reconstructed_df.values) ** 2, axis=1)
    
    # Calcular threshold para anomalías (percentil 95)
    # En producción, este threshold debería venir del conjunto de entrenamiento
    anomaly_threshold = np.percentile(reconstruction_error, 95)
    
    # Detectar anomalías
    is_anomaly = reconstruction_error > anomaly_threshold
    anomaly_score = reconstruction_error / (anomaly_threshold + 1e-10)  # Normalizar score
    
    print(f"📊 Estadísticas de reconstrucción:")
    print(f"   - Error medio: {np.mean(reconstruction_error):.6f}")
    print(f"   - Error mediano: {np.median(reconstruction_error):.6f}")
    print(f"   - Threshold (percentil 95): {anomaly_threshold:.6f}")
    print(f"   - Anomalías detectadas: {np.sum(is_anomaly)} / {len(is_anomaly)} ({100*np.mean(is_anomaly):.2f}%)")
    
    # Construir DataFrame de resultados
    results = pd.DataFrame({
        'reconstruction_error': reconstruction_error,
        'anomaly_score': anomaly_score,
        'is_anomaly': is_anomaly.astype(int)
    }, index=X.index)
    
    # Agregar reconstrucciones como columnas
    for i, col in enumerate(X.columns):
        results[f'reconstruction_{col}'] = X_reconstructed_df[col].values
        results[f'original_{col}'] = X[col].values
    
    print(f"✅ Inferencia completada")
    print(f"   - Shape de resultados: {results.shape}")
    
    # Enviar telemetría de inferencia a Splunk
    try:
        # ⚠️ CRÍTICO: Convertir valores NumPy/Pandas a tipos nativos de Python para JSON serialization
        # Los valores int64/float64 de NumPy no son serializables a JSON directamente
        
        # IMPORTANTE: Usar .item() para convertir scalars NumPy a tipos nativos de Python
        # Esto es más robusto que int() o float() porque maneja todos los tipos NumPy
        num_predictions = int(len(df))  # len() ya retorna int nativo
        
        # Para valores NumPy, usar .item() si está disponible, sino usar int()/float()
        if hasattr(is_anomaly.sum(), 'item'):
            num_anomalies = int(is_anomaly.sum().item())
        else:
            num_anomalies = int(is_anomaly.sum())
        
        if hasattr(reconstruction_error.mean(), 'item'):
            avg_reconstruction_error = float(reconstruction_error.mean().item())
        else:
            avg_reconstruction_error = float(reconstruction_error.mean())
        
        if hasattr(anomaly_threshold, 'item'):
            anomaly_threshold_native = float(anomaly_threshold.item())
        else:
            anomaly_threshold_native = float(anomaly_threshold)
        
        # ⚠️ DIAGNÓSTICO: Verificar que todos los valores son serializables a JSON
        # Esto ayuda a identificar problemas antes de pasarlos al helper
        import json
        telemetry_data = {
            "model_name": MODEL_NAME,
            "num_predictions": num_predictions,
            "num_anomalies": num_anomalies,
            "avg_reconstruction_error": avg_reconstruction_error,
            "anomaly_threshold": anomaly_threshold_native,
            "app_name": APP_NAME,
            "model_version": VERSION,
            "project": USE_CASE
        }
        
        # Eliminar valores None
        telemetry_data = {k: v for k, v in telemetry_data.items() if v is not None}
        
        # Verificar serialización JSON ANTES de llamar al helper
        try:
            json.dumps(telemetry_data)
            print("✅ Todos los valores son serializables a JSON")
        except TypeError as e:
            print(f"❌ ERROR DE SERIALIZACIÓN ANTES DEL HELPER: {e}")
            print(f"   Valores problemáticos:")
            for k, v in telemetry_data.items():
                try:
                    json.dumps({k: v})
                except TypeError:
                    print(f"      - {k}: {type(v)} = {v}")
                    # Convertir cualquier valor NumPy restante
                    if hasattr(v, 'item'):
                        telemetry_data[k] = v.item()
                    elif isinstance(v, (np.integer, np.floating)):
                        telemetry_data[k] = float(v) if isinstance(v, np.floating) else int(v)
            
            # Intentar de nuevo
            try:
                json.dumps(telemetry_data)
                print("✅ Valores corregidos, ahora son serializables")
            except TypeError as e2:
                print(f"❌ ERROR PERSISTENTE: {e2}")
                raise  # Re-lanzar el error para que se capture en el except externo
        
        # ⚠️ CRÍTICO: Importar funciones de telemetría DENTRO del bloque try-except
        # Esto asegura que las funciones estén disponibles cuando se llamen
        # Importar log_prediction si está disponible
        try:
            from telemetry_helper import log_prediction
            log_prediction(
                model_name=telemetry_data["model_name"],
                num_predictions=telemetry_data["num_predictions"],
                num_anomalies=telemetry_data["num_anomalies"],
                avg_reconstruction_error=telemetry_data["avg_reconstruction_error"],
                anomaly_threshold=telemetry_data["anomaly_threshold"],
                app_name=telemetry_data["app_name"],
                model_version=telemetry_data["model_version"],
                owner=OWNER if 'OWNER' in globals() else None,
                project=telemetry_data["project"]
            )
            print("✅ Telemetría de inferencia enviada a Splunk")
        except ImportError:
            # Si log_prediction no existe, usar log_metrics como alternativa
            from telemetry_helper import log_metrics
            log_metrics(
                model_name=telemetry_data["model_name"],
                num_predictions=telemetry_data["num_predictions"],
                num_anomalies=telemetry_data["num_anomalies"],
                avg_reconstruction_error=telemetry_data["avg_reconstruction_error"],
                anomaly_threshold=telemetry_data["anomaly_threshold"],
                app_name=telemetry_data["app_name"],
                model_version=telemetry_data["model_version"],
                project=telemetry_data["project"]
            )
            print("✅ Telemetría de inferencia enviada a Splunk (usando log_metrics)")
        except Exception as telemetry_error:
            # Capturar cualquier otro error de telemetría (no solo ImportError)
            print(f"⚠️  Error en telemetría (después de verificación JSON): {telemetry_error}")
            import traceback
            print(f"   Traceback: {traceback.format_exc()}")
            # No re-lanzar el error para que apply() pueda continuar
    except Exception as e:
        print(f"⚠️  Error enviando telemetría de inferencia a Splunk: {e}")
        import traceback
        print(f"   Traceback completo: {traceback.format_exc()}")
    
    return results
```

### 6.2 Probar Función `apply()` Localmente

```python
# THIS CELL IS NOT EXPORTED - Test apply localmente
# Crear datos nuevos para inferencia
test_df_apply = pd.DataFrame({
    'feature_0': np.random.randn(100),
    'feature_1': np.random.randn(100),
    'feature_2': np.random.randn(100),
    'feature_3': np.random.randn(100),
    'feature_4': np.random.randn(100)
})

# Agregar scaler al param (simulando que viene de fit)
test_param_apply = {
    'feature_variables': ['feature_0', 'feature_1', 'feature_2', 'feature_3', 'feature_4'],
    'scaler': fit_results.get('scaler')  # Usar scaler del fit anterior
}

# Aplicar modelo
results = apply(test_model_fit, test_df_apply, test_param_apply)

print("\n📊 Primeras 10 filas de resultados:")
print(results.head(10))

print("\n📈 Estadísticas de anomalías:")
print(f"   - Total muestras: {len(results)}")
print(f"   - Anomalías detectadas: {results['is_anomaly'].sum()}")
print(f"   - Porcentaje: {100 * results['is_anomaly'].mean():.2f}%")
```

**✅ Validación**: Verifica que la inferencia funciona y que detecta anomalías correctamente.

---

## 📊 Paso 7: Definir Función `summary()` - Metadatos del Modelo

### 7.1 Crear Función `summary()` Completa

En la célula marcada con `# return model summary`, reemplaza con:

```python
# return model summary

def summary(model=None):
    """
    Proporcionar metadatos y resumen del modelo.
    
    Args:
        model: Modelo Keras (opcional)
    
    Returns:
        dict: Metadatos del modelo
    """
    returns = {
        "model_name": MODEL_NAME,
        "app_name": APP_NAME,
        "model_type": MODEL_TYPE,
        "use_case": USE_CASE,
        "version": VERSION,
        "version_info": {
            "tensorflow": tf.__version__,
            "keras": keras.__version__,
            "numpy": np.__version__,
            "pandas": pd.__version__
        }
    }
    
    if model is not None:
        # Guardar resumen del modelo como string
        s = []
        model.summary(print_fn=lambda x: s.append(x + '\n'))
        returns["model_summary"] = ''.join(s)
        
        # Información de la arquitectura
        # ⚠️ CRÍTICO: Convertir valores NumPy a tipos nativos de Python para JSON serialization
        # DSDL serializa el resultado de summary() a JSON, y valores NumPy causan errores
        total_params = model.count_params()
        trainable_params = sum([tf.size(w).numpy() for w in model.trainable_weights])
        
        # Convertir a tipos nativos de Python
        if hasattr(total_params, 'item'):
            total_params = int(total_params.item())
        else:
            total_params = int(total_params)
        
        if hasattr(trainable_params, 'item'):
            trainable_params = int(trainable_params.item())
        else:
            trainable_params = int(trainable_params)
        
        returns["model_architecture"] = {
            "input_shape": str(model.input_shape) if hasattr(model, 'input_shape') else "N/A",
            "output_shape": str(model.output_shape) if hasattr(model, 'output_shape') else "N/A",
            "total_params": total_params,  # Ya convertido a int nativo
            "trainable_params": trainable_params  # Ya convertido a int nativo
        }
        
        # Información de capas
        returns["layers"] = []
        for i, layer in enumerate(model.layers):
            # Obtener output_shape de manera segura
            output_shape = "N/A"
            try:
                # En Keras 2.x/TensorFlow 2.x, intentar múltiples métodos
                if hasattr(layer, 'output') and layer.output is not None:
                    # Método 1: Desde el tensor output (disponible después de build)
                    try:
                        output_shape = str(layer.output.shape)
                    except:
                        pass
                
                if output_shape == "N/A":
                    # Método 2: Intentar obtener desde config
                    if hasattr(layer, 'get_config'):
                        config = layer.get_config()
                        if 'output_shape' in config:
                            output_shape = str(config['output_shape'])
                
                if output_shape == "N/A":
                    # Método 3: Calcular si es posible
                    if callable(getattr(layer, 'compute_output_shape', None)):
                        # Necesitamos input_shape, intentar obtenerlo
                        if i == 0 and hasattr(model, 'input_shape') and model.input_shape:
                            # Primera capa: usar input_shape del modelo
                            computed = layer.compute_output_shape(model.input_shape)
                            output_shape = str(computed)
                        elif hasattr(layer, 'input_shape') and layer.input_shape:
                            # Capas intermedias: usar input_shape de la capa
                            computed = layer.compute_output_shape(layer.input_shape)
                            output_shape = str(computed)
            except Exception:
                # Si todo falla, usar "N/A"
                output_shape = "N/A"
            
            # Obtener parámetros de manera segura
            params = 0
            try:
                params_raw = layer.count_params()
                # ⚠️ CRÍTICO: Convertir a tipo nativo de Python para JSON serialization
                if hasattr(params_raw, 'item'):
                    params = int(params_raw.item())
                else:
                    params = int(params_raw)
            except Exception:
                params = 0
            
            returns["layers"].append({
                "index": i,  # Ya es int nativo
                "name": layer.name,
                "type": type(layer).__name__,
                "output_shape": output_shape,
                "params": params  # Ya convertido a int nativo
            })
    
    return returns
```

### 7.2 Probar Función `summary()`

```python
# THIS CELL IS NOT EXPORTED - Test summary
model_summary = summary(test_model_fit)
print("📊 Resumen del modelo:")
print(json.dumps(model_summary, indent=2, default=str))
```

**✅ Validación**: Verifica que `summary()` retorna toda la información necesaria.

---

## 💾 Paso 8: Definir Función `save()` - REQUERIDA por DSDL

### ⚠️ IMPORTANTE: `save()` es REQUERIDA

**DSDL llama automáticamente a `save()` después de ejecutar `fit()`**. Si esta función no existe o tiene la firma incorrecta, verás el error:
```
MLTKC error: /fit: ERROR: unable to save model. Ended with exception: module 'app.model.app1_autoencoder_demo_anomalias_v1' has no attribute 'save'
```

**Firma requerida**: `def save(model, name):`
- `model`: El modelo entrenado (retornado por `fit()`)
- `name`: Nombre del modelo (pasado por DSDL desde `into app:model_name`)

### 8.1 Crear Función `save()` para Modelos Keras

**⚠️ IMPORTANTE**: La celda que contiene `save()` **DEBE tener metadata especial** para que DSDL la exporte automáticamente.

**⚠️ ERROR COMÚN**: Si después de guardar el notebook el archivo `.py` NO tiene `save()`, verifica:
1. ✅ La función está definida como `def save(model, name):` (NO `def load()`)
2. ✅ El comentario en la celda es `# mltkc_save` (NO `# mltkc_load`)
3. ✅ **CRÍTICO**: El metadata `"name": "mltkc_save"` está en la **CELDA DE CÓDIGO** que contiene `def save()`, NO en la celda markdown
4. ✅ El metadata de la celda de código tiene `"name": "mltkc_save"` (NO `"name": "mltkc_load"`)

**⚠️ ERROR MÁS COMÚN**: El metadata está en la celda markdown (ej: "### Stage 8 - save model") en lugar de estar en la celda de código que contiene `def save()`. **El metadata DEBE estar en la celda de código, NO en la celda markdown.**

**Pasos para crear la función `save()`**:

1. **Crea una nueva celda de código** después de `summary()`
2. **Configura el metadata de la celda** (en JupyterLab: View → Cell Toolbar → Edit Metadata)
   - Agrega: `"name": "mltkc_save"` en el metadata de la celda
3. **Agrega el código de la función** (⚠️ IMPORTANTE: debe ser `def save()`, NO `def load()`):

```python
# mltkc_save
# Función REQUERIDA: DSDL llama a save(model, name) después de fit()

def save(model, name):
    """
    Guardar modelo Keras en disco.
    
    IMPORTANTE: Esta función es llamada automáticamente por DSDL después de fit().
    
    Args:
        model: Modelo Keras entrenado (retornado por fit())
        name: Nombre del modelo (pasado por DSDL desde "into app:model_name")
    
    Returns:
        model: Retorna el modelo (requerido por DSDL)
    """
    # Importar os si no está disponible (para cuando DSDL exporta el módulo)
    import os
    
    # Asegurar que el directorio existe
    os.makedirs(MODEL_DIRECTORY, exist_ok=True)
    
    # Guardar modelo Keras
    filepath = MODEL_DIRECTORY + name + ".keras"
    model.save(filepath)
    
    print(f"✅ Modelo guardado en: {filepath}")
    print(f"📊 Tamaño del archivo: {os.path.getsize(filepath) / (1024*1024):.2f} MB")
    
    # NOTA: Si tienes un scaler u otros objetos, guárdalos también
    # Ejemplo: si el scaler está en el modelo o en globals
    # from sklearn.externals import joblib  # o import joblib
    # if hasattr(model, 'scaler'):
    #     joblib.dump(model.scaler, MODEL_DIRECTORY + name + "_scaler.pkl")
    
    # DSDL espera que retornes el modelo
    return model
```

### 8.2 Probar Función `save()` Localmente

```python
# THIS CELL IS NOT EXPORTED - Test save localmente
print("💾 Probando función save()...")

# Verificar que las variables necesarias existen
if 'test_model_fit' not in globals():
    print("⚠️  test_model_fit no está definido.")
    print("   Necesitas ejecutar primero el test de fit() (Paso 6.2)")
    print("   Para crear un modelo de prueba rápido, ejecuta:")
    print("""
    # Crear datos dummy
    test_df_fit = pd.DataFrame({
        'feature_0': np.random.randn(100),
        'feature_1': np.random.randn(100),
        'feature_2': np.random.randn(100),
        'feature_3': np.random.randn(100),
        'feature_4': np.random.randn(100)
    })
    test_param_fit = {
        'feature_variables': ['feature_0', 'feature_1', 'feature_2', 'feature_3', 'feature_4'],
        'options': {'params': {'epochs': '5', 'batch_size': '32'}}
    }
    test_model_fit = init(test_df_fit, test_param_fit)
    fit_results = fit(test_model_fit, test_df_fit, test_param_fit)
    """)
else:
    try:
        # Asegurar que MODEL_DIRECTORY está definido
        try:
            model_dir = MODEL_DIRECTORY
        except NameError:
            model_dir = "/srv/app/model/data/"
        
        # Guardar modelo de prueba usando la firma correcta
        saved_model = save(test_model_fit, name="test_autoencoder")
        print(f"✅ Modelo guardado exitosamente")
        
        # Verificar que el archivo existe
        filepath = model_dir + "test_autoencoder.keras"
        if os.path.exists(filepath):
            file_size = os.path.getsize(filepath) / (1024 * 1024)
            print(f"📊 Tamaño del archivo: {file_size:.2f} MB")
            print(f"✅ Archivo creado correctamente: {filepath}")
        else:
            print(f"⚠️  Archivo no encontrado: {filepath}")
            
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
```

**✅ Validación**: Verifica que `save()` funciona correctamente con la firma `save(model, name)`.

**Nota**: Si obtienes el error `name 'test_model_fit' is not defined`, necesitas ejecutar primero el test de `fit()` (Paso 6.2) para crear el modelo de prueba.

### 8.3 Función Opcional `load()` para Desarrollo Local

**NOTA**: `load()` NO es requerida por DSDL, pero es útil para desarrollo local. Si quieres que DSDL la exporte, agrega el metadata `"name": "mltkc_load"` a la celda.

**Para que DSDL exporte `load()`** (opcional):

⚠️ **IMPORTANTE**: Para una explicación completa sobre qué es el metadata, por qué es importante y cómo agregarlo correctamente, consulta la **Sección 3.5: Entender el Metadata de Celdas** en esta guía.

1. **Crea una nueva celda de código** después de `save()`
2. **Configura el metadata de la celda** (en JupyterLab: View → Cell Toolbar → Edit Metadata)
   - Agrega el metadata completo (ver **Paso 3.5** para más detalles):
   ```json
   {
     "editable": true,
     "slideshow": {
       "slide_type": ""
     },
     "tags": [],
     "deletable": false,
     "name": "mltkc_load"
   }
   ```
3. **Agrega el código de la función**:

```python
# mltkc_load
# Función opcional para cargar modelo guardado durante desarrollo
# DSDL NO llama a esta función automáticamente

def load(name):
    """
    Cargar modelo Keras desde disco.
    
    Útil para desarrollo local o pruebas.
    DSDL NO usa esta función automáticamente.
    
    Args:
        name: Nombre del archivo (sin extensión)
    
    Returns:
        Model: Modelo Keras cargado
    """
    # Importar os si no está disponible
    import os
    
    # Asegurar que MODEL_DIRECTORY está definido (usar variable global o local)
    try:
        # Intentar usar MODEL_DIRECTORY global
        model_dir = MODEL_DIRECTORY
    except NameError:
        # Si no existe, usar valor por defecto
        model_dir = "/srv/app/model/data/"
    
    filepath = model_dir + name + ".keras"
    
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"❌ Archivo no encontrado: {filepath}")
    
    print(f"📥 Cargando modelo desde: {filepath}")
    model = keras.models.load_model(filepath)
    
    print(f"✅ Modelo cargado exitosamente")
    print(f"📊 Arquitectura: {model.input_shape} → {model.output_shape}")
    
    return model
```

### 8.4 Probar Función `load()` Localmente (Opcional)

```python
# THIS CELL IS NOT EXPORTED - Test load localmente (opcional)
print("📥 Probando función load()...")

# Verificar que el archivo existe antes de intentar cargarlo
import os

# Asegurar que MODEL_DIRECTORY está definido
try:
    model_dir = MODEL_DIRECTORY
except NameError:
    model_dir = "/srv/app/model/data/"

test_filepath = model_dir + "test_autoencoder.keras"
if not os.path.exists(test_filepath):
    print(f"⚠️  Archivo no encontrado: {test_filepath}")
    print("   Necesitas ejecutar primero el test de save() (Paso 8.2)")
    print("   O asegúrate de que test_model_fit existe y ejecuta:")
    print("   saved_model = save(test_model_fit, name='test_autoencoder')")
else:
    try:
        loaded_model = load("test_autoencoder")
        print("✅ Modelo cargado exitosamente")
        
        # Verificar que son equivalentes (solo si test_model_fit existe)
        if 'test_model_fit' in globals():
            print("\n🔍 Verificando que el modelo cargado funciona...")
            test_input = np.random.randn(1, 5)  # 5 features
            output_original = test_model_fit.predict(test_input, verbose=0)
            output_loaded = loaded_model.predict(test_input, verbose=0)
            
            if np.allclose(output_original, output_loaded):
                print("✅ Los modelos producen resultados idénticos")
            else:
                print("⚠️  Los modelos producen resultados diferentes")
        else:
            print("⚠️  test_model_fit no está definido, no se puede verificar equivalencia")
            print("   Pero el modelo se cargó correctamente ✅")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
```

**Nota**: Este test requiere que:
1. Se haya ejecutado el test de `save()` primero (Paso 8.2)
2. El archivo `test_autoencoder.keras` exista en `MODEL_DIRECTORY`

### 8.5 Notas sobre `save()` y DSDL

**¿Cómo DSDL usa `save()`?**

Cuando ejecutas desde SPL:
```spl
| fit MLTKContainer algo=app1_autoencoder_demo_anomalias_v1 into app:demo_model_v1
```

DSDL automáticamente:
1. Ejecuta `fit(model, df, param)` y obtiene el modelo entrenado
2. **Llama a `save(model, "demo_model_v1")`** ← REQUERIDO
3. Persiste el modelo guardado
4. Cuando ejecutas `apply demo_model_v1`, DSDL carga el modelo y lo pasa a `apply()`

**Importante**: 
- La función `save()` **DEBE** tener la firma: `def save(model, name):`
- **DEBE** retornar el modelo: `return model`
- El parámetro `name` viene de `into app:model_name` en SPL

---

## 🧪 Paso 9: Testing End-to-End Local

### 9.1 Test Completo con Datos Reales de Splunk

```python
# THIS CELL IS NOT EXPORTED - Test E2E completo local
from dsdlsupport import SplunkSearch

print("=" * 60)
print("TEST END-TO-END COMPLETO")
print("=" * 60)

# 1. Obtener datos reales de Splunk
print("\n📥 Paso 1: Obteniendo datos de Splunk...")
search = SplunkSearch.SplunkSearch(
    search='index=demo_anomalias_data | head 500 | table feature_*'
)
df_real = search.as_df()
print(f"✅ Datos obtenidos: {df_real.shape}")

# 2. Inicializar modelo
print("\n🔧 Paso 2: Inicializando modelo...")
param_init = {
    'feature_variables': [col for col in df_real.columns if col.startswith('feature_')],
    'options': {
        'params': {
            'encoding_dim': 10
        }
    }
}
model_real = init(df_real, param_init)
print("✅ Modelo inicializado")

# 3. Entrenar modelo
print("\n🏋️  Paso 3: Entrenando modelo (esto tomará varios minutos)...")
param_fit = {
    'feature_variables': [col for col in df_real.columns if col.startswith('feature_')],
    'options': {
        'params': {
            'epochs': '20',  # Pocas épocas para test rápido
            'batch_size': '32',
            'validation_split': '0.2'
        }
    }
}
fit_results_real = fit(model_real, df_real, param_fit)
print("✅ Modelo entrenado")

# 4. Aplicar modelo
print("\n🔮 Paso 4: Aplicando modelo...")
param_apply = {
    'feature_variables': [col for col in df_real.columns if col.startswith('feature_')],
    'scaler': fit_results_real.get('scaler')
}
results_real = apply(model_real, df_real, param_apply)
print("✅ Modelo aplicado")

# 5. Resumen
print("\n📊 Paso 5: Resumen del modelo...")
summary_real = summary(model_real)
print(f"✅ Resumen generado")

# 6. Mostrar resultados
print("\n" + "=" * 60)
print("RESULTADOS FINALES")
print("=" * 60)
print(f"✅ Modelo: {MODEL_NAME}")
print(f"✅ Datos procesados: {df_real.shape[0]} muestras")
print(f"✅ Anomalías detectadas: {results_real['is_anomaly'].sum()} ({100*results_real['is_anomaly'].mean():.2f}%)")
print(f"✅ Loss final: {fit_results_real.get('model_loss', 'N/A')}")
print(f"✅ RMSE: {fit_results_real.get('rmse', 'N/A')}")

print("\n🎉 Test E2E completado exitosamente!")
```

**✅ Validación**: Verifica que todo el flujo funciona de extremo a extremo con datos reales.

---

## 💾 Paso 10: Guardar el Notebook - Publicación Automática

### 10.1 Preparar Notebook para Guardado

**IMPORTANTE**: Antes de guardar, verifica:

1. **Todas las funciones están definidas**:
   - [ ] `init(df, param)` con comentario `# mltkc_init` y metadata `"name": "mltkc_init"`
   - [ ] `fit(model, df, param)` con comentario `# mltkc_stage_create_model_fit` y metadata `"name": "mltkc_stage_create_model_fit"`
   - [ ] `apply(model, df, param)` con comentario `# mltkc_stage_create_model_apply` y metadata `"name": "mltkc_stage_create_model_apply"`
   - [ ] `summary(model=None)` con comentario adecuado
   - [ ] `save(model, name)` **REQUERIDA** - Con metadata `"name": "mltkc_save"` en la celda

2. **Imports están en la célula correcta**:
   - [ ] Imports principales en célula con `# mltkc_import`
   - [ ] Helpers empresariales importados

3. **Sin errores de sintaxis**:
   - [ ] Ejecuta "Cell → Run All" para verificar que no hay errores
   - [ ] Revisa que todas las células ejecutan correctamente

### 10.2 Guardar el Notebook

1. En JupyterLab, haz clic en: **File → Save Notebook**
2. O usa el atajo: `Cmd+S` (Mac) / `Ctrl+S` (Windows/Linux)

**Esto dispara automáticamente**:
- DSDL escanea el notebook
- Extrae las funciones `init`, `fit`, `apply`, `summary`, `save`
- Exporta a `/srv/app/model/app1_autoencoder_demo_anomalias_v1.py`
- Publica el modelo para uso desde SPL

### 10.3 Verificar Exportación Automática

```python
# THIS CELL IS NOT EXPORTED - Verificar exportación
import os

model_file = f"/srv/app/model/{MODEL_NAME}.py"
print(f"🔍 Verificando archivo exportado: {model_file}")

if os.path.exists(model_file):
    print(f"✅ Archivo exportado encontrado!")
    print(f"📄 Tamaño: {os.path.getsize(model_file)} bytes")
    
    # Leer primeras líneas
    with open(model_file, 'r') as f:
        lines = f.readlines()[:20]
        print("\n📝 Primeras 20 líneas del archivo exportado:")
        print("=" * 60)
        for i, line in enumerate(lines, 1):
            print(f"{i:3d}: {line.rstrip()}")
else:
    print(f"⚠️  Archivo no encontrado aún. Esto es normal si:")
    print(f"   - Acabas de guardar (puede tardar unos segundos)")
    print(f"   - Hay errores en las funciones")
    print(f"   - Las funciones no tienen los comentarios correctos")
```

### 10.4 Verificar Logs de DSDL

Si el archivo no aparece, revisa los logs:

```python
# THIS CELL IS NOT EXPORTED - Revisar logs
import subprocess

print("🔍 Buscando logs de exportación...")
# Nota: Los logs están en el contenedor, no en el notebook
# Para ver logs, ejecuta en terminal del contenedor o revisa Splunk
print("💡 Para ver logs completos, ejecuta en terminal del contenedor:")
print("   docker logs <container-id> | grep -i export")
print("\n💡 O busca en Splunk:")
print("   index=_internal \"mltk-container\" export")
```

---

## 🚀 Paso 11: Validar Modelo desde Splunk SPL

### 11.1 Usar Modelo con `fit` desde SPL

Una vez guardado el notebook y exportado, prueba desde Splunk Web:

```spl
index=demo_anomalias_data
| head 1000
| fit MLTKContainer algo=app1_autoencoder_demo_anomalias_v1 epochs=20 batch_size=32 encoding_dim=10 from feature_* into app:demo_anomalias_model_v1
```

**Explicación**:
- `algo=app1_autoencoder_demo_anomalias_v1`: Nombre del notebook (sin .ipynb)
- `epochs=20`: Parámetro pasado a `fit()`
- `from feature_*`: Selecciona todas las columnas que empiezan con `feature_`
- `into app:demo_anomalias_model_v1`: Nombre del modelo guardado

### 11.2 Verificar que `fit` Funciona

Después de ejecutar el comando `fit`, deberías ver:
- ✅ Mensaje de éxito
- ✅ Métricas de entrenamiento
- ✅ Modelo guardado

Si hay errores:
1. Revisa los logs en Splunk: `index=_internal "mltk-container" ERROR`
2. Verifica que el archivo `.py` se exportó correctamente
3. Verifica que las funciones tienen las firmas correctas

### 11.3 Usar Modelo con `apply` desde SPL

Una vez entrenado, prueba la inferencia:

```spl
index=demo_anomalias_data
| head 500
| apply demo_anomalias_model_v1
| table feature_*, reconstruction_error, anomaly_score, is_anomaly
| head 20
```

**Resultado esperado**: Deberías ver columnas nuevas:
- `reconstruction_error`: Error de reconstrucción
- `anomaly_score`: Score normalizado de anomalía
- `is_anomaly`: 1 si es anomalía, 0 si no

### 11.4 Visualizar Anomalías en Splunk

```spl
index=demo_anomalias_data
| apply demo_anomalias_model_v1
| stats count by is_anomaly
| eval anomaly_percentage = if(is_anomaly=1, count, 0) / sum(count) * 100
```

---

## 🔧 Troubleshooting

Si encuentras problemas durante el flujo E2E, consulta la **Guía de Troubleshooting** para soluciones detalladas:

📄 **`TROUBLESHOOTING.md`** - Guía completa de solución de problemas

**Problemas comunes**:
- El notebook no se exporta automáticamente
- Errores al ejecutar `fit` desde SPL
- Helpers no se importan
- Telemetría no llega a Splunk
- Error "no attribute 'save'"
- Problemas de serialización JSON

**Para diagnóstico completo de telemetría**, consulta también:
📄 **`DIAGNOSTICO_TELEMETRIA.md`** - Diagnóstico específico de telemetría

---

## ✅ Checklist Final de Publicación

Antes de considerar el modelo "publicado y listo":

- [ ] Notebook guardado con nombre estándar: `app1_autoencoder_demo_anomalias_v1.ipynb`
- [ ] Archivo `.py` exportado existe en `/srv/app/model/`
- [ ] Función `init()` funciona correctamente
- [ ] Función `fit()` entrena sin errores
- [ ] Función `apply()` detecta anomalías
- [ ] Función `summary()` retorna metadatos
- [ ] Test E2E local funciona completamente
- [ ] Comando `fit` desde SPL funciona
- [ ] Comando `apply` desde SPL funciona
- [ ] Telemetría llega a Splunk (si está configurada)
- [ ] Anomalías detectadas son razonables

---

## 📚 Recursos Adicionales

### Documentación
- **Documentación DSDL**: https://docs.splunk.com/Documentation/DSDL
- **Guía de Troubleshooting**: `TROUBLESHOOTING.md` - Solución de problemas comunes
- **Diagnóstico de Telemetría**: `DIAGNOSTICO_TELEMETRIA.md` - Diagnóstico específico de telemetría

### Archivos del Sistema
- **Template empresarial**: `/dltk/notebooks_custom/template_empresa_base.ipynb`
- **Helpers empresariales**: `/dltk/notebooks_custom/helpers/`

### Splunk Queries
- **Logs de DSDL**: `index=_internal "mltk-container"`
- **Métricas del modelo**: `index=ml_metrics model_name=app1_autoencoder_demo_anomalias_v1`
- **Logs de entrenamiento**: `index=ml_model_logs model_name=app1_autoencoder_demo_anomalias_v1`

---

## 🎯 Próximos Pasos

Una vez que el modelo está publicado y funcionando:

1. **Monitorear métricas**: Revisar `index=ml_metrics` regularmente
2. **Ajustar thresholds**: Modificar percentil de anomalías según necesidad
3. **Crear dashboards**: Visualizar anomalías en tiempo real
4. **Configurar alertas**: Alertar cuando anomalías superen umbral
5. **Refinar modelo**: Iterar con más datos o arquitecturas diferentes

---

**¡Felicidades! Has completado el workflow end-to-end de un Data Scientist con DSDL.** 🎉

