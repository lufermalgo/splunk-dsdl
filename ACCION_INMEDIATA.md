# Siguiente Paso Inmediato

## 🎯 Acción Ahora

**Explorar JupyterLab**:
1. Click en `barebone_template.ipynb` (template base de DSDL)
2. Leer estructura de funciones `fit`/`apply`/`summary`
3. Click en `autoencoder.ipynb` (comparar con Cristian)
4. Identificar gaps de librerías

---

## ⚡ Rápido (5 min)

```python
# En nuevo notebook Python 3, ejecutar:
import pandas as pd
import numpy as np
import tensorflow as tf
import torch
import sklearn

print("✅ Librerías base OK")

try:
    import aeon
    print("✅ aeon disponible")
except:
    print("❌ aeon FALTA")
```

---

## 📋 Próximo Sprint

1. **Sesión con Cristian**: Mostrar JupyterLab → adaptar su notebook
2. **Validar custom image**: Si falta `aeon`, crear según sección 9.4 del análisis
3. **Test end-to-end**: Datos Splunk → Training → Inference

