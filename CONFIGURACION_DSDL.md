# Guía de Configuración: DSDL en Splunk Web

**Fecha**: 2025-01-31  
**Objetivo**: Configurar DSDL para sandbox local  
**Status**: Pendiente de configuración

---

## 📍 Ubicación de Configuración

Acceder a: http://localhost:9000  
App: **Data Science and Deep Learning (DSDL)**  
Menú: **Configuration** → **Setup**

---

## 1️⃣ Docker Settings (Configuración Principal)

### Campos Requeridos

| Campo | Valor para macOS | Notas |
|-------|------------------|-------|
| **Docker Host** | `unix:///var/run/docker.sock` | Socket de Docker en macOS |
| **Endpoint URL** | `localhost` | URL interna del contenedor |
| **External URL** | `localhost` | URL externa para acceso desde navegador |
| **Docker network** | *(vacío)* | Dejar vacío para desarrollo |
| **API Workers** | `1` | Concurrencia FastAPI (default=1) |

### Ejemplo de Configuración

```
Docker Host:      unix:///var/run/docker.sock
Endpoint URL:     localhost
External URL:     localhost
Docker network:   [vacío]
API Workers:      1
```

### Tabla de Referencia (Single-Instance Linux)

| Deployment | Docker Host | Endpoint URL | External URL | Host OS |
|------------|-------------|--------------|--------------|---------|
| single-instance | `unix:///var/run/docker.sock` | `localhost` | `localhost` | linux |

**Nota**: macOS usa Docker Desktop que monta `/var/run/docker.sock` dentro del contenedor, por lo que esta configuración debería funcionar.

### Configuración Adicional (Opcional)

#### Splunk Docker Logging

| Campo | Valor | Estado |
|-------|-------|--------|
| **Splunk Docker Logging Endpoint** | *(vacío)* | Opcional |
| **Splunk Docker Logging (HEC) Token** | *(vacío)* | Opcional |

**Dejar vacíos** para primera configuración.

---

## 2️⃣ Certificate Settings (Configuración SSL)

### Configuración Recomendada para Sandbox

| Setting | Valor Recomendado | Razón |
|---------|-------------------|-------|
| **Check Hostname** | `Disabled` | Desarrollo local con certificados self-signed |
| **Certificate filename or path** | *(vacío)* | Usar certificado por defecto del contenedor |
| **Enable container certificates** | `Yes` | Habilitar HTTPS en contenedores |
| **Enable KEEPALIVE flag** | `No` | No necesario en local |

### Notas de Seguridad

> ⚠️ **Security notes**: For production use it is highly recommended that you use your own certificate. Please generate it according to the security requirements in your environment and build it into your container images or configure it in your container environment.

**Para sandbox local**: Usar configuración por defecto es aceptable.

---

## 3️⃣ Password Settings (Tokens y Contraseñas)

### API Endpoint Token

| Campo | Valor | Estado |
|-------|-------|--------|
| **Endpoint Token** | *(vacío)* | Dejar vacío para token random por defecto |

> Nota: Cambios solo aplican a contenedores nuevos.

### Jupyter Lab Password

| Campo | Acción | Notas |
|-------|--------|-------|
| **Jupyter Password** | *(vacío o personalizada)* | Si vacía, usar password por defecto |

**Recomendación para sandbox**: Dejar vacío y usar password por defecto, o configurar una contraseña simple.

> ⚠️ **Security notes**: It is strongly recommended to set a custom password here. Alternatively you can manage this in your container environment by overriding the JUPYTER_PASSWD environment variable.

**Para obtener el password por defecto**: Click en el botón "Click to show the default Jupyter Lab password"

---

## 4️⃣ Splunk Access Settings (Acceso desde Jupyter a Splunk)

### Configuración Opcional pero Útil

| Campo | Valor | Estado |
|-------|-------|--------|
| **Enable Splunk Access** | `Yes` | ✅ Recomendado para pulling data desde notebooks |
| **Splunk Access Token** | *[generar en Settings→Tokens]* | Ver sección de creación |
| **Splunk Host Address** | `localhost` | ✅ Ya pre-configurado correctamente |
| **Splunk Management Port** | `8089` | ✅ Ya pre-configurado correctamente |

### Pasos para Obtener Splunk Access Token

1. En Splunk Web: **Settings** → **Tokens**
2. Click **"Create New Token"**
3. Configurar:
   - **Name**: `dsdl-api-token`
   - **Capability**: Seleccionar permisos mínimos necesarios
4. Copiar el token generado
5. Pegar en **"Splunk Access Token"** de DSDL

> ⚠️ **Security notes**: It is strongly recommended to restrict the Splunk access token to only necessary capabilities to scope permissions down, e.g. to only allow access to selected indexes.

---

## 5️⃣ Splunk HEC Settings (Enviar Resultados a Splunk)

### Configuración Opcional

| Campo | Valor | Estado |
|-------|-------|--------|
| **Enable Splunk HEC** | `Yes` | ✅ Recomendado para enviar resultados |
| **Splunk HEC Token** | *[crear en Data Inputs]* | Ver sección de creación |
| **Splunk HEC Endpoint URL** | `http://localhost:8088` | ✅ Ya pre-configurado |

