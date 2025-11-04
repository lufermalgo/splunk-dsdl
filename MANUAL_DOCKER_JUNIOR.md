# Manual Docker: Crear imágenes personalizadas DSDL

## Objetivo

Este manual guía el proceso completo para crear imágenes Docker personalizadas para Splunk DSDL, desde la configuración inicial del repositorio hasta la validación final en producción.

**Objetivos principales:**
- Crear imágenes Docker personalizadas con librerías y herramientas específicas de tu organización
- Validar que la imagen funciona correctamente antes de publicarla
- Publicar y registrar la imagen en Splunk DSDL
- Realizar pruebas completas de funcionamiento

## Audiencia

Este manual está diseñado para usuarios técnicos junior que no tienen experiencia previa con Docker, Git o DSDL. Cada paso incluye explicaciones detalladas y validaciones para asegurar el éxito del proceso.

**Roles:**
- **Usuario Técnico Junior**: Sigue este manual paso a paso sin experiencia previa
- **Administrador de Splunk**: Valida la configuración final en images.conf y reinicia Splunk
- **Desarrollador de Imágenes**: Personaliza librerías y helpers en el repositorio

## Prerequisitos

Antes de comenzar, asegúrate de tener instalado y configurado:

- **Docker**: Instalado y funcionando (verifica con `docker --version`)
- **Git**: Instalado (verifica con `git --version`)
- **Acceso al Registry**: Credenciales para publicar imágenes (Docker Hub, registry privado, etc.)
- **Splunk DSDL**: Splunk con DSDL instalado y permisos para editar `images.conf`
- **Editor de texto**: Cualquier editor para modificar archivos de configuración

## Estructura del Proceso

El proceso completo consta de 12 pasos principales:

1. **Preparación**: Clonar repositorio y configurar Git
2. **Configuración**: Crear requirements custom y registrar tag
3. **Construcción**: Build de la imagen
4. **Validación**: Pruebas locales
5. **Publicación**: Publicar en registry
6. **Registro**: Configurar en Splunk
7. **Validación final**: Pruebas en DSDL UI y con SPL

---

## Paso 1: Clonar el Repositorio

### ¿Qué es esto?

El repositorio oficial de Splunk contiene todos los archivos necesarios para construir imágenes Docker personalizadas.

### Procedimiento

1. Abre tu terminal (Command Prompt en Windows, Terminal en macOS/Linux)

2. Navega al directorio donde quieres guardar el proyecto:
```bash
cd ~/Proyectos  # o el directorio que prefieras
```

3. Clona el repositorio oficial:
```bash
git clone https://github.com/splunk/mltk-container-docker.git
```

4. Entra al directorio del proyecto:
```bash
cd mltk-container-docker
```

### Validación

Verifica que el clon fue exitoso:
```bash
ls -la
# Debes ver archivos como: build.sh, Dockerfile*, requirements_files/, tag_mapping.csv
```

**✅ Resultado esperado**: Ves los archivos del repositorio en tu directorio.

---

## Paso 2: Configurar Git (Primera vez)

### ¿Qué es esto?

Git necesita saber quién eres para poder hacer commits (guardar cambios). Esta configuración es global y solo necesitas hacerla una vez.

### Procedimiento

1. Configura tu nombre (usa el nombre que aparece en tu organización):
```bash
git config --global user.name "Tu Nombre"
```

2. Configura tu email (usa el email de tu organización):
```bash
git config --global user.email "tu.email@empresa.com"
```

3. Verifica la configuración:
```bash
git config --global --list
# Debes ver user.name y user.email con los valores que configuraste
```

### Validación

**✅ Resultado esperado**: Git muestra tu nombre y email en la lista de configuración.

---

## Paso 3: Crear Requirements Custom

### ¿Qué es esto?

Un archivo `requirements.txt` es una lista de librerías de Python que quieres instalar en tu imagen Docker. Necesitas crear uno personalizado para agregar las librerías que tu organización necesita.

