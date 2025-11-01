# Solución: Error OpenSSL 1.0.2 en DSDL

**Fecha**: 2025-01-31  
**Problema**: Setup Failed - DSDL no puede cargar handlers debido a incompatibilidad OpenSSL

---

## 🔍 Error Identificado

```
ERROR The REST handler module "configure_handler" could not be found.
Python files must be in $SPLUNK_HOME/etc/apps/$MY_APP/bin/

RuntimeError: You are linking against OpenSSL 1.0.2, which is no longer supported 
by the OpenSSL project.
```

---

## ✅ Solución Aplicada

### Paso 1: Agregar Variable de Entorno

Editar archivo: `/Applications/Splunk/etc/splunk-launch.conf`

Agregar al final:
```
CRYPTOGRAPHY_ALLOW_OPENSSL_102=1
```

### Paso 2: Reiniciar Splunk

```bash
# Detener Splunk
/Applications/Splunk/bin/splunk stop

# Iniciar Splunk
/Applications/Splunk/bin/splunk start
```

### Paso 3: Verificar

1. Acceder a http://localhost:9000
2. Ir a DSDL → Configuration → Setup
3. Intentar configurar nuevamente
4. Click en "Test & Save"

---

## 📝 Archivo Modificado

**Antes**:
```
PYTHONHTTPSVERIFY=0
PYTHONUTF8=1
```

**Después**:
```
PYTHONHTTPSVERIFY=0
PYTHONUTF8=1
CRYPTOGRAPHY_ALLOW_OPENSSL_102=1
```

---

## 🔗 Referencias

- **Documentación OpenSSL**: https://cryptography.io/en/latest/faq/#installing-cryptography
- **Variable de entorno**: CRYPTOGRAPHY_ALLOW_OPENSSL_102
- **Archivo Splunk**: `/Applications/Splunk/etc/splunk-launch.conf`

---

## ⚠️ Nota de Seguridad

Esta solución es temporal y para desarrollo. Para producción:
- Actualizar OpenSSL a versión soportada
- Actualizar Splunk a versión compatible
- Revisar compatibilidad de apps con Python y OpenSSL

