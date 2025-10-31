# Análisis Comparativo: Necesidades de Científicos de Datos vs. Capacidades de Splunk DSDL

## Resumen Ejecutivo

Este documento compara las capacidades técnicas requeridas por el científico de datos (Cristian) que trabaja con autoencoders y modelos de deep learning para detección de anomalías en procesos industriales, con las capacidades que ofrece Splunk DSDL 5.2.2.

## Metodología de Análisis

- **Fuente de necesidades**: Análisis de 13 notebooks de Jupyter desarrollados por el científico de datos
- **Fuente de capacidades**: Documentación oficial de Splunk DSDL 5.2.2 (User Guide)
- **Enfoque**: Comparación técnica directa de librerías, patrones de trabajo y funcionalidades

---

## 1. Librerías y Frameworks Utilizados

### 1.1 Necesidades Identificadas en los Notebooks

| Categoría | Librerías/Frameworks | Uso Principal |
|-----------|---------------------|--------------|
| **Deep Learning** | TensorFlow, Keras | Modelos Sequential con Conv1D, Dense layers, Dropout |
| **Machine Learning Clásico** | Scikit-learn | PCA, IsolationForest, KMeans, RandomForest, LinearRegression, StandardScaler |
| **Manipulación de Datos** | Pandas, NumPy | Preprocesamiento, feature engineering, ventanas deslizantes |
| **Visualización** | Matplotlib, Seaborn | Análisis exploratorio, visualización de resultados |
| **Procesamiento de Señales** | scipy | gaussian_filter para suavizado |
| **Series Temporales** | aeon | ClaSPSegmenter para detección de cambios |
| **Series Temporales** | statsmodels | ARIMA para forecasting |
| **MLOps** | MLflow | Tracking de experimentos (uso limitado) |

### 1.2 Capacidades de DSDL

| Categoría | Soporte DSDL | Estado |
|-----------|--------------|--------|
| **Deep Learning** | ✅ TensorFlow, PyTorch, Keras | Soportado en contenedores preconstruidos |
| **Machine Learning Clásico** | ✅ Scikit-learn | Incluido en imágenes Golden Image |
| **Manipulación de Datos** | ✅ Pandas, NumPy | Biblioteca estándar en contenedores |
| **Visualización** | ✅ Matplotlib, Seaborn | Disponible en notebooks JupyterLab |
| **Procesamiento de Señales** | ⚠️ scipy | Probablemente disponible, no documentado explícitamente |
| **Series Temporales** | ❓ aeon | **NO MENCIONADO** - Verificar disponibilidad |
| **Series Temporales** | ❓ statsmodels | **NO MENCIONADO** - Verificar disponibilidad |
| **MLOps** | ✅ MLflow | Opcionalmente disponible según documentación |

### 1.3 Gap Analysis - Librerías

| Librería | Estado | Acción Requerida |
|----------|--------|------------------|
| **aeon** | ⚠️ No confirmado | Verificar si está en imagen Golden Image o agregar custom image |
| **statsmodels** | ⚠️ No confirmado | Verificar si está en imagen Golden Image o agregar custom image |
| **scipy** | ⚠️ Probablemente disponible | Confirmar en documentación o imagen |

---

## 2. Patrones de Trabajo y Flujos

### 2.1 Flujo de Trabajo Actual del Científico de Datos

```
1. Carga de datos desde archivos CSV locales
   ↓
2. Preprocesamiento extensivo:
   - Resampling temporal (resample("min"))
   - Interpolación (interpolate(method='time'))
   - Feature engineering (diferencias, porcentajes, ventanas deslizantes)
   ↓
3. Análisis exploratorio:
   - Correlaciones, covarianzas
   - Visualizaciones (heatmaps, scatter plots, series temporales)
   ↓
4. Modelado:
   - Pipelines con sklearn
   - Modelos deep learning con Keras/TensorFlow
   - Entrenamiento con múltiples epochs
   ↓
5. Evaluación y visualización de resultados
   ↓
6. Persistencia de modelos (pickle, joblib, .keras)
```

### 2.2 Flujo de Trabajo DSDL

```
1. Carga de datos desde Splunk (REST API o mode=stage)
   ↓
2. Desarrollo en JupyterLab notebook:
   - Funciones fit(), apply(), summary()
   ↓
3. Auto-exportación a módulo Python (.py)
   ↓
4. Invocación desde SPL:
   - | fit MLTKContainer algo=notebook_name ...
   - | apply model_name
```

