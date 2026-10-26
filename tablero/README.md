# Gemelo Digital · Velocidad Autopista Sur

Tablero de monitoreo y predicción de velocidad media del corredor Autopista Sur (Bogotá – Soacha – Granada).
Piloto del Gemelo Digital de la Región Metropolitana Bogotá–Cundinamarca · Observatorio de Dinámica Regional.

## Cómo actualizar los datos

El tablero lee los archivos de la carpeta `datos/`. Para actualizarlo:

1. En GitHub, entra a la carpeta `datos/`.
2. **Add file → Upload files** y arrastra los CSV nuevos con **el mismo nombre** (reemplazan a los anteriores).
3. **Commit changes**. En 1–2 minutos el sitio se actualiza en el mismo enlace.

| Archivo | Sale de (cuaderno 07) |
|---|---|
| `dia_monitoreo.csv`, `perfil_tipico.csv` | celda 12.9 |
| `dia_info.csv` | se arma con `dia_monitoreo.json` (fecha, día de la semana, horas) |
| `predicciones_ultima_ventana.csv` | celda 12.5 |
| `metricas_*.csv`, `referencia_promedio30.csv`, `importancia_variables.csv`, `serie_ejemplo.csv` | celdas 11c, 12.1–12.7 |
| `geometria_segmentos.csv`, `red_shp.csv`, `ficha_tecnica.csv` | trazado del corredor y ficha técnica |

Nota: `datos/datos_local.js` es una copia de los CSV que solo se usa al abrir `index.html` con doble clic desde el computador. En GitHub Pages el tablero lee los CSV, así que para actualizar el enlace basta con reemplazar los CSV.
