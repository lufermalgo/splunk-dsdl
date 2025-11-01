# Resumen de Descarga de Imagen Golden CPU

**Fecha**: 2025-01-31  
**Acción**: Descarga de imagen Docker para DSDL

---

## 📦 Origen de la Imagen

| Campo | Valor |
|-------|-------|
| **Registry** | `docker.io` (Docker Hub) |
| **Organización** | `splunk` (oficial de Splunk) |
| **Repositorio** | `mltk-container-golden-cpu` |
| **Tag/Versión** | `5.2.2` |
| **URL Pública** | https://hub.docker.com/r/splunk/mltk-container-golden-cpu |
| **Digest SHA256** | `sha256:2e495a0540471a3f3114ea783adb62accac1711f5b3296672ab12eeaa36098ff` |

### Comando de Descarga

```bash
docker pull splunk/mltk-container-golden-cpu:5.2.2
```

### Formato Completo

La imagen se descarga desde:
```
docker.io/splunk/mltk-container-golden-cpu:5.2.2
```

Donde:
- `docker.io` = Docker Hub (registry por defecto)
- `splunk/` = Organización oficial de Splunk
- `mltk-container-golden-cpu` = Nombre del repositorio
- `:5.2.2` = Tag específico de versión

---

## 📊 Detalles de la Imagen

| Propiedad | Valor |
|-----------|-------|
| **Tamaño comprimido** | ~1.7 GB (descarga) |
| **Tamaño sin comprimir** | 7.42 GB |
| **Fecha de build** | ~2 meses atrás |
| **Arquitectura** | x86_64 (AMD64) |
| **Runtime** | `none` (CPU solamente) |

---

## 🔍 Imágenes Preconfiguradas en DSDL

La configuración de DSDL (`images.conf`) incluye **10 imágenes** predefinidas:

| ID Configuración | Nombre | Runtime | Caso de Uso |
|------------------|--------|---------|-------------|
| `golden-cpu` | Golden Image CPU | CPU | **Usada para desarrollo local** |
| `golden-cpu-arm` | Golden Image ARM64 | CPU | Apple Silicon |
| `golden-gpu` | Golden Image GPU | NVIDIA GPU | Deep Learning acelerado |
| `golden-cpu-transformers` | Transformers CPU | CPU | NLP/HuggingFace |
| `golden-gpu-transformers` | Transformers GPU | NVIDIA GPU | NLP acelerado |
| `golden-gpu-rapids` | Rapids GPU | NVIDIA GPU | Data Science acelerado |
| `llm-rag` | LLM RAG (Red Hat UBI) | CPU | LLM/RAG workloads |
| `escu-cpu` | ESCU CPU | CPU | Threat detection |
| `spark` | Spark 3.5.1 | CPU | Big data processing |
| `agentic-ai` | Agentic AI | CPU | AI agent workflows |

---

## 📍 Ubicación Local

Una vez descargada, la imagen se almacena en:

**macOS Docker Desktop**:
```
~/Library/Containers/com.docker.docker/Data/vms/
```

**Verificar**:
```bash
docker images | grep mltk-container-golden-cpu
docker system df
```

---

## ✅ Estado de Descarga

```
✅ Descargada exitosamente
✅ Validada con digest SHA256
✅ Disponible para uso en DSDL
✅ Referenciada en configuración images.conf
```

---

## 🔗 Referencias

- **Docker Hub**: https://hub.docker.com/u/splunk
- **Documentación**: Ver archivo `DSDL-docs.md`
- **Configuración**: `/Applications/Splunk/etc/apps/mltk-container/default/images.conf`
- **Análisis**: Ver `ANALISIS_COMPARATIVO_DSDL.md`

---

## 📝 Notas

1. La imagen es **oficial de Splunk** y está disponible públicamente sin autenticación
2. **No requiere login** en Docker Hub para descarga pública
3. Si tienes `us-central1-docker.pkg.dev` configurado, es para **imágenes custom** (GCP Artifact Registry)
4. Para producción, considera usar **registry privado** (GCP/Azure) con scanning de seguridad

