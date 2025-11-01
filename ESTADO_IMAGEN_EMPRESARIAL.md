# Estado: Imagen Empresarial Custom

**Fecha**: 2025-01-31  
**Versión**: 5.2.2  
**Tag**: golden-cpu-empresa

---

## ✅ Completado

### Fase 1: Preparación
- [x] Clonado repositorio base DSDL
- [x] Creada estructura `notebooks_custom/helpers/`
- [x] Creado `requirements_files/empresa_custom.txt` con:
  - Todas las librerías de Golden CPU RedHat
  - **aeon>=0.5.0** agregado
- [x] Actualizado `tag_mapping.csv` con nueva entrada:
  ```
  golden-cpu-empresa,redhat/ubi9,Dockerfile.redhat,base_functional.txt,empresa_custom.txt,none,Dockerfile.redhat.requirements,Golden CPU Empresarial Custom (5.2.2)
  ```
- [x] Creados helpers empresariales:
  - `telemetry_helper.py` - Logging automático a HEC
  - `metrics_calculator.py` - Cálculo de métricas ML
  - `preprocessor.py` - Preprocesamiento estándar
  - `splunk_connector.py` - Validación de configuración Splunk
- [x] Copiado `template_empresa_base.ipynb` desde autoencoder
- [x] Modificado `Dockerfile.redhat` para copiar `notebooks_custom`

---

## 🔨 Próximos Pasos

### Fase 3: Build
```bash
cd splunk-mltk-container-docker

# Opción A: Build directo (toma 15-30 min)
./build.sh golden-cpu-empresa splunk/ 5.2.2

# Opción B: Pre-compilar requirements primero (más rápido)
./compile_image_python_requirements.sh golden-cpu-empresa
./build.sh golden-cpu-empresa splunk/ 5.2.2
```

### Fase 4: Deploy Local
```bash
# Push a Docker Hub (o registry local)
docker tag splunk/golden-cpu-empresa:5.2.2 YOUR_USER/golden-cpu-empresa:5.2.2
docker push YOUR_USER/golden-cpu-empresa:5.2.2

# Copiar archivo .conf generado a Splunk
cp images_conf_files/golden-cpu-empresa.conf /Applications/Splunk/etc/apps/mltk-container/local/images.conf

# Reiniciar Splunk o recargar DSDL
```

### Fase 5: Validación
- [ ] Iniciar contenedor desde DSDL UI
- [ ] Verificar JupyterLab accesible
- [ ] Verificar helpers importables
- [ ] Probar template_empresa_base
- [ ] Verificar aeon instalado

---

## 📋 Archivos Creados

```
splunk-mltk-container-docker/
├── requirements_files/
│   └── empresa_custom.txt                          ✅ 64 líneas (Golden + aeon)
├── tag_mapping.csv                                 ✅ Modificado
├── dockerfiles/
│   └── Dockerfile.redhat                           ✅ Modificado (línea 54)
└── notebooks_custom/
    ├── template_empresa_base.ipynb                 ✅ Copiado
    └── helpers/
        ├── telemetry_helper.py                     ✅ 166 líneas
        ├── metrics_calculator.py                   ✅ 97 líneas
        ├── preprocessor.py                         ✅ 176 líneas
        └── splunk_connector.py                     ✅ 48 líneas
```

---

## ⚠️ Notas Importantes

1. **Build time**: El build puede tomar 15-30 minutos (descarga de imágenes base, instalación de paquetes)
2. **Espacio**: La imagen resultante será ~2-3GB
3. **Requirements**: `aeon>=0.5.0` se instala desde PyPI durante el build
4. **Template**: El template necesita ser actualizado manualmente con helpers (copy-paste)
5. **Testing**: Probar en sandbox local antes de producción

---

## 🐛 Troubleshooting

### Error: Build fails en requirements
```bash
# Verificar formato de empresa_custom.txt
cat requirements_files/empresa_custom.txt

# Probar instalar aeon localmente primero
pip install aeon>=0.5.0
```

### Error: Dockerfile no encuentra notebooks_custom
```bash
# Verificar estructura
ls -R notebooks_custom/
# Debe mostrar helpers/ y template_empresa_base.ipynb
```

### Error: Image too large
```bash
# Considerar usar Docker multi-stage build
# O eliminar dependencias no usadas de requirements
```

---

## 📚 Referencias

- Documentación original: `DSDL-docs.md`
- Scope del proyecto: `IMAGEN_EMPRESARIAL_SCOPE.md`
- Análisis comparativo: `ANALISIS_COMPARATIVO_DSDL.md`

