# Instrucciones: Desactivar AirPlay Receiver en macOS

**Problema**: Puerto 5000 ocupado por AirPlay Receiver  
**Solución**: Desactivar desde System Settings

---

## 🎯 Pasos Manuales

### Opción 1: Desde System Settings (macOS 13+)

1. **Abrir System Settings**:
   - Apple Menu (🍎) → **System Settings**
   - O usar Spotlight: `Cmd + Space` → escribir "System Settings"

2. **Navegar a AirDrop & Handoff**:
   - Click en **"General"** (en barra lateral izquierda)
   - Click en **"AirDrop & Handoff"**

3. **Desactivar AirPlay Receiver**:
   - Buscar toggle **"AirPlay Receiver"**
   - Cambiar a **OFF** (gris)

4. **Verificar**:
   ```bash
   lsof -i :5000
   # No debería mostrar ControlCenter
   ```

### Opción 2: Desde System Preferences (macOS anterior a 13)

1. **Abrir System Preferences**:
   - Apple Menu → **System Preferences**

2. **Ir a Sharing**:
   - Click en **"Sharing"**

3. **Desactivar AirPlay Receiver**:
   - Marca el checkbox **"AirPlay Receiver"**
   - Click en **OFF**

---

## ⚡ Solución Temporal (Para Probar Ahora)

Si necesitas liberar el puerto inmediatamente:

```bash
# Detener todos los procesos AirPlay
killall -9 ControlCenter
killall -9 AirPlayUIAgent

# Iniciar inmediatamente el contenedor DSDL
# (antes de que se reactive)

# Verificar puerto libre
lsof -i :5000 || echo "Puerto libre"
```

**⚠️ Importante**: Este proceso se reinicia automáticamente, así que es temporal.

---

## 🔍 Verificación

### Ver Puerto 5000

```bash
# Ver qué usa el puerto
lsof -i :5000

# Si está vacío, está OK
# Si muestra ControlCenter, AirPlay sigue activo
```

### Ver Estado AirPlay

```bash
# Ver configuración
defaults read com.apple.controlcenter.plist AirplayRecieverEnabled

# Resultado: 0 = desactivado, 1 = activado
```

---

## 🚀 Una Vez Desactivado

1. Ir a DSDL → Containers
2. Click en **"START"** (botón verde)
3. Esperar 30-60 segundos
4. Ver **Active: 1**

---

## 📝 Notas

- **macOS 26**: System Settings está en beta, puede requerir método alternativo
- **AirPlay**: Se desactiva permanentemente hasta reactivar manualmente
- **Puerto alternativo**: Si AirPlay es crítico para ti, necesitarías cambiar puerto DSDL (complejo)

---

**Después de desactivar AirPlay**: Volver a DSDL UI y click en START.

