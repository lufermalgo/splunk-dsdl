# Cómo Lanzar un Contenedor DEV en DSDL

**Fecha**: 2025-01-31  
**Objetivo**: Guía paso a paso para iniciar tu primer contenedor

---

## 📋 Entendiendo las Imágenes

### ¿Las imágenes existen?

**Sí**, todas las imágenes existen:

1. ✅ **Ya descargadas**: `golden-cpu` (7.42 GB) está en tu Docker local
2. 🌐 **En Docker Hub**: Las demás se descargan automáticamente al iniciar
3. 📝 **Configuradas**: DSDL conoce las URLs y las descarga cuando sea necesario

### Lista de Imágenes Disponibles

| Imagen | Estado en tu Mac | Tamaño Aprox |
|--------|------------------|--------------|
| **Golden Image CPU (5.2.2)** | ✅ Descargada | 7.42 GB |
| Golden Image ARM64 (5.2.2) | ⏳ En Docker Hub | ~7 GB |
| Golden Image GPU (5.2.2) | ⏳ En Docker Hub | ~15 GB |
| Transformers CPU (5.2.2) | ⏳ En Docker Hub | ~8 GB |
| Transformers GPU (5.2.2) | ⏳ En Docker Hub | ~16 GB |
| Rapids 24.08 (5.2.2) | ⏳ En Docker Hub | ~18 GB |
| ESCU (5.2.2) | ⏳ En Docker Hub | ~7 GB |
| Spark 3.5.1 (5.2.2) | ⏳ En Docker Hub | ~9 GB |
| Agentic AI (5.2.2) | ⏳ En Docker Hub | ~10 GB |
| Red Hat LLM RAG CPU (5.2.2) | ⏳ En Docker Hub | ~11 GB |

---

## 🚀 Paso a Paso: Lanzar Contenedor

### Paso 1: Seleccionar Imagen

En la interfaz **DSDL → Containers**:

1. Ver sección **"Development Container"**
2. Dropdown **"Container Image"**: Seleccionar **"Golden Image CPU (5.2.2)"**
3. Dropdown **"GPU runtime"**: `none` (ya seleccionado - correcto)
4. Dropdown **"Cluster target"**: `docker` (ya seleccionado - correcto)

### Paso 2: Buscar Botón "Start"

El botón **"Start"** o **"Start Development Container"** debería estar:

- **Opción A**: Debajo de los dropdowns
- **Opción B**: Como botón grande azul/verde en la parte superior
- **Opción C**: En la parte inferior de la sección "Development Container"

**Si no lo ves**:
- Recarga la página (F5)
- Verifica que no haya errores en la consola del navegador
- Asegúrate de estar en la pestaña **"Containers"**

### Paso 3: Click en "Start"

1. Click en **"Start"** o **"Start Development Container"**
2. Aparecerá indicador de carga (spinner)
3. **Esperar 30-60 segundos** mientras se inicia el contenedor

### Paso 4: Ver Contenedor Activo

Una vez iniciado, verás:

- Número en **"Active"**: cambia de `0` a `1`
- Sección **"Status of all Container Models"**: muestra el contenedor
- Opciones para el contenedor:
  - **"Open JupyterLab"** 🔗
  - **"View Logs"** 📋
  - **"Stop"** ⏹️

### Paso 5: Verificar desde Terminal

```bash
# Ver contenedor activo
docker ps | grep mltk-container

# Deberías ver algo como:
# CONTAINER ID   IMAGE                                      COMMAND                  STATUS
# abc123def456   splunk/mltk-container-golden-cpu:5.2.2   "python app.py"         Up 30 seconds
```

---

## 🔍 Si No Encuentras el Botón Start

### Troubleshooting

1. **Verificar permisos**:
   ```bash
   # Verificar que DSDL tenga permisos
   curl -k -u admin:'Splunk2025.' "https://localhost:8089/servicesNS/admin/mltk-container/services/mltk_container_status" | head -50
   ```

2. **Ver logs de DSDL**:
   ```bash
   # En Splunk: Search
   index=_internal app=mltk-container ERROR
   ```

3. **Recargar página**:
   - Press `F5` o `Cmd+R`
   - Limpiar cache del navegador

4. **Verificar JavaScript**:
   - Abrir consola del navegador (F12)
   - Ver si hay errores rojos

---

## 📸 Ubicaciones Probables del Botón

Según la documentación, el botón debería estar en:

### Opción 1: Botón Prominente
```
┌─────────────────────────────────────┐
│  DSDL - Containers                  │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━│
│                                     │
│  Overview of all Container Models   │
│                                     │
│  Development Container              │
│  Container Image: [Dropdown ▼]     │
│  GPU runtime: [Dropdown ▼]         │
│  Cluster target: [Dropdown ▼]      │
│                                     │
│  [    START DEVELOPMENT CONTAINER  ]  ← AQUÍ
│                                     │
│  Status of all Container Models    │
│  Active: 0                          │
│  Inactive: 0                        │
└─────────────────────────────────────┘
```

### Opción 2: Botón Pequeño
```
┌─────────────────────────────────────┐
│  Development Container              │
│  ─────────────────────────────────  │
│  Container Image: [Golden CPU ▼]   │
│  GPU runtime: [none ▼]             │
│  Cluster target: [docker ▼]        │
│                                     │
│  [Start]  [Edit]  [Export]  ⚙️     ← Opciones aquí
└─────────────────────────────────────┘
```

---

## 🎯 Qué Esperar

### Primera Ejecución

- **Descarga**: Si la imagen no existe, Docker la descargará (demora varios minutos)
- **Inicio**: El contenedor tarda 30-60 segundos en iniciar
- **Puertos**: JupyterLab en puerto dinámico (ej: 8888, 8889, etc.)

### Errores Comunes

| Error | Causa | Solución |
|-------|-------|----------|
| "Cannot connect to Docker" | Docker no corriendo | `open -a Docker` |
| "Port already in use" | Puerto ocupado | Ver `lsof -i :5000` |
| "Failed to pull image" | Imagen no encontrada | Ya descargaste golden-cpu ✅ |
| Timeout | Lento inicio | Esperar más tiempo |

---

## ✅ Siguiente Paso Después de Iniciar

Una vez que veas **Active: 1**, podrás:

1. **Click en "Open JupyterLab"** → Abre interfaz de notebooks
2. **Ir a Examples** en DSDL → Ejecutar ejemplos predefinidos
3. **Crear tu propio notebook** → Adaptar notebooks de Cristian

---

## 📚 Referencias

- **Documentación oficial**: Ver `DSDL-docs.md` líneas 2191-2218
- **Validación**: Ver `VALIDACION_DSDL.md`
- **Configuración**: Ver `CONFIGURACION_DSDL.md`

---

**Si aún no encuentras el botón Start, prueba**:
1. Scroll hacia abajo en la página
2. Buscar en la barra superior derecha
3. Intentar desde otra pestaña (Overview, etc.)