### 2.3 Gap Analysis - Patrones de Trabajo

| Patrón Actual | Compatibilidad DSDL | Consideraciones |
|---------------|---------------------|-----------------|
| **CSV locales** | ⚠️ Parcial | DSDL espera datos desde Splunk. CSV se puede usar en JupyterLab pero no es el flujo principal |
| **Preprocesamiento complejo** | ✅ Compatible | Se puede hacer en notebook con Pandas |
| **Ventanas deslizantes** | ✅ Compatible | Lógica Python en notebook |
| **Pipelines sklearn** | ✅ Compatible | Se pueden usar en funciones fit/apply |
| **Modelos Keras/TensorFlow** | ✅ Compatible | Totalmente soportado |
| **Visualizaciones exploratorias** | ✅ Compatible | Matplotlib/Seaborn en JupyterLab |
| **Persistencia modelos** | ⚠️ Diferente | DSDL guarda automáticamente con `into app:`. Persistencia manual requiere gestión en contenedor |

---

## 3. Tipos de Modelos Implementados

### 3.1 Modelos Identificados en Notebooks

| Tipo de Modelo | Ejemplos en Notebooks | Arquitectura |
|----------------|----------------------|--------------|
| **Clasificación Binaria** | Detección de anomalías | Conv1D + Dense layers, Binary Crossentropy |
| **Regresión** | Predicción de consumo | Dense layers, MSE loss |
| **Clustering** | Segmentación de datos | KMeans |
| **Detección Anomalías** | IsolationForest + PCA | Pipeline sklearn |
| **Series Temporales** | Forecasting ARIMA | statsmodels ARIMA |
| **Modelos de Red Neuronal** | Varios casos de uso | Sequential, Conv1D, Dense, Dropout |

### 3.2 Compatibilidad con DSDL

| Tipo de Modelo | Compatible DSDL | Notas |
|----------------|-----------------|-------|
| **Clasificación Binaria** | ✅ SÍ | Implementación directa en función apply() |
| **Regresión** | ✅ SÍ | Retorno de valores continuos en apply() |
| **Clustering** | ⚠️ PARCIAL | Funciona pero etiquetas no se integran directamente en Splunk |
| **Detección Anomalías** | ✅ SÍ | IsolationForest + PCA en pipeline |
| **Series Temporales (ARIMA)** | ❓ NO CONFIRMADO | Requiere statsmodels - verificar disponibilidad |
| **Modelos Deep Learning** | ✅ SÍ | TensorFlow/Keras totalmente soportado |

---

## 4. Entrada y Salida de Datos

### 4.1 Fuentes de Datos Actuales

- **Archivos CSV locales** con timestamps y múltiples features
- **Formatos**: CSV con delimitadores custom, encoding de fechas
- **Volumen**: Datasets grandes (500K+ filas, 25-59 features)
- **Temporalidad**: Series temporales con índices DatetimeIndex

### 4.2 Entrada de Datos en DSDL

**Opciones disponibles:**
1. **Pull desde Splunk**: `SplunkSearch.SplunkSearch()` en notebook
2. **Push desde Splunk**: `| fit MLTKContainer mode=stage ...`
3. **Archivos locales en contenedor**: Posible pero no es flujo principal

**Formato esperado:**
- CSV desde Splunk (automático en mode=stage)
- JSON con metadata (parámetros, features)
- Pandas DataFrame en notebook

### 4.3 Gap Analysis - Datos

| Aspecto | Actual | DSDL | Compatibilidad |
|---------|--------|------|----------------|
| **Origen de datos** | CSV locales | Splunk indexes | ⚠️ Requiere migración o integración |
| **Formato temporal** | DatetimeIndex | Splunk _time field | ✅ Compatible con transformación |
| **Volumen de datos** | 500K+ eventos | Limitado por memoria contenedor | ⚠️ Considerar particionamiento |
| **Feature engineering** | En notebook | En notebook o SPL | ✅ Compatible |

---

## 5. Características Específicas Identificadas

### 5.1 Procesamiento de Series Temporales

**Necesidades identificadas:**
- Resampling temporal (`resample("min")`)
- Interpolación (`interpolate(method='time')`)
- Ventanas deslizantes para crear tensores/imágenes
- Segmentación de series (ClaSPSegmenter de aeon)
- Detección de cambios y periodos dominantes

