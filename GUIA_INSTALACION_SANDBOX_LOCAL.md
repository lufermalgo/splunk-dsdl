# Guía de Instalación: Sandbox Local Splunk DSDL

**Fecha**: 2025-01-31  
**Objetivo**: Configurar sandbox local para desarrollo y pruebas de Splunk DSDL  
**Instalación Base**: macOS con Splunk Enterprise y Docker Desktop

---

## 📋 Estado Actual de Prerrequisitos

### ✅ Componentes Instalados

| Componente | Estado | Detalles |
|------------|--------|----------|
| **Splunk Enterprise** | ✅ Instalado y Corriendo | Puerto web: 9000, Admin: 8089 |
| **Docker Desktop** | ✅ Instalado | Versión 28.5.1 |
| **Python** | ✅ Disponible | Versión 3.13.4 |

### ⚠️ Pendientes de Validación

| Componente | Acción Requerida | Estado |
|------------|------------------|--------|
| **Credenciales Splunk** | Validar usuario/password correctos | Pendiente |
| **App MLTK** | Instalar desde Splunkbase | Pendiente |
| **Add-on PSC** | Instalar desde Splunkbase | Pendiente |
| **App DSDL** | Instalar desde Splunkbase | Pendiente |
| **Golden Images** | Descargar desde Docker Hub | Pendiente |

---

## 📦 Fase 1: Instalación de Apps de Splunk

### 1.1 Verificar Versión de Splunk

Acceder a la consola web de Splunk: `http://localhost:9000`

**Comandos de validación**:
```bash
# Verificar versión de Splunk
curl -k http://localhost:9000/services/server/info
```

**Requisito**: Splunk Enterprise 8.2.x o superior

### 1.2 Descargar Apps desde Splunkbase

| App | URL Splunkbase | Versión Requerida |
|-----|----------------|-------------------|
| **Machine Learning Toolkit (MLTK)** | https://splunkbase.splunk.com/app/2890/ | 5.4.2+ |
| **Python for Scientific Computing (PSC)** | https://splunkbase.splunk.com/app/2889/ | 3.2.3, 3.2.4, o 4.2.3 |
| **Data Science and Deep Learning (DSDL)** | https://splunkbase.splunk.com/app/4607/ | 5.2.0+ |

**Nota**: Requiere cuenta de Splunkbase (gratuita)

### 1.3 Instalación mediante Splunk Web

1. Abrir Splunk Web: `http://localhost:9000`
2. Login con credenciales (validar que funcionan)
3. Navegar a: **Settings** → **Apps** (o usar menú Apps en barra lateral)
4. Click en **"Install app from file"** o **"Browse more apps"**
5. Para cada app:
   - Si descargaste el `.spl`, subir mediante **"Install app from file"**
   - Si instalas desde Splunkbase, buscar por nombre e instalar
6. Después de cada instalación, reiniciar Splunk

**Comandos post-instalación**:
```bash
# Reiniciar Splunk (macOS)
/Applications/Splunk/bin/splunk restart

# Verificar instalación de apps
ls -la /Applications/Splunk/etc/apps/ | grep -E "MLTK|python|dsdl"
```

### 1.4 Configurar Permisos de MLTK

**Importante**: MLTK debe tener permisos **Global** para compartir objetos de conocimiento:

1. En Splunk Web: **Settings** → **Apps**
2. Localizar **"Machine Learning Toolkit"**
3. Click en **"Permissions"**
4. Cambiar a **"Global - objects are shared across all apps"**
5. Guardar

---

## 🐳 Fase 2: Configuración de Docker

### 2.1 Verificar Conectividad de Docker

```bash
docker ps
docker info
```

### 2.2 Descargar Golden Images de Docker Hub

DSDL utiliza imágenes preconstruidas con librerías ML/DL:

| Imagen | Descripción |
|--------|-------------|
| `splunk/mltk-container-golden-image-cpu` | Imagen CPU con TensorFlow, PyTorch, scikit-learn |
| `splunk/mltk-container-golden-image-gpu` | Imagen GPU con soporte CUDA (no usaremos por ahora) |

