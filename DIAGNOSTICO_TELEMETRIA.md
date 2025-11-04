# 🔍 Diagnóstico de Telemetría: Por qué no llegan los datos a Splunk

## 🎯 Problema Reportado

- ✅ `fit()` y `apply()` ejecutan sin errores desde Splunk
- ❌ No hay registros en `index=ml_metrics`
- ❌ No hay registros en `index=ml_model_logs`

## 🔍 Análisis del Código Actual

### Verificaciones Necesarias

1. **¿HEC está configurado y funcionando?**
2. **¿Las funciones de telemetría están fallando silenciosamente?**
3. **¿El formato de los eventos es correcto?**
4. **¿Los índices existen y el token tiene acceso?**

---

## 📋 Checklist de Diagnóstico

### Paso 1: Verificar que HEC está Configurado

**En JupyterLab, ejecuta:**

```python
# THIS CELL IS NOT EXPORTED - Diagnóstico HEC
import os
import sys
sys.path.append('/dltk/notebooks_custom/helpers')

print("🔍 Diagnóstico de Configuración HEC\n")
print("=" * 60)

# Verificar variables de entorno
hec_enabled = os.environ.get('splunk_hec_enabled', 'NO DEFINIDO')
hec_url = os.environ.get('splunk_hec_url', 'NO DEFINIDO')
hec_token = os.environ.get('splunk_hec_token', 'NO DEFINIDO')

print(f"✅ splunk_hec_enabled: {hec_enabled}")
print(f"✅ splunk_hec_url: {hec_url}")
print(f"✅ splunk_hec_token: {'DEFINIDO' if hec_token != 'NO DEFINIDO' else 'NO DEFINIDO'}...")

if hec_enabled != '1':
    print("\n❌ PROBLEMA: splunk_hec_enabled no es '1'")
    print("   Solución: Configurar HEC en DSDL Setup → Splunk HEC Settings")
    print("   Luego: Reiniciar el contenedor")
elif hec_url == 'NO DEFINIDO' or hec_token == 'NO DEFINIDO':
    print("\n❌ PROBLEMA: HEC URL o Token no están definidos")
    print("   Solución: Configurar HEC en DSDL Setup → Splunk HEC Settings")
    print("   Luego: Reiniciar el contenedor")
else:
    print("\n✅ HEC está configurado correctamente")
```

### Paso 2: Probar Telemetría Manualmente con Traceback Completo

**En JupyterLab, ejecuta:**

```python
# THIS CELL IS NOT EXPORTED - Test telemetría con diagnóstico completo
import sys
import traceback
sys.path.append('/dltk/notebooks_custom/helpers')

print("🧪 Test de Telemetría con Diagnóstico Completo\n")
print("=" * 60)

# Test 1: Verificar que las funciones existen
try:
    from telemetry_helper import log_metrics, log_training_step
    print("✅ telemetry_helper importado correctamente")
except ImportError as e:
    print(f"❌ Error importando telemetry_helper: {e}")
    print(f"   Traceback: {traceback.format_exc()}")
    sys.exit(1)

# Test 2: Probar log_metrics con diagnóstico
print("\n📊 Test 1: log_metrics()")
try:
    log_metrics(
        model_name="test_diagnostico_v1",
        r2_score=0.95,
        mae=0.05,
        rmse=0.08,
        loss=0.1,
        app_name="app1",
        model_version="v1",
        project="test"
    )
    print("✅ log_metrics() ejecutado sin errores")
except Exception as e:
    print(f"❌ Error en log_metrics(): {e}")
    print(f"   Tipo de error: {type(e).__name__}")
    print(f"   Traceback completo:")
    print(traceback.format_exc())

# Test 3: Probar log_training_step con diagnóstico
print("\n📈 Test 2: log_training_step()")
try:
    log_training_step(
        model_name="test_diagnostico_v1",
        epoch=1,
        loss=0.5,
        val_loss=0.6,
        mae=0.1,
        val_mae=0.12
    )
    print("✅ log_training_step() ejecutado sin errores")
except Exception as e:
    print(f"❌ Error en log_training_step(): {e}")
    print(f"   Tipo de error: {type(e).__name__}")
    print(f"   Traceback completo:")
    print(traceback.format_exc())

print("\n📊 Verificar en Splunk:")
print("   index=ml_metrics model_name=test_diagnostico_v1 | head 10")
print("   index=ml_model_logs model_name=test_diagnostico_v1 | head 10")
```