### Procedimiento

1. Ve al directorio de requirements:
```bash
cd requirements_files
```

2. Crea un nuevo archivo (por ejemplo, `empresa_custom.txt`):
```bash
touch empresa_custom.txt
# En Windows: type nul > empresa_custom.txt
```

3. Abre el archivo con tu editor de texto y agrega las librerías que necesitas, una por línea:
```
aeon>=0.5.0
telemetry-helper
preprocessor-utils
```

**Nota**: Puedes usar versiones específicas (ej: `tensorflow==2.10.0`) o rangos (ej: `pandas>=1.5.0,<2.0.0`).

4. Guarda el archivo y cierra el editor.

5. Vuelve al directorio raíz:
```bash
cd ..
```

### Validación

Verifica que el archivo existe y tiene el contenido correcto:
```bash
cat requirements_files/empresa_custom.txt
# En Windows: type requirements_files\empresa_custom.txt
```

**✅ Resultado esperado**: Ves las librerías que agregaste, una por línea.

---

## Paso 4: Registrar Tag en tag_mapping.csv

### ¿Qué es esto?

El archivo `tag_mapping.csv` le dice al script de build qué Dockerfile usar y qué archivo de requirements incluir para cada tipo de imagen. Necesitas agregar una nueva línea para tu imagen personalizada.

### Procedimiento

1. Abre el archivo `tag_mapping.csv` con tu editor de texto.

2. Observa el formato de las líneas existentes. Debería verse así:
```csv
Tag,base_image,dockerfile,specific_requirements
golden-cpu,splunk/debian:bullseye,Dockerfile.debian.golden-cpu,requirements_golden.txt
minimal-cpu,splunk/debian:bullseye,Dockerfile.debian.minimal-cpu,requirements_minimal.txt
```

3. Agrega una nueva línea al final del archivo con tu configuración. Ejemplo:
```csv
golden-cpu-empresa-arm,splunk/debian:bullseye,Dockerfile.debian.golden-cpu,empresa_custom.txt
```

**Explicación de los campos:**
- **Tag**: El nombre de tu imagen (puede ser `golden-cpu-empresa-arm`)
- **base_image**: La imagen base de Docker (generalmente `splunk/debian:bullseye`)
- **dockerfile**: El Dockerfile a usar (puede ser `Dockerfile.debian.golden-cpu`)
- **specific_requirements**: Tu archivo custom (el que creaste en el Paso 3)

4. Guarda el archivo.

### Validación

Verifica que la línea fue agregada correctamente:
```bash
tail -n 1 tag_mapping.csv
# Debes ver tu nueva línea con todos los campos separados por comas
```

**✅ Resultado esperado**: La última línea del CSV muestra tu configuración nueva.

---

## Paso 5: Build de la Imagen

### ¿Qué es esto?

El "build" es el proceso de construir tu imagen Docker usando los archivos que configuraste. Esto crea una imagen que puedes usar localmente o publicar.

### Procedimiento

1. Asegúrate de estar en el directorio raíz del proyecto:
```bash
pwd
# Debe mostrar: .../mltk-container-docker
```

2. Verifica que el script `build.sh` existe y tiene permisos de ejecución:
```bash
ls -l build.sh
# En Windows: dir build.sh
```

Si no tiene permisos, dale permisos de ejecución:
```bash
chmod +x build.sh
# Windows: No es necesario
```

3. Ejecuta el build. El formato del comando es:
```bash
./build.sh <TAG> <ORGANIZACION> <VERSION>
```

Ejemplo real:
```bash
./build.sh golden-cpu-empresa-arm splunk/ 5.2.2
```

**Explicación de los parámetros:**
- `<TAG>`: El tag que definiste en `tag_mapping.csv` (ej: `golden-cpu-empresa-arm`)
- `<ORGANIZACION>`: Tu organización en Docker (ej: `splunk/` o `tu-org/`)
- `<VERSION>`: Versión de la imagen (ej: `5.2.2`)

