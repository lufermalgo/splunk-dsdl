# Nombres "Random" de Contenedores Docker

**Fecha**: 2025-11-01  
**Objetivo**: Explicar por qué los contenedores tienen nombres aleatorios como `flamboyant_wilson`

---

## 🤔 Tu Observación

Al abrir **Docker Desktop**, ves contenedores con nombres como:

- `flamboyant_wilson`
- `vigorous_jennings`  
- `unruffled_curie`
- `sharp_carver`

**Pregunta**: ¿Por qué estos nombres tan "random"?

---

## ✅ Respuesta

### Es el Comportamiento Normal de Docker

Cuando Docker crea un contenedor **sin especificar un nombre explícito**, genera automáticamente un nombre aleatorio usando el formato:

```
<adjetivo>_<nombre_científico>
```

Ejemplos reales de Docker:
- `flamboyant_wilson` - Sir Thomas Wilson (escritor inglés)
- `vigorous_jennings` - Howard Jennings (aventurero)
- `unruffled_curie` - Marie Curie (científica)
- `sharp_carver` - George Washington Carver (botánico)

---

## 🔍 ¿Cómo Determina DSDL los Nombres?

### Opción A: Sin Nombre Explícito (Actual)

DSDL llama a la Docker API SIN especificar un nombre:

```python
# DSDL internamente hace algo como:
docker.run(image="splunk/mltk-container-golden-cpu-empresa-arm:5.2.2")
# Sin el parámetro --name, Docker genera uno random
```

**Resultado**: Nombres aleatorios como `flamboyant_wilson`

### Opción B: Nombre Explícito (No disponible en DSDL actualmente)

Si DSDL permitiera especificar nombres, sería:

```python
docker.run(
    image="splunk/mltk-container-golden-cpu-empresa-arm:5.2.2",
    name="dsdl-cristian-modelo-corona"  # ← No existe en DSDL
)
```

---

## 🔍 Verificación

### Inspeccionar Contenedor Actual

```bash
# Ver info del contenedor
docker inspect flamboyant_wilson | grep Name

# Resultado:
# "Name": "/flamboyant_wilson"
```

### Cómo DSDL Lanza Contenedores

Según la documentación:

> "DSDL starts and stops the container through the Docker API. Development containers might keep running until manually stopped."

DSDL usa la Docker API directamente desde Splunk, y no especifica nombres custom.

---

## ⚠️ ¿Es un Problema?

**NO**, es completamente normal:

### ✅ Ventajas de Nombres Aleatorios

1. **Sin conflictos**: Imposible que dos contenedores tengan el mismo nombre
2. **Automático**: No requiere gestión manual de nombres
3. **Funcional**: Los contenedores funcionan igual independientemente del nombre
4. **Tracking**: Puedes ver contenedores en DSDL UI por otro identificador

### ⚠️ Desventajas

1. **Difícil recordar**: "¿Cuál era el contenedor de Cristian?"
2. **Confuso en Docker Desktop**: Muchos nombres aleatorios juntos

---

## 🔍 Cómo Identificar Tu Contenedor

### Opción 1: Por Imagen

```bash
# Ver todos los contenedores con tu imagen custom
docker ps --filter "ancestor=splunk/mltk-container-golden-cpu-empresa-arm:5.2.2"

# Resultado:
# CONTAINER ID   IMAGE                                                 NAMES
# 1d0fa7980bbf   mltk-container-golden-cpu-empresa-arm:5.2.2    flamboyant_wilson
```

### Opción 2: Por Puerto

```bash
# Tu contenedor expone JupyterLab en puerto 8888
docker ps --filter "publish=8888"

# Ver puertos completos
docker ps --format "table {{.Names}}\t{{.Ports}}"
```

### Opción 3: Por Volumen Montado

```bash
# Tu contenedor monta el volumen mltk-container-data
docker ps --filter "volume=mltk-container-data"

# Ver mounts completos
docker inspect flamboyant_wilson | grep -A 5 '"Mounts"'
```

### Opción 4: Desde DSDL UI

En Splunk Web → **DSDL → Configuration → Containers**:

- Muestra estado de contenedores activos
- Botones para Stop/Start
- **NO muestra el nombre Docker**, pero muestra el estado

---

## 🛠️ Soluciones

### Solución 1: Renombrar Manualmente (Después de Crear)

```bash
# Renombrar un contenedor existente
docker rename flamboyant_wilson dsdl-empresa-main

# Ver nuevo nombre
docker ps
```

**Limitación**: Si detienes y vuelves a iniciar desde DSDL, volverá a tener nombre random.

### Solución 2: Usar Labels Personalizados

DSDL podría configurarse para usar Docker labels (no disponible actualmente).

### Solución 3: Trabajar con Container ID

```bash
# Usar ID corto en vez de nombre
docker exec 1d0fa7980bbf ls /srv

# O ID largo
docker exec 1d0fa7980bbf60861a29dd7e82cbc6c3cfa884a4a1c0d6f4a7e5d6e3b3f0e8 ls /srv
```

---

## 📊 Estado Actual

### En tu Setup

```bash
# Tu contenedor actual
docker ps | grep empresa-arm

# Resultado:
# 1d0fa7980bbf   splunk/mltk-container-golden-cpu-empresa-arm:5.2.2   \
#   "/dltk/bootstrap_fas…"   About an hour ago   Up About an hour   \
#   0.0.0.0:4040->4040/tcp, ... 0.0.0.0:8888->8888/tcp, ... \
#   flamboyant_wilson    ← Nombre random
```

### Verificación en DSDL

1. Ir a Splunk Web → DSDL → Containers
2. Deberías ver tu contenedor listado
3. El nombre mostrado NO es el de Docker, es un ID interno de DSDL

---

## 🎯 Recomendación

### Para Desarrollo Local

✅ **Usar nombres aleatorios está bien**:
- El contenedor funciona igual
- La persistencia NO depende del nombre
- Solo es un tema cosmético

Si te molesta, puedes renombrar manualmente:

```bash
docker rename flamboyant_wilson dsdl-main
```

### Para Producción

En producción con Kubernetes/OpenShift:
- Los nombres son gestionados por el orchestrator
- Pods tienen nombres como `dsdl-dev-abc123def`
- No afecta funcionalidad

---

## 📚 Referencias

- **Docker Naming**: https://docs.docker.com/engine/reference/run/#name---name
- **Docker Names Format**: Adjective + Scientist name
- **DSDL Container Lifecycle**: Ver `DSDL-docs.md` sección "Container lifecycle"

---

## ✅ Conclusión

**¿Por qué nombres aleatorios?**

✅ **Es el comportamiento normal de Docker** cuando no especificas `--name`

✅ **DSDL no configura nombres custom** (por diseño o limitación)

✅ **NO es un problema**, solo cosmético

✅ **Todo funciona igual** independientemente del nombre

**Tu contenedor `flamboyant_wilson` es completamente funcional y persistente** ✅

