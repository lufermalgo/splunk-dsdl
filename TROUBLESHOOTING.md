# 🔧 Troubleshooting: Guía de Solución de Problemas para DSDL

**Objetivo**: Esta guía contiene soluciones detalladas para problemas comunes que pueden surgir durante el desarrollo y despliegue de modelos en Splunk DSDL.

**Cuándo usar esta guía**: Si encuentras errores durante el flujo E2E, consulta esta guía después de revisar la **Guía Completa Data Scientist E2E**.

---

## 📋 Índice de Problemas

1. [El Notebook No se Exporta Automáticamente](#1-el-notebook-no-se-exporta-automáticamente)
2. [Errores al Ejecutar `fit` desde SPL](#2-errores-al-ejecutar-fit-desde-spl)
3. [Helpers No se Importan](#3-helpers-no-se-importan)
4. [Telemetría No Llega a Splunk](#4-telemetría-no-llega-a-splunk)
5. [Error "no attribute 'save'" al Ejecutar `fit` desde SPL](#5-error-no-attribute-save-al-ejecutar-fit-desde-spl)
6. [Modelo No Guarda el Scaler](#6-modelo-no-guarda-el-scaler)
7. [Diagnóstico de Telemetría Completo](#7-diagnóstico-de-telemetría-completo)
8. [Problemas Críticos de Serialización JSON](#8-problemas-críticos-de-serialización-json)

---

## 1. El Notebook No se Exporta Automáticamente

### Problema

Después de guardar el notebook, el archivo `.py` no aparece en `/srv/app/model/`

### Soluciones

#### 1.1 Verificar Comentarios en Funciones

Los comentarios especiales son **CRÍTICOS** para que DSDL identifique las funciones:

```python
# mltkc_init  ← Debe estar antes de def init()
# mltkc_stage_create_model_fit  ← Debe estar antes de def fit()
# mltkc_stage_create_model_apply  ← Debe estar antes de def apply()
# mltkc_save  ← Debe estar antes de def save()
```

#### 1.2 Verificar Nombres de Funciones

Los nombres deben ser **exactos**:
- ✅ `init`, `fit`, `apply`, `summary`, `save`
- ❌ `init_model`, `fit_model`, `train_model`, etc.

#### 1.3 Verificar Firmas de Funciones

Las firmas deben coincidir exactamente:

```python
def init(df, param):  # ✅ Correcto
def fit(model, df, param):  # ✅ Correcto
def apply(model, df, param):  # ✅ Correcto
def summary(model=None):  # ✅ Correcto
def save(model, name):  # ✅ Correcto
```

#### 1.4 Verificar Metadata de Celdas

**⚠️ CRÍTICO**: Cada función debe tener el metadata correcto en su celda de código.

Para más detalles sobre cómo agregar metadata, consulta la **Sección 3.5: Entender el Metadata de Celdas** en la **Guía Completa Data Scientist E2E**.

#### 1.5 Reiniciar Contenedor DEV

Si nada funciona:
1. En DSDL → Containers → Stop
2. Espera a que se detenga completamente
3. En DSDL → Containers → Start
4. Esto fuerza una re-escaneo de notebooks

---

## 2. Errores al Ejecutar `fit` desde SPL

### Problema

El comando `fit` falla con error de importación o sintaxis cuando se ejecuta desde Splunk.

### Soluciones

#### 2.1 Revisar Logs en Splunk

```spl
index=_internal "mltk-container" ERROR
| head 50
| table _time message
```

#### 2.2 Verificar Librerías Instaladas

En JupyterLab, ejecuta:

```python
# Verificar librerías principales
import tensorflow
import keras
from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd

print(f"✅ TensorFlow: {tensorflow.__version__}")
print(f"✅ Keras: {keras.__version__}")
print(f"✅ NumPy: {np.__version__}")
print(f"✅ Pandas: {pd.__version__}")
```

Si alguna falla, la imagen Docker no tiene las librerías necesarias.

#### 2.3 Verificar Paths de Helpers

Los helpers deben estar en `/dltk/notebooks_custom/helpers/` o `/srv/notebooks_custom/helpers/`

En JupyterLab, ejecuta:

```python
import os
helpers_paths = [
    '/dltk/notebooks_custom/helpers',
    '/srv/notebooks_custom/helpers'
]

for path in helpers_paths:
    exists = os.path.exists(path)
    print(f"{'✅' if exists else '❌'} {path}: {'EXISTE' if exists else 'NO EXISTE'}")
    
    if exists:
        files = os.listdir(path)
        print(f"   Archivos: {files}")
```

---

## 3. Helpers No se Importan

### Problema

Error `ModuleNotFoundError: No module named 'telemetry_helper'`

### Soluciones

#### 3.1 Verificar Path

```python
import sys
sys.path.append('/dltk/notebooks_custom/helpers')
print(sys.path)  # Verificar que el path está agregado
```

#### 3.2 Verificar que los Archivos Existen

```python
import os
helpers_dir = '/dltk/notebooks_custom/helpers'
print(f"Directorio existe: {os.path.exists(helpers_dir)}")

if os.path.exists(helpers_dir):
    files = os.listdir(helpers_dir)
    print(f"Archivos: {files}")
    
    if 'telemetry_helper.py' in files:
        print("✅ telemetry_helper.py encontrado")
    else:
        print("❌ telemetry_helper.py NO encontrado")
```

#### 3.3 Verificar Permisos

En terminal del contenedor:

```bash
ls -la /dltk/notebooks_custom/helpers/
```

Si no tienes acceso, verifica permisos del contenedor.

---

## 4. Telemetría No Llega a Splunk

### Problema

Las métricas no aparecen en `index=ml_metrics` o `index=ml_model_logs`

### Soluciones Rápidas

#### 4.1 Verificar Configuración HEC

En Splunk Web:
1. Ve a: **DSDL → Setup → Splunk HEC Settings**
2. Verifica que:
   - **Enable Splunk HEC**: `Yes`
   - **Splunk HEC Token**: Token válido
   - **Splunk HEC Endpoint URL**: URL correcta

#### 4.2 Verificar Índices

En Splunk Web:
1. Ve a: **Settings → Indexes**
2. Verifica que existen:
   - `ml_metrics`
   - `ml_model_logs`

#### 4.3 Verificar Permisos del Token

En Splunk Web:
1. Ve a: **Settings → Data Inputs → HTTP Event Collector**
2. Haz clic en tu token HEC
3. Verifica que **"Allowed Indexes"** incluye:
   - `ml_metrics`
   - `ml_model_logs`

#### 4.4 Probar Telemetría Manualmente

En JupyterLab:

```python
from telemetry_helper import log_metrics
log_metrics(model_name="test", mse=0.5, rmse=0.7)
```

Luego verifica en Splunk (después de 10-30 segundos):

```spl
index=ml_metrics model_name=test
| head 10
```

### Diagnóstico Completo

Para un diagnóstico completo de telemetría, consulta la **Sección 7: Diagnóstico de Telemetría Completo** más abajo en este documento.

---

## 5. Error "no attribute 'save'" al Ejecutar `fit` desde SPL

### Problema

Error: `module 'app.model.app1_autoencoder_demo_anomalias_v1' has no attribute 'save'`

### Causa Común

La función `save()` no tiene el metadata correcto en la celda del notebook, por lo que DSDL no la exporta automáticamente.

### Solución Paso a Paso

#### 5.1 Verificar que la Función `save()` Está Definida

En el notebook, busca la función:

```python
def save(model, name):
    # ... código ...
    return model
```

#### 5.2 ⚠️ CRÍTICO: Agregar Metadata a la Celda

**IMPORTANTE**: Para una explicación completa sobre qué es el metadata, por qué es importante y cómo agregarlo correctamente, consulta la **Sección 3.5: Entender el Metadata de Celdas** en la **Guía Completa Data Scientist E2E**.

**Resumen rápido**:

1. **Selecciona la CELDA DE CÓDIGO** que contiene `def save()`, NO la celda markdown
2. Ve a: **View → Cell Toolbar → Edit Metadata**
3. En el editor JSON, agrega el metadata completo:

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

4. Haz clic en "Apply" o "Save"
5. **Guarda el notebook** (Cmd+S / Ctrl+S)

#### 5.3 Verificar Firma Correcta

```python
def save(model, name):  # ✅ Correcto
    return model  # ✅ Debe retornar el modelo
```

#### 5.4 Verificar que el Archivo `.py` Exportado Contiene `save()`

En JupyterLab:

```python
import os
py_file = "/srv/app/model/app1_autoencoder_demo_anomalias_v1.py"

if os.path.exists(py_file):
    with open(py_file, 'r') as f:
        content = f.read()
        if 'def save(' in content:
            print("✅ Función save() encontrada en archivo exportado")
        else:
            print("❌ Función save() NO encontrada en archivo exportado")
            print("⚠️  Verifica que la celda tiene metadata 'name': 'mltkc_save'")
else:
    print(f"❌ Archivo .py no existe: {py_file}")
```

---

## 6. Modelo No Guarda el Scaler

### Problema

En `apply()`, el scaler no está disponible cuando se necesita.

### Solución

El scaler debe pasarse desde `fit()` a `apply()` a través de `param`:

#### En `fit()`:

```python
def fit(model, df, param):
    # ... código ...
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # ⚠️ IMPORTANTE: Guardar scaler en returns
    returns = {}
    returns['scaler'] = scaler  # Guardar para uso posterior
    
    # ... resto del código ...
    return returns
```

#### En `apply()`:

```python
def apply(model, df, param):
    # ... código ...
    
    # Obtener scaler de param (viene de fit)
    if 'scaler' in param:
        scaler = param['scaler']
        print("✅ Usando scaler del entrenamiento")
    else:
        # Fallback: crear nuevo (menos ideal)
        print("⚠️  Scaler no encontrado. Creando nuevo...")
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
    
    # ... resto del código ...
```

**Nota**: DSDL pasa el `returns` de `fit()` como parte de `param` en `apply()`. Si esto no funciona, puede ser un bug de DSDL o un problema de configuración.

---

## 7. Diagnóstico de Telemetría Completo

### ⚠️ PROBLEMA CRÍTICO: No se ve telemetría en Splunk después de ejecutar `fit` y `apply`

**El monitoreo de modelos es CRUCIAL para el desarrollo de ciencia de datos en producción.** Si ejecutaste `fit` y `apply` desde Splunk pero no ves telemetría en los índices `ml_metrics` o `ml_model_logs`, sigue estos pasos de diagnóstico **EN ORDEN**:

### 🔴 PASO CRÍTICO 0: Verificar Logs del Contenedor cuando Ejecutas desde Splunk

**⚠️ IMPORTANTE**: Cuando ejecutas `fit` o `apply` desde Splunk (no desde JupyterLab), los errores de telemetría pueden estar en los logs del contenedor pero NO aparecen en la salida de Splunk.

**Ejecuta esto INMEDIATAMENTE después de ejecutar `fit` o `apply` desde Splunk:**

```bash
# En terminal local (NO en JupyterLab)
# Obtener ID del contenedor DSDL activo
docker ps | grep mltk-container

# Ver logs recientes del contenedor (últimas 500 líneas)
CONTAINER_ID=$(docker ps | grep mltk-container | awk '{print $1}' | head -1)
docker logs $CONTAINER_ID --tail 500 | grep -i "telemetry\|hec\|error\|traceback" -A 5 -B 2

# O ver TODOS los logs recientes
docker logs $CONTAINER_ID --tail 1000 | tail -100
```

**O en Splunk, busca logs del contenedor:**

```spl
index=_internal "mltk-container" 
| search "telemetry" OR "hec" OR "Error enviando" OR "traceback"
| head 50
| table _time message
```

**Si ves errores de telemetría en los logs**, copia el error completo y continúa con el diagnóstico correspondiente abajo.

### Paso 1: Verificar que HEC está Configurado

**En Splunk Web:**
1. Ve a: **DSDL → Setup → Splunk HEC Settings**
2. Verifica que:
   - **Enable Splunk HEC**: `Yes`
   - **Splunk HEC Token**: Tiene un token válido
   - **Splunk HEC Endpoint URL**: Configurado correctamente (ej: `http://localhost:8088` o `http://host.docker.internal:8088`)

**⚠️ IMPORTANTE**: Si estás en macOS con Docker Desktop, usa `http://host.docker.internal:8088` en lugar de `http://localhost:8088`.

### Paso 2: Verificar que los Índices Existen

**En Splunk Web:**
1. Ve a: **Settings → Indexes**
2. Verifica que existen:
   - `ml_metrics` (para métricas del modelo)
   - `ml_model_logs` (para logs de entrenamiento e inferencia)

**Si no existen, créalos:**
```bash
# En Splunk CLI
/Applications/Splunk/bin/splunk cmd
./splunk add index ml_metrics
./splunk add index ml_model_logs
```

### Paso 3: Verificar que el HEC Token Tiene Acceso a los Índices

**En Splunk Web:**
1. Ve a: **Settings → Data Inputs → HTTP Event Collector**
2. Haz clic en tu token HEC
3. Verifica que **"Allowed Indexes"** incluye:
   - `ml_metrics`
   - `ml_model_logs`

**Si no están, agrega los índices al token.**

### Paso 4: Verificar que las Funciones de Telemetría Están en el Código

**En JupyterLab, ejecuta:**
```python
# Verificar que el archivo .py exportado tiene telemetría
import os
py_file = f"/srv/app/model/{MODEL_NAME}.py"

if os.path.exists(py_file):
    with open(py_file, 'r') as f:
        content = f.read()
        
        # Verificar fit() tiene telemetría
        if 'log_metrics' in content and 'def fit(' in content:
            print("✅ fit() tiene llamadas a log_metrics")
        else:
            print("❌ fit() NO tiene llamadas a log_metrics")
            
        # Verificar fit() tiene callback de telemetría
        if 'log_training_step' in content:
            print("✅ fit() tiene callback de telemetría por época")
        else:
            print("❌ fit() NO tiene callback de telemetría por época")
            
        # Verificar apply() tiene telemetría
        if 'log_prediction' in content or ('log_metrics' in content and 'def apply(' in content):
            print("✅ apply() tiene llamadas de telemetría")
        else:
            print("❌ apply() NO tiene llamadas de telemetría")
            print("   ⚠️  AGREGAR: Código de telemetría en apply()")
else:
    print(f"❌ Archivo .py no existe: {py_file}")
```

### Paso 5: Verificar que los Helpers Están Importados Correctamente

**En JupyterLab, ejecuta:**
```python
# Verificar que los helpers están disponibles
import sys
sys.path.append('/dltk/notebooks_custom/helpers')

try:
    from telemetry_helper import log_metrics, log_training_step, log_error
    print("✅ telemetry_helper importado correctamente")
    
    # Verificar que log_prediction existe (o usar log_metrics)
    try:
        from telemetry_helper import log_prediction
        print("✅ log_prediction disponible")
    except ImportError:
        print("⚠️  log_prediction NO disponible (usar log_metrics como alternativa)")
        
except ImportError as e:
    print(f"❌ Error importando telemetry_helper: {e}")
    print("   Verifica que el path es correcto: /dltk/notebooks_custom/helpers")
```

### Paso 6: Probar Telemetría Manualmente (Test End-to-End) - CRÍTICO

**⚠️ IMPORTANTE**: Este test debe ejecutarse desde el MISMO entorno donde DSDL ejecuta el modelo (no solo JupyterLab).

**En JupyterLab, ejecuta:**
```python
# THIS CELL IS NOT EXPORTED - Test telemetría manual con diagnóstico completo
import sys
import os
import traceback

# CRÍTICO: Verificar path de helpers (puede ser diferente cuando DSDL ejecuta)
print("🔍 Diagnóstico Completo de Telemetría\n")
print("=" * 60)

# Verificar variables de entorno HEC
print("\n1️⃣ Variables de Entorno HEC:")
hec_enabled = os.environ.get('splunk_hec_enabled', 'NO DEFINIDO')
hec_url = os.environ.get('splunk_hec_url', 'NO DEFINIDO')
hec_token = os.environ.get('splunk_hec_token', 'NO DEFINIDO')

print(f"   splunk_hec_enabled: {hec_enabled}")
print(f"   splunk_hec_url: {hec_url}")
print(f"   splunk_hec_token: {'DEFINIDO (' + str(len(hec_token)) + ' chars)' if hec_token != 'NO DEFINIDO' else 'NO DEFINIDO'}")

if hec_enabled != '1':
    print("\n❌ PROBLEMA: splunk_hec_enabled no es '1'")
    print("   Solución: Configurar HEC en DSDL Setup → Splunk HEC Settings")
    print("   Luego: REINICIAR el contenedor")
elif hec_url == 'NO DEFINIDO' or hec_token == 'NO DEFINIDO':
    print("\n❌ PROBLEMA: HEC URL o Token no están definidos")
    print("   Solución: Configurar HEC en DSDL Setup → Splunk HEC Settings")
    print("   Luego: REINICIAR el contenedor")
else:
    print("\n✅ HEC está configurado en variables de entorno")

# Verificar path de helpers
print("\n2️⃣ Path de Helpers:")
helpers_paths = [
    '/dltk/notebooks_custom/helpers',
    '/srv/notebooks_custom/helpers',
    '/srv/notebooks/helpers'
]

for path in helpers_paths:
    exists = os.path.exists(path)
    status = "✅" if exists else "❌"
    print(f"   {status} {path}: {'EXISTE' if exists else 'NO EXISTE'}")
    
    if exists:
        try:
            files = os.listdir(path)
            if 'telemetry_helper.py' in files:
                print(f"      ✅ telemetry_helper.py encontrado")
            else:
                print(f"      ❌ telemetry_helper.py NO encontrado")
                print(f"      Archivos disponibles: {files[:5]}")
        except Exception as e:
            print(f"      ⚠️  Error listando archivos: {e}")

# Intentar importar helpers
print("\n3️⃣ Importación de Helpers:")
sys.path.extend(helpers_paths)

try:
    from telemetry_helper import log_metrics, log_training_step, log_error
    print("✅ telemetry_helper importado correctamente")
    
    # Verificar que las funciones están disponibles
    print(f"   Funciones disponibles: log_metrics={callable(log_metrics)}, log_training_step={callable(log_training_step)}")
    
except ImportError as e:
    print(f"❌ Error importando telemetry_helper: {e}")
    print(f"   Traceback completo:")
    print(traceback.format_exc())
    print("\n⚠️  ACCIÓN REQUERIDA: Verificar que telemetry_helper.py existe en uno de los paths")
    sys.exit(1)

# Test 1: Enviar métricas con diagnóstico completo
print("\n4️⃣ Test 1: log_metrics()")
print("-" * 60)
try:
    result = log_metrics(
        model_name=MODEL_NAME,
        r2_score=0.95,
        mae=0.05,
        rmse=0.08,
        loss=0.1,
        app_name=APP_NAME,
        model_version=VERSION,
        project=USE_CASE
    )
    print("✅ Test 1: log_metrics() ejecutado sin errores")
    print(f"   Retorno: {result}")
except Exception as e:
    print(f"❌ Test 1: Error en log_metrics(): {e}")
    print(f"   Tipo de error: {type(e).__name__}")
    print(f"   Traceback completo:")
    print(traceback.format_exc())
    print("\n⚠️  ACCIÓN REQUERIDA: Revisar el traceback para identificar el problema")

# Test 2: Enviar training step con diagnóstico completo
print("\n5️⃣ Test 2: log_training_step()")
print("-" * 60)
try:
    result = log_training_step(
        model_name=MODEL_NAME,
        epoch=1,
        loss=0.5,
        val_loss=0.6,
        mae=0.1,
        val_mae=0.12
    )
    print("✅ Test 2: log_training_step() ejecutado sin errores")
    print(f"   Retorno: {result}")
except Exception as e:
    print(f"❌ Test 2: Error en log_training_step(): {e}")
    print(f"   Tipo de error: {type(e).__name__}")
    print(f"   Traceback completo:")
    print(traceback.format_exc())
    print("\n⚠️  ACCIÓN REQUERIDA: Revisar el traceback para identificar el problema")

print("\n" + "=" * 60)
print("📊 Verificar en Splunk (después de 10-30 segundos):")
print("   index=ml_metrics model_name=app1_autoencoder_demo_anomalias_v1 | head 10")
print("   index=ml_model_logs model_name=app1_autoencoder_demo_anomalias_v1 | head 10")
print("\n⚠️  Si los tests pasan pero no ves datos en Splunk:")
print("   1. Verifica que HEC está habilitado en Splunk")
print("   2. Verifica que el token tiene acceso a ml_metrics y ml_model_logs")
print("   3. Verifica que los índices existen")
print("   4. Revisa los logs del contenedor (ver Paso 0)")
```

### Paso 7: Verificar Telemetría en Splunk

**En Splunk, ejecuta:**
```spl
# Verificar métricas de entrenamiento
index=ml_metrics model_name=app1_autoencoder_demo_anomalias_v1
| head 10
| table _time model_name loss mae rmse

# Verificar logs de entrenamiento por época
index=ml_model_logs model_name=app1_autoencoder_demo_anomalias_v1
| head 10
| table _time model_name epoch loss val_loss

# Verificar métricas de inferencia
index=ml_metrics model_name=app1_autoencoder_demo_anomalias_v1 num_predictions=*
| head 10
| table _time model_name num_predictions num_anomalies avg_reconstruction_error
```

**Si no ves datos:**
1. Verifica que HEC está habilitado en Splunk
2. Verifica que el token tiene acceso a los índices
3. Verifica que no hay errores en los logs del contenedor (ver Paso 0)

### Paso 8: Revisar Logs del Contenedor

**En terminal, ejecuta:**
```bash
# Ver logs del contenedor DSDL
docker ps | grep mltk-container
docker logs <CONTAINER_ID> --tail 100 | grep -i "hec\|telemetry\|error"
```

### Paso 9: Verificar Variables de Entorno del Contenedor - CRÍTICO

**⚠️ IMPORTANTE**: Las variables de entorno pueden ser diferentes cuando DSDL ejecuta desde Splunk vs cuando ejecutas desde JupyterLab.

**En JupyterLab, ejecuta:**
```python
# THIS CELL IS NOT EXPORTED - Verificar variables de entorno HEC
import os

print("🔍 Variables de Entorno HEC - Diagnóstico Completo\n")
print("=" * 60)

# Obtener todas las variables relacionadas con HEC
hec_vars = {
    'splunk_hec_enabled': os.environ.get('splunk_hec_enabled', 'NO DEFINIDO'),
    'splunk_hec_url': os.environ.get('splunk_hec_url', 'NO DEFINIDO'),
    'splunk_hec_token': os.environ.get('splunk_hec_token', 'NO DEFINIDO')
}

print("Variables de entorno:")
for key, value in hec_vars.items():
    if key == 'splunk_hec_token':
        # Mostrar solo primeros y últimos caracteres del token por seguridad
        if value != 'NO DEFINIDO':
            token_preview = value[:10] + '...' + value[-10:] if len(value) > 20 else '***'
            status = "✅"
            print(f"{status} {key}: {token_preview} (longitud: {len(value)})")
        else:
            status = "❌"
            print(f"{status} {key}: {value}")
    else:
        status = "✅" if value != 'NO DEFINIDO' else "❌"
        print(f"{status} {key}: {value}")

print("\n" + "=" * 60)

# Diagnóstico
if hec_vars['splunk_hec_enabled'] != '1':
    print("\n❌ PROBLEMA CRÍTICO: splunk_hec_enabled no es '1'")
    print("   Esto significa que HEC NO está habilitado")
    print("\n   Solución:")
    print("   1. Ve a: DSDL → Setup → Splunk HEC Settings")
    print("   2. Configura: Enable Splunk HEC = Yes")
    print("   3. REINICIA el contenedor (DSDL configura variables al iniciar)")
    print("   4. Vuelve a ejecutar este test")
elif hec_vars['splunk_hec_url'] == 'NO DEFINIDO' or hec_vars['splunk_hec_token'] == 'NO DEFINIDO':
    print("\n❌ PROBLEMA CRÍTICO: HEC URL o Token no están definidos")
    print("   Esto significa que HEC no está configurado correctamente")
    print("\n   Solución:")
    print("   1. Ve a: DSDL → Setup → Splunk HEC Settings")
    print("   2. Configura: Splunk HEC Token y Splunk HEC Endpoint URL")
    print("   3. REINICIA el contenedor")
    print("   4. Vuelve a ejecutar este test")
else:
    print("\n✅ HEC está configurado en variables de entorno")
    print("   Si aún no funciona, revisa:")
    print("   - Paso 1: HEC habilitado en Splunk")
    print("   - Paso 2: Índices existen")
    print("   - Paso 3: Token tiene acceso a índices")
    print("   - Paso 6: Test manual de telemetría")
    print("   - Paso 0: Logs del contenedor (CUANDO ejecutas desde Splunk)")

# Verificar URL específica
if hec_vars['splunk_hec_url'] != 'NO DEFINIDO':
    print(f"\n🔍 URL de HEC: {hec_vars['splunk_hec_url']}")
    if 'localhost' in hec_vars['splunk_hec_url']:
        print("   ⚠️  ADVERTENCIA: 'localhost' puede no funcionar desde contenedor Docker")
        print("   Si estás en macOS con Docker Desktop, cambia a: http://host.docker.internal:8088")
        print("   En DSDL Setup → Splunk HEC Endpoint URL")
```

**Si `splunk_hec_enabled` no es `"1"` o `splunk_hec_url` está vacío:**
1. Ve a: **DSDL → Setup → Splunk HEC Settings**
2. Configura HEC correctamente:
   - **Enable Splunk HEC**: `Yes`
   - **Splunk HEC Token**: Token válido (debe tener acceso a `ml_metrics` y `ml_model_logs`)
   - **Splunk HEC Endpoint URL**: URL correcta (`http://localhost:8088` o `http://host.docker.internal:8088` en macOS)
3. **REINICIA el contenedor** (DSDL configura HEC en variables de entorno al iniciar)
4. **Vuelve a ejecutar este test** para verificar que las variables están definidas

### Paso 10: Solución de Problemas Comunes

#### Problema: "Connection refused" o "Connection timeout"

**Causa**: HEC URL incorrecta o HEC no está habilitado en Splunk.

**Solución**:
1. Verifica que HEC está habilitado: **Settings → Data Inputs → HTTP Event Collector → Enable**
2. Si estás en macOS con Docker Desktop, cambia la URL a `http://host.docker.internal:8088`
3. Reinicia el contenedor después de cambiar la configuración

#### Problema: "Unauthorized" o "Invalid token"

**Causa**: Token HEC incorrecto o sin permisos.

**Solución**:
1. Verifica que el token en DSDL Setup coincide con el token en Splunk
2. Verifica que el token tiene acceso a los índices `ml_metrics` y `ml_model_logs`

#### Problema: Datos no aparecen en Splunk

**Causa**: Índices incorrectos o token sin acceso.

**Solución**:
1. Verifica que los índices existen: `index=ml_metrics` y `index=ml_model_logs`
2. Verifica que el token tiene acceso a estos índices
3. Verifica que el source type del HEC token es `_json` (recomendado)

#### Problema: Funciones de telemetría no están en el `.py` exportado

**Causa**: El código de telemetría no está en el notebook o no se exportó correctamente.

**Solución**:
1. Verifica que el código de telemetría está en las celdas de código (no en markdown)
2. Verifica que el notebook se guardó correctamente
3. Verifica que el archivo `.py` exportado contiene las funciones de telemetría (ver Paso 4)

### ✅ Checklist de Validación de Telemetría - ORDEN CRÍTICO

**⚠️ IMPORTANTE**: Sigue este checklist EN ORDEN. Si un paso falla, NO continúes hasta resolverlo.

#### Fase 1: Configuración Básica
- [ ] **Paso 1**: HEC está habilitado en Splunk (Settings → Data Inputs → HTTP Event Collector → Enable)
- [ ] **Paso 2**: Los índices `ml_metrics` y `ml_model_logs` existen (Settings → Indexes)
- [ ] **Paso 3**: El token HEC tiene acceso a ambos índices (Settings → Data Inputs → HTTP Event Collector → Tu Token → Allowed Indexes)
- [ ] **Paso 1 (DSDL)**: HEC está configurado en DSDL Setup (DSDL → Setup → Splunk HEC Settings)
  - [ ] Enable Splunk HEC: `Yes`
  - [ ] Splunk HEC Token: Token válido
  - [ ] Splunk HEC Endpoint URL: URL correcta
- [ ] **REINICIO**: El contenedor fue REINICIADO después de configurar HEC (DSDL configura variables al iniciar)

#### Fase 2: Verificación de Variables de Entorno
- [ ] **Paso 9**: Variables de entorno del contenedor tienen `splunk_hec_enabled=1`
- [ ] **Paso 9**: Variables `splunk_hec_url` y `splunk_hec_token` están definidas
- [ ] **Paso 9**: URL es correcta (usar `host.docker.internal` en macOS si es necesario)

#### Fase 3: Verificación de Código
- [ ] **Paso 4**: Las funciones de telemetría están en el archivo `.py` exportado
- [ ] **Paso 5**: Los helpers están importados correctamente (path correcto)
- [ ] **Paso 6**: El test manual de telemetría funciona SIN ERRORES (desde JupyterLab)

#### Fase 4: Verificación End-to-End
- [ ] **Paso 0**: Revisaste logs del contenedor DESPUÉS de ejecutar `fit` desde Splunk (no desde JupyterLab)
- [ ] **Paso 6**: El test manual envió datos y aparecen en Splunk (verificar después de 10-30 segundos)
- [ ] **Paso 7**: Los datos aparecen en Splunk después de ejecutar `fit` desde Splunk (no desde JupyterLab)
- [ ] **Paso 7**: Los datos aparecen en Splunk después de ejecutar `apply` desde Splunk

#### Si TODO el checklist está completo pero NO ves telemetría:
1. **Revisa logs del contenedor en tiempo real** mientras ejecutas `fit` desde Splunk:
   ```bash
   docker logs -f <CONTAINER_ID> | grep -i "telemetry\|hec\|error"
   ```
2. **Verifica que telemetry_helper.py existe y es accesible** desde el path que DSDL usa
3. **Verifica que el formato del evento es correcto** (ver implementación de telemetry_helper)
4. **Contacta al equipo de DevOps** para verificar configuración de HEC en Splunk

---

## 8. Problemas Críticos de Serialización JSON

### 🔴 PROBLEMA CRÍTICO #1: "UnboundLocalError: local variable 'log_metrics' referenced before assignment"

**⚠️ IMPORTANTE**: Si ves este error en los logs del contenedor:
```
⚠️  Error enviando telemetría de inferencia a Splunk: local variable 'log_metrics' referenced before assignment
UnboundLocalError: local variable 'log_metrics' referenced before assignment
```

**CAUSA**: El código intenta usar `log_metrics()` fuera del bloque `try-except` que lo importa, o hay un problema de scope donde Python piensa que `log_metrics` es una variable local pero no está asignada.

**SOLUCIÓN**: Asegúrate de que:
1. La importación de `log_metrics` esté DENTRO del bloque `try-except`
2. El uso de `log_metrics()` esté DENTRO del mismo bloque `try-except` donde se importa
3. No haya código que intente usar `log_metrics` FUERA de los bloques de importación

**Código CORRECTO**:
```python
try:
    from telemetry_helper import log_prediction
    log_prediction(...)  # Usar DENTRO del try
except ImportError:
    from telemetry_helper import log_metrics
    log_metrics(...)  # Usar DENTRO del except
except Exception as e:
    # Capturar cualquier otro error
    print(f"Error: {e}")
```

**Código INCORRECTO** (causa el error):
```python
try:
    from telemetry_helper import log_prediction
except ImportError:
    from telemetry_helper import log_metrics

# ❌ ERROR: log_metrics puede no estar definido si log_prediction sí existe
log_metrics(...)  # Usar FUERA del try-except
```

### 🔴 PROBLEMA CRÍTICO #2: "Object of type int64 is not JSON serializable" en `summary()`

**⚠️ IMPORTANTE**: Si ves este error en los logs del contenedor:
```
TypeError: Object of type int64 is not JSON serializable
File "/srv/app/main.py", line 113, in get_summary
    return json.dumps(return_object)
```

**CAUSA**: DSDL intenta serializar el resultado de `summary()` a JSON automáticamente. Si `summary()` retorna valores NumPy (como `int64` de `model.count_params()` o `layer.count_params()`), DSDL fallará con `TypeError: Object of type int64 is not JSON serializable`.

**SOLUCIÓN**: En `summary()`, convertir TODOS los valores NumPy a tipos nativos de Python antes de retornarlos:
- `model.count_params()` → `int(model.count_params())` o `int(model.count_params().item())`
- `sum([tf.size(w).numpy() for w in model.trainable_weights])` → Convertir cada elemento a int nativo
- `layer.count_params()` → `int(layer.count_params())` o `int(layer.count_params().item())`

**Ejemplo completo**:
```python
def summary(model=None):
    returns = {
        "model_name": MODEL_NAME,
        # ... otros campos ...
    }
    
    if model is not None:
        # ⚠️ CRÍTICO: Convertir valores NumPy a tipos nativos de Python
        total_params = model.count_params()
        if hasattr(total_params, 'item'):
            total_params = int(total_params.item())
        else:
            total_params = int(total_params)
        
        returns["model_architecture"] = {
            "total_params": total_params,  # Ya convertido a int nativo
            # ... otros campos ...
        }
    
    return returns
```

### 🔴 PROBLEMA CRÍTICO #3: "Object of type int64 is not JSON serializable" en telemetría

**⚠️ IMPORTANTE**: Si ves este error en los logs del contenedor:
```
⚠️  Error enviando inference stats: Object of type int64 is not JSON serializable
✅ Telemetría de inferencia enviada a Splunk
```

**CAUSA**: El error `"Error enviando inference stats"` está siendo generado **DENTRO** de `log_metrics()` o `log_prediction()` en el helper de telemetría (`telemetry_helper.py`), NO en el código del notebook. Esto significa que:

1. **El código del notebook está convirtiendo los valores correctamente** (ya lo hiciste)
2. **PERO el helper está recibiendo o creando valores NumPy adicionales** que no están siendo convertidos
3. **O el helper está creando valores NumPy internamente** cuando construye el evento JSON

**SOLUCIÓN 1: Verificar qué valores están causando el problema**

El error está siendo capturado silenciosamente dentro del helper. Necesitas ver el traceback completo. Agrega este código temporalmente en `apply()` para ver qué está pasando:

```python
# En apply(), ANTES de llamar a log_metrics/log_prediction, agregar:
import json

# Preparar todos los valores convertidos
telemetry_data = {
    "model_name": MODEL_NAME,
    "num_predictions": int(len(df)),
    "num_anomalies": int(is_anomaly.sum()),
    "avg_reconstruction_error": float(reconstruction_error.mean()),
    "anomaly_threshold": float(anomaly_threshold),
    "app_name": APP_NAME,
    "model_version": VERSION,
    "project": USE_CASE
}

# Eliminar valores None
telemetry_data = {k: v for k, v in telemetry_data.items() if v is not None}

# INTENTAR serializar a JSON para verificar que todos los valores son serializables
try:
    json.dumps(telemetry_data)
    print("✅ Todos los valores son serializables a JSON")
except TypeError as e:
    print(f"❌ ERROR DE SERIALIZACIÓN: {e}")
    print(f"   Valores problemáticos:")
    for k, v in telemetry_data.items():
        try:
            json.dumps({k: v})
        except TypeError:
            print(f"      - {k}: {type(v)} = {v}")
            # Convertir cualquier valor NumPy restante
            if hasattr(v, 'item'):  # Es un scalar NumPy
                telemetry_data[k] = v.item()
            elif isinstance(v, (np.integer, np.floating)):
                telemetry_data[k] = float(v) if isinstance(v, np.floating) else int(v)
    
    # Intentar de nuevo
    try:
        json.dumps(telemetry_data)
        print("✅ Valores corregidos, ahora son serializables")
    except TypeError as e2:
        print(f"❌ ERROR PERSISTENTE: {e2}")

# Ahora pasar los valores convertidos al helper
log_metrics(**telemetry_data)
```

**SOLUCIÓN 2: Función helper para convertir valores recursivamente**

Agrega esta función helper al inicio de tu notebook (en la celda de imports) para convertir recursivamente todos los valores NumPy a tipos nativos:

```python
def convert_to_native_types(obj):
    """
    Convierte recursivamente valores NumPy/Pandas a tipos nativos de Python.
    Útil para serialización JSON.
    """
    import numpy as np
    import pandas as pd
    
    if isinstance(obj, (np.integer, np.int8, np.int16, np.int32, np.int64)):
        return int(obj)
    elif isinstance(obj, (np.floating, np.float16, np.float32, np.float64)):
        return float(obj)
    elif isinstance(obj, np.ndarray):
        return obj.tolist()
    elif isinstance(obj, pd.Series):
        return obj.tolist()
    elif isinstance(obj, dict):
        return {k: convert_to_native_types(v) for k, v in obj.items()}
    elif isinstance(obj, (list, tuple)):
        return [convert_to_native_types(item) for item in obj]
    elif isinstance(obj, (np.bool_, bool)):
        return bool(obj)
    else:
        return obj

# Usar en apply():
telemetry_data = {
    "model_name": MODEL_NAME,
    "num_predictions": len(df),
    "num_anomalies": is_anomaly.sum(),
    "avg_reconstruction_error": reconstruction_error.mean(),
    "anomaly_threshold": anomaly_threshold,
    "app_name": APP_NAME,
    "model_version": VERSION,
    "project": USE_CASE
}

# Convertir TODOS los valores recursivamente
telemetry_data = convert_to_native_types(telemetry_data)

# Ahora pasar al helper (todos los valores son nativos de Python)
log_metrics(**telemetry_data)
```

**SOLUCIÓN 3: Verificar si el helper tiene el problema**

Si el error persiste después de aplicar las Soluciones 1 y 2, el problema puede estar dentro del helper mismo. En este caso, necesitas:

1. **Verificar el código del helper** (`telemetry_helper.py` en `/dltk/notebooks_custom/helpers/`)
2. **Asegurarte de que el helper también convierte valores** antes de serializar a JSON
3. **O contactar al equipo de DevOps** para que corrija el helper

**Valores que SIEMPRE necesitan conversión**:
- `is_anomaly.sum()` → `int(is_anomaly.sum())` o `int(is_anomaly.sum().item())`
- `reconstruction_error.mean()` → `float(reconstruction_error.mean())` o `float(reconstruction_error.mean().item())`
- `anomaly_threshold` → `float(anomaly_threshold)` o `float(anomaly_threshold.item())`
- `epoch + 1` → `int(epoch + 1)`
- `logs.get('loss', 0)` → `float(logs.get('loss', 0))` o `float(logs.get('loss', 0).item())` si es NumPy
- `returns['model_mae']` → `float(returns['model_mae'])` o `float(returns['model_mae'].item())` si es NumPy
- `rmse`, `mse`, `test_results[0]` → `float(rmse)`, `float(mse)`, `float(test_results[0])` o usar `.item()` si son NumPy

**⚠️ NOTA IMPORTANTE**: Si el error dice `"Error enviando inference stats"` pero luego dice `"✅ Telemetría de inferencia enviada a Splunk"`, significa que el error está siendo capturado dentro del helper y la telemetría NO está llegando a Splunk. El mensaje de éxito es engañoso.

---

## 📚 Recursos Adicionales

- **Guía Completa Data Scientist E2E**: `GUIA_COMPLETA_DATA_SCIENTIST_E2E.md`
- **Diagnóstico de Telemetría**: `DIAGNOSTICO_TELEMETRIA.md`
- **Documentación DSDL**: https://docs.splunk.com/Documentation/DSDL
- **Logs de DSDL**: `index=_internal "mltk-container"`

---

**💡 Si no encuentras solución aquí**, contacta al equipo de DevOps o revisa los logs del contenedor en detalle para identificar el problema específico.