**Comando para descargar**:
```bash
# Descargar imagen CPU (para desarrollo local)
docker pull splunk/mltk-container-golden-image-cpu:latest

# Verificar descarga
docker images | grep mltk-container
```

**Estimación de descarga**: ~5-10 GB dependiendo de la imagen

### 2.3 Validar Acceso a Docker Hub

Si estás detrás de un firewall corporativo o proxy:
```bash
# Probar conectividad
docker pull hello-world
```

Si falla, configurar proxy en Docker Desktop:
- Settings → Resources → Proxies

---

## 🔧 Fase 3: Configuración de DSDL

### 3.1 Acceder a DSDL Configuration

1. En Splunk Web, navegar a la app **"DSDL"** o **"Data Science and Deep Learning"**
2. Click en **"Configuration"** → **"Setup"**
3. Verás varios paneles de configuración

### 3.2 Configurar Docker

En el panel de **Docker Configuration**:

| Campo | Valor Local Sandbox |
|-------|---------------------|
| **Docker Host** | `unix:///var/run/docker.sock` (macOS default) |
| **Image Tag** | `splunk/mltk-container-golden-image-cpu:latest` |
| **Container Port** | `5000` (default) |
| **External Port** | `5000` (puede cambiar dinámicamente en DEV mode) |
| **Mode** | `DEV` (Development para interactividad) |

### 3.3 (Opcional) Configurar HEC

Si quieres que los notebooks envíen resultados/métricas a Splunk:

| Campo | Valor |
|-------|-------|
| **Enable HEC** | ✅ |
| **HEC URL** | `http://localhost:8088/services/collector` |
| **HEC Token** | [Crear token en Settings → Data Inputs → HTTP Event Collector] |

**Crear token HEC**:
1. Settings → Data Inputs
2. HTTP Event Collector → New Token
3. Nombre: `dsdl-hec-token`
4. Copiar token generado

### 3.4 (Opcional) Configurar Splunk REST API Access

Para que notebooks puedan hacer búsquedas SPL desde JupyterLab:

1. Settings → Tokens → Create New Token
2. Nombre: `dsdl-api-token`
3. Permisos: Acceso a búsquedas y datos
4. Copiar token

En DSDL Configuration:
- Host: `localhost` o `host.docker.internal`
- Port: `8089`
- Token: [Pegar token]

### 3.5 Test y Save

1. Click en **"Test & Save"** al final de la página
2. Esperar validación de conectividad
3. Si hay errores, revisar logs: `index=_internal "mltk-container"`

---

## 🧪 Fase 4: Validación Inicial

### 4.1 Lanzar Contenedor DEV

1. En DSDL: **Containers**
2. Click en **"Start Development Container"**
3. Seleccionar **Image**: `splunk/mltk-container-golden-image-cpu:latest`
4. Esperar inicio (30-60 segundos)
5. Verificar status: **Running**

**Comando alternativo**:
```bash
# Ver contenedores activos
docker ps | grep mltk-container
```

### 4.2 Acceder a JupyterLab

1. En el contenedor DEV, click en **"Open JupyterLab"**
2. Se abre navegador en puerto `8888` (o dinámico)
3. Login con token mostrado en UI o usar `splunk` / `splunk`

**O por comando**:
```bash
# Ver token de acceso
docker logs <container-id> | grep token
```

### 4.3 Ejecutar Ejemplo Predefinido

1. En DSDL: **Examples**
2. Seleccionar ejemplo: **"Neural Network Classifier Example for Tensorflow"**
3. Click en **"Run"**
4. Verificar que ejecuta sin errores

Si hay errores, revisar:
```bash
# Logs de Splunk
index=_internal "mltk-container" ERROR

# Logs de Docker
docker logs <container-id>
```

---

## 📊 Fase 5: Preparar Datos de Prueba

### 5.1 Crear Índice de Prueba

```bash
# Desde Splunk CLI
/Applications/Splunk/bin/splunk add index test_dsdl -maxTotalDataSizeMB 1000
```