**En Windows**, usa:
```powershell
bash build.sh golden-cpu-empresa-arm splunk/ 5.2.2
```

4. Espera a que termine el build. Esto puede tomar varios minutos (5-15 minutos dependiendo de tu conexión y computadora).

### Validación

Durante el build, verás mensajes como:
```
Building image...
Step 1/20 : FROM splunk/debian:bullseye
Step 2/20 : COPY requirements_files/empresa_custom.txt /tmp/
...
Successfully built abc123def456
Successfully tagged splunk/mltk-container-golden-cpu-empresa-arm:5.2.2
```

**✅ Resultado esperado**: Al final ves "Successfully built" y "Successfully tagged" sin errores.

Si hay errores, lee el mensaje completo. Los errores comunes incluyen:
- Librerías que no se pueden instalar (revisa el nombre y versión en `empresa_custom.txt`)
- Problemas de conexión (verifica tu internet)
- Permisos de Docker (en Linux, puede necesitar `sudo`)

---

## Paso 6: Validar Build Local

### ¿Qué es esto?

Antes de publicar la imagen, debes verificar que se construyó correctamente y que puedes ejecutarla localmente.

### Procedimiento

1. Lista las imágenes Docker para verificar que tu imagen está ahí:
```bash
docker images | grep mltk-container-golden-cpu-empresa-arm
# O simplemente:
docker images
```

**✅ Resultado esperado**: Ves tu imagen en la lista con el TAG que especificaste (ej: `5.2.2`).

2. Prueba ejecutar un comando simple en la imagen:
```bash
docker run --rm splunk/mltk-container-golden-cpu-empresa-arm:5.2.2 python -c "import sys; print('Python funciona correctamente')"
```

**✅ Resultado esperado**: Ves el mensaje "Python funciona correctamente".

3. (Opcional) Verifica que las librerías custom están instaladas:
```bash
docker run --rm splunk/mltk-container-golden-cpu-empresa-arm:5.2.2 python -c "import aeon; print('aeon instalado correctamente')"
```

**✅ Resultado esperado**: Si agregaste `aeon` a tus requirements, ves "aeon instalado correctamente". Si no, verás un error de importación.

### Validación

**✅ Checklist de validación:**
- [ ] La imagen aparece en `docker images`
- [ ] Puedes ejecutar Python en la imagen
- [ ] (Si aplica) Las librerías custom están instaladas

---

## Paso 7: (Opcional) Escanear Vulnerabilidades

### ¿Qué es esto?

Puedes escanear tu imagen en busca de vulnerabilidades de seguridad antes de publicarla. Esto es opcional pero recomendado para producción.

### Procedimiento

1. Verifica que el script `scan_container.sh` existe:
```bash
ls -l scan_container.sh
```

2. Ejecuta el escaneo:
```bash
./scan_container.sh golden-cpu-empresa-arm splunk/ 5.2.2
```

**En Windows**:
```powershell
bash scan_container.sh golden-cpu-empresa-arm splunk/ 5.2.2
```

3. Revisa el reporte de vulnerabilidades. El script mostrará vulnerabilidades críticas, altas, medias y bajas.

### Validación

**✅ Resultado esperado**: El escaneo completa sin errores y muestra un reporte. Decide si las vulnerabilidades encontradas son aceptables para tu uso.

**Nota**: Muchas imágenes base tienen vulnerabilidades menores. Consulta con tu equipo de seguridad si encuentras vulnerabilidades críticas o altas.

---

## Paso 8: Publicar en Registry

### ¿Qué es esto?

El registry es donde almacenas tu imagen Docker para que otros sistemas puedan descargarla. Puede ser Docker Hub, un registry privado de tu organización, o cualquier otro registry compatible.

### Procedimiento

1. Inicia sesión en tu registry (si es privado):
```bash
docker login docker.io
# O para un registry privado:
docker login registry.empresa.com
```

