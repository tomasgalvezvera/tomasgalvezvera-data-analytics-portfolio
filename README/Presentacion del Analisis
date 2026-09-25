# Portfolio de Análisis de Datos — Tomás Galvez Vera 🎯📊🌍

# 🏙️ Turismo CABA: Prestigio Internacional vs. Demanda Operativa Real

> Un análisis de datos aplicado sobre 340.000+ registros de atención turística en la Ciudad de Buenos Aires, enfocado en ingeniería de datos, limpieza de fuentes públicas y visualización para toma de decisiones.

---

## 🎯 1. Presentación del Problema & Métrica Principal

Buenos Aires fue distinguida internacionalmente por la revista Wanderlust por sus atributos culturales (tango, gastronomía, barrios)[cite: 1]. Sin embargo, los registros reales de los Centros de Atención Turística (CAT) revelan la dinámica operativa diaria del visitante[cite: 1].

### 📊 Hallazgo Final Depurado (Segmentación de Demanda)
Tras depurar la base de datos oficial (174.812 registros / 360.209 pasajeros)[cite: 4], la demanda presencial se distribuye de la siguiente manera:

* 🌍 **Turismo Internacional:** Concentra el **57,3% de las consultas** (100.103 registros) y el **60,2% de los pasajeros totales** (216.764 personas)[cite: 4].
* 🇦🇷 **Turismo Nacional:** Representa el **41,8% de las consultas** (73.139 registros) y el **38,5% de los pasajeros** (138.829 personas)[cite: 4].
* ❓ **Sin Dato / No especificado:** Reducido al **0,9%** gracias al pipeline de limpieza[cite: 4].

**Conclusión Clave:** La demanda operativa en los CAT está dominada por el turismo internacional de conectividad regional, con una fuerte presencia de turismo interno (4 de cada 10 visitantes) que exige un soporte de orientación predominantemente logístico (mapas y transporte)[cite: 1, 4].

---

## 🧹 2. Limpieza de Datos y Diagnóstico de Calidad (Data Hygiene)

El valor técnico principal del proyecto reside en la transformación de datos públicos desordenados e inestables en una base limpia y modelada para análisis de negocio:

* **Unificación de Procedencia Dispersa:** La procedencia del turista estaba fragmentada en tres campos distintos (`pais_residencia_si_extranjero`, `otro_pais_residencia_si_extranjero` y `provincia_residencia_si_argentino`)[cite: 4]. Se diseñó un algoritmo de consolidación jerárquica en Python para asignar el origen exacto y reducir los valores nulos al mínimo[cite: 4].
* **Auditoría de Inconsistencias Territoriales (SQL):** Se identificó que la *Comuna 4* registraba visitas y pasajeros pero no poseía ningún punto CAT físico registrado en la tabla de infraestructura, documentando la anomalía para el pipeline ETL[cite: 3].
* **Depuración de Duplicados Sintácticos:** Normalización de nombres de países duplicados por espacios o variantes de tipeo (ej. *Finlandia*, *Holanda* / *Países Bajos*)[cite: 3].

---

## 🛠️ 3. Evolución del Proyecto en 4 Módulos Técnicos

### 🟢 Módulo 1: Análisis Descriptivo Inicial (Looker Studio + Excel)
* **Objetivo:** Comparación de la hipótesis de posicionamiento internacional (Wanderlust) frente a la demanda operativa real 2016-2019 (341.700 registros)[cite: 1, 2].
* **Entregable:** Dashboard interactivo enfocado en la brecha entre consultas logísticas y culturales[cite: 1].
* 🔗 [Ver Dashboard Interactivo](https://datastudio.google.com/reporting/7210dc12-294b-4bff-aedd-70c684c9fb97) | 🔗 [Publicación en LinkedIn](https://www.linkedin.com/posts/tomasggalvezvera_prestigio-internacional-vs-datos-reales-ugcPost-7482594738542632960-fFCJ/)

### 🔵 Módulo 2: Modelado Relacional y Consultas Avanzadas (SQL) *En Desarrollo*
* **Objetivo:** Estructuración de datos planos en un modelo de 5 tablas (`visitas`, `cat`, `barrios`, `comunas`, `paises`)[cite: 3].
* **Habilidades Demostradas:**
  * Uso de `JOIN` multinivel para relacionar entidades geográficas y de atención[cite: 3].
  * Clasificación de países por volumen (`Alta`, `Media`, `Baja`) mediante `CASE`[cite: 3].
  * Agregaciones con `GROUP BY` y `HAVING` para identificar nodos de saturación (CAT Florida / Comuna 1)[cite: 1, 3].
* 📁 [`/sql/trabajo_practico_sql.sql`](./sql/)

### 🟡 Módulo 3: Pipeline de Limpieza y ETL (Python / Pandas) *En Desarrollo*
* **Objetivo:** Procesamiento automatizado de 174.812 encuestas (2017-2018)[cite: 4].
* **Habilidades Demostradas:**
  * Tratamiento de nulos con reemplazos condicionales (`.replace()`, `.fillna()`, `.loc[]`)[cite: 4].
  * Creación de banderas sintéticas de análisis (`tipo_visitante`: *Nacional* vs. *Internacional*)[cite: 4].
  * Exportación de dataset depurado `cat_buenos_aires_limpio.csv`[cite: 4].
* 📁 [`/python/analisis_cat.py`](./python/)

### 🔴 Módulo 4: Visualización Ejecutiva & DAX (Power BI) — *En Desarrollo*
* **Objetivo:** Consolidación final utilizando modelo en estrella y métricas dinámicas DAX para presentar a stakeholders no técnicos.