**Compatibilidad DSDL:**
- ✅ Resampling e interpolación: Pandas disponible
- ✅ Ventanas deslizantes: Implementación Python
- ⚠️ Segmentación: Requiere aeon (no confirmado)
- ✅ Detección de cambios: Lógica custom en notebook

### 5.2 Feature Engineering Avanzado

**Técnicas usadas:**
- Diferencias entre valores actuales y setpoints
- Cálculo de porcentajes de cambio (`pct_change()`)
- Normalización y escalado (StandardScaler, MinMaxScaler)
- Generación de características estadísticas
- Agrupación por turnos/ventanas temporales

**Compatibilidad DSDL:**
- ✅ Todas las técnicas son compatibles con Pandas/Scikit-learn
- ✅ Se pueden implementar en funciones fit/apply del notebook

### 5.3 Visualización y Análisis Exploratorio

**Uso actual:**
- Heatmaps de correlación/covarianza
- Scatter plots multidimensionales
- Visualización de series temporales
- Histogramas y distribuciones
- Visualización de anomalías sobre series

**Compatibilidad DSDL:**
- ✅ Matplotlib y Seaborn disponibles en JupyterLab
- ✅ Visualizaciones interactivas posibles
- ⚠️ No se integran directamente en dashboards de Splunk (solo resultados)

---

## 6. Consideraciones de Infraestructura

### 6.1 Recursos Computacionales

**Uso actual:**
- Modelos deep learning con entrenamiento de múltiples epochs (8-12)
- Batch sizes variables (10-150)
- Datasets grandes en memoria (500K+ filas × 25-59 features)
- Procesamiento de ventanas deslizantes (crea datasets aún mayores)

**Recursos DSDL:**
- ✅ Soporte GPU para entrenamiento
- ⚠️ Memoria limitada por configuración de contenedor
- ⚠️ Timeouts posibles con datasets muy grandes
- ✅ Escalabilidad horizontal con Kubernetes

### 6.2 Persistencia y Versionado

**Uso actual:**
- Pickle para modelos sklearn
- `.keras` para modelos TensorFlow
- `.pkl` para pipelines
- Guardado manual en sistema de archivos

**DSDL:**
- ✅ Persistencia automática con `into app:model_name`
- ✅ Versionado a través de Splunk platform
- ⚠️ Formato interno de DSDL (no pickle directo)
- ✅ Compatible con guardado manual adicional si se requiere

---

## 7. Limitaciones y Gaps Identificados

### 7.1 Gaps Críticos

| Gap | Impacto | Solución Posible |
|-----|---------|------------------|
| **aeon library no confirmada** | Alto | Verificar en imagen Golden Image o crear custom Docker image |
| **statsmodels no confirmado** | Medio | Verificar disponibilidad o usar alternativas |
| **Integración con CSV locales** | Medio | Migrar a Splunk indexes o usar modo stage temporalmente |
| **Volumen de datos** | Medio | Implementar streaming o particionamiento en SPL antes de enviar |

### 7.2 Limitaciones Arquitectónicas

| Limitación | Descripción | Impacto |
|------------|-------------|---------|
| **Modelos atómicos** | 1 modelo = 1 contenedor | Medio - Requiere gestión cuidadosa de recursos |
| **Sin distribución indexer** | Datos procesados en search head | Medio - Puede ser cuello de botella |
| **Permisos Global** | Modelos deben ser Global para compartir | Bajo - Configuración administrativa |

---

## 8. Compatibilidad General por Categoría

### 8.1 Totalmente Compatible ✅

- Modelos TensorFlow/Keras (Sequential, Conv1D, Dense)
- Pipelines Scikit-learn (PCA, IsolationForest, RandomForest, etc.)
- Manipulación de datos con Pandas/NumPy
- Feature engineering personalizado
- Visualizaciones exploratorias en JupyterLab
- Preprocesamiento temporal (resampling, interpolación)

### 8.2 Parcialmente Compatible ⚠️

- Carga de datos desde CSV (requiere migración a Splunk)
- Volumen de datos grandes (requiere optimización)
- Persistencia de modelos (formato diferente pero funcional)
- MLflow tracking (opcional, no integrado directamente)

### 8.3 Requiere Verificación ❓

- **aeon library** (ClaSPSegmenter)
- **statsmodels** (ARIMA)
- **scipy** (gaussian_filter - probablemente disponible)