Ingresa tus credenciales cuando se te soliciten.

2. Verifica que estás autenticado:
```bash
docker info | grep Username
# O simplemente verifica que no hay errores de autenticación
```

3. Publica la imagen:
```bash
docker push splunk/mltk-container-golden-cpu-empresa-arm:5.2.2
```

**Nota**: Si tu organización no es `splunk/`, cambia `splunk/` por tu organización.

4. Espera a que termine la publicación. Esto puede tomar varios minutos dependiendo del tamaño de la imagen y tu conexión.

### Validación

Durante la publicación, verás mensajes como:
```
The push refers to repository [docker.io/splunk/mltk-container-golden-cpu-empresa-arm]
abc123def456: Pushing [==================================================>] 500MB
5.2.2: digest: sha256:abc123... size: 1234
```

**✅ Resultado esperado**: Al final ves "digest: sha256:..." indicando que la imagen fue publicada exitosamente.

Puedes verificar en tu registry (Docker Hub web, etc.) que la imagen está disponible.

---

## Paso 9: Registrar en Splunk (images.conf)

### ¿Qué es esto?

Necesitas decirle a Splunk dónde encontrar tu imagen Docker. Esto se hace editando el archivo `images.conf` en Splunk.

### Procedimiento

1. Durante el build, se generó un archivo de configuración en `images_conf_files/`. Busca el archivo que corresponde a tu imagen:
```bash
ls images_conf_files/
```

Deberías ver algo como: `images_golden-cpu-empresa-arm.conf`

2. Abre el archivo y revisa su contenido:
```bash
cat images_conf_files/images_golden-cpu-empresa-arm.conf
```

El contenido debería verse así:
```
[image:golden-cpu-empresa-arm]
repository = splunk/mltk-container-golden-cpu-empresa-arm
tag = 5.2.2
```

3. Copia este archivo a la ubicación de configuración local de DSDL en Splunk:
```bash
cp images_conf_files/images_golden-cpu-empresa-arm.conf $SPLUNK_HOME/etc/apps/mltk-container/local/images.conf
```

**En Windows**:
```powershell
copy images_conf_files\images_golden-cpu-empresa-arm.conf $env:SPLUNK_HOME\etc\apps\mltk-container\local\images.conf
```

**Nota**: Si el directorio `local/` no existe, créalo primero:
```bash
mkdir -p $SPLUNK_HOME/etc/apps/mltk-container/local/
```

4. Reinicia Splunk para que cargue la nueva configuración:
```bash
$SPLUNK_HOME/bin/splunk restart
```

O desde Splunk Web: Settings → Server controls → Restart Splunk

### Validación

1. Verifica que el archivo fue copiado correctamente:
```bash
cat $SPLUNK_HOME/etc/apps/mltk-container/local/images.conf
```

**✅ Resultado esperado**: Ves la configuración de tu imagen en el archivo.

2. Verifica en Splunk Web:
   - Ve a: **DSDL → Configuration → Container Images**
   - Busca tu imagen (ej: `golden-cpu-empresa-arm`)
   - Debe aparecer con el tag correcto (ej: `5.2.2`)

**✅ Resultado esperado**: Tu imagen aparece en la lista de imágenes disponibles.

---

## Paso 10: Validar en DSDL UI

### ¿Qué es esto?

DSDL UI es la interfaz web donde puedes gestionar contenedores y modelos. Aquí validarás que tu imagen funciona correctamente.

### Procedimiento

1. Abre Splunk Web y navega a: **DSDL → Configuration → Container Images**

2. Busca tu imagen en la lista (debe aparecer el nombre del tag, ej: `golden-cpu-empresa-arm`)

3. Haz clic en **"Start"** para lanzar el contenedor de desarrollo (DEV).

4. Espera a que el contenedor inicie (puede tomar 1-2 minutos). Verás un indicador de estado que cambia de "Stopped" a "Running".

