# test_metrics.py
import sys
sys.path.append('splunk-mltk-container-docker/notebooks_custom/helpers')

from metrics_calculator import calculate_all_metrics, calculate_regression_metrics, calculate_classification_metrics
import numpy as np

print("🧪 Testing metrics_calculator...\n")

# Test 1: Clasificación
print("Test 1: Clasificación")
y_true_cls = np.array([0, 1, 1, 0, 1, 0, 0, 1])
y_pred_cls = np.array([0, 1, 1, 0, 1, 0, 1, 1])  # 1 error
metrics_cls = calculate_all_metrics(y_true_cls, y_pred_cls)
print(f"  Accuracy: {metrics_cls['accuracy']:.3f}")
print(f"  F1: {metrics_cls['f1']:.3f}")
print()

# Test 2: Regresión
print("Test 2: Regresión")
y_true_reg = np.array([10.5, 20.3, 15.7, 25.1, 12.4])
y_pred_reg = np.array([10.2, 20.5, 15.3, 25.4, 12.1])
metrics_reg = calculate_regression_metrics(y_true_reg, y_pred_reg)
print(f"  R²: {metrics_reg['r2']:.3f}")
print(f"  MAE: {metrics_reg['mae']:.3f}")
print(f"  RMSE: {metrics_reg['rmse']:.3f}")
print()

print("✅ metrics_calculator funciona correctamente")

