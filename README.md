# Splunk DSDL - Ecosistema Empresarial para Científicos de Datos

**Repositorio**: https://github.com/lufermalgo/splunk-dsdl.git  
**Versión**: 1.2.0  
**Fecha**: 2025-01-31

---

## 🎯 Objetivo

Implementar un ecosistema completo basado en **Splunk DSDL** que permita a científicos de datos desarrollar, experimentar y desplegar modelos de ML/DL para detección de anomalías en procesos industriales, con telemetría estándar, gobernanza y MLOps integrados.

---

## ✅ Estado del Proyecto

### 🟢 Completado

- ✅ Análisis comparativo de necesidades vs capacidades DSDL
- ✅ Imagen Docker empresarial custom con aeon y helpers
- ✅ Sandbox local funcional en macOS ARM64
- ✅ Validación end-to-end del ecosistema
- ✅ Template empresarial con telemetría automática
- ✅ Checklist DevOps para despliegues
- ✅ Estrategia de gobernanza y métricas

### 🟡 En Desarrollo

- Sandbox cloud (GCP/Azure) para compartir con equipo
- Integración con notebooks reales de data scientists
- Dashboards de monitoreo de modelos

### 🔴 Pendiente

- Deployment producción
- CI/CD para custom images
- Integración con Splunk Cloud

---

## 📚 Documentación

### Documentación Principal

| Documento | Descripción | Estado |
|-----------|-------------|--------|
| **ANALISIS_COMPARATIVO_DSDL.md** | Análisis completo DSDL vs necesidades DS | ✅ v1.1.0 |
| **IMAGEN_EMPRESARIAL_SCOPE.md** | Scope y diseño de imagen custom | ✅ |
| **CHECKLIST_DEVOPS_DSDL.md** | Guía DevOps para despliegue | ✅ |
| **ESTRATEGIA_GOVERNANCE_INDEXING.md** | Gobernanza, índices y metadatos | ✅ |
| **BUILD_EXITOSO.md** | Validación build imagen | ✅ |

### Guías de Instalación y Configuración

| Documento | Descripción |
|-----------|-------------|
| **GUIA_INSTALACION_SANDBOX_LOCAL.md** | Setup Splunk + Docker |
| **CONFIGURACION_DSDL.md** | Configuración completa DSDL |
| **CONFIG_RAPIDA_DSDL.md** | Configuración rápida 5 min |
| **ESTADO_SANDBOX_LOCAL.md** | Estado actual del sandbox |

### Troubleshooting

| Documento | Problema |
|-----------|----------|
| **SOLUCION_OPENSSL_ERROR.md** | Error OpenSSL 1.0.2 |
| **SOLUCION_PUERTO_5000.md** | Puerto 5000 ocupado |
| **INSTRUCCIONES_AIRPLAY.md** | Deshabilitar AirPlay |

### Explicaciones Técnicas

| Documento | Tema |
|-----------|------|
| **EXPLICACION_HELPERS.md** | Qué son y cómo funcionan helpers |
| **ACLARACION_METRICAS.md** | Sklearn vs frameworks |
| **ACLARACION_HEC_TELEMETRIA.md** | HEC, índices, tokens |
| **DIFERENCIA_TELEMETRIA_DSDL_VS_HELPERS.md** | Infra vs negocio |
| **ESTRATEGIA_GOVERNANCE_INDEXING.md** | Naming, índices, metadatos |

### Validación y Testing

| Documento | Propósito |
|-----------|-----------|
| **VALIDACION_DSDL.md** | Checklist validación inicial |
| **SANDBOX_FUNCIONAL.md** | Confirmación sandbox listo |
| **VALIDACION_IMAGEN_EMPRESARIAL.md** | Tests imagen custom |
| **TEST_HELPERS_LOCAL.md** | Testing local sin contenedor |
| **TEST_TELEMETRIA_REAL_SPLUNK.md** | Tests end-to-end con Splunk |

### Estado de Contenedores

| Documento | Descripción |
|-----------|-------------|
| **LANZAMIENTO_CONTENEDOR.md** | Cómo lanzar contenedores |
| **PROXIMOS_PASOS_SANDBOX.md** | Qué hacer después setup |
| **ACCION_INMEDIATA.md** | Próximos pasos inmediatos |

### Build y Deploy

| Documento | Descripción |
|-----------|-------------|
| **BUILD_IMAGEN_EN_PROGRESO.md** | Estado durante build |
| **BUILD_EXITOSO.md** | Resultado build exitoso |
| **ESTADO_IMAGEN_EMPRESARIAL.md** | Estado actual imagen |
| **RESUMEN_BUILD.md** | Resumen técnico build |

