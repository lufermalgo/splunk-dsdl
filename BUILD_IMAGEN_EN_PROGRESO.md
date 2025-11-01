# Build de Imagen Empresarial en Progreso

**Fecha inicio**: 2025-01-31  
**Comando**: `./build.sh golden-cpu-empresa splunk/ 5.2.2`  
**Log**: `splunk-mltk-container-docker/build.log`

---

## ⏳ Estado Actual

**EN PROGRESO** - Instalando dependencias de `empresa_custom.txt`

### Progreso Visible

```
#19 [15/37] RUN pip3 install empresa_custom.txt
  Downloading datashader-0.17.0...
  Downloading seaborn-0.13.2...
  Downloading scipy-1.13.1...
  Downloading scikit_learn-1.6.1...
  Downloading tensorflow-cpu...
  Downloading torch...
  Downloading mlflow...
  Downloading prophet...
  Downloading xgboost...
  Downloading shap...
  Downloading lime...
  ...
  Downloading aeon>=0.5.0...  ← Librería custom
```

---

## 📊 Monitoreo

### Ver progreso en vivo

```bash
cd splunk-mltk-container-docker
tail -f build.log

# Filtrar por etapas importantes
tail -f build.log | grep -E "(Step|Building|Success|Error|Installing aeon)"
```

### Verificar proceso

```bash
# Ver PID del proceso
ps aux | grep build.sh

# Ver tamaño actual de build.log
ls -lh build.log

# Ver últimas líneas
tail -20 build.log
```

---

## ⏱️ Tiempo Estimado

| Etapa | Tiempo Estimado |
|-------|-----------------|
| Descargar imagen base | 2-5 min |
| Instalar sistema base | 3-5 min |
| Instalar Python requirements base | 5-10 min |
| Instalar empresa_custom.txt | 10-15 min |
| Build helpers y copy | 2-3 min |
| **Total** | **15-30 min** |

---

## ✅ Qué Instalará

### Base (base_functional.txt)
- fastapi, uvicorn
- jupyterlab
- pandas, numpy
- splunk-sdk

### Custom (empresa_custom.txt)
- ✅ TensorFlow, PyTorch
- ✅ sklearn, scipy, statsmodels
- ✅ Prophet, XGBoost, LightGBM
- ✅ SHAP, LIME, MLflow
- ✅ Datashader, Seaborn
- ✅ **aeon>=0.5.0** (librería faltante)

---

## 🔍 Validación Post-Build

### Checklist

- [ ] Build completó sin errores
- [ ] Imagen creada: `docker images | grep golden-cpu-empresa`
- [ ] Helpers presentes: `docker run --rm splunk/mltk-container-golden-cpu-empresa:5.2.2 ls -R /dltk/notebooks_custom/`
- [ ] aeon instalado: `docker run --rm splunk/mltk-container-golden-cpu-empresa:5.2.2 python3 -c "import aeon; print(aeon.__version__)"`
- [ ] Archivo .conf generado: `ls images_conf_files/golden-cpu-empresa.conf`

---

## 🚨 Troubleshooting

### Build falla en requirements

**Problema**: Error instalando alguna librería

**Solución**:
```bash
# Ver logs de error
tail -100 build.log | grep -A 5 "ERROR"

# Revisar empresa_custom.txt
cat requirements_files/empresa_custom.txt

# Probar instalar manualmente
docker run -it --rm redhat/ubi9 bash
pip install aeon>=0.5.0
```

### Build toma demasiado tiempo (>1 hora)

**Problema**: Descargando desde PyPI muy lento

**Solución**:
- Considerar pre-compilar requirements
- Usar mirror de PyPI si disponible

### Build success pero helpers no presentes

**Problema**: Dockerfile no copió notebooks_custom

**Solución**:
```bash
# Verificar modificaciones
diff dockerfiles/Dockerfile.redhat.orig dockerfiles/Dockerfile.redhat

# Verificar archivos
ls -R notebooks_custom/
```

---

## 📝 Próximos Pasos Después de Build

### 1. Verificar imagen

```bash
docker images | grep golden-cpu-empresa
```

### 2. Push a registry (opcional)

```bash
docker tag splunk/mltk-container-golden-cpu-empresa:5.2.2 \
  your-registry/golden-cpu-empresa:5.2.2
docker push your-registry/golden-cpu-empresa:5.2.2
```

### 3. Configurar en DSDL

```bash
# Copiar .conf a Splunk
cp splunk-mltk-container-docker/images_conf_files/golden-cpu-empresa.conf \
  /Applications/Splunk/etc/apps/mltk-container/local/images.conf

# Reiniciar Splunk o recargar DSDL
```

### 4. Test en DSDL UI

- DSDL → Configuration → Container Images
- Verificar `golden-cpu-empresa:5.2.2` disponible
- Click "Start"
- Verificar JupyterLab accesible
- Test helpers

---

## 📊 Métricas de Build

Verificar después de completar:

```bash
# Tamaño final de imagen
docker images splunk/mltk-container-golden-cpu-empresa:5.2.2

# Tiempo total
grep -E "Step|Successfully built" build.log | tail -40

# Recursos usados
docker system df
```

---

## ⏸️ Pausar Build (si es necesario)

```bash
# Ver PID
ps aux | grep build.sh

# Pausar (Ctrl+Z)
# O kill si necesario
kill <PID>
```

---

## 📚 Referencias

- Build original: https://github.com/splunk/splunk-mltk-container-docker
- Documentación: `DSDL-docs.md`
- Checklist: `CHECKLIST_DEVOPS_DSDL.md`