---

## 9. Recomendaciones para el POC

### 9.1 Prerequisitos para Validación

1. **Verificar librerías:**
   - Confirmar presencia de aeon, statsmodels, scipy en imagen Golden Image
   - Si no están, evaluar creación de custom Docker image

2. **Preparar datos de prueba:**
   - Migrar dataset de ejemplo a Splunk index
   - Preparar SPL queries equivalentes al preprocesamiento actual

3. **Adaptar notebooks:**
   - Convertir lectura CSV → Splunk REST API o mode=stage
   - Implementar funciones fit/apply/summary según estructura DSDL
   - Validar formato de retorno en apply() para integración Splunk

### 9.2 Estrategia de Validación

**Validación por Documentación (COMPLETADA):**

**Hallazgos sobre Librerías:**
- **Golden Image**: Contiene "most of the recent popular libraries including TensorFlow, PyTorch, NLP, and classical machine learning"
- **Documentación no especifica** el listado completo de librerías incluidas en Golden Image
- **Repositorio GitHub**: https://github.com/splunk/splunk-mltk-container-docker contiene archivos de requirements:
  - `requirements_files/base_functional.txt` - Librerías base funcionales
  - `requirements_files/specific_golden_cpu.txt` - Librerías específicas Golden Image CPU
  - `requirements_files/specific_golden_gpu.txt` - Librerías específicas Golden Image GPU
- **Librerías NO confirmadas en documentación**: `aeon`, `statsmodels`, `scipy` (requieren verificación directa en repositorio GitHub)

**Hallazgos sobre mode=stage:**
- **Propósito**: Desarrollo iterativo en JupyterLab
- **Funcionamiento**: `| fit MLTKContainer mode=stage algo=my_notebook features_* into app:MyFirstModel`
  - NO ejecuta entrenamiento real, solo transfiere datos al contenedor
  - Datos enviados como CSV desde Splunk al contenedor
  - Permite desarrollo interactivo con datos de Splunk indexes
- **Limitaciones**: No permite carga directa de CSV locales (requiere que datos estén en Splunk primero)
- **Flujo recomendado**: Migrar datos CSV a Splunk index → usar mode=stage para desarrollo → luego fit para entrenamiento

**Custom Images:**
- **Proceso documentado**: Fork/clone repositorio → agregar librerías a requirements → crear nueva fila en tag_mapping.csv → build custom image
- **Ejemplo**: Para agregar `pyarrow` o `transformers` no incluidos en Golden Image
- **Ubicación archivos**: `/requirements_files/my_custom_libraries.txt` y `tag_mapping.csv`

**Próximo paso práctico:**
- ⚠️ **Revisión directa en GitHub requerida**: Los archivos `requirements_files/specific_golden_cpu.txt` y `specific_golden_gpu.txt` deben revisarse directamente en https://github.com/splunk/splunk-mltk-container-docker para confirmar presencia de `aeon`, `statsmodels`, `scipy`
- Documentación menciona "classical machine learning" pero no especifica listado completo

**Validación Práctica en Sandbox (1-2 semanas):**

### 9.3 Verificación de Librerías en Golden Image

**Estado actual:**
- **Documentación**: Menciona "most of the recent popular libraries including TensorFlow, PyTorch, NLP, and classical machine learning"
- **No especifica listado completo** de librerías incluidas
- **Menciona librerías específicas**: TensorFlow, PyTorch, Prophet (forecasting), spaCy (NLP), PyOD (outlier detection), River (streaming ML), Spark, Rapids
- **NO menciona**: `aeon`, `statsmodels`, `scipy` explícitamente

**Librerías a verificar en GitHub:**
- **Repositorio**: https://github.com/splunk/splunk-mltk-container-docker
- **Archivos a revisar**:
  - `requirements_files/base_functional.txt` - Librerías base
  - `requirements_files/specific_golden_cpu.txt` - Librerías Golden Image CPU
  - `requirements_files/specific_golden_gpu.txt` - Librerías Golden Image GPU
- **Buscar**: `aeon`, `statsmodels`, `scipy` en estos archivos

**URLs directas para verificación:**

**Carpeta requirements_files:**
- https://github.com/splunk/splunk-mltk-container-docker/tree/master/requirements_files