---

## 🏗️ Arquitectura

### Componentes Implementados

```
┌─────────────────────────────────────────────────────────┐
│                  Splunk DSDL App                        │
│  - Machine Learning Toolkit (MLTK)                      │
│  - Data Science & Deep Learning (DSDL)                  │
│  - Python Security Controller (PSC)                     │
└─────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────┐
│           Custom Docker Image                           │
│  splunk/mltk-container-golden-cpu-empresa-arm:5.2.2    │
│                                                          │
│  📦 Librerías:                                          │
│    • TensorFlow 2.20.0, PyTorch 2.8.0                   │
│    • sklearn, scipy, statsmodels                        │
│    • aeon 1.1.0 ← CUSTOM AGREGADA                       │
│                                                          │
│  🛠️ Helpers Empresariales:                              │
│    • telemetry_helper.py                                │
│    • metrics_calculator.py                              │
│    • preprocessor.py                                    │
│    • splunk_connector.py                                │
│                                                          │
│  📝 Template:                                           │
│    • template_empresa_base.ipynb                        │
└─────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────┐
│                 Splunk Platform                         │
│  • HEC para telemetría                                  │
│  • ml_metrics (Metrics index)                           │
│  • ml_model_logs (Events index)                         │
│  • Dashboards y alertas                                 │
└─────────────────────────────────────────────────────────┘
```

---

## 🚀 Inicio Rápido

### Para DevOps

```bash
# 1. Ver checklist completo
cat CHECKLIST_DEVOPS_DSDL.md

# 2. Crear índices
# Settings → Indexes → New Index
# - ml_metrics (type: Metrics)
# - ml_model_logs (type: Events)

# 3. Crear tokens
# - HEC Token → apuntar a ml_metrics
# - Auth Token → para REST API

# 4. Configurar DSDL
# Ver CONFIGURACION_DSDL.md

# 5. Deploy imagen empresarial
cat BUILD_EXITOSO.md
```

### Para Data Scientists

```bash
# 1. Abrir JupyterLab desde DSDL UI

# 2. Importar helpers
import sys
sys.path.append("/dltk/notebooks_custom/helpers")
from telemetry_helper import log_metrics
from metrics_calculator import calculate_all_metrics

# 3. Usar template empresarial
# /dltk/notebooks_custom/template_empresa_base.ipynb

# 4. Nombrar modelos: app_tipo_caso_version
# Ejemplo: app1_autoencoder_horno4_v1
```

---

## 📊 Componentes de la Imagen Empresarial

### Librerías Python

**Base (Golden CPU):**
- TensorFlow, PyTorch, Keras
- scikit-learn, scipy, statsmodels
- Pandas, NumPy
- Matplotlib, Seaborn
- Prophet, XGBoost, LightGBM
- SHAP, LIME, MLflow
- ONNX, TensorBoard
- Dask, UMAP, tslearn
- PyOD, Isolation Forest
- Boto3, Plotly

**Custom agregadas:**
- **aeon 1.1.0** ← Para series temporales

### Helpers Empresariales

**telemetry_helper.py** (173 líneas)
- `log_metrics()` - Envío métricas a Splunk
- `log_training_step()` - Tracking entrenamiento
- `log_error()` - Logging de errores
- `log_prediction()` - Estadísticas inferencia

**metrics_calculator.py** (95 líneas)
- `calculate_all_metrics()` - Detección automática clasificación/regresión
- `calculate_regression_metrics()` - R², MAE, RMSE, MSE
- `calculate_classification_metrics()` - Accuracy, F1, Precision, Recall

**preprocessor.py** (176 líneas)
- `standard_preprocessing()` - Preprocesamiento estándar
- `apply_preprocessing()` - Aplicar scaler entrenado
- `encode_categorical()` - Codificación categóricas
- `handle_outliers()` - Detección outliers

**splunk_connector.py** (48 líneas)
- `validate_splunk_config()` - Validar configuración
- `get_splunk_config()` - Obtener config actual

### Template

**template_empresa_base.ipynb**
- Estructura DSDL (init/fit/apply/summary)
- Integración helpers empresariales
- Pre-configuración telemetría
- Ejemplos de uso

---

## 📋 Índices de Splunk

### ml_metrics (Tipo: Metrics)

