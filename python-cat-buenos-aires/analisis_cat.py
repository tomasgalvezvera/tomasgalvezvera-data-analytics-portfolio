# -*- coding: utf-8 -*-
"""Analisis CAT Buenos Aires

Análisis descriptivo y limpieza de datos de la Encuesta a Centros de
Atención Turística (CAT) de la Ciudad de Buenos Aires (2017-2018).

Fuente: https://data.buenosaires.gob.ar/sl/dataset/encuesta-centros-atencion-turistica-cat/resource/juqdkmgo-942-resource
Fecha de última actualización del dataset: 18/06/2026
Fecha de descarga: 18/09/2026

Originalmente desarrollado en Google Colab.
"""

import pandas as pd

# ---------------------------------------------------------------------------
# Parte 1 - Carga de la base de datos
# ---------------------------------------------------------------------------
df = pd.read_csv("resultado-de-encuestas-2017-2018.csv")
print("La base se cargó correctamente")

# ---------------------------------------------------------------------------
# Parte 2 - Primer análisis descriptivo
# ---------------------------------------------------------------------------
print("Cantidad de filas y columnas:", df.shape)
print("Nombre de mis columnas/variables:")
print(df.columns)
print("Información general de las variables con las que voy a trabajar:")
print(df.info())

# ---------------------------------------------------------------------------
# Parte 3 - Cómo están almacenados mis datos (análisis descriptivo por variable)
# ---------------------------------------------------------------------------
print(df["centro_atencion_turistica"].value_counts())
print(df["barrio"].value_counts())

# Cruce a explorar más adelante: barrio y punto CAT (ej. Florida = San Nicolás)

# ---------------------------------------------------------------------------
# Parte 4 - Duplicados
# ---------------------------------------------------------------------------
print("¿Hay duplicados?", df.duplicated().sum())

# ---------------------------------------------------------------------------
# Parte 5 - Selección y renombre de columnas
# ---------------------------------------------------------------------------
df2 = df[[
    "id", "fecha", "centro_atencion_turistica", "barrio", "pasajeros",
    "pais_residencia_si_extranjero", "otro_pais_residencia_si_extranjero",
    "provincia_residencia_si_argentino", "primera_vez",
]].copy()

df2 = df2.rename(columns={
    "centro_atencion_turistica": "cat",
    "pais_residencia_si_extranjero": "pais_extranjero",
    "otro_pais_residencia_si_extranjero": "otro_pais_extranjero",
    "provincia_residencia_si_argentino": "provincia_argentina",
    "primera_vez": "primera_visita",
})
print("Columnas renombradas ok")

# ---------------------------------------------------------------------------
# Parte 6 - Unificación de país de residencia
#
# Lógica:
#   1. Si hay un valor en pais_extranjero, se mantiene.
#   2. Si no hay valor en pais_extranjero pero sí en otro_pais_extranjero,
#      se usa ese valor.
#   3. Si no hay valor en ninguna de las dos anteriores pero sí en
#      provincia_argentina, se asigna 'Argentina'.
#   4. Lo que queda sin resolver se marca como 'Sin dato'.
# ---------------------------------------------------------------------------
df2["pais"] = (
    df2["pais_extranjero"]
    .replace("Otro país de residencia si es extranjero", pd.NA)
    .fillna(df2["otro_pais_extranjero"])
)

df2.loc[
    df2["pais"].isna() & df2["provincia_argentina"].notna(),
    "pais",
] = "Argentina"

df2["pais"] = df2["pais"].fillna("Sin dato")

print("Distribución final de país de residencia:")
print(df2["pais"].value_counts())

# ---------------------------------------------------------------------------
# Parte 7 - Columna de tipo de visitante (Argentina / Extranjero / Sin dato)
# ---------------------------------------------------------------------------
df2["tipo_visitante"] = "Sin dato"
df2.loc[df2["pais"] == "Argentina", "tipo_visitante"] = "Argentina"
df2.loc[
    (df2["pais"] != "Argentina") & (df2["pais"] != "Sin dato"),
    "tipo_visitante",
] = "Extranjero"

print(df2["tipo_visitante"].value_counts())

# ---------------------------------------------------------------------------
# Parte 8 - Chequeo de duplicados post-limpieza y exportación
# ---------------------------------------------------------------------------
print("¿Hay duplicados en df2?", df2.duplicated().sum())

df2.to_csv("cat_buenos_aires_limpio.csv", index=False)
print("Dataset limpio exportado como cat_buenos_aires_limpio.csv")
