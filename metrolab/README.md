# MetroLab · línea de actualización del tablero

| Cuaderno | Qué hace |
|---|---|
| `01_PANEL_WAZE` | Feed de Waze (solo archivos nuevos) → panel de 5 min por segmento |
| `02_TABLA_MODELADO` | Panel → tabla de modelado (historia, vecinos, calendario, objetivos) |
| `03_MODELO` | Modelo XGBoost: predice el último día y arma los CSV del tablero (`reentrenar` en Colab con GPU) |
| `04_PUBLICAR_TABLERO` | Código del tablero + CSV → carpeta `tablero/` de este repositorio |

**Automático:** `.github/workflows/actualizar_tablero.yml` corre 01 → 04 en modo `actualizar` cada 6 horas.
Necesita en *Settings → Secrets and variables → Actions*: `AZURE_STORAGE_ACCOUNT`, `AZURE_STORAGE_KEY`, `AZURE_FILE_SYSTEM`.

**Reentrenar** (una vez al mes): en Colab con GPU, `03_MODELO` con `MODO = "reentrenar"` y luego `04_PUBLICAR_TABLERO`.