**Uso**: Métricas de performance de modelos  
**Optimizado**: Para agregaciones y timecharts  
**Estructura**:
```json
{
  "event_type": "model_metrics",
  "app_name": "app1",
  "model_name": "app1_autoencoder_horno4_v1",
  "model_version": "1.0.0",
  "owner": "cristian",
  "project": "horno4_anomalies",
  "r2_score": 0.95,
  "accuracy": 0.92,
  "f1_score": 0.90,
  "mae": 0.05,
  "rmse": 0.08
}
```

### ml_model_logs (Tipo: Events)

**Uso**: Logs de entrenamiento, debugging  
**Estructura**:
```json
{
  "event_type": "training_step",
  "model_name": "app1_autoencoder_horno4_v1",
  "epoch": 50,
  "loss": 0.023,
  "timestamp": "2025-01-31T20:00:00"
}
```

---

## 🔐 Tokens Requeridos

### HEC Token

- **Name**: `dsdl-ml-telemetry-hec`
- **Index**: `ml_metrics`
- **Source Type**: `_json`
- **Configurado en**: DSDL Setup → Splunk HEC Settings

### Authentication Token

- **Name**: `dsdl-api-token`
- **Capability**: Admin (o restringido según necesidad)
- **Configurado en**: DSDL Setup → Splunk Access

---

## 🎯 Convención de Naming

### Modelos

```
{app_name}_{model_type}_{use_case}_{version}

Ejemplos:
  app1_autoencoder_horno4_v1
  app1_lstm_demand_forecast_v2
  app2_xgboost_churn_prediction_v1
```

**Componentes**:
- `app_name`: Identificador de aplicación
- `model_type`: autoencoder, lstm, xgboost, etc.
- `use_case`: horno4, demand_forecast, churn, etc.
- `version`: v1, v2, v3 (incremental)

---

## 🧪 Validación

### Tests Local
```bash
# Ver TEST_HELPERS_LOCAL.md
python3 test_metrics.py
python3 test_all_helpers.py
```

### Tests en Contenedor
```bash
# Ver VALIDACION_IMAGEN_EMPRESARIAL.md
docker run --rm splunk/mltk-container-golden-cpu-empresa-arm:5.2.2 \
  python3 -c "import aeon; print(f'aeon: {aeon.__version__}')"
```

### Checklist Validación
- [ ] Helpers importables
- [ ] aeon instalado
- [ ] TensorFlow/PyTorch funcionando
- [ ] Template ejecutable
- [ ] HEC configurado (opcional)

---

## 🔄 CI/CD y Mejores Prácticas

### Agregar Librería Nueva

**Proceso DevOps** (ver CHECKLIST_DEVOPS_DSDL.md):

1. Agregar librería a `empresa_custom.txt`
2. Build imagen: `./build.sh golden-cpu-empresa-arm splunk/ 5.2.2`
3. Escanear: `./scan_container.sh ...`
4. Push a registry
5. Actualizar Splunk config
6. Validar en sandbox
7. Deploy producción

**Tiempo estimado**: 2-4 horas

### Gobernanza

- **Naming**: `app_tipo_caso_version`
- **Versioning**: Manual + Git
- **Permisos**: Rol por app o usuario
- **Telemetría**: Automática con helpers

---

## 📊 Próximos Pasos

### Inmediato
1. ✅ Validar helpers en JupyterLab
2. ✅ Test template con datos sintéticos
3. ⏳ Integrar notebooks de Cristian

### Corto Plazo
1. ⏳ Configurar índices ml_metrics y ml_model_logs
2. ⏳ Crear HEC Token
3. ⏳ Test telemetría real en Splunk
4. ⏳ Crear dashboards base

### Mediano Plazo
1. ⏳ Deploy sandbox cloud (GCP)
2. ⏳ Terraform para infraestructura
3. ⏳ CI/CD para custom images
4. ⏳ Integración Splunk Cloud

---

## 📞 Contacto y Soporte

**Equipo**: DSDL + DevOps  
**Repositorio**: https://github.com/lufermalgo/splunk-dsdl.git  
**Documentación**: Ver archivos `.md` en este directorio

---

## 📝 Changelog

### Versión 1.2.0 (31-Enero-2025)
- ✅ Imagen empresarial build exitoso
- ✅ Contenedor running en sandbox local
- ✅ Validación end-to-end iniciada

### Versión 1.1.0 (31-Enero-2025)
- ✅ Helpers empresariales implementados
- ✅ Template base creado
- ✅ Estrategia gobernanza definida

### Versión 1.0.0 (31-Enero-2025)
- ✅ Análisis comparativo inicial
- ✅ Sandbox local funcional
- ✅ Identificación gaps y soluciones