5. Una vez que el contenedor está "Running", haz clic en **"Open JupyterLab"** (o el enlace similar).

6. JupyterLab debería abrirse en una nueva pestaña. Si no se abre, verifica que no hay un bloqueador de ventanas emergentes.

### Validación

En JupyterLab:

1. Verifica que puedes crear un nuevo notebook:
   - Click en "New" → "Python 3" (o similar)

2. Prueba importar tus librerías custom:
```python
import aeon
print("aeon importado correctamente")
```

**✅ Resultado esperado**: No hay errores de importación.

3. Prueba los helpers custom (si los tienes):
```python
from telemetry_helper import log_metrics
print("Helpers custom funcionan")
```

**✅ Resultado esperado**: No hay errores de importación.

**✅ Checklist de validación:**
- [ ] El contenedor inicia correctamente (estado "Running")
- [ ] JupyterLab se abre sin errores
- [ ] Puedes importar librerías custom
- [ ] Puedes importar helpers custom (si aplica)

---

## Paso 11: Validar con SPL (fit/apply)

### ¿Qué es esto?

SPL (Search Processing Language) es el lenguaje de búsqueda de Splunk. Aquí validarás que puedes usar tu imagen para entrenar y usar modelos directamente desde Splunk.

### Procedimiento

#### 11.1: Staging (Desarrollo)

El modo "stage" prepara datos y abre JupyterLab para desarrollo interactivo:

```spl
index=demo_anomalias_data
| fit MLTKContainer algo=flujo_cristian_completo mode=stage into app:mi_modelo_v1 container_image="splunk/mltk-container-golden-cpu-empresa-arm:5.2.2"
```

**Explicación:**
- `index=demo_anomalias_data`: El índice de Splunk con tus datos
- `algo=flujo_cristian_completo`: El nombre del notebook/algoritmo
- `mode=stage`: Modo de desarrollo (no entrena completamente)
- `into app:mi_modelo_v1`: Guarda el modelo con este nombre
- `container_image=...`: Tu imagen personalizada

**✅ Resultado esperado**: El comando completa sin errores y puede abrir JupyterLab si está configurado.

#### 11.2: Entrenamiento Completo (fit)

Este comando entrena el modelo completamente y guarda los artefactos:

```spl
index=demo_anomalias_data
| fit MLTKContainer algo=flujo_cristian_completo into app:mi_modelo_v1 container_image="splunk/mltk-container-golden-cpu-empresa-arm:5.2.2"
```

**✅ Resultado esperado**: 
- El comando completa sin errores
- Ves mensajes de progreso del entrenamiento
- El modelo se guarda exitosamente

**Tiempo esperado**: Puede tomar varios minutos dependiendo del tamaño de los datos.

#### 11.3: Inferencia (apply)

Este comando usa el modelo entrenado para hacer predicciones:

```spl
index=demo_anomalias_data
| apply flujo_cristian_completo
```

**Explicación:**
- `apply`: El comando de inferencia
- `flujo_cristian_completo`: El nombre del modelo a usar (debe coincidir con el usado en `fit`)

**✅ Resultado esperado**: 
- El comando completa sin errores
- Ves una columna nueva con los resultados (ej: `anomaly_score`)
- Los resultados son valores numéricos razonables

### Validación

**✅ Checklist de validación:**
- [ ] El comando `fit` completa sin errores
- [ ] El modelo se entrena correctamente
- [ ] El comando `apply` completa sin errores
- [ ] Los resultados de inferencia son razonables

**Errores comunes:**
- `No module named 'X'`: La librería no está instalada en la imagen (revisa `empresa_custom.txt`)
- `Unable to save model`: Problema con permisos o estructura del modelo (revisa las funciones `save` y `load` en el notebook)
- `Container failed to start`: Problema con la imagen o configuración (revisa logs en `index=_internal "mltk-container"`)

---

