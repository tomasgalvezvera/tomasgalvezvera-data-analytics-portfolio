# 🗺️ Análisis de Atención Turística en CABA: Modelo Relacional, Data Hygiene & Business Insights

Proyecto de análisis de datos enfocado en el comportamiento de visitantes en los **Centros de Atención al Turista (CAT)** de la Ciudad de Buenos Aires, basado en el dataset oficial del Gobierno de la Ciudad (174.812 registros / 360.209 pasajeros)[cite: 3, 4].

🔗 **Fuente de datos:** [data.buenosaires.gob.ar - Encuestas CAT](https://data.buenosaires.gob.ar)

---

## 📌 Contexto & Problema 

Buenos Aires cuenta con una destacada proyección turística internacional[cite: 1]. Este módulo analiza la demanda presencial real en los nodos de atención física (Puerto Madero, Retiro, Florida, Recoleta, etc.) para determinar las necesidades operativas de la red, evaluando si el flujo responde a consultas logísticas o culturales y cómo se distribuye entre visitantes **Nacionales e Internacionales**[cite: 1, 4].

---

## 🧹 Calidad de Datos & Limpieza (Data Hygiene)

Un pilar fundamental de este proyecto fue auditar y solucionar las inconsistencias presentes en la base de datos pública:

* **Unificación de procedencia:** Se resolvió la fragmentación del origen del turista (distribuido originalmente en campos de país extranjero, campo libre y provincia argentina) para construir una dimensión limpia de países[cite: 4].
* **Auditoría territorial (SQL):** Se identificaron y aislaron anomalías de registro, como visitas asignadas a la *Comuna 4* sin un punto CAT físico correspondiente en la tabla de infraestructura[cite: 3].
* **Depuración sintáctica:** Normalización de nombres de países duplicados por diferencias de tipeo o variantes regionales (ej. *Finlandia*, *Holanda* vs. *Países Bajos*)[cite: 3].

---

## 🧱 Modelo Relacional (Diagrama ER)

El modelo en SQL normaliza la información en 5 tablas estructuradas con jerarquía territorial[cite: 7]:


