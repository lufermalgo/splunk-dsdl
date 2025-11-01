# Gap Encontrado: notebooks_custom No Visible en JupyterLab

**Fecha**: 2025-01-31  
**Problema**: El bootstrap script no copia `/dltk/notebooks_custom` a `/srv/notebooks_custom`

---

## 🔍 Problema

Cuando lanzamos un contenedor con la imagen empresarial custom, el directorio `notebooks_custom` NO aparece en JupyterLab porque:

1. ✅ Dockerfile copia correctamente: `COPY notebooks_custom /dltk/notebooks_custom`
2. ❌ Bootstrap script NO copia a `/srv/`: Solo copia `/dltk/app` y `/dltk/notebooks`
3. ❌ JupyterLab se ejecuta desde `/srv`, por lo que no ve el directorio

---

## ✅ Solución Aplicada

**Archivo modificado**: `splunk-mltk-container-docker/bootstrap_scripts/bootstrap_fast.sh`

**Línea agregada** (después de línea 8):
```bash
cp -R /dltk/notebooks_custom /srv
```

**Antes:**
```bash
umask 002
/dltk/bootstrap_backup.sh
cp -R /dltk/app /srv
cp -R /dltk/notebooks /srv
if [ -w /etc/passwd ]; then
```

**Después:**
```bash
umask 002
/dltk/bootstrap_backup.sh
cp -R /dltk/app /srv
cp -R /dltk/notebooks /srv
cp -R /dltk/notebooks_custom /srv  # ← AGREGADO
if [ -w /etc/passwd ]; then
```

---

## 🔄 Próximo Paso: Rebuild

Necesitamos rebuild completo de la imagen para aplicar el fix:

```bash
cd /Users/lufermalgo/Proyectos/Splunk-DSDL/splunk-mltk-container-docker
./build.sh golden-cpu-empresa-arm splunk/ 5.2.2
```

---

## 📋 Checklist Post-Rebuild

- [ ] Build exitoso sin errores
- [ ] Imagen aparece en `docker images`
- [ ] Stop contenedores actuales
- [ ] Launcher nueva imagen en DSDL UI
- [ ] Verificar `/srv/notebooks_custom` visible en JupyterLab
- [ ] Test import helpers
- [ ] Test abrir template

---

## 🎯 Estado Actual

- ✅ Fix aplicado en código fuente
- ⏳ Pendiente rebuild
- ⏳ Pendiente validación