**Archivos específicos a revisar (formato raw para lectura directa):**
- `base_functional.txt`: https://raw.githubusercontent.com/splunk/splunk-mltk-container-docker/master/requirements_files/base_functional.txt
- `specific_golden_cpu.txt`: https://raw.githubusercontent.com/splunk/splunk-mltk-container-docker/master/requirements_files/specific_golden_cpu.txt
- `specific_golden_gpu.txt`: https://raw.githubusercontent.com/splunk/splunk-mltk-container-docker/master/requirements_files/specific_golden_gpu.txt

**Acción requerida:**
1. ✅ Abrir URLs raw de archivos `requirements_files/` en GitHub
2. Buscar en cada archivo (Ctrl+F o Cmd+F): `aeon`, `statsmodels`, `scipy`
3. Documentar presencia/ausencia de cada librería
4. Si NO están incluidos: preparar custom Docker image antes del sandbox

**Verificación realizada (2025-01-31):**

**Resultados:**
- ✅ **`scipy`**: **INCLUIDO** en `specific_golden_cpu.txt` y `specific_golden_gpu.txt`
- ✅ **`statsmodels`**: **INCLUIDO** en `specific_golden_cpu.txt`
- ❌ **`aeon`**: **NO INCLUIDO** en ningún archivo de requirements

**Conclusión:**
- `scipy` y `statsmodels` están disponibles en Golden Image CPU
- `aeon` **NO está incluido** - requiere custom Docker image antes del sandbox
- Para agregar `aeon`: crear archivo de requirements custom → referenciar en tag_mapping.csv → build custom image

### 9.4 Procedimiento para Agregar Librerías Faltantes

**Enfoque recomendado:** Crear archivo de requirements custom (más simple que crear imagen completa desde cero)

**Proceso paso a paso:**

**1. Fork/clone del repositorio:**
```bash
git clone https://github.com/splunk/splunk-mltk-container-docker
cd splunk-mltk-container-docker
```

**2. Crear archivo de requirements custom:**
- Crear archivo en `requirements_files/` (ej: `my_custom_libraries.txt`)
- Agregar librerías faltantes con versiones pinned:
```text
# requirements_files/my_custom_libraries.txt
aeon>=0.5.0
# Otras librerías futuras aquí
```

**3. Referenciar en `tag_mapping.csv`:**
- Agregar nueva fila o editar existente:
```csv
Tag,base_image,dockerfile,base_requirements,specific_requirements,runtime,requirements_dockerfile
golden-cpu-custom,deb:bullseye,Dockerfile.debian.golden-cpu,base_functional.txt,my_custom_libraries.txt,none,Dockerfile.debian.requirements
```
- **Nota**: `specific_requirements` puede apuntar a múltiples archivos separados por espacios o usar solo el custom

**4. (Opcional) Pre-compilar requirements:**
```bash
./compile_image_python_requirements.sh golden-cpu-custom
```
- Acelera build futuro al fijar versiones exactas

**5. Build de la imagen custom:**
```bash
./build.sh golden-cpu-custom splunk/ 5.2.2
```
- Resultado: `splunk/golden-cpu-custom:5.2.2`

**6. Escanear imagen (recomendado):**
```bash
./scan_container.sh golden-cpu-custom splunk/ 5.2.2
```
- Detecta vulnerabilidades y CVEs

**7. Push a registry:**
```bash
docker push splunk/golden-cpu-custom:5.2.2
```
- Docker Hub público o registry privado

**8. Configurar en Splunk:**
- Copiar contenido de `images_conf_files/golden-cpu-custom.conf` a `$SPLUNK_HOME/etc/apps/mltk-container/local/images.conf`
- Reiniciar Splunk o recargar DSDL

**9. Usar imagen custom en DSDL:**
```spl
index=my_data 
| fit MLTKContainer algo=my_notebook mode=stage into app:MyModel 
container_image="splunk/golden-cpu-custom:5.2.2"
```

**Ventajas de este enfoque:**
- ✅ No requiere crear imagen desde cero (reutiliza Golden Image base)
- ✅ Fácil agregar más librerías futuras (editar `my_custom_libraries.txt`)
- ✅ Versionado claro de librerías custom
- ✅ Mantiene compatibilidad con actualizaciones de base

**Para futuras librerías:**
- Simplemente agregar al archivo `my_custom_libraries.txt` y rebuild imagen

### 9.5 Puntos Clave Antes de Configurar Sandbox

