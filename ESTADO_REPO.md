# Estado de Repositorios - Splunk DSDL Project

**Fecha**: 2025-11-01  
**Versión**: 1.0

## 📦 Estructura de Repositorios

### Repo Principal: `Splunk-DSDL`

**Ubicación**: `/Users/lufermalgo/Proyectos/Splunk-DSDL/`  
**Git Remote**: `https://github.com/lufermalgo/splunk-dsdl.git`  
**Branch**: `main`

**Contiene**:
- ✅ Documentación del proyecto (Markdown files)
- ✅ Análisis comparativo DSDL
- ✅ Checklists y guías DevOps
- ✅ Estrategias de governance e indexing
- ✅ Templates de notebooks de prueba
- ✅ Ejemplos de notebooks de Cristian
- ✅ Scripts de testing locales

### Fork de Docker: `splunk-mltk-container-docker`

**Ubicación**: `/Users/lufermalgo/Proyectos/Splunk-DSDL/splunk-mltk-container-docker/`  
**Git Remote (origin)**: `https://github.com/splunk/splunk-mltk-container-docker.git`  
**Git Remote (custom)**: `https://github.com/lufermalgo/splunk-dsdl.git`  
**Branch**: `master`

**Contiene**:
- ✅ Dockerfiles y scripts de build
- ✅ `notebooks_custom/` - Helpers y templates empresariales
- ✅ `requirements_files/empresa_custom.txt` - Librerías custom
- ✅ Modificaciones a `bootstrap_fast.sh` y `Dockerfile.redhat`
- ✅ `tag_mapping.csv` con tag `golden-cpu-empresa-arm`

**Último Commit**: `41a3183` - "feat: Imagen empresarial DSDL completa"

---

## ⚠️ Situación Actual

### El Fork Docker NO está sincronizado con Repo Principal

El directorio `splunk-mltk-container-docker` es un **subdirectorio independiente** con su propio `.git`, no un submódulo de Git.

**Problema**: Los cambios en `splunk-mltk-container-docker` no están en el repo principal `Splunk-DSDL`.

---

## ✅ Soluciones Recomendadas

### Opción 1: Mantener Separados (Actual)

**Ventajas**:
- Clean separation de concerns
- Fork Docker puede trackear upstream de Splunk
- Repo principal ligero (solo docs)

**Desventajas**:
- Dos repos para mantener
- Más complejo para clonar

**Proceso**:
1. Fork: `git push custom master` (con LFS resuelto)
2. Principal: Documentación y testing scripts

### Opción 2: Convertir en Submódulo Git

**Ventajas**:
- Un solo repo para clonar
- Referencia específica al fork Docker

**Desventajas**:
- Más complejo de manejar
- Requiere setup de submódulo

**Proceso**:
```bash
cd /Users/lufermalgo/Proyectos/Splunk-DSDL
git rm -r splunk-mltk-container-docker
git submodule add https://github.com/lufermalgo/splunk-dsdl.git splunk-mltk-container-docker
```

### Opción 3: Mover Todo a Repo Único

**Ventajas**:
- Simple y directo

**Desventajas**:
- Pierdes sync con upstream de Splunk
- Repo pesado

---

## 🚀 Acción Recomendada

**Para ahora**: Mantener separados pero documentar claramente cómo trabajar con ambos.

**Para producción**: Decidir entre Opción 1 o 2 según necesidades del equipo.

---

## 📝 Próximos Pasos

1. ✅ Push fork Docker a GitHub (resolver LFS)
2. ✅ Push repo principal con docs actualizadas
3. 📋 Crear README.md principal que explique la estructura
4. 📋 Actualizar `.gitignore` si es necesario

---

## 🔗 Referencias

- **Imagen Docker Custom**: `mltk-container-golden-cpu-empresa-arm:5.2.2`
- **Validación**: Ver `VALIDACION_EXITOSA_COMPLETA.md`
- **Checklist DevOps**: Ver `CHECKLIST_DEVOPS_DSDL.md`

