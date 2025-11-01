# Solución: Puerto 5000 en Uso

**Fecha**: 2025-01-31  
**Problema**: `bind: address already in use` al iniciar contenedor DSDL

---

## 🔍 Problema Identificado

```
Error: ports are not available: exposing port TCP 0.0.0.0:5000 -> 127.0.0.1:0: 
listen tcp 0.0.0.0:5000: bind: address already in use
```

**Proceso que usa puerto 5000**: `ControlCenter` (AirPlay Receiver de macOS)

**PID**: 1118

---

## ✅ Solución Aplicada

### Opción 1: Desactivar AirPlay Receiver (Temporal)

```bash
# Detener proceso ControlCenter
killall ControlCenter

# Verificar puerto liberado
lsof -i :5000
```

**Nota**: Este proceso se reinicia automáticamente con el sistema.

### Opción 2: Desactivar AirPlay Permanente (Recomendado)

**Desde macOS**:
1. Apple Menu → **System Settings** (o System Preferences en macOS antiguo)
2. Navegar a **General** → **AirDrop & Handoff**
3. Desactivar **"AirPlay Receiver"**

O desde terminal:
```bash
# Desactivar AirPlay Receiver
defaults write com.apple.controlcenter.plist AirplayRecieverEnabled -bool false

# Reiniciar ControlCenter
killall ControlCenter
```

---

## 🔄 Alternativa: Cambiar Puerto DSDL

Si prefieres mantener AirPlay activo, puedes cambiar el puerto de DSDL:

### Modificar Configuración Docker

**Archivo**: Configurar en DSDL UI

En **DSDL → Configuration → Setup → Docker Settings**:

Cambiar **"Endpoint URL"** y **"External URL"** a puerto diferente:
- Opciones: 5001, 5002, 8080, 9090

**Nota**: Requiere reiniciar Splunk y reconfigurar DSDL.

---

## 📊 Verificación

### Paso 1: Verificar Puerto Libre

```bash
# Ver qué usa puerto 5000
lsof -i :5000

# Si está vacío, está listo
```

### Paso 2: Intentar Iniciar Contenedor

1. Ir a DSDL → Containers
2. Click **"START"**
3. Esperar 30-60 segundos
4. Ver **Active: 1**

### Paso 3: Verificar Contenedor

```bash
# Ver contenedor corriendo
docker ps | grep mltk-container

# Deberías ver:
# CONTAINER ID   IMAGE                                      STATUS         PORTS
# abc123def456   splunk/mltk-container-golden-cpu:5.2.2   Up 30 seconds  0.0.0.0:5000->5000/tcp, ...
```

---

## 🔒 Prevención Futura

### Desactivar AirPlay Permanentemente

```bash
# Comando one-liner
defaults write com.apple.controlcenter.plist AirplayRecieverEnabled -bool false && killall ControlCenter

# Verificar que quedó desactivado
defaults read com.apple.controlcenter.plist AirplayRecieverEnabled
# Debería mostrar: 0 (desactivado)
```

### Script de Verificación

```bash
#!/bin/bash
# verificar_puerto_5000.sh

echo "Verificando puerto 5000..."

if lsof -i :5000 | grep -q "ControlCenter"; then
    echo "⚠️  AirPlay Receiver usando puerto 5000"
    echo "Ejecutar: defaults write com.apple.controlcenter.plist AirplayRecieverEnabled -bool false && killall ControlCenter"
    exit 1
else
    echo "✅ Puerto 5000 disponible"
    exit 0
fi
```

---

## 📝 Notas Importantes

### macOS y Puerto 5000

- **macOS 12+**: AirPlay Receiver usa puerto 5000 por defecto
- **Conflicto**: Muchas apps de desarrollo usan puerto 5000
- **Solución**: Desactivar AirPlay si no se usa (recomendado)

### DSDL y Puertos

- **Puerto 5000**: API interna de DSDL
- **Puerto 8888**: JupyterLab (o dinámico)
- **Puerto 8089**: Splunk REST API
- **Puerto 9000**: Splunk Web UI

---

## 🔗 Referencias

- **Documentación DSDL**: Ver `DSDL-docs.md`
- **Puertos requeridos**: Ver `GUIA_INSTALACION_SANDBOX_LOCAL.md`
- **Validación**: Ver `VALIDACION_DSDL.md`

---

**Después de aplicar solución**: Intentar de nuevo iniciar contenedor DEV.