**Prerequisitos Técnicos:**
1. **Librería faltante**: `aeon` NO está en Golden Image. Preparar custom Docker image con `aeon` antes de comenzar sandbox. (`statsmodels` y `scipy` ✅ ya incluidos)
2. **Datos en Splunk**: `mode=stage` requiere datos en Splunk indexes. Preparar migración de CSV locales a Splunk index antes de sandbox.
3. **Notebook de referencia**: Seleccionar notebook simple (ej: `prediccion_anomalias.ipynb`) para adaptar a estructura DSDL (fit/apply/summary).
4. **Estructura DSDL**: Entender funciones requeridas:
   - `fit()`: entrenamiento del modelo
   - `apply()`: inferencia (retorna DataFrame con columnas para Splunk)
   - `summary()`: resumen del modelo (opcional)
5. **Volumen de prueba**: Definir tamaño de dataset inicial (empezar pequeño, luego escalar a 500K+ eventos).
6. **Custom image**: Si faltan librerías, tener listo proceso: fork repositorio → agregar a requirements → build imagen.

**Decisiones Arquitectónicas:**
- **Container runtime**: Docker (dev/test) vs Kubernetes/OpenShift (producción)
- **GPU**: ¿Requiere GPU para modelos deep learning?
- **Registry**: ¿Usar Docker Hub público o registry privado?
- **Certificados TLS**: Self-signed para dev vs certificados propios para producción

**Validaciones Prácticas a Realizar:**
- Volumen de datos: límites de memoria con datasets grandes (500K+ eventos)
- Latencia/throughput: medición real de `apply` en SPL
- Adaptación de notebook: convertir uno existente a estructura DSDL (fit/apply)
- Flujo end-to-end: Splunk → Contenedor → Resultados

---

## 10. Conclusiones

### 10.1 Compatibilidad General: **ALTA** ✅

DSDL es **mayoritariamente compatible** con las necesidades técnicas identificadas. Los modelos deep learning, pipelines sklearn, y manipulación de datos están totalmente soportados.

### 10.2 Gaps Principales

1. **Librerías**: `aeon` NO incluida en Golden Image (requiere custom image). `statsmodels` y `scipy` ✅ incluidos.
2. **Fuente de datos**: `mode=stage` requiere datos en Splunk indexes (no acepta CSV locales directamente). Solución: migrar CSV a Splunk primero
3. **Volumen de datos**: Requiere optimización y particionamiento (documentación sugiere usar Dask, Vaex, o Spark para multi-million rows)

### 10.3 Viabilidad del POC: **ALTA** ✅

El POC es **viable** con las siguientes condiciones:
- Verificar disponibilidad de librerías específicas (aeon, statsmodels)
- Adaptar notebooks a estructura DSDL (fit/apply/summary)
- Preparar datos en formato Splunk o usar mode=stage temporalmente

### 10.4 Próximos Pasos Inmediatos

1. ✅ Verificar librerías aeon y statsmodels en imagen Golden Image
2. ✅ Seleccionar notebook de referencia para POC
3. ✅ Preparar dataset de prueba en Splunk
4. ✅ Adaptar notebook a estructura DSDL
5. ✅ Ejecutar POC end-to-end

---

## Anexos

### A. Lista de Notebooks Analizados

1. `modelo_corona.ipynb` - Clustering y análisis de temperaturas
2. `prediccion_anomalias.ipynb` - Clasificación con RandomForest
3. `anomalias_ej_corona.ipynb` - Detección de anomalías con Conv1D + IsolationForest
4. `modelo_gas_corona.ipynb` - Modelos de regresión y ARIMA
5. `experimento_curvas.ipynb` - RandomForest para curvas
6. `Molino_Crudo.ipynb` - Pipeline con IsolationForest + StandardScaler
7. `Parrilla_Clinker.ipynb` - Similar a Molino_Crudo
8. `corana_curva_solo_temp.ipynb` - Modelo Keras para curvas
9. `setpoints_corona_h4.ipynb` - Modelos de setpoints
10. `setponts_modelos.ipynb` - Modelos relacionados
11. `curvas_solas.ipynb` - Análisis de curvas
12. `gn_to_glp.ipynb` - Conversión de datos
13. `medicion_gasto_paros.ipynb` - Medición de gastos

### B. Referencias Técnicas

- Splunk DSDL 5.2.2 User Guide
- Notebooks de Cristian (Summan Data Scientist)

---

**Fecha de análisis**: $(date)
**Versión**: 1.0