## Paso 12: Validar Resultados en Splunk

### ¿Qué es esto?

Después de ejecutar `fit` y `apply`, debes validar que:
1. Los logs de DSDL muestran que todo funcionó correctamente
2. La telemetría (si la implementaste) está llegando a Splunk

### Procedimiento

#### 12.1: Validar Logs de DSDL

Busca en los logs de DSDL para verificar que no hay errores:

```spl
index=_internal "mltk-container"
| stats count by log_level, component
| sort -count
```

**✅ Resultado esperado**: 
- No ves errores críticos (`ERROR`, `CRITICAL`)
- Ves mensajes de éxito (`INFO`, `DEBUG`) relacionados con tu modelo

Si ves errores, lee el mensaje completo:
```spl
index=_internal "mltk-container" ERROR
| head 20
```

#### 12.2: Validar Telemetría (si aplica)

Si tu modelo envía telemetría (métricas y eventos), verifica que están llegando:

**Métricas:**
```spl
index=ml_metrics model_name=mi_modelo_v1
| stats avg(_value) by metric_name
```

**Eventos:**
```spl
index=ml_model_logs model_name=mi_modelo_v1
| head 20
```

**✅ Resultado esperado**: 
- Ves métricas con valores razonables (ej: `r2_score`, `accuracy`)
- Ves eventos de entrenamiento y predicción

### Validación

**✅ Checklist de validación:**
- [ ] Los logs de DSDL no muestran errores críticos
- [ ] (Si aplica) Las métricas están llegando al índice `ml_metrics`
- [ ] (Si aplica) Los eventos están llegando al índice `ml_model_logs`
- [ ] Los valores de métricas son razonables (ej: `accuracy` entre 0 y 1)

---

## Troubleshooting

### Problema: "git: command not found"

**Solución**: Git no está instalado. Descarga e instala Git desde https://git-scm.com/downloads

### Problema: "docker: command not found"

**Solución**: Docker no está instalado o no está en el PATH. 
- Verifica que Docker Desktop está corriendo
- En Linux, puede necesitar agregar tu usuario al grupo `docker`: `sudo usermod -aG docker $USER` (luego reinicia sesión)

### Problema: "Permission denied" al ejecutar `./build.sh`

**Solución**: El archivo no tiene permisos de ejecución.
```bash
chmod +x build.sh
```

### Problema: Build falla con "No module named 'X'"

**Solución**: La librería no está instalada o el nombre es incorrecto.
1. Verifica el nombre exacto de la librería en PyPI: https://pypi.org/
2. Asegúrate de que está en `empresa_custom.txt` con la sintaxis correcta
3. Vuelve a hacer el build

### Problema: "Unable to connect to Docker daemon"

**Solución**: Docker no está corriendo.
- En Windows/Mac: Abre Docker Desktop
- En Linux: `sudo systemctl start docker`

### Problema: Imagen no aparece en DSDL UI

**Solución**: 
1. Verifica que copiaste `images.conf` al lugar correcto
2. Verifica que reiniciaste Splunk
3. Revisa los logs de Splunk para errores de configuración:
```spl
index=_internal "images.conf" ERROR
```

### Problema: Contenedor falla al iniciar

**Solución**: 
1. Revisa los logs de DSDL:
```spl
index=_internal "mltk-container" ERROR
| head 20
```
2. Verifica que la imagen existe en el registry
3. Verifica que tienes acceso al registry (credenciales correctas)

### Problema: `fit` o `apply` fallan con errores de importación

**Solución**: 
1. Verifica que las librerías están en `empresa_custom.txt`
2. Verifica que hiciste el build con la versión correcta
3. Prueba importar las librerías en JupyterLab dentro del contenedor DEV

### Problema: Telemetría no llega a Splunk

**Solución**:
1. Verifica que HEC está configurado correctamente en DSDL Setup
2. Verifica que los índices `ml_metrics` y `ml_model_logs` existen
3. Verifica que el token de HEC tiene permisos para escribir en esos índices
4. Revisa los logs del contenedor para errores de conexión

