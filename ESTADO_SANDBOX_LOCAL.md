# Estado del Sandbox Local - Splunk DSDL

**Fecha Validación**: 2025-01-31  
**Responsable**: Luis Fernando Maldonado

---

## ✅ Prerrequisitos Validados

### Infraestructura Base

| Componente | Estado | Detalles |
|------------|--------|----------|
| **Splunk Enterprise** | ✅ Corriendo | Puerto admin 8089 activo |
| **Docker Desktop** | ✅ Instalado | Versión 28.5.1, daemon activo |
| **Python** | ✅ Disponible | Versión 3.13.4 |

### Apps de Splunk Instaladas

| App | Estado | Detalles |
|-----|--------|----------|
| **MLTK (Machine Learning Toolkit)** | ✅ Instalada | Versión 5.6.3 - AI Toolkit |
| **PSC (Python for Scientific Computing)** | ✅ Instalada | Splunk_SA_Scientific_Python_linux_x86_64 |
| **DSDL (Data Science and Deep Learning)** | ✅ Instalada | mltk-container v5.2.2 |

### Docker Images

| Imagen | Estado | Tamaño | Origen |
|--------|--------|--------|--------|
| **golden-cpu** | ✅ Descargada | 7.42 GB | Docker Hub: splunk/mltk-container-golden-cpu:5.2.2 |

---

## ✅ Estado Actual del Sandbox

**Última actualización**: 2025-01-31

### Componentes Validados

| Componente | Estado | Version/Detalles |
|------------|--------|------------------|
| Splunk Enterprise | ✅ | 9.4.1 (build e3bdab203ac8) |
| Docker Desktop | ✅ | 28.5.1 |
| Python | ✅ | 3.13.4 |
| Credenciales | ✅ | admin/Splunk2025. |
| App MLTK | ✅ | 5.6.3 instalada |
| Add-on PSC | ✅ | Instalado |
| App DSDL | ✅ | 5.2.2 instalada |
| Golden Image CPU | ✅ | 5.2.2 descargada |

### Puerto web
El puerto web de Splunk está accesible en `http://localhost:9000`.

---

## 🎯 Plan de Acción Inmediato

### Paso 1: ✅ COMPLETADO - Validar Credenciales de Splunk

**Acción**: Acceder manualmente a Splunk Web

```bash
# Abrir en navegador
open http://localhost:9000

# O desde terminal
curl -s http://localhost:9000/en-US/
```

**Validar**:
- Usuario: `admin`
- Password: `Splunk2025.` (Es correcto)

### Paso 2: ✅ COMPLETADO - Descargar Apps desde Splunkbase

