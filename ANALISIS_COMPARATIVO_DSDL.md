# Análisis Comparativo: Necesidades de Científicos de Datos vs. Capacidades de Splunk DSDL

**Repositorio GitHub**: https://github.com/lufermalgo/splunk-dsdl.git

## Control de Versiones

**Versión actual**: 1.0.1  
**Última actualización**: 2025-01-31  
**Mantenido por**: Equipo DSDL

### Changelog

Ver sección completa de [Historial de Versiones](#historial-de-versiones) al final del documento.

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

### 9.5 Proceso DevOps: Agregar Librerías a Contenedores Custom (GCP/Azure)

**Contexto:** Cristian (científico de datos) o cliente requiere librería faltante (ej: `aeon`). El equipo DevOps debe agregarla rápidamente a custom image y desplegarla en GCP o Azure.

**Flujo completo end-to-end:**

**Paso 1: Solicitud del Científico de Datos**

**Cristian solicita librería:**
- Opción A: Issue en repositorio Git (recomendado para tracking)
- Opción B: Ticket en sistema de gestión (Jira, ServiceNow, etc.)
- Opción C: Slack/Teams directo con DevOps

**Información requerida en solicitud:**
- Librería: `aeon>=0.5.0`
- Justificación: "Necesaria para segmentación de series temporales en proyecto autoencoder"
- Urgencia: Alta/Media/Baja
- Proyecto: Autoencoder anomalías - Horno 4

**Paso 2: DevOps - Preparar Custom Image**

**2.1 Clone/Fork del repositorio base:**
```bash
# Si no existe fork del repositorio
git clone https://github.com/splunk/splunk-mltk-container-docker
cd splunk-mltk-container-docker

# O si ya existe fork interno
git clone https://github.com/empresa/splunk-mltk-container-docker-custom
cd splunk-mltk-container-docker-custom
```

**2.2 Crear/actualizar archivo de requirements custom:**
```bash
# Editar archivo existente o crear nuevo
vim requirements_files/my_custom_libraries.txt

# Agregar nueva librería
aeon>=0.5.0

# (Otras librerías previas se mantienen)
# statsmodels>=0.14.0
# pyarrow>=14.0.1
```

**2.3 Actualizar tag_mapping.csv:**
```bash
# Editar tag_mapping.csv
vim tag_mapping.csv

# Verificar que existe fila para golden-cpu-custom:
# Tag,base_image,dockerfile,base_requirements,specific_requirements,runtime,requirements_dockerfile
# golden-cpu-custom,deb:bullseye,Dockerfile.debian.golden-cpu,base_functional.txt,my_custom_libraries.txt,none,Dockerfile.debian.requirements
```

**2.4 Pre-compilar requirements (recomendado):**
```bash
# Acelera build y fija versiones exactas
./compile_image_python_requirements.sh golden-cpu-custom
```

**Paso 3: Build de la Imagen**

**3.1 Build local (opción 1) o CI/CD (opción 2):**

**Opción A: Build manual:**
```bash
# Build imagen custom
./build.sh golden-cpu-custom splunk/ 5.2.2

# Output: splunk/golden-cpu-custom:5.2.2
```

**Opción B: CI/CD pipeline (recomendado para producción):**

**GitHub Actions / GitLab CI / Jenkins:**
```yaml
# Ejemplo: .github/workflows/build-custom-image.yml
name: Build Custom DSDL Image

on:
  push:
    branches: [main]
    paths:
      - 'requirements_files/my_custom_libraries.txt'

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Setup Docker Buildx
        uses: docker/setup-buildx-action@v2
      
      - name: Compile requirements
        run: ./compile_image_python_requirements.sh golden-cpu-custom
      
      - name: Build image
        run: ./build.sh golden-cpu-custom splunk/ 5.2.2
      
      - name: Scan image
        run: ./scan_container.sh golden-cpu-custom splunk/ 5.2.2
```

**Paso 4: Scanning de Seguridad**

**4.1 Escanear imagen antes de push:**
```bash
# Usando Trivy (incluido en scripts)
./scan_container.sh golden-cpu-custom splunk/ 5.2.2

# Output: scan_logs/golden-cpu-custom_scan.txt
# Revisar vulnerabilidades críticas antes de continuar
```

**4.2 Verificar resultados:**
- Si hay vulnerabilidades críticas → evaluar si proceder o corregir
- Si solo hay vulnerabilidades menores → documentar y proceder

**Paso 5: Push a Registry (GCP o Azure)**

**Opción A: GCP - Artifact Registry**

**5.1 Configurar autenticación:**
```bash
# Configurar gcloud CLI
gcloud auth login
gcloud auth configure-docker us-central1-docker.pkg.dev

# O usar Service Account para CI/CD
echo $GCP_SERVICE_ACCOUNT_KEY | docker login -u _json_key --password-stdin https://us-central1-docker.pkg.dev
```

**5.2 Tag imagen para Artifact Registry:**
```bash
# Formato: REGION-docker.pkg.dev/PROJECT/REPO/IMAGE:TAG
docker tag splunk/golden-cpu-custom:5.2.2 \
  us-central1-docker.pkg.dev/my-gcp-project/dsdl-images/golden-cpu-custom:5.2.2

# O con tag semántico adicional
docker tag splunk/golden-cpu-custom:5.2.2 \
  us-central1-docker.pkg.dev/my-gcp-project/dsdl-images/golden-cpu-custom:latest
```

**5.3 Push a Artifact Registry:**
```bash
docker push us-central1-docker.pkg.dev/my-gcp-project/dsdl-images/golden-cpu-custom:5.2.2
docker push us-central1-docker.pkg.dev/my-gcp-project/dsdl-images/golden-cpu-custom:latest
```

**5.4 Configurar IAM y permisos:**
```bash
# Otorgar permisos a servicio de cuentas para pull
gcloud artifacts docker images add-iam-policy-binding \
  us-central1-docker.pkg.dev/my-gcp-project/dsdl-images/golden-cpu-custom:5.2.2 \
  --member="serviceAccount:gke-sa@my-gcp-project.iam.gserviceaccount.com" \
  --role="roles/artifactregistry.reader"
```

**Opción B: Azure - Container Registry (ACR)**

**5.1 Configurar autenticación:**
```bash
# Login a Azure
az login

# Login a ACR
az acr login --name myacrregistry

# O usar Service Principal para CI/CD
az acr login --name myacrregistry --username $SP_APP_ID --password $SP_PASSWORD
```

**5.2 Tag imagen para ACR:**
```bash
# Formato: ACR_NAME.azurecr.io/IMAGE:TAG
docker tag splunk/golden-cpu-custom:5.2.2 \
  myacrregistry.azurecr.io/golden-cpu-custom:5.2.2

# O con tag semántico adicional
docker tag splunk/golden-cpu-custom:5.2.2 \
  myacrregistry.azurecr.io/golden-cpu-custom:latest
```

**5.3 Push a ACR:**
```bash
docker push myacrregistry.azurecr.io/golden-cpu-custom:5.2.2
docker push myacrregistry.azurecr.io/golden-cpu-custom:latest
```

**5.4 Configurar permisos (si necesario):**
```bash
# Otorgar permisos de lectura a servicio/cluster
az acr repository show --name myacrregistry --repository golden-cpu-custom
```

**Paso 6: Actualizar Configuración en Splunk**

**6.1 Copiar .conf generado:**
```bash
# El build.sh genera automáticamente:
# images_conf_files/golden-cpu-custom.conf

# Copiar a Splunk search head
scp images_conf_files/golden-cpu-custom.conf \
  splunk-server:/opt/splunk/etc/apps/mltk-container/local/images.conf

# O editar manualmente en Splunk
```

**6.2 Editar images.conf en Splunk:**
```ini
# $SPLUNK_HOME/etc/apps/mltk-container/local/images.conf

[golden-cpu-custom]
# Para GCP Artifact Registry
repo = us-central1-docker.pkg.dev/my-gcp-project/dsdl-images/
image = golden-cpu-custom:5.2.2
runtime = none
short_name = Golden CPU Custom (con aeon)

# O para Azure ACR
# repo = myacrregistry.azurecr.io/
# image = golden-cpu-custom:5.2.2
```

**6.3 Configurar autenticación en Kubernetes/GKE/AKS:**

**Para GCP (GKE):**
```bash
# Crear secret para Artifact Registry
kubectl create secret docker-registry gcp-artifact-registry-secret \
  --docker-server=us-central1-docker.pkg.dev \
  --docker-username=oauth2accesstoken \
  --docker-password=$(gcloud auth print-access-token) \
  --docker-email=not@val.id \
  --namespace=splunk-dsdl
```

**Para Azure (AKS):**
```bash
# Crear secret para ACR
kubectl create secret docker-registry azure-acr-secret \
  --docker-server=myacrregistry.azurecr.io \
  --docker-username=$SP_APP_ID \
  --docker-password=$SP_PASSWORD \
  --docker-email=not@val.id \
  --namespace=splunk-dsdl
```

**6.4 Verificar configuración de pull secrets en deployments:**
```yaml
# Verificar que deployment/pod usa el secret
apiVersion: v1
kind: Pod
spec:
  imagePullSecrets:
    - name: gcp-artifact-registry-secret  # o azure-acr-secret
```

**Paso 7: Recargar DSDL en Splunk**

**7.1 Desde Splunk UI:**
- Ir a **Configuration > Containers**
- Click **Reload** o reiniciar contenedor

**7.2 Desde CLI:**
```bash
# SSH a Splunk search head
ssh splunk-server

# Recargar configuración
$SPLUNK_HOME/bin/splunk reload deploy-server -app mltk-container

# O reiniciar Splunk (si es necesario)
$SPLUNK_HOME/bin/splunk restart
```

**Paso 8: Notificar a Científico de Datos**

**8.1 Confirmar disponibilidad:**
- Actualizar Issue/ticket: "Librería agregada, imagen disponible"
- Notificar: "Reinicia tu contenedor DSDL para usar nueva imagen"

**8.2 Instrucciones para Cristian:**
```
1. Ir a Configuration > Containers en Splunk DSDL
2. Seleccionar contenedor activo
3. Click "Stop" → "Start" (o simplemente seleccionar nueva imagen)
4. Al abrir JupyterLab, ejecutar: import aeon ✅
```

**Paso 9: Verificación y Rollback**

**9.1 Verificar funcionamiento:**
- Cristian confirma que `import aeon` funciona
- Probar notebook con nueva librería
- Si funciona → cerrar Issue/ticket

**9.2 Rollback (si hay problemas):**
```bash
# Si nueva imagen tiene problemas, rollback a versión anterior
# Editar images.conf en Splunk:
[golden-cpu-custom]
image = golden-cpu-custom:5.2.1  # Versión anterior

# Reload DSDL
```

**Tiempos estimados del proceso:**

| Paso | Tiempo | Automatizable |
|------|--------|---------------|
| Solicitud | - | - |
| Preparar requirements | 5-10 min | ✅ Con CI/CD |
| Build imagen | 20-40 min | ✅ Con CI/CD |
| Scanning | 5-10 min | ✅ Con CI/CD |
| Push a registry | 2-5 min | ✅ Con CI/CD |
| Actualizar Splunk | 5-10 min | ⚠️ Parcial |
| Reload DSDL | 1-2 min | ✅ Scriptable |
| Verificación | 5-10 min | - |
| **Total manual** | **45-90 min** | - |
| **Total con CI/CD** | **15-30 min** (más rápido) | - |

**Automatización recomendada (CI/CD):**

**GitHub Actions workflow completo:**
```yaml
name: Build and Deploy Custom DSDL Image

on:
  push:
    paths:
      - 'requirements_files/my_custom_libraries.txt'
  workflow_dispatch:

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Setup Docker
        uses: docker/setup-buildx-action@v2
      
      # GCP Auth
      - name: Authenticate to GCP
        uses: google-github-actions/auth@v1
        with:
          credentials_json: ${{ secrets.GCP_SA_KEY }}
      
      - name: Set up Cloud SDK
        uses: google-github-actions/setup-gcloud@v1
      
      # Build
      - name: Compile requirements
        run: ./compile_image_python_requirements.sh golden-cpu-custom
      
      - name: Build image
        run: ./build.sh golden-cpu-custom splunk/ ${{ github.sha }}
      
      # Security scan
      - name: Scan image
        run: ./scan_container.sh golden-cpu-custom splunk/ ${{ github.sha }}
      
      # Push to GCP Artifact Registry
      - name: Configure Docker for Artifact Registry
        run: gcloud auth configure-docker us-central1-docker.pkg.dev
      
      - name: Tag and push
        run: |
          docker tag splunk/golden-cpu-custom:${{ github.sha }} \
            us-central1-docker.pkg.dev/${{ secrets.GCP_PROJECT }}/dsdl-images/golden-cpu-custom:${{ github.sha }}
          docker tag splunk/golden-cpu-custom:${{ github.sha }} \
            us-central1-docker.pkg.dev/${{ secrets.GCP_PROJECT }}/dsdl-images/golden-cpu-custom:latest
          docker push us-central1-docker.pkg.dev/${{ secrets.GCP_PROJECT }}/dsdl-images/golden-cpu-custom:${{ github.sha }}
          docker push us-central1-docker.pkg.dev/${{ secrets.GCP_PROJECT }}/dsdl-images/golden-cpu-custom:latest
      
      # Notify (Slack, email, etc.)
      - name: Notify team
        uses: 8398a7/action-slack@v3
        with:
          status: ${{ job.status }}
          text: 'Custom DSDL image built and deployed'
```

**Azure DevOps pipeline equivalente:**
```yaml
# azure-pipelines.yml
trigger:
  branches:
    include:
      - main
  paths:
    include:
      - requirements_files/my_custom_libraries.txt

pool:
  vmImage: 'ubuntu-latest'

steps:
- task: Docker@2
  displayName: 'Build custom image'
  inputs:
    command: 'build'
    dockerfile: 'dockerfiles/Dockerfile.debian.golden-cpu'
    tags: |
      $(ACR_NAME).azurecr.io/golden-cpu-custom:$(Build.BuildId)
      $(ACR_NAME).azurecr.io/golden-cpu-custom:latest

- task: AzureContainerRegistry@1
  displayName: 'Push to ACR'
  inputs:
    azureSubscription: 'Azure-ServiceConnection'
    azureContainerRegistry: '$(ACR_NAME)'
    action: 'Push an image'
```

**Mejores prácticas DevOps:**

1. **Versionado:**
   - Usar versiones semánticas: `5.2.2`, `5.2.2-aeon-v1`
   - Tag con commit SHA: `5.2.2-abc123`
   - Mantener `latest` para versión actual estable

2. **Repositorio Git interno:**
   - Fork del repositorio oficial en Git interno
   - Branch por librería/proyecto: `feature/aeon-support`
   - Pull requests para revisión antes de merge

3. **Documentación:**
   - Mantener changelog de librerías agregadas
   - Documentar versiones específicas
   - Registrar dependencias entre librerías

4. **Seguridad:**
   - Scanning automático en CI/CD
   - Bloquear deploy si hay vulnerabilidades críticas
   - Rotar credenciales regularmente

5. **Monitoring:**
   - Alertas si build falla
   - Métricas de uso de imágenes
   - Logs de deployments

**Resumen del flujo automatizado:**

```
1. Científico agrega librería a requirements (PR)
   ↓
2. CI/CD detecta cambio automáticamente
   ↓
3. Build → Scan → Push a registry (GCP/Azure)
   ↓
4. Actualiza images.conf automáticamente (o notifica)
   ↓
5. Notifica a científico que está listo
   ↓
6. Científico reinicia contenedor → usa nueva librería ✅
```

**Tiempo total con automatización: 15-30 minutos** (vs 45-90 minutos manual)

### 9.6 Perspectiva del Científico de Datos: Flujo de Trabajo Real con DSDL

**Contexto:** Cristian (científico de datos) trabaja en un proyecto de autoencoder para detección de anomalías. Los datos están en Splunk, DSDL está implementado, y los contenedores están corriendo (no le interesa dónde ni cómo).

**Flujo de trabajo día a día:**

**Día 1: Inicio del proyecto**
1. **Acceso a JupyterLab:**
   - Abre navegador → URL del contenedor DSDL → JupyterLab se abre
   - Crea nuevo notebook: `autoencoder_anomalias.ipynb`

2. **Obtener datos desde Splunk:**
   ```python
   from splunklib.client import SplunkSearch
   search = SplunkSearch(host="splunk-server", 
                        port=8089, 
                        username="usuario", 
                        password="pass")
   
   # Buscar datos de sensores del horno
   search_query = """
   index=horno_data 
   | head 10000
   | table _time, k1, k2, k3, temp_*, presion_*
   """
   
   df = search.get_dataframe(search_query)
   df.set_index('_time', inplace=True)
   ```
   - **Primera sorpresa**: No lee CSV local como antes. Debe adaptarse a Splunk REST API o `mode=stage`

3. **Preprocesamiento (igual que antes):**
   ```python
   # Esto funciona igual que sus notebooks actuales
   df = df.resample("min").first()
   df = df.interpolate(method='time')
   df_diff = df - df_setpoints
   ```
   - ✅ Pandas funciona igual. No hay problema aquí.

4. **Análisis exploratorio:**
   ```python
   import seaborn as sns
   import matplotlib.pyplot as plt
   
   sns.heatmap(df.corr())
   plt.show()
   ```
   - ✅ Matplotlib/Seaborn disponibles. Visualizaciones funcionan.

**Día 2: Implementando modelo**

1. **Importar librerías:**
   ```python
   from sklearn.preprocessing import StandardScaler
   from sklearn.model_selection import train_test_split
   from tensorflow import keras
   from tensorflow.keras import layers
   ```
   - ✅ TensorFlow/Keras disponibles. Funciona bien.

2. **Implementar autoencoder:**
   ```python
   # Define autoencoder
   input_dim = df.shape[1]
   encoder = layers.Dense(64, activation='relu')(input_layer)
   decoder = layers.Dense(input_dim, activation='sigmoid')(encoder)
   autoencoder = keras.Model(input_layer, decoder)
   ```
   - ✅ Keras funciona igual. Código migra sin cambios.

3. **Entrenamiento:**
   ```python
   autoencoder.compile(optimizer='adam', loss='mse')
   history = autoencoder.fit(X_train, X_train, 
                            epochs=50, 
                            batch_size=32,
                            validation_data=(X_val, X_val))
   ```
   - ✅ Entrenamiento funciona. Puede monitorear con TensorBoard si quiere.

**Día 3: Problema - Librería faltante**

1. **Necesita aeon para segmentación de series temporales:**
   ```python
   from aeon.segmentation import ClaSPSegmenter
   ```
   - ❌ **Error**: `ModuleNotFoundError: No module named 'aeon'`

2. **Qué hace Cristian:**
   - No puede instalar en runtime (requiere permisos o rebuild)
   - Opción A: Contacta a DevOps/equipo DSDL para agregar librería al contenedor
   - Opción B: Usa alternativa temporal (otra librería) si existe
   - Opción C: Espera a que agreguen la librería al custom image

3. **Solución (desde perspectiva DevOps):**
   - Equipo agrega `aeon>=0.5.0` a `my_custom_libraries.txt`
   - Rebuild imagen: `./build.sh golden-cpu-custom splunk/ 5.2.2`
   - Push a registry: `docker push splunk/golden-cpu-custom:5.2.2`
   - Actualizan `images.conf` en Splunk
   - **Cristian recibe**: "Librería agregada, reinicia tu contenedor"

4. **Cristian continúa:**
   - Reinicia contenedor desde DSDL UI
   - Vuelve a abrir JupyterLab
   - Ahora `import aeon` funciona ✅

**Día 4: Preparar modelo para producción**

1. **Estructura DSDL requerida:**
   - Descubre que debe crear funciones `fit()`, `apply()`, `summary()`
   - Adapta su código:

   ```python
   def fit(df, epochs=50, batch_size=32, **kwargs):
       """Entrenamiento del modelo"""
       # Preprocesamiento
       scaler = StandardScaler()
       X_scaled = scaler.fit_transform(df)
       
       # Crear y entrenar autoencoder
       autoencoder = create_autoencoder(X_scaled.shape[1])
       autoencoder.fit(X_scaled, X_scaled, 
                      epochs=epochs, 
                      batch_size=batch_size)
       
       # Guardar modelo y scaler
       autoencoder.save('/srv/app/model/autoencoder.h5')
       joblib.dump(scaler, '/srv/app/model/scaler.pkl')
       
       return {"status": "trained", "loss": history.history['loss'][-1]}
   
   def apply(df, **kwargs):
       """Inferencia - detecta anomalías"""
       # Cargar modelo y scaler
       autoencoder = keras.models.load_model('/srv/app/model/autoencoder.h5')
       scaler = joblib.load('/srv/app/model/scaler.pkl')
       
       # Preprocesar
       X_scaled = scaler.transform(df)
       
       # Reconstruir
       X_reconstructed = autoencoder.predict(X_scaled)
       
       # Calcular error de reconstrucción
       mse = np.mean((X_scaled - X_reconstructed)**2, axis=1)
       
       # Retornar DataFrame con columnas para Splunk
       result = df.copy()
       result['anomaly_score'] = mse
       result['is_anomaly'] = (mse > threshold).astype(int)
       
       return result
   
   def summary(**kwargs):
       """Resumen del modelo"""
       return {
           "model_type": "autoencoder",
           "input_dim": 26,
           "encoder_dim": 64,
           "status": "ready"
       }
   ```

2. **Probar localmente en JupyterLab:**
   ```python
   # Test fit
   result = fit(df_train, epochs=10)
   print(result)
   
   # Test apply
   anomalies = apply(df_test)
   print(anomalies[['anomaly_score', 'is_anomaly']].head())
   ```
   - ✅ Funciona en notebook

**Día 5: Probar con datos reales desde Splunk**

1. **Stage datos para desarrollo:**
   ```spl
   index=horno_data 
   | where _time > relative_time(now(), "-7d@d")
   | table _time, k1, k2, k3, k4, s5-s20, k21-k26
   | fit MLTKContainer algo=autoencoder_anomalias mode=stage into app:AutoencoderDev
   ```
   - Datos llegan al contenedor como CSV
   - Puede trabajar interactivamente en JupyterLab

2. **Entrenar con datos reales:**
   ```spl
   index=horno_data 
   | where _time > relative_time(now(), "-30d@d")
   | fit MLTKContainer algo=autoencoder_anomalias epochs=100 batch_size=32 into app:AutoencoderModel
   ```
   - Modelo se entrena en contenedor
   - Resultados guardados automáticamente

3. **Aplicar en producción:**
   ```spl
   index=horno_data 
   | head 1000
   | apply AutoencoderModel
   | where is_anomaly=1
   | table _time, k1, k2, anomaly_score, is_anomaly
   ```
   - ✅ Inferencia funciona. Resultados integrados en Splunk.

**Desafíos y soluciones encontradas:**

**Desafío 1: Librerías faltantes**
- **Problema**: `aeon` no está disponible
- **Solución**: Solicitar al equipo agregar al custom image
- **Tiempo de espera**: ~2-4 horas (depende de proceso DevOps)
- **Alternativa temporal**: Usar otra librería o implementar manualmente

**Desafío 2: Datos en Splunk vs CSV locales**
- **Problema**: No puede leer CSV directamente en flujo principal
- **Solución**: Aprender SplunkSearch REST API o usar `mode=stage`
- **Aprendizaje**: ~1-2 días de curva

**Desafío 3: Estructura DSDL (fit/apply)**
- **Problema**: Código actual no tiene estructura DSDL
- **Solución**: Adaptar código a funciones fit/apply/summary
- **Tiempo**: ~1 día de refactoring

**Desafío 4: Debugging en producción**
- **Problema**: Errores en `apply` son más difíciles de debuggear
- **Solución**: Usar logs del contenedor, probar primero en `mode=stage`
- **Mejora**: Mejor logging y manejo de errores

**Ventajas descubiertas:**

✅ **Integración directa con Splunk**: No necesita exportar/importar datos  
✅ **Versionado automático**: Modelos versionados por Splunk  
✅ **Escalabilidad**: Contenedor escala automáticamente según carga  
✅ **Reproducibilidad**: Notebooks y modelos sincronizados automáticamente  
✅ **Colaboración**: Otros pueden usar sus modelos directamente desde SPL  

**Resumen del flujo de trabajo típico:**

```
1. Abrir JupyterLab (navegador)
   ↓
2. Crear/abrir notebook
   ↓
3. Obtener datos (SplunkSearch API o mode=stage)
   ↓
4. Experimentar/desarrollar (igual que antes)
   ↓
5. Si falta librería → solicitar agregar al custom image
   ↓
6. Adaptar código a estructura fit/apply/summary
   ↓
7. Probar con mode=stage (datos reales, desarrollo iterativo)
   ↓
8. Entrenar con fit (producción)
   ↓
9. Aplicar con apply (inferencia en producción)
```

**Para futuros experimentos:**
- Crea nuevo notebook
- Usa datos desde Splunk
- Prueba diferentes arquitecturas
- Si necesita nueva librería → solicita agregar (proceso ya establecido)

### 9.7 Puntos Clave Antes de Configurar Sandbox

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

---

## 11. Arquitectura y Operación de Contenedores

### 11.1 Relación Modelo-Contenedor

**Arquitectura fundamental de DSDL:**
- **1 modelo = 1 contenedor**: Cada modelo entrenado requiere un contenedor dedicado
- **Modelos atómicos**: No se pueden compartir contenedores entre múltiples modelos
- **Modelo Global**: Si un modelo se comparte, debe tener permisos `Global`

### 11.2 Diferenciación por Arquitectura de Procesamiento

Las imágenes Docker en DSDL se diferencian principalmente por el tipo de aceleración hardware:

| Imagen | Arquitectura | Runtime | Librerías Incluidas |
|--------|--------------|---------|---------------------|
| `golden-cpu` | CPU | `none` | TensorFlow CPU, PyTorch CPU, sklearn, Pandas, NumPy |
| `golden-gpu` | GPU (NVIDIA) | `nvidia` | TensorFlow GPU, PyTorch GPU, CUDA, cuDNN, sklearn, Pandas, NumPy |
| `golden-cpu-custom` | CPU + Custom | `none` | Golden CPU + librerías custom (ej: aeon) |
| `golden-gpu-custom` | GPU + Custom | `nvidia` | Golden GPU + librerías custom |

**Nota**: TPU (Google) y NPU no están soportados oficialmente. Solo NVIDIA GPU.

**Ejemplo de uso:**
```spl
# Modelo CPU
| fit MLTKContainer algo=randomforest 
  container_image="splunk/golden-cpu:5.2.2" 
  runtime="none"
  into app:Model1

# Modelo GPU
| fit MLTKContainer algo=autoencoder 
  container_image="splunk/golden-gpu:5.2.2" 
  runtime="nvidia"
  into app:Model2

# Modelo Custom CPU
| fit MLTKContainer algo=segmentacion 
  container_image="splunk/golden-cpu-custom:5.2.2" 
  runtime="none"
  into app:Model3
```

### 11.3 Escalabilidad y Rendimiento

**Múltiples modelos requeridos:**
- Si tienes 5 modelos, DSDL crea 5 contenedores separados
- Cada contenedor puede usar la misma imagen base o diferentes

**Gestión de demanda alta:**

**En Docker (single host):**
- ⚠️ Limitado a 1 contenedor por host
- Si el contenedor está saturado → requests se encolan
- Impacto en Splunk: Latencia alta o timeouts

**En Kubernetes/OpenShift:**
- ✅ Escalabilidad horizontal automática (HPA)
- Múltiples réplicas del mismo contenedor para alto tráfico
- Load balancing automático entre pods
- No impacta a Splunk (mejor performance)

**Ejemplo HPA:**
```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
spec:
  minReplicas: 1
  maxReplicas: 5
  metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 70
```

---

## 12. Gobernanza y Colaboración Entre Científicos de Datos

### 12.1 Acceso Compartido a JupyterLab

**Limitación arquitectónica:**
- **Mismo contenedor DEV**: Todos los científicos acceden a la misma instancia de JupyterLab
- **Sin aislamiento**: Todos ven los notebooks de otros científicos
- **Riesgo de sobrescritura**: Si dos científicos usan el mismo nombre de archivo

**Ubicación de notebooks:**
- `/srv/notebooks/` (o `/srv/app/model/` en versiones anteriores)
- Volúmenes persistentes para persistencia entre reinicios

### 12.2 Control de Acceso y Permisos

**Roles disponibles:**

| Rol | Capacidades |
|-----|-------------|
| `mltk_container_user` | Listar modelos, iniciar/detener contenedores |
| `mltk_container_admin` | Todo lo anterior + configurar setup, settings |

**Model sharing:**

| Nivel | Visibilidad |
|-------|-------------|
| **User** | Solo el creador (por defecto) |
| **App** | Usuarios de la misma app Splunk |
| **Global** | Todos en la plataforma (producción/HPC) |

**Convención recomendada:**
```spl
# Desarrollo privado
| fit MLTKContainer algo=Cristian_Autoencoder_Horno4_v1 
  into app:Cristian_Autoencoder_Horno4_v1

# Producción compartida
| fit MLTKContainer algo=Cristian_Autoencoder_Horno4_v1 
  into app:AutoencoderHorno4_GLOBAL
```

### 12.3 Estándar de Nombrado Requerido

**Porque es crítico:**
- Sin naming conventions → colisiones y sobrescrituras
- Difícil rastrear modelos de diferentes científicos
- Imposible versionar efectivamente

**Formato recomendado:**
```
Usuario_TipoModelo_CasoUso_Version.ipynb

Ejemplos:
- Cristian_Autoencoder_Horno4_v1.ipynb
- Maria_RandomForest_Fallos_v1.ipynb
- Pedro_ARIMA_Forecasting_v2.ipynb
```

**Uso en comandos:**
```spl
| fit MLTKContainer algo=Cristian_Autoencoder_Horno4_v1 
  into app:Cristian_Autoencoder_Horno4_v1
        ↑                           ↑
    Mismo nombre del archivo .ipynb
```

### 12.4 Desarrollo desde IDE Local

**Limitación:**
- ❌ **NO soportado oficialmente**: Desarrollo exclusivo en JupyterLab browser
- Alternativa: Trabajo manual con Git (clonar → editar local → push)

**Flujo alternativo (no recomendado):**
```
1. Descargar .ipynb desde JupyterLab
2. Editar en VS Code / PyCharm localmente
3. Subir de nuevo a JupyterLab
4. Guardar y usar
```

**Flujo recomendado:**
```
1. Trabajar directamente en JupyterLab del contenedor
2. Usar git desde terminal JupyterLab para versionado
3. Beneficios: Datos accesibles, librerías disponibles, sin desincronización
```

---

## 13. Versionado de Modelos

### 13.1 Limitaciones de Versionado en DSDL

**Lo que NO tiene DSDL:**
- ❌ Versionado automático de modelos
- ❌ Comparación A/B automática
- ❌ Rollback automático a versiones anteriores
- ❌ Model registry centralizado

**Implicación:**
```spl
# Si usas el mismo nombre de modelo, DSDL sobrescribe
| fit ... into app:MyModel     # Primera versión
| fit ... into app:MyModel     # ❌ SOBRESCRIBE la anterior

# Versionado manual requerido
| fit ... into app:MyModel_v1  # Versión 1
| fit ... into app:MyModel_v2  # Versión 2 (separado)
```

### 13.2 Solución: Git/Azure DevOps Integrado

**Posibilidad:**
- ✅ Git está disponible desde terminal de JupyterLab
- ✅ Puedes clonar repositorio Azure DevOps / GitHub / GitLab
- ✅ Commits, pushes, pull requests funcionan normalmente

**Flujo recomendado:**
```bash
# Desde terminal JupyterLab
cd /srv/notebooks
git clone https://dev.azure.com/empresa/dsdl-notebooks.git
cd dsdl-notebooks

# Editar notebook
# git add .
# git commit -m "Add Cristian_Autoencoder_Horno4_v1"
# git push
```

**Estructura sugerida de repositorio:**
```
dsdl-notebooks/
├── notebooks/
│   ├── Cristian_Autoencoder_Horno4_v1.ipynb
│   ├── Maria_RandomForest_Fallos_v1.ipynb
│   └── Pedro_ARIMA_Forecasting_v2.ipynb
├── templates/
│   └── template_empresa_base.ipynb
└── helpers/
    ├── telemetry_helper.py
    └── metrics_calculator.py
```

### 13.3 Comparación A/B Manual

**Proceso:**
```spl
# Entrenar dos versiones
| fit ... into app:AutoencoderHorno4_v1
| fit ... into app:AutoencoderHorno4_v2

# Aplicar ambas a datos de prueba
| apply AutoencoderHorno4_v1 | eval version="v1" | outputto index=test_results
| apply AutoencoderHorno4_v2 | eval version="v2" | outputto index=test_results

# Comparar métricas
index=test_results
| stats avg(anomaly_score), count by version
| eval diff = v1_score - v2_score
```

**Limitación:** Todo debe hacerse manualmente. No hay dashboard automático.

---

## 14. Observabilidad y Monitoreo de Modelos

### 14.1 Telemetría Automática de DSDL

**Lo que DSDL captura automáticamente:**

| Métrica | Descripción | Integración |
|---------|-------------|-------------|
| **CPU/Memoria** | Uso de recursos del contenedor | Splunk Observability Cloud |
| **GPU** | Uso de GPUs (si NVIDIA) | Observability + device plugin |
| **Latencia** | Tiempo de respuesta de requests | OpenTelemetry traces |
| **Errores** | Excepciones y crash loops | Container logs → Splunk |
| **Throughput** | Request/segundo | Observability metrics |

**Configuración:**
1. DSDL → Setup → Observability Settings
2. Enable Observability
3. Agregar Splunk Observability Access Token
4. Configurar endpoint OpenTelemetry

**Resultado:** Instrumentación automática. No requiere código adicional.

### 14.2 Métricas de Negocio (Limitación)

**Lo que NO captura automáticamente:**

| Métrica | Requerimiento |
|---------|---------------|
| **R²** | Implementación manual |
| **Accuracy** | Implementación manual |
| **Precision/Recall/F1** | Implementación manual |
| **MAE/RMSE** | Implementación manual |
| **Model drift** | Implementación manual |
| **Training loss per epoch** | Implementación manual |

**Limitación crítica:**
- Científicos de datos DEBEN implementar estas métricas manualmente
- Sin template → cada científico reimplementa
- Sin estándar → métricas inconsistentes entre proyectos

### 14.3 Solución Propuesta: Template Base + Helpers

**Estructura de imagen custom:**

```
golden-cpu-empresa:5.2.2
├── /mnt/srv/notebooks/
│   ├── barebone_template.ipynb          # Original Splunk
│   ├── template_empresa_base.ipynb      # ⭐ TU TEMPLATE
│   └── helpers/
│       ├── telemetry_helper.py          # HEC logging automático
│       ├── metrics_calculator.py        # R², Accuracy, F1, etc.
│       ├── preprocessor.py              # Preprocesamiento estándar
│       └── splunk_connector.py          # SplunkSearch reusable
```

**Ejemplo de template_empresa_base.ipynb:**

**Cell 1: Imports con helpers**
```python
import pandas as pd
import numpy as np
import joblib
from sklearn.metrics import r2_score, accuracy_score, f1_score
from dsdlsupport import SplunkHEC, SplunkSearch

# ✅ Helpers custom incluidos
import sys
sys.path.append('/mnt/srv/notebooks/helpers')
from telemetry_helper import log_metrics, log_training_step
from metrics_calculator import calculate_all_metrics
```

**Cell 2: fit() con telemetría**
```python
def fit(df, epochs=50, batch_size=32, **kwargs):
    # Preprocesamiento estándar
    X_processed, scaler = standard_preprocessing(df)
    
    # Científico SOLO agrega su modelo
    model = crear_su_modelo_especifico(X_processed.shape[1])
    history = model.fit(X_processed, X_processed, epochs=epochs)
    
    # ✅ Telemetría automática
    log_training_step(
        model_name=kwargs.get('model_name', 'default'),
        epoch=epochs,
        loss=history.history['loss'][-1]
    )
    
    model.save('/srv/app/model/modelo.h5')
    joblib.dump(scaler, '/srv/app/model/scaler.pkl')
    return {"status": "trained"}
```

**Cell 3: apply() con métricas**
```python
def apply(df, **kwargs):
    model = keras.models.load_model('/srv/app/model/modelo.h5')
    scaler = joblib.load('/srv/app/model/scaler.pkl')
    X_processed = scaler.transform(df)
    predictions = model.predict(X_processed)
    
    # ✅ Métricas automáticas si ground_truth existe
    if 'ground_truth' in df.columns:
        metrics = calculate_all_metrics(df['ground_truth'], predictions)
        log_metrics(
            model_name=kwargs.get('model_name', 'default'),
            **metrics  # R², accuracy, F1, precision, recall, MAE, RMSE
        )
    
    return resultados
```

**helpers/telemetry_helper.py:**
```python
from dsdlsupport import SplunkHEC

_hec = None

def init_hec():
    global _hec
    if _hec is None:
        _hec = SplunkHEC.SplunkHEC()
    return _hec

def log_metrics(model_name, r2=None, accuracy=None, f1=None, **kwargs):
    hec = init_hec()
    hec.send({'event': {
        'event_type': 'model_metrics',
        'model_name': model_name,
        'r2_score': r2,
        'accuracy': accuracy,
        'f1_score': f1,
        **kwargs
    }})

def log_training_step(model_name, epoch, loss, project):
    hec = init_hec()
    hec.send({'event': {
        'event_type': 'training_step',
        'model_name': model_name,
        'epoch': epoch,
        'loss': loss,
        'project': project
    }})
```

**helpers/metrics_calculator.py:**
```python
from sklearn.metrics import r2_score, accuracy_score, f1_score
from sklearn.metrics import precision_score, recall_score
import numpy as np

def calculate_all_metrics(y_true, y_pred):
    return {
        'r2': r2_score(y_true, y_pred),
        'accuracy': accuracy_score(y_true, y_pred),
        'f1': f1_score(y_true, y_pred, average='weighted'),
        'precision': precision_score(y_true, y_pred, average='weighted'),
        'recall': recall_score(y_true, y_pred, average='weighted'),
        'mae': np.mean(np.abs(y_true - y_pred)),
        'rmse': np.sqrt(np.mean((y_true - y_pred)**2))
    }
```

### 14.4 Dashboard de Monitoreo en Splunk

**Búsqueda ejemplo:**
```spl
index=ml_metrics event_type="model_metrics"
| timechart span=1h 
    avg(r2_score) as avg_r2,
    avg(accuracy) as avg_accuracy,
    avg(f1_score) as avg_f1
  by model_name
```

**Alert para model drift:**
```spl
index=ml_metrics event_type="model_metrics"
| stats latest(r2_score) as current_r2, latest(accuracy) as current_accuracy by model_name
| eval drift_r2 = if(current_r2 < 0.85, 1, 0)
| eval drift_acc = if(current_accuracy < 0.90, 1, 0)
| where drift_r2=1 OR drift_acc=1
| eval alert_message="Model drift detected: " + model_name
```

---

## 15. Recomendaciones Operacionales

### 15.1 Imagen Docker Custom Empresarial

**Objetivo:** Crear una imagen base que contenga todo lo necesario para que los científicos de datos se concentren SOLO en desarrollar modelos, sin preocuparse por:
- Configuración de telemetría
- Implementación de métricas
- Preprocesamiento estándar
- Conexión a Splunk
- Logging estructurado

**Proceso de creación:**

**1. Fork repositorio base:**
```bash
git clone https://github.com/splunk/splunk-mltk-container-docker
cd splunk-mltk-container-docker
```

**2. Agregar librerías custom a requirements:**
```text
# requirements_files/empresa_custom.txt
aeon>=0.5.0
# Otras librerías específicas de la empresa
```

**3. Actualizar tag_mapping.csv:**
```csv
Tag,base_image,dockerfile,base_requirements,specific_requirements,runtime,requirements_dockerfile
golden-cpu-empresa,deb:bullseye,Dockerfile.debian.golden-cpu,base_functional.txt,empresa_custom.txt,none,Dockerfile.debian.requirements
```

**4. Crear template y helpers:**

**Antes de build**, agregar archivos:
```
splunk-mltk-container-docker/
├── notebooks_custom/
│   ├── template_empresa_base.ipynb
│   └── helpers/
│       ├── telemetry_helper.py
│       ├── metrics_calculator.py
│       ├── preprocessor.py
│       └── splunk_connector.py
```

**5. Modificar Dockerfile para copiar archivos custom:**
```dockerfile
# En el Dockerfile, agregar antes del COPY de notebooks originales:
COPY notebooks_custom/ /mnt/srv/notebooks/
```

**6. Build imagen custom:**
```bash
./build.sh golden-cpu-empresa splunk/ 5.2.2
```

**7. Push a registry:**
```bash
docker tag splunk/golden-cpu-empresa:5.2.2 \
  us-central1-docker.pkg.dev/project/repo/golden-cpu-empresa:5.2.2
docker push us-central1-docker.pkg.dev/project/repo/golden-cpu-empresa:5.2.2
```

### 15.2 Workflow del Científico de Datos

**Con imagen custom:**
```
1. Abrir JupyterLab
2. Abrir template_empresa_base.ipynb
3. File → Save As → Cristian_Autoencoder_Horno4_v1.ipynb
4. Editar SOLO la función de modelo específico
5. Guardar
6. Usar: | fit MLTKContainer algo=Cristian_Autoencoder_Horno4_v1
```

**Sin tocar:**
- ✅ Telemetría (ya configurada)
- ✅ Métricas (helpers incluidos)
- ✅ Preprocesamiento (estándar)
- ✅ Conexión Splunk (configurada)
- ✅ Logging (automático)

### 15.3 Mejores Prácticas Resumidas

| Práctica | Implementación |
|----------|----------------|
| **Estándar de nombrado** | `Usuario_TipoModelo_CasoUso_Version.ipynb` |
| **Template base** | Incluir en imagen custom con telemetría preconfigurada |
| **Git integrado** | Clonar repo desde terminal JupyterLab |
| **Model permissions** | User (dev) → Global (producción) |
| **Versionado** | Convención de nombres + Git |
| **Observabilidad** | Splunk Observability + HEC para métricas negocio |
| **Separación DEV/PROD** | Containers DEV con JupyterLab, PROD minimal |

---

## Historial de Versiones

### Versión 1.0.0 (2025-01-31)

**Estado**: Versión inicial

**Contenido agregado:**
- ✅ Análisis comparativo completo: Necesidades vs. Capacidades DSDL
- ✅ Metodología de análisis (13 notebooks analizados)
- ✅ Comparación de librerías y frameworks
- ✅ Análisis de patrones de trabajo y flujos
- ✅ Tipos de modelos identificados y compatibilidad
- ✅ Entrada/salida de datos y gaps
- ✅ Características específicas (series temporales, feature engineering)
- ✅ Consideraciones de infraestructura
- ✅ Limitaciones y gaps principales

**Validaciones realizadas:**
- ✅ Verificación de librerías en Golden Image (GitHub)
  - `scipy`: ✅ INCLUIDO
  - `statsmodels`: ✅ INCLUIDO
  - `aeon`: ❌ NO INCLUIDO (requiere custom image)
- ✅ Validación de `mode=stage` y fuente de datos
- ✅ Análisis de custom images y proceso de agregar librerías

**Documentación agregada:**
- ✅ Procedimiento paso a paso para agregar librerías faltantes
- ✅ Perspectiva del científico de datos (flujo de trabajo real)
- ✅ Proceso DevOps completo (GCP/Azure)
  - Build de imágenes custom
  - Push a Artifact Registry (GCP)
  - Push a Container Registry (Azure)
  - CI/CD pipelines (GitHub Actions, Azure DevOps)
  - Configuración de Kubernetes (GKE/AKS)
  - Scanning de seguridad
  - Rollback y versionado

**Conclusión:**
- ✅ Compatibilidad general: **ALTA**
- ✅ POC viable con condiciones (custom image para `aeon`)
- ✅ Proceso DevOps documentado y automatizable
- ✅ Tiempo de respuesta: 15-30 min con CI/CD (vs 45-90 min manual)

---

**Próxima versión planificada**: 1.1.0 (validaciones prácticas en sandbox)

### Versión 1.0.1 (2025-01-31)

**Estado**: Actualización arquitectónica operacional

**Estado**: Actualización con hallazgos arquitectónicos y operacionales

**Nuevas secciones agregadas:**

**1. Arquitectura y Operación de Contenedores (Sección 11)**

- **Arquitectura de Contenedores**: 1 modelo = 1 contenedor
  - Explicación de la relación modelo-contenedor
  - Diferenciación por arquitectura (CPU vs GPU/NVIDIA)
  - Imágenes disponibles: Golden CPU, Golden GPU, Custom variants

- **Gobernanza y Colaboración (Sección 12)**
  - **Acceso compartido a JupyterLab**: Limitación - Mismo contenedor para todos los científicos
  - **Control de acceso**: Roles (`mltk_container_user`, `mltk_container_admin`)
  - **Model sharing**: Permisos User/App/Global
  - **Estándar de nombrado requerido**: `Usuario_TipoModelo_CasoUso_Version.ipynb`
  - **Desarrollo desde IDE local**: NO soportado (desarrollo exclusivo en JupyterLab)

- **Versionado de Modelos (Sección 13)**
  - **Versionado manual**: No hay versionado automático en DSDL
  - **Git/Azure DevOps integrado**: Sí posible desde terminal JupyterLab
  - **Práctica recomendada**: Convención de nombres + Git para código
  - **Limitación**: No hay comparación A/B o rollback automático
  - **Alternativa**: Proceso manual de versionado con nombres diferentes (`v1`, `v2`, etc.)

- **Observabilidad y Monitoreo (Sección 14)**
  - **Telemetría automática DSDL**: CPU, memoria, GPU, latencia, errores
  - **Integración**: Splunk Observability Cloud + HEC
  - **Limitación**: Métricas de negocio (R², Accuracy, F1) NO automáticas
  - **Solución propuesta**: Template base con helpers de telemetría
  - **Imagen custom recomendada**: Incluir helpers estandarizados

**2. Recomendaciones Operacionales (Sección 15)**

- **Imagen Docker Custom Empresarial**
  - Estructura propuesta para golden-cpu-empresa:5.2.2
  - Template base con telemetría integrada
  - Helpers reutilizables para científicos de datos
  - Preprocesamiento estandarizado
  - Configuración Git/Azure DevOps incluida

**Limitaciones Arquitectónicas Identificadas:**

| Limitación | Descripción | Impacto |
|------------|-------------|---------|
| **JupyterLab compartido** | Mismo contenedor DEV para todos los científicos | Alto - Riesgo de sobrescritura sin naming conventions |
| **Sin aislamiento de usuarios** | Todos ven notebooks de otros | Medio - Requiere disciplina de nombres |
| **Versionado manual** | DSDL no versiona automáticamente | Medio - Depende de Git + nombres |
| **No IDE local** | Desarrollo exclusivo en JupyterLab browser | Bajo - Curva de aprendizaje |
| **Métricas negocio manuales** | R², Accuracy, F1 requieren implementación | Medio - Necesita template base |
| **No model registry** | No hay comparación A/B automática | Medio - Proceso manual |

**Mejores Prácticas Documentadas:**

- ✅ Estándar de nombrado: `Usuario_TipoModelo_CasoUso_Version.ipynb`
- ✅ Template base con telemetría preconfigurada
- ✅ Helpers reutilizables en imagen custom
- ✅ Git para versionado de código
- ✅ Model permissions (User para dev, Global para prod)
- ✅ Separación DEV/PROD containers

---