---

## Checklist Final

Antes de considerar que la imagen está lista para producción:

- [ ] La imagen se construye sin errores
- [ ] La imagen pasa las validaciones locales (Python funciona, librerías instaladas)
- [ ] La imagen se publica exitosamente en el registry
- [ ] La imagen aparece en DSDL UI
- [ ] El contenedor DEV inicia correctamente
- [ ] JupyterLab funciona y puede importar librerías custom
- [ ] El comando `fit` completa exitosamente
- [ ] El comando `apply` completa exitosamente
- [ ] Los resultados de inferencia son razonables
- [ ] Los logs de DSDL no muestran errores críticos
- [ ] (Si aplica) La telemetría llega correctamente a Splunk

---

## Recursos Adicionales

- **Repositorio oficial**: https://github.com/splunk/mltk-container-docker
- **Documentación de DSDL**: [Documentación oficial de Splunk DSDL]
- **Documentación de Docker**: https://docs.docker.com/
- **Documentación de Git**: https://git-scm.com/doc

---

## Glosario

- **Build**: Proceso de construir una imagen Docker a partir de archivos de configuración
- **Container**: Instancia ejecutándose de una imagen Docker
- **Dockerfile**: Archivo de configuración que define cómo construir una imagen Docker
- **DSDL**: Data Science and Deep Learning, la app de Splunk para Machine Learning
- **HEC**: HTTP Event Collector, mecanismo de Splunk para ingerir datos
- **Image**: Plantilla de solo lectura para crear contenedores
- **Registry**: Repositorio donde se almacenan imágenes Docker
- **SPL**: Search Processing Language, el lenguaje de búsqueda de Splunk
- **Tag**: Etiqueta que identifica una versión específica de una imagen Docker

---

## Notas Finales

Este manual está diseñado para ser completamente autoexplicativo. Si encuentras algún paso que no está claro o necesitas ayuda adicional, consulta con tu equipo o revisa la documentación oficial.

**Recordatorio importante**: Siempre valida cada paso antes de continuar al siguiente. Esto te ayudará a identificar problemas temprano y ahorrar tiempo.

---

## POC: Splunk DSDL

### Repositorio de Imágenes Docker Oficiales

DSDL puede usar imágenes Docker pre-construidas oficialmente por Splunk. Todas las imágenes oficiales están disponibles en **Docker Hub** bajo la organización de Splunk.

#### Información del Repositorio

| Item | Detalle |
|------|---------|
| **Registry** | `docker.io` (Docker Hub) |
| **Organización** | `splunk` |
| **Repositorio base** | `mltk-container-*` |
| **URL web** | https://hub.docker.com/u/splunk |
| **URL de búsqueda** | https://hub.docker.com/search?q=splunk%2Fmltk-container |

#### Imágenes Oficiales Disponibles

Las siguientes imágenes están disponibles oficialmente en Docker Hub bajo la organización `splunk/`:

| Nombre de Imagen | Tag de Configuración | Descripción | Caso de Uso |
|-----------------|---------------------|-------------|-------------|
| `splunk/mltk-container-golden-cpu` | `golden-cpu` | Golden Image CPU (completo) | Desarrollo y producción general |
| `splunk/mltk-container-golden-cpu-arm` | `golden-cpu-arm` | Golden Image CPU ARM64 | Apple Silicon (M1/M2/M3) |
| `splunk/mltk-container-golden-gpu` | `golden-gpu` | Golden Image GPU (NVIDIA) | Deep Learning acelerado |
| `splunk/mltk-container-minimal-cpu` | `minimal-cpu` | Imagen mínima CPU | Casos ligeros, solo librerías base |
| `splunk/mltk-container-golden-cpu-transformers` | `golden-cpu-transformers` | Transformers CPU | NLP/HuggingFace |
| `splunk/mltk-container-golden-gpu-transformers` | `golden-gpu-transformers` | Transformers GPU | NLP acelerado |
| `splunk/mltk-container-golden-gpu-rapids` | `golden-gpu-rapids` | Rapids GPU | Data Science acelerado |
| `splunk/mltk-container-ubi-llm-rag` | `ubi-llm-rag` | LLM RAG (Red Hat UBI) | LLM/RAG workloads |
| `splunk/mltk-container-escu-cpu` | `escu-cpu` | ESCU CPU | Threat detection |
| `splunk/mltk-container-spark` | `spark` | Spark CPU | Big Data processing |

