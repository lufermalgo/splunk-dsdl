# Scope: Imagen Docker Custom Empresarial

**Fecha**: 2025-01-31  
**Objetivo**: Definir componentes de imagen base empresarial para científicos de datos

---

## 🎯 Objetivo

Crear imagen base que permita que los científicos de datos se concentren **SOLO** en desarrollar modelos, sin preocuparse por:
- ✅ Telemetría/Monitoreo
- ✅ Métricas de negocio
- ✅ Preprocesamiento estándar
- ✅ Conexión Splunk
- ✅ Logging estructurado

---

## 📦 Componentes a Incluir

### 1. Librerías Python Custom

**Archivo**: `requirements_files/empresa_custom.txt`

```text
# ML/DL Base
scikit-learn>=1.3.0
tensorflow>=2.15.0
torch>=2.0.0

# Series temporales
aeon>=0.5.0
statsmodels>=0.14.0
scipy>=1.11.0

# Visualización
matplotlib>=3.8.0
seaborn>=0.13.0

# Utilidades
joblib>=1.3.0
pickle5>=0.0.11  # Si Python < 3.8
```

**Status**: Pendiente validar compatibilidad de versiones

---

### 2. Template Base Empresarial

**Archivo**: `notebooks_custom/template_empresa_base.ipynb`

**Funciones incluidas**:
- ✅ `init(df, param)` - Inicialización estándar
- ✅ `fit(df, param)` - Con telemetría automática
- ✅ `apply(df, param)` - Con métricas automáticas
- ✅ `summary(model)` - Metadata del modelo
- ✅ Stage data desde Splunk
- ✅ Preprocesamiento estándar (normalización, etc.)

**Células**:
1. Imports con helpers empresariales
2. Configuración estándar (HEC, conexión Splunk)
3. Función `init()`
4. Función `fit()` con logging
5. Función `apply()` con métricas
6. Función `summary()`
7. Células de prueba (no exportables)

---

### 3. Helpers Empresariales

**Directorio**: `notebooks_custom/helpers/`

#### 3.1 `telemetry_helper.py`
- Logging HEC automático
- Funciones: `log_metrics()`, `log_training_step()`, `log_error()`
- Configuración automática desde variables de entorno

#### 3.2 `metrics_calculator.py`
- Cálculo de métricas estándar
- Funciones: `calculate_all_metrics()`, `calculate_regression_metrics()`, `calculate_classification_metrics()`
- Retorna dict estandarizado

#### 3.3 `preprocessor.py`
- Preprocesamiento estándar
- Funciones: `standard_preprocessing()`, `handle_missing()`, `encode_categorical()`
- Scalers reutilizables

#### 3.4 `splunk_connector.py`
- Wrappers Splunk Search API
- Funciones: `get_data()`, `send_results()`, `validate_splunk_config()`

#### 3.5 `model_registry.py` (Opcional)
- Registro de modelos en MLflow
- Funciones: `log_model()`, `load_model_version()`, `compare_models()`

---

### 4. Configuración Empresarial

**Variables de entorno** (configurables en DSDL):
- HEC endpoint (automático desde DSDL)
- HEC token (automático)
- Splunk host (automático)
- Project/caso de uso (pasado por parámetro)
- Index destino para métricas (configurable)

---

## 🏗️ Estructura de Archivos

```
golden-cpu-empresa:5.2.2/
├── requirements_files/
│   └── empresa_custom.txt          # ✅ Librerías custom
├── notebooks_custom/
│   ├── template_empresa_base.ipynb  # ✅ Template base
│   └── helpers/
│       ├── telemetry_helper.py      # ✅ Logging automático
│       ├── metrics_calculator.py    # ✅ Métricas
│       ├── preprocessor.py          # ✅ Preprocesamiento
│       ├── splunk_connector.py      # ✅ Conexión Splunk
│       └── model_registry.py        # ⚠️ Opcional MLflow
├── tag_mapping.csv
│   └── golden-cpu-empresa row       # ✅ Config build
└── Dockerfile modificado
    └── COPY notebooks_custom/       # ✅ Copiar helpers
```

---

## 📋 Checklist de Implementación

### Fase 1: Preparación (1 día)
- [ ] Fork/clone del repositorio base DSDL
- [ ] Crear `empresa_custom.txt` con librerías
- [ ] Crear `helpers/` con archivos Python
- [ ] Crear `template_empresa_base.ipynb`
- [ ] Actualizar `tag_mapping.csv`

### Fase 2: Docker Configuration (1 día)
- [ ] Modificar Dockerfile para copiar `notebooks_custom/`
- [ ] Validar estructura de paths
- [ ] Compilar requirements custom

### Fase 3: Build & Test (1 día)
- [ ] Build local de imagen
- [ ] Ejecutar tests de helpers
- [ ] Validar template en JupyterLab
- [ ] Escanear vulnerabilidades

### Fase 4: Deploy Local Sandbox (0.5 día)
- [ ] Push a registry local/Docker Hub
- [ ] Configurar en DSDL
- [ ] Test con dato real

### Fase 5: Documentación (0.5 día)
- [ ] Documentar uso del template
- [ ] Guía para científicos de datos
- [ ] Ejemplos de uso

---

## 🎯 Resultado Esperado

**Científico de datos**:
1. Abre `template_empresa_base.ipynb`
2. File → Save As → `SuNombre_Modelo_CasoUso_v1.ipynb`
3. Edita **SOLO** la función de modelo
4. Guarda
5. Usa desde SPL

**Sin tocar**:
- Telemetría
- Métricas
- Preprocesamiento
- Conexión Splunk
- Logging

---

## ⚠️ Decisiones Pendientes

1. **Librerías adicionales**: ¿Qué más incluir en `empresa_custom.txt`?
2. **MLflow**: ¿Incluir helpers de MLflow o solo Splunk HEC?
3. **Index destino**: ¿Qué índice usar para métricas?
4. **Versioning**: ¿Incluir helper de versionado automático?

---

## 🚀 Próximo Paso

**Comenzar Fase 1**: Crear estructura de archivos y helpers base

