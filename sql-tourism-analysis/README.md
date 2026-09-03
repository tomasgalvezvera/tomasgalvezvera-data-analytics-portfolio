🗺️ Análisis de Turismo en CABA: Centros de Atención al Turista (CAT)

Proyecto de SQL enfocado en analizar el comportamiento de visitantes en los Centros de Atención al Turista (CAT) de la Ciudad de Buenos Aires, basado en el dataset público del Gobierno de la Ciudad:

🔗 data.buenosaires.gob.ar - Encuesta CAT

📌 Contexto

Los CAT son puntos de información turística ubicados en distintos barrios de CABA (Puerto Madero, Retiro, Florida, Recoleta, etc.) donde se registran visitas de turistas nacionales y extranjeros. Este proyecto analiza esos registros para responder preguntas de negocio típicas de un análisis de turismo urbano.

🧱 Diagrama Entidad-Relación

   screenshots/diagrama-er.png

El modelo relaciona 5 tablas con una jerarquía territorial:

paises
   │
   └──> visitas <──── cat <──── barrios <──── comunas
paises: país de origen del turista
comunas: división administrativa de CABA
barrios: barrios de la ciudad, asociados a una comuna
cat: Centros de Atención al Turista, ubicados en un barrio
visitas: registro de pasajeros por fecha, CAT, barrio, comuna y país
❓ Preguntas que responde el análisis
¿Qué centro de atención turística recibe más visitantes?
¿Qué barrios y comunas concentran mayor afluencia?
¿De qué países vienen los turistas que visitan cada centro?
¿Cómo varía el turismo a lo largo del año (estacionalidad)?
¿Qué centros son más estables y cuáles más estacionales?
🗂️ Estructura del proyecto
├── schema_y_datos_reales.sql   → Creación de tablas + carga de datos reales
├── queries.sql                 → Consultas de análisis, comentadas
├── trabajo_practico_sql.sql    → Ejercicios progresivos (SELECT → CASE)
├── screenshots/                → Diagrama ER y capturas de resultados
└── README.md                   → Este archivo
🛠️ Técnicas de SQL utilizadas
JOIN entre múltiples tablas relacionadas
GROUP BY y funciones de agregación (SUM, AVG, COUNT, MAX, MIN)
HAVING para filtrar sobre resultados agrupados
Subqueries (cálculo de porcentaje sobre el total)
CTEs (Common Table Expressions) con WITH
Window functions (ROW_NUMBER() OVER PARTITION BY) para rankear dentro de cada grupo
CASE para categorizar registros según reglas de negocio
💡 Hallazgos principales
CAT Florida concentra la mayor cantidad de pasajeros registrados, siendo el punto de mayor tránsito turístico del dataset.
Se observa estacionalidad en la demanda a lo largo del año.
El análisis por país permite identificar los principales orígenes de los turistas que consultan en cada centro.
🚀 Cómo ejecutarlo
Ejecutar schema_y_datos_reales.sql en MySQL Workbench (o cualquier motor MySQL) para crear la base y cargar los datos reales.
Ejecutar las consultas de queries.sql o trabajo_practico_sql.sql una por una para explorar cada análisis.

Proyecto desarrollado como parte de mi portfolio de Data Analytics, con foco en modelado relacional y consultas SQL orientadas a negocio.