### Pasos para Crear HEC Token

1. En Splunk Web: **Settings** → **Data Inputs**
2. Click **"HTTP Event Collector"**
3. Click **"New Token"**
4. Configurar:
   - **Name**: `dsdl-hec-token`
   - **App context**: `Search & Reporting`
5. Click **"Next"** → Seleccionar índices permitidos
6. Copiar el token generado
7. Pegar en **"Splunk HEC Token"** de DSDL

> ⚠️ **Nota importante**: When you change the settings below you need to restart your container(s) so that the configuration changes take effect in the container.

---

## 6️⃣ Observability Settings (Opcional - Saltar para Sandbox)

| Setting | Valor | Estado |
|---------|-------|--------|
| **Enable Observability** | `No` | Saltar para sandbox local |

**Justificación**: Splunk Observability Cloud requiere cuenta y configuración adicional. No necesario para desarrollo local.

---

## ✅ Checklist de Configuración

### Mínima Requerida (Primera Prueba)

- [x] Docker Settings configurados
- [x] Certificate Settings configurados (default)
- [x] Click en **"Test & Save"**

### Recomendada (Para Desarrollo)

- [x] Docker Settings configurados
- [x] Certificate Settings configurados
- [x] Password Settings configurados (Jupyter password opcional)
- [x] Splunk Access Settings → **Enable** + Token creado
- [x] Splunk HEC Settings → **Enable** + Token creado
- [x] Click en **"Test & Save"**

### Opcional Avanzada

- [ ] Observability Settings configurados
- [ ] Docker Logging configurado
- [ ] Custom certificates configurados

---

## 🧪 Validación Post-Configuración

### Paso 1: Lanzar Contenedor DEV

1. Navegar a **DSDL** → **Containers**
2. Click **"Start Development Container"**
3. Seleccionar imagen: `golden-cpu` (Golden Image CPU 5.2.2)
4. Esperar inicio: 30-60 segundos

### Paso 2: Verificar Contenedor Activo

```bash
# Desde terminal
docker ps | grep mltk-container

# Deberías ver algo como:
# CONTAINER ID   IMAGE                                      STATUS
# abc123def456   splunk/mltk-container-golden-cpu:5.2.2   Up X seconds
```

### Paso 3: Acceder a JupyterLab

1. En DSDL: **Containers**
2. Ver contenedor activo → Click **"Open JupyterLab"**
3. Se abre navegador en puerto `8888` (o dinámico)
4. Login con password configurada

### Paso 4: Ejecutar Ejemplo Predefinido

1. En DSDL: **Examples**
2. Seleccionar: **"Neural Network Classifier Example for Tensorflow"**
3. Click **"Run"**
4. Verificar que ejecuta sin errores

---

## 🚨 Troubleshooting Común

### Error: "Cannot connect to Docker"

**Solución**:
```bash
# Verificar Docker corriendo
docker ps

# Si no está corriendo, iniciar Docker Desktop
open -a Docker
```

### Error: "Failed to pull image"

**Solución**:
```bash
# Verificar imagen descargada
docker images | grep mltk-container-golden-cpu

# Si no está, descargar manualmente
docker pull splunk/mltk-container-golden-cpu:5.2.2
```

### Error: "Port already in use"

**Solución**:
```bash
# Ver qué usa el puerto
lsof -i :8888
lsof -i :5000

# Detener proceso o cambiar configuración en DSDL
```

### Error: "Container starts but JupyterLab not accessible"

**Verificar**:
1. Container status: `docker ps | grep mltk`
2. Logs: `docker logs <container-id> | tail -50`
3. Firewall de macOS permitiendo conexiones

---

## 📝 Notas Importantes

### Orden de Configuración

1. ✅ Docker Settings (obligatorio)
2. ✅ Certificate Settings (obligatorio)
3. ⚠️ Password Settings (recomendado)
4. ⚠️ Splunk Access (opcional pero útil)
5. ⚠️ Splunk HEC (opcional pero útil)
6. ❌ Observability (opcional - saltar)

### Cambios Requieren Restart

- Cambios en HEC Settings → Requieren restart de contenedores
- Cambios en Password Settings → Aplican a contenedores nuevos
- Cambios en Splunk Access → Aplican a contenedores nuevos

### Acceso Local vs Remoto

**Local (tu Mac)**:
- Docker Host: `unix:///var/run/docker.sock`
- Hostnames: `localhost`, `host.docker.internal`

**Remoto (Kubernetes/GCP/Azure)**:
- Docker Host: `tcp://remote.host:2375` o Kubernetes endpoint
- Hostnames: IP o FQDN del cluster

---

## 🔗 Referencias

- **Documentación DSDL**: Ver `DSDL-docs.md`
- **Guía instalación**: Ver `GUIA_INSTALACION_SANDBOX_LOCAL.md`
- **Estado actual**: Ver `ESTADO_SANDBOX_LOCAL.md`
- **Análisis técnico**: Ver `ANALISIS_COMPARATIVO_DSDL.md`

---

**Próximo paso después de configurar**: Lanzar primer contenedor DEV y ejecutar ejemplo predefinido.