### Paso 3: Verificar Implementación de telemetry_helper

**En JupyterLab, ejecuta:**

```python
# THIS CELL IS NOT EXPORTED - Inspeccionar telemetry_helper
import sys
import inspect
sys.path.append('/dltk/notebooks_custom/helpers')

print("🔍 Inspección de telemetry_helper\n")
print("=" * 60)

try:
    import telemetry_helper
    
    # Verificar funciones disponibles
    print("✅ Funciones disponibles:")
    for name in dir(telemetry_helper):
        if not name.startswith('_'):
            obj = getattr(telemetry_helper, name)
            if callable(obj):
                print(f"   - {name}()")
    
    # Verificar implementación de log_metrics
    print("\n📋 Implementación de log_metrics:")
    try:
        source = inspect.getsource(telemetry_helper.log_metrics)
        print(source[:500] + "..." if len(source) > 500 else source)
    except Exception as e:
        print(f"   ⚠️  No se pudo obtener código fuente: {e}")
    
    # Verificar implementación de log_training_step
    print("\n📋 Implementación de log_training_step:")
    try:
        source = inspect.getsource(telemetry_helper.log_training_step)
        print(source[:500] + "..." if len(source) > 500 else source)
    except Exception as e:
        print(f"   ⚠️  No se pudo obtener código fuente: {e}")
        
except ImportError as e:
    print(f"❌ Error importando telemetry_helper: {e}")
    print(f"   Verifica que el path es correcto: /dltk/notebooks_custom/helpers")
```

### Paso 4: Verificar que los Eventos se Envían Correctamente

**En JupyterLab, ejecuta:**

```python
# THIS CELL IS NOT EXPORTED - Test directo de HEC
import os
import sys
import json
import requests
from datetime import datetime

print("🔍 Test Directo de HEC\n")
print("=" * 60)

# Obtener configuración HEC
hec_url = os.environ.get('splunk_hec_url', 'http://localhost:8088')
hec_token = os.environ.get('splunk_hec_token', '')

print(f"📡 HEC URL: {hec_url}")
print(f"🔑 Token: {'DEFINIDO' if hec_token else 'NO DEFINIDO'}")

if not hec_token:
    print("\n❌ Token HEC no está definido")
    print("   Solución: Configurar HEC en DSDL Setup")
else:
    # Construir URL completa
    hec_endpoint = f"{hec_url}/services/collector/event"
    
    # Crear evento de prueba
    event = {
        'event': {
            'event_type': 'test_telemetry',
            'model_name': 'test_directo_hec',
            'message': 'Test directo de HEC',
            'timestamp': datetime.now().isoformat()
        },
        'time': datetime.now().timestamp()
    }
    
    # Enviar evento
    print(f"\n📤 Enviando evento a: {hec_endpoint}")
    print(f"   Evento: {json.dumps(event, indent=2)}")
    
    try:
        headers = {
            'Authorization': f'Splunk {hec_token}',
            'Content-Type': 'application/json'
        }
        
        response = requests.post(
            hec_endpoint,
            headers=headers,
            json=event,
            timeout=5
        )
        
        print(f"\n📥 Respuesta HEC:")
        print(f"   Status Code: {response.status_code}")
        print(f"   Response: {response.text}")
        
        if response.status_code == 200:
            print("\n✅ Evento enviado exitosamente a HEC")
            print("   Verificar en Splunk:")
            print("   index=ml_metrics event_type=test_telemetry | head 10")
        else:
            print(f"\n❌ Error enviando evento: {response.status_code}")
            print(f"   Response: {response.text}")
            
    except requests.exceptions.ConnectionError as e:
        print(f"\n❌ Error de conexión: {e}")
        print("   Verifica que:")
        print("   1. Splunk está corriendo")
        print("   2. HEC está habilitado en Splunk")
        print("   3. La URL es correcta (usar host.docker.internal en macOS)")
    except Exception as e:
        print(f"\n❌ Error inesperado: {e}")
        import traceback
        print(traceback.format_exc())
```

### Paso 5: Verificar Logs del Contenedor

**En terminal, ejecuta:**

