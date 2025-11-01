# Configuración Rápida DSDL - Sandbox Local

**Objetivo**: Configurar DSDL en 5 minutos para primera prueba

---

## ⚡ Configuración Rápida

### 1️⃣ Docker Settings

```
Docker Host:      unix:///var/run/docker.sock
Endpoint URL:     localhost
External URL:     localhost
Docker network:   [vacío]
API Workers:      1
```

### 2️⃣ Certificate Settings

```
Check Hostname:                 Disabled
Certificate path:               [vacío]
Enable container certificates:  Yes
Enable KEEPALIVE:               No
```

### 3️⃣ Password Settings

```
Endpoint Token:   [vacío - usar random]
Jupyter Password: [vacío o personalizada]
```

### 4️⃣ Splunk Access (Opcional - SKIP si quieres ir rápido)

```
Enable Splunk Access:  No
```

**SKIP** para primera prueba rápida.

### 5️⃣ Splunk HEC (Opcional - SKIP si quieres ir rápido)

```
Enable Splunk HEC:  No
```

**SKIP** para primera prueba rápida.

### 6️⃣ Observability (Opcional - SKIP)

```
Enable Observability:  No
```

---

## ✅ Click en "Test & Save"

Después de configurar secciones 1-3, hacer click en **"Test & Save"** al final de la página.

---

## 🚀 Próximo Paso

Ver archivo `CONFIGURACION_DSDL.md` para:
- Configuración recomendada completa
- Cómo crear tokens HEC/Access
- Validación y troubleshooting
- Ejecución de primeros ejemplos