#### Cómo Descargar una Imagen

Para descargar una imagen oficial, usa el comando `docker pull`:

```bash
# Ejemplo: Descargar Golden Image CPU
docker pull splunk/mltk-container-golden-cpu:5.2.2

# Ejemplo: Descargar Golden Image GPU
docker pull splunk/mltk-container-golden-gpu:5.2.2

# Ejemplo: Descargar Golden Image ARM64 (para Apple Silicon)
docker pull splunk/mltk-container-golden-cpu-arm:5.2.2
```

**Formato completo:**
```
docker pull <organizacion>/mltk-container-<tipo>:<version>
```

Donde:
- `<organizacion>` = `splunk` (para imágenes oficiales)
- `<tipo>` = `golden-cpu`, `golden-gpu`, `minimal-cpu`, etc.
- `<version>` = `5.2.2`, `5.2.1`, `latest`, etc.

#### Versiones Disponibles

Las versiones disponibles pueden variar. Para ver todas las versiones/tags disponibles:

1. **Desde Docker Hub web:**
   - Visita: https://hub.docker.com/r/splunk/mltk-container-golden-cpu/tags
   - Busca la organización y repositorio específico
   - Revisa la lista de tags/versiones

2. **Desde la línea de comandos:**
   ```bash
   # Listar tags disponibles (requiere herramientas adicionales)
   curl -s https://hub.docker.com/v2/repositories/splunk/mltk-container-golden-cpu/tags/ | grep -o '"name":"[^"]*"' | grep -o '[^"]*$'
   ```

#### Verificar Imágenes Instaladas Localmente

Para ver qué imágenes DSDL tienes instaladas localmente:

```bash
# Ver todas las imágenes de mltk-container
docker images | grep mltk-container

# Ver solo imágenes de splunk
docker images | grep splunk/mltk-container
```

#### Uso de Imágenes Oficiales en DSDL

Una vez descargada, la imagen oficial está disponible para usar en DSDL:

1. **Desde DSDL UI:**
   - Ve a: **DSDL → Configuration → Container Images**
   - Busca la imagen por su tag de configuración (ej: `golden-cpu`)
   - Haz clic en **"Start"** para iniciar el contenedor

2. **Desde SPL (Search Processing Language):**
   ```spl
   index=mis_datos
   | fit MLTKContainer algo=mi_modelo container_image="golden-cpu" into app:mi_modelo
   ```

#### Notas Importantes

- **Imágenes oficiales**: Las imágenes bajo `splunk/` son mantenidas oficialmente por Splunk
- **Versiones**: Usa siempre versiones específicas (ej: `:5.2.2`) en producción, no `latest`
- **Arquitectura**: Verifica que la imagen sea compatible con tu arquitectura (AMD64, ARM64)
- **Actualizaciones**: Las imágenes oficiales se actualizan periódicamente con parches de seguridad
- **Tamaño**: Las imágenes pueden ser grandes (3-7GB), asegúrate de tener suficiente espacio en disco

#### Referencias

- **Repositorio GitHub oficial**: https://github.com/splunk/mltk-container-docker
- **Documentación DSDL**: https://docs.splunk.com/Documentation/DSDL
- **Docker Hub - Organización Splunk**: https://hub.docker.com/u/splunk

---

