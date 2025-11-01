# Validación DSDL - Sandbox Local

**Fecha**: 2025-01-31  
**Status**: Configuración completada ✅

---

## ✅ Validación Completada

### Setup Inicial

| Componente | Estado | Detalle |
|------------|--------|---------|
| Prerrequisitos | ✅ | Splunk 9.4.1, Docker 28.5.1, Python 3.13.4 |
| Credenciales | ✅ | admin/Splunk2025. |
| App MLTK | ✅ | 5.6.3 instalada |
| Add-on PSC | ✅ | Instalado |
| App DSDL | ✅ | 5.2.2 instalada |
| Golden Image | ✅ | splunk/mltk-container-golden-cpu:5.2.2 |
| Docker Settings | ✅ | Configured |
| Certificate Settings | ✅ | Self-signed OK |

### Errores Resueltos

| Error | Causa | Solución |
|-------|-------|----------|
| Setup Failed | OpenSSL 1.0.2 incompatibility | CRYPTOGRAPHY_ALLOW_OPENSSL_102=1 |

---

## 🚀 Próximos Pasos

### 1. Lanzar Contenedor DEV

**Desde Splunk Web**:
1. Navegar a **DSDL** → **Containers**
2. Click **"Start Development Container"**
3. Seleccionar imagen: `golden-cpu` (Golden Image CPU 5.2.2)
4. Esperar inicio: 30-60 segundos

**Verificar desde terminal**:
```bash
docker ps | grep mltk-container
```

### 2. Acceder a JupyterLab

1. En DSDL: **Containers** → Ver contenedor activo
2. Click **"Open JupyterLab"**
3. Se abre navegador en puerto `8888` (o dinámico)
4. Login con password configurada

### 3. Ejecutar Ejemplo Predefinido

1. En DSDL: **Examples**
2. Seleccionar: **"Neural Network Classifier Example for Tensorflow"**
3. Click **"Run"**
4. Verificar ejecución sin errores

---

## 📊 Comandos de Validación

### Verificar Contenedores

```bash
# Contenedores activos
docker ps | grep mltk-container

# Logs de contenedor
docker logs <container-id> | tail -50

# Estado de espacio
docker system df
```

### Verificar Splunk

```bash
# Estado de Splunk
/Applications/Splunk/bin/splunk status

# Verificar variable OpenSSL
grep CRYPTOGRAPHY /Applications/Splunk/etc/splunk-launch.conf

# Logs de DSDL
index=_internal app=mltk-container ERROR
```

---

## 🔍 Troubleshooting

### Contenedor no inicia

**Verificar**:
1. Docker corriendo: `docker ps`
2. Imagen descargada: `docker images | grep mltk`
3. Puerto disponible: `lsof -i :5000`
4. Logs en Splunk: `index=_internal "mltk-container" ERROR`

**Solución**:
```bash
# Ver logs detallados
docker logs <container-id>

# Restart Docker Desktop
open -a Docker

# Reiniciar contenedor desde DSDL UI
```

### JupyterLab no accesible

**Verificar**:
1. Container status: `docker ps | grep mltk`
2. Puerto externo: Ver en DSDL UI
3. Firewall: macOS puede bloquear puerto

**Solución**:
```bash
# Ver puerto asignado
docker port <container-id>

# Probar conectividad
curl http://localhost:8888
```

### Errores en ejemplos

**Verificar**:
1. Permisos MLTK Global: Settings → Apps → MLTK → Permissions
2. Datos disponibles: Verificar índices
3. Logs: `index=_internal "mltk-container"` 

---

## 📝 Notas de Configuración

### Docker Settings Usados

```
Docker Host:      unix:///var/run/docker.sock
Endpoint URL:     localhost
External URL:     localhost
Docker network:   [vacío]
API Workers:      1
```

### Certificate Settings Usados

```
Check Hostname:                 Disabled
Certificate path:               [vacío]
Enable container certificates:  Yes
Enable KEEPALIVE:               No
```

### Variables de Entorno Configuradas

**Archivo**: `/Applications/Splunk/etc/splunk-launch.conf`

```
PYTHONHTTPSVERIFY=0
PYTHONUTF8=1
CRYPTOGRAPHY_ALLOW_OPENSSL_102=1
```

---

## ✅ Checklist Final

- [x] Splunk Enterprise 9.4.1 corriendo
- [x] Apps MLTK, PSC, DSDL instaladas
- [x] Golden Image descargada
- [x] Error OpenSSL resuelto
- [x] DSDL configuración completada
- [ ] Contenedor DEV iniciado
- [ ] JupyterLab accesible
- [ ] Ejemplo predefinido ejecutado
- [ ] Datos de prueba cargados
- [ ] Notebook de Cristian adaptado

---

## 📚 Referencias

- **Guía instalación**: `GUIA_INSTALACION_SANDBOX_LOCAL.md`
- **Configuración**: `CONFIGURACION_DSDL.md`
- **Quick ref**: `CONFIG_RAPIDA_DSDL.md`
- **Análisis**: `ANALISIS_COMPARATIVO_DSDL.md`
- **Estado**: `ESTADO_SANDBOX_LOCAL.md`
- **OpenSSL fix**: `SOLUCION_OPENSSL_ERROR.md`

---

**Próxima actualización**: Después de validar JupyterLab y ejecutar primer ejemplo.