```bash
# Ver logs del contenedor DSDL
docker ps | grep mltk-container
CONTAINER_ID=$(docker ps | grep mltk-container | awk '{print $1}')

# Ver logs relacionados con HEC/telemetría
docker logs $CONTAINER_ID --tail 200 | grep -i "hec\|telemetry\|error" | tail -20
```

**O en JupyterLab:**

```python
# THIS CELL IS NOT EXPORTED - Verificar logs del contenedor
import os
import subprocess

print("📋 Logs del Contenedor (últimas líneas relacionadas con HEC/telemetría)\n")
print("=" * 60)

container_id = os.environ.get('HOSTNAME', 'unknown')
print(f"📦 Container ID: {container_id}")

# Nota: Los logs pueden estar en stdout/stderr del contenedor
# Para verlos completos, necesitas acceso a docker logs
print("\n⚠️  Para ver logs completos, ejecuta en terminal:")
print(f"   docker logs {container_id} --tail 200 | grep -i 'hec\\|telemetry\\|error'")
```

---

## 🔧 Problemas Comunes y Soluciones

### Problema 1: HEC no está habilitado o no está configurado

**Síntomas:**
- Variables de entorno `splunk_hec_*` no están definidas
- `splunk_hec_enabled` no es `"1"`

**Solución:**
1. Ve a: **DSDL → Setup → Splunk HEC Settings**
2. Configura:
   - **Enable Splunk HEC**: `Yes`
   - **Splunk HEC Token**: Token válido
   - **Splunk HEC Endpoint URL**: URL correcta
3. **Reinicia el contenedor** (DSDL configura variables de entorno al iniciar)

### Problema 2: Errores silenciosos en las funciones de telemetría

**Síntomas:**
- `fit()` y `apply()` no arrojan errores
- Pero no hay datos en Splunk

**Solución:**
1. Ejecutar el test manual (Paso 2) para ver errores completos
2. Verificar que `telemetry_helper` está correctamente implementado
3. Verificar que HEC está disponible cuando se llama

### Problema 3: Índices no existen o token sin acceso

**Síntomas:**
- HEC funciona (status 200)
- Pero datos no aparecen en índices

**Solución:**
1. Verificar que los índices existen: `index=ml_metrics` y `index=ml_model_logs`
2. Verificar que el token HEC tiene acceso a estos índices
3. Verificar en Splunk: `index=_internal "hec"` para ver errores de HEC

### Problema 4: URL de HEC incorrecta (macOS/Docker Desktop)

**Síntomas:**
- Connection refused o timeout
- HEC funciona desde terminal pero no desde contenedor

**Solución:**
1. Si estás en macOS con Docker Desktop, cambia la URL a: `http://host.docker.internal:8088`
2. Reinicia el contenedor después de cambiar la configuración

---

## ✅ Checklist Final

Antes de reportar que la telemetría no funciona, verifica:

- [ ] HEC está habilitado en Splunk
- [ ] HEC está configurado en DSDL Setup
- [ ] Variables de entorno `splunk_hec_*` están definidas en el contenedor
- [ ] El contenedor fue reiniciado después de configurar HEC
- [ ] Los índices `ml_metrics` y `ml_model_logs` existen
- [ ] El token HEC tiene acceso a ambos índices
- [ ] El test manual de telemetría funciona (Paso 2)
- [ ] El test directo de HEC funciona (Paso 4)
- [ ] No hay errores en los logs del contenedor

---

## 📊 Verificación en Splunk

Después de ejecutar los tests, verifica en Splunk:

```spl
# Verificar métricas de test
index=ml_metrics model_name=test_diagnostico_v1 OR model_name=test_directo_hec
| head 10
| table _time model_name event_type r2_score mae rmse

# Verificar logs de test
index=ml_model_logs model_name=test_diagnostico_v1
| head 10
| table _time model_name epoch loss val_loss

# Verificar eventos de test directo
index=ml_metrics event_type=test_telemetry
| head 10
| table _time model_name message
```

---

## 🎯 Próximos Pasos

1. **Ejecutar todos los pasos de diagnóstico** en orden
2. **Documentar los resultados** de cada paso
3. **Identificar el problema específico** que está impidiendo que lleguen los datos
4. **Aplicar la solución correspondiente** según el problema identificado