**Requisito**: Cuenta de Splunkbase (https://splunkbase.splunk.com, gratuita si no la tienes)

| App | URL | Acción |
|-----|-----|--------|
| MLTK | https://splunkbase.splunk.com/app/2890/ | Download .spl |
| PSC | https://splunkbase.splunk.com/app/2889/ | Download .spl |
| DSDL | https://splunkbase.splunk.com/app/4607/ | Download .spl |

**Ubicación de descarga recomendada**: `~/Downloads/`

### Paso 3: ✅ COMPLETADO - Instalar Apps en Splunk

**Opción A: Via Splunk Web (Recomendado)**  
1. Abrir: http://localhost:9000
2. Login con credenciales
3. **Settings** → **Apps** (o menú Apps en barra lateral)
4. Click **"Install app from file"**
5. Seleccionar archivo `.spl` descargado
6. Click **Upload**
7. Esperar instalación
8. Reiniciar Splunk: `/Applications/Splunk/bin/splunk restart`

**Opción B: Via CLI**  
```bash
# Copiar archivo .spl a directorio de apps
cp ~/Downloads/*.spl /Applications/Splunk/etc/apps/

# Reiniciar Splunk
/Applications/Splunk/bin/splunk restart

# Verificar instalación
ls -la /Applications/Splunk/etc/apps/ | grep -E "MLTK|python|dsdl"
```

### Paso 4: ⚠️ PENDIENTE - Configurar Permisos MLTK

**Importante**: Debe ser Global

1. Splunk Web: **Settings** → **Apps** → **Machine Learning Toolkit**
2. Click **"Permissions"**
3. Seleccionar **"Global"**
4. Guardar

### Paso 5: ✅ COMPLETADO - Descargar Golden Image

```bash
# Pull imagen CPU desde Docker Hub
docker pull splunk/mltk-container-golden-cpu:5.2.2

# Verificar
docker images | grep mltk-container

# Esperado: ~5-10 GB descargado
```

### Paso 6: Configurar DSDL

1. Abrir app **DSDL** en Splunk Web
2. **Configuration** → **Setup**
3. Configurar Docker:
   - Docker Host: `unix:///var/run/docker.sock`
   - Image Tag: `splunk/mltk-container-golden-image-cpu:latest`
   - Mode: `DEV`
4. Click **Test & Save**

### Paso 7: Validar End-to-End

1. En DSDL: **Containers** → **Start Development Container**
2. Esperar inicio
3. Click **"Open JupyterLab"**
4. Navegar a **Examples** y ejecutar ejemplo de prueba

---

## 📊 Comandos de Validación Continua

### Verificar Splunk
```bash
# Estado de procesos
ps aux | grep splunk | grep -v grep

# Puerto web
curl -s http://localhost:9000 | grep -q Splunk && echo "OK" || echo "ERROR"

# Puerto admin
nc -z localhost 8089 && echo "OK" || echo "ERROR"
```

### Verificar Docker
```bash
# Docker corriendo
docker ps

# Imágenes descargadas
docker images | grep mltk

# Espacio utilizado
docker system df
```

### Verificar Apps
```bash
# Apps instaladas
ls -la /Applications/Splunk/etc/apps/ | grep -E "MLTK|python|dsdl"

# Permisos MLTK
cat /Applications/Splunk/etc/apps/Splunk_ML_Toolkit/app.conf | grep -i sharing
```

### Verificar Contenedores
```bash
# Contenedores activos
docker ps | grep mltk-container

# Logs de contenedor
docker logs <container-id> | tail -50
```

---

## 🚨 Troubleshooting Rápido

### Splunk no responde en puerto 9000

**Causa**: Proceso web no iniciado o puerto cambiado

**Solución**:
```bash
# Ver puerto real
netstat -an | grep LISTEN | grep 9000

# Ver logs
tail -f /Applications/Splunk/var/log/splunk/splunkd.log
```

### Docker error "Cannot connect"

**Solución**:
```bash
# Reiniciar Docker Desktop
open -a Docker

# Esperar inicio
while ! docker ps >/dev/null 2>&1; do sleep 1; done
```

### App no aparece en Splunk Web

**Causa**: Instalación fallida o permisos incorrectos

**Solución**:
```bash
# Ver logs de instalación
tail -f /Applications/Splunk/var/log/splunk/splunkd.log

# Verificar permisos
ls -la /Applications/Splunk/etc/apps/

# Forzar restart
/Applications/Splunk/bin/splunk restart
```

---

## 📝 Notas

- **Credenciales Splunk**: Confirmar que `admin/Splunk2025.` es correcto
- **Espacio en disco**: Golden Image requiere ~5-10 GB
- **Tiempo estimado**: 30-60 minutos para instalación completa
- **Primera prueba**: Usar ejemplo predefinido de DSDL antes de cargar notebooks de Cristian

---

## 🔗 Referencias

- **Guía completa**: `GUIA_INSTALACION_SANDBOX_LOCAL.md`
- **Análisis técnico**: `ANALISIS_COMPARATIVO_DSDL.md`
- **Documentación DSDL**: `DSDL-docs.md`
- **Splunkbase**: https://splunkbase.splunk.com

---

**Próxima Actualización**: Después de validar Paso 1 (credenciales Splunk)