O desde Splunk Web:
1. Settings → Indexes → New Index
2. Nombre: `test_dsdl`
3. Max Data Size: 1000 MB

### 5.2 Cargar Datos de Muestra

**Opción 1: Generar datos sintéticos desde notebook**
- Usar el notebook de Cristian como base
- Adaptar para generar datos temporales

**Opción 2: Usar datos de ejemplo de Splunk**
```bash
# Splunk incluye índices de ejemplo (_internal, main con algunas entradas)
# Verificar:
index=_internal | head 100
```

### 5.3 Verificar Acceso a Datos

Desde JupyterLab, probar búsqueda SPL:
```python
import splunklib.client as client
import splunklib.results as results

# Conectar (si configuraste REST API token)
service = client.connect(
    host='localhost',
    port=8089,
    username='admin',
    password='Splunk2025.'
)

# Ejecutar búsqueda
search_query = "index=_internal | head 10"
job = service.jobs.create(search_query)
rr = results.ResultsReader(job.results())

for result in rr:
    print(result)
```

---

## 🔍 Troubleshooting Común

### Error: "Cannot connect to Docker"

**Causa**: Docker Desktop no está corriendo o permisos incorrectos

**Solución**:
```bash
# Verificar Docker corriendo
docker ps

# Si no está corriendo:
open -a Docker
```

### Error: "Image not found"

**Causa**: No se descargó la Golden Image

**Solución**:
```bash
docker pull splunk/mltk-container-golden-image-cpu:latest
```

### Error: "MLTK not found"

**Causa**: MLTK no instalado o permisos no Global

**Solución**:
1. Verificar instalación: `ls /Applications/Splunk/etc/apps/ | grep MLTK`
2. Configurar permisos Global en Settings → Apps → MLTK → Permissions

### Error: "Port already in use"

**Causa**: Puerto 5000 u otro puerto ocupado

**Solución**:
```bash
# Ver qué usa el puerto
lsof -i :5000

# Si es otro contenedor, detener:
docker stop <container-id>
```

### Error: "Cannot load JupyterLab"

**Causa**: Puerto externo no accesible o firewal

**Solución**:
```bash
# Ver puertos del contenedor
docker port <container-id>

# Probar conectividad
curl http://localhost:8888
```

---

## ✅ Checklist de Validación Final

- [ ] Splunk Enterprise corriendo (puertos 9000, 8089)
- [ ] Docker Desktop corriendo y accesible
- [ ] App MLTK instalada con permisos Global
- [ ] Add-on PSC instalado
- [ ] App DSDL instalada
- [ ] Golden Image CPU descargada
- [ ] DSDL configurado y conectado a Docker
- [ ] Contenedor DEV iniciado exitosamente
- [ ] JupyterLab accesible en navegador
- [ ] Ejemplo predefinido ejecuta sin errores
- [ ] Datos de prueba cargados en índice `test_dsdl`
- [ ] Búsqueda SPL funciona desde notebook

---

## 📚 Próximos Pasos

Una vez validado el sandbox local:

1. **Cargar notebook de Cristian**: Adaptar uno de los notebooks de `Cristian-Autoencoder-Ejemplos`
2. **Prueba end-to-end**: Datos → Preprocesado → Fit → Apply → Resultados en Splunk
3. **Documentar hallazgos**: Actualizar `ANALISIS_COMPARATIVO_DSDL.md` con resultados prácticos
4. **Planear sandbox GCP**: Si todo funciona local, avanzar a infraestructura en la nube

---

## 📞 Referencias

- [Documentación oficial DSDL](./DSDL-docs.md)
- [Análisis comparativo actual](./ANALISIS_COMPARATIVO_DSDL.md)
- [Notebooks de Cristian](./Cristian-Autoencoder-Ejemplos/)
- [GitHub DSDL Examples](https://github.com/splunk/mltk-container-golden-image)
- [Splunkbase MLTK](https://splunkbase.splunk.com/app/2890/)
- [Splunkbase DSDL](https://splunkbase.splunk.com/app/4607/)

