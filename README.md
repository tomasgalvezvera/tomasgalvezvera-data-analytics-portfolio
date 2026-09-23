# Análisis CAT Buenos Aires (Python)

Análisis exploratorio y limpieza de datos de la **Encuesta a Centros de Atención Turística (CAT)** de la Ciudad de Buenos Aires, correspondiente al período 2017-2018.

Este proyecto aborda el mismo dataset que [`sql-cat-buenos-aires`](../sql-cat-buenos-aires), pero con un enfoque distinto: en vez de SQL/MySQL Workbench, acá se trabaja con **Python y pandas**, orientado a procesos de limpieza y transformación de datos.

## Fuente de datos

- Dataset: [Resultado de encuestas en Centros de Atención Turística (CAT)](https://data.buenosaires.gob.ar/sl/dataset/encuesta-centros-atencion-turistica-cat/resource/juqdkmgo-942-resource) — GCBA (Gobierno de la Ciudad de Buenos Aires)
- Última actualización del dataset: 18/06/2026
- Fecha de descarga: 18/09/2026

## Herramientas

- Python 3
- pandas

## ¿Qué hace el script?

1. **Carga** del dataset (`resultado-de-encuestas-2017-2018.csv`).
2. **Análisis descriptivo inicial**: dimensiones, columnas, tipos de datos, frecuencia de valores por CAT y por barrio.
3. **Chequeo de duplicados**.
4. **Selección y renombre de columnas** relevantes para el análisis.
5. **Unificación de país de residencia**, combinando tres columnas originales (`pais_extranjero`, `otro_pais_extranjero`, `provincia_argentina`) en una sola columna `pais`, con una jerarquía de reglas de prioridad.
6. **Clasificación de tipo de visitante** (Argentina / Extranjero / Sin dato) a partir de la columna `pais`.
7. **Exportación** del dataset limpio (`cat_buenos_aires_limpio.csv`).

## Cómo correrlo

```bash
pip install pandas
python analisis_cat.py
```

> Nota: el archivo CSV original no está incluido en este repositorio. Podés descargarlo desde el [link oficial](https://data.buenosaires.gob.ar/sl/dataset/encuesta-centros-atencion-turistica-cat/resource/juqdkmgo-942-resource) y colocarlo en esta misma carpeta antes de ejecutar el script.

## Próximos pasos

- Visualización de la distribución geográfica y por tipo de visitante.
- Análisis temporal (por fecha/temporada).
- Cruce entre barrio y punto CAT.
