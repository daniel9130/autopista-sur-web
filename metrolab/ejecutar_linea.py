"""Corre la línea MetroLab en orden (01 → 04) en modo "actualizar".

Se usa desde GitHub Actions (.github/workflows/actualizar_tablero.yml), pero también
funciona en cualquier máquina con Java 17 y las librerías de requirements.txt:
    python metrolab/ejecutar_linea.py
Los secretos se leen de variables de entorno: AZURE_STORAGE_ACCOUNT, AZURE_STORAGE_KEY,
AZURE_FILE_SYSTEM y GITHUB_TOKEN.
"""
import os
import sys
import time

import papermill as pm

AQUI = os.path.dirname(os.path.abspath(__file__))
CUADERNOS = ["01_PANEL_WAZE", "02_TABLA_MODELADO", "03_MODELO", "04_PUBLICAR_TABLERO"]
os.makedirs("salidas", exist_ok=True)

for nombre in CUADERNOS:
    t0 = time.time()
    print(f"\n========== {nombre} ==========", flush=True)
    try:
        pm.execute_notebook(f"{AQUI}/notebooks/{nombre}.ipynb", f"salidas/{nombre}.ipynb",
                            parameters={"MODO": "actualizar"}, kernel_name="python3",
                            log_output=True, cwd=os.getcwd())
    except pm.PapermillExecutionError as e:
        if e.ename == "SystemExit":          # p. ej. "No hay datos nuevos": termina sin error
            print(f"{nombre}: {e.evalue}\nFin de la corrida: no hay nada que actualizar.")
            sys.exit(0)
        raise
    print(f"{nombre} listo en {(time.time() - t0) / 60:.1f} min", flush=True)

print("\nLínea completa: el tablero quedó publicado.")
