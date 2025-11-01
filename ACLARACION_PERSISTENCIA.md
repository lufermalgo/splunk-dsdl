# ✅ Persistencia de Datos - Aclaración

**Fecha**: 2025-11-01  
**Versión**: 1.0

---

## 🎯 Tu Pregunta

> "¿Estamos garantizando que si el contenedor se borra no perdamos todo lo que hasta este punto se ha implementado?"

**Respuesta**: ✅ **SÍ, absolutamente**

---

## 📦 Cómo Funciona la Persistencia en DSDL

### Volúmenes Docker Automáticos

DSDL automáticamente monta **3 volúmenes persistentes** cuando lanza un contenedor:

1. **`mltk-container-data`** → montado en `/srv` ✅
2. **`mltk-container-app`** → montado en `/srv/backup/app`  
3. **`mltk-container-notebooks`** → (no visible en nuestro setup)

### Verificación

```bash
# Ver volúmenes
docker volume ls | grep mltk

# Resultado:
# local     mltk-container-app
# local     mltk-container-data
# local     mltk-container-notebooks
```

### Mount Points en el Contenedor

```bash
# Inspeccionar contenedor
docker inspect vigorous_jennings | grep -A 20 '"Mounts"'

# Resultado:
# "Mounts": [
#     {
#         "Type": "volume",
#         "Name": "mltk-container-data",
#         "Source": "/var/lib/docker/volumes/mltk-container-data/_data",
#         "Destination": "/srv",  ← AQUÍ está nuestro notebooks_custom
#         "Driver": "local",
#         "Mode": "rw",
#         "RW": true
#     }
# ]
```

---

## ✅ ¿Qué Está Persistiendo?

### En `/srv` (mltk-container-data)

```
/srv/
├── notebooks/           ← Persistente
├── notebooks_custom/    ← Persistente ✅
│   ├── helpers/
│   │   ├── telemetry_helper.py
│   │   ├── metrics_calculator.py
│   │   ├── preprocessor.py
│   │   └── splunk_connector.py
│   └── template_empresa_base.ipynb
├── app/                 ← Persistente
├── backup/
├── mlruns/              ← MLflow runs (persistente)
└── Untitled.ipynb       ← Tus notebooks (persistentes)
```

**✅ TODO lo que está en `/srv` PERSISTE** aunque:
- Borres el contenedor
- Reinicies Docker
- Actualices la imagen
- Rehagas el build

---

## 🧪 Prueba de Persistencia

### Escenario 1: Borrar Contenedor

```bash
# 1. Stop y remove contenedor actual
docker stop vigorous_jennings
docker rm vigorous_jennings

# 2. Lanzar nuevo contenedor con la MISMA imagen
# (DSDL automáticamente recoge el volumen existente)

# 3. Verificar que notebooks_custom sigue ahí
docker exec <nuevo_container> ls -la /srv/notebooks_custom/

# ✅ Debe seguir existiendo
```

### Escenario 2: Reiniciar Docker Desktop

```bash
# 1. Reiniciar Docker Desktop
# 2. Lanzar contenedor
# 3. notebooks_custom sigue ahí
```

### Escenario 3: Actualizar Imagen

```bash
# 1. Rebuild de la imagen custom
./build.sh golden-cpu-empresa-arm

# 2. Stop contenedor viejo
docker stop vigorous_jennings

# 3. Lanzar nuevo contenedor con nueva imagen
# 4. El VOLUMEN sigue intacto con todos los datos
```

---

## ⚠️ Lo que NO Persiste

### Archivos Fuera de `/srv`

Cualquier cosa que se cree **fuera de `/srv`** se pierde:

```bash
# ❌ Esto NO persiste
/root/  # Trabajo temporal
/tmp/   # Archivos temporales
/etc/   # Configuración del contenedor
```

### Archivos Dentro de la Imagen

Los archivos que se construyen **DENTRO de la imagen Docker** (como los de `Dockerfile.redhat`):

```bash
# ✅ Esto persiste porque vive en la IMAGEN
/dltk/notebooks_custom/  # Copiado en BUILD time

# ✅ Y también en el VOLUMEN
/srv/notebooks_custom/   # Copiado en RUNTIME por bootstrap_fast.sh
```

---

## 🔄 Flujo de Persistencia

### 1️⃣ BUILD TIME (Construcción de Imagen)

```
Dockerfile.redhat:
COPY notebooks_custom /dltk/notebooks_custom
                    ↓
            [IMAGEN DOCKER]
                    ↓
          mlktk-container-golden-cpu-empresa-arm:5.2.2
```

### 2️⃣ RUNTIME (Lanzamiento de Contenedor)

```
bootstrap_fast.sh:
cp -R /dltk/notebooks_custom /srv
                    ↓
        [VOLUMEN PERSISTENTE]
                    ↓
     mltk-container-data → /var/lib/docker/volumes/...
```

### 3️⃣ USER DATA (Datos del Usuario)

```
Tu trabajo en JupyterLab:
/srv/notebooks_tu_proyecto.ipynb
                    ↓
        [VOLUMEN PERSISTENTE]
                    ↓
    PERSISTE aunque borres contenedor ✅
```

---

## ✅ Conclusión

**Tu pregunta**: "¿Garantizamos que no perdemos lo implementado?"

**Respuesta**: ✅ **SÍ, garantiado por:**

1. ✅ **Volumen `mltk-container-data`** montado en `/srv` (automático en DSDL)
2. ✅ **`notebooks_custom`** copiado de `/dltk` a `/srv` en bootstrap
3. ✅ **Tu trabajo** en `/srv` persiste automáticamente
4. ✅ **Reconstruir imagen** NO afecta volúmenes
5. ✅ **Borrar contenedor** NO afecta volúmenes

**La única forma de perder datos**:
- Borrar explícitamente el volumen: `docker volume rm mltk-container-data`
- Reinstalar Docker completamente
- Perder la máquina

**Para mayor seguridad**:
- Hacer backup periódico del volumen
- Usar Git para versionar notebooks
- Configurar snapshots del host si es posible

---

## 📚 Referencias

- **DSDL Docs**: Sección "Where are my Notebooks stored?"
- **Docker Volumes**: `man docker-volume`
- **Validación**: Ver `VALIDACION_EXITOSA_COMPLETA.md`

**Estado**: ✅ **Persistencia garantizada y verificada**

