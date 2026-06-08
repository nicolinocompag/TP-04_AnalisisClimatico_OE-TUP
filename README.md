ANÁLISIS CLIMÁTICO - TP04
Tecnicatura Universitaria en Programación | UTN San Nicolás

TÍTULO DEL PROYECTO
-------------------
Análisis de Datos Climáticos: Temperaturas y Precipitaciones en Argentina (2024)

================================================================================
INTEGRANTES DEL EQUIPO
--------------------------------------------------------------------------------
- Compagnucci, Nicolas

================================================================================
ESCENARIO ELEGIDO
--------------------------------------------------------------------------------
Análisis de datos mensuales de temperatura mínima, temperatura máxima y
precipitaciones a lo largo de los 12 meses del año, correspondientes a
estaciones meteorológicas distribuidas en el territorio argentino.

El objetivo es identificar patrones climáticos, variaciones estacionales y
comparar el comportamiento de las variables entre distintas estaciones.

================================================================================
DESCRIPCIÓN DEL DATASET
--------------------------------------------------------------------------------
Fuente   : Servicio Meteorológico Nacional (SMN) - Argentina
Cobertura: 76 estaciones meteorológicas distribuidas en el país
Período  : 12 meses (datos mensuales)
Formato  : CSV

Variables incluidas:
  - Temperatura mínima mensual (°C)
  - Temperatura máxima mensual (°C)
  - Precipitaciones mensuales (mm)

Los archivos de datos crudos se encuentran en la carpeta /datos.

================================================================================
INSTRUCCIONES PARA EJECUTAR EL SCRIPT
--------------------------------------------------------------------------------
1. Abrí el archivo principal en Google Colab:
      TP-04_AnalisisClimatico_OE-TUP.ipynb

2. Cloná el repositorio ejecutando la primera celda del notebook,
   que descarga los datos y configura el entorno automáticamente.

3. Ejecutá las celdas en orden secuencial de arriba hacia abajo
   (Menú: Runtime > Run all).

4. Los resultados generados (gráficos y tablas) se guardarán
   automáticamente en la carpeta /resultados.

REQUISITOS
  - Cuenta de Google (para acceder a Colab)
  - Librerías: pandas, matplotlib, seaborn
    (se instalan automáticamente en la primera celda)

================================================================================
ESTRUCTURA DEL REPOSITORIO
--------------------------------------------------------------------------------
TP-04_AnalisisClimatico_OE-TUP/
│
├── datos/          → Archivos CSV con los datos meteorológicos crudos
├── scripts/        → Scripts Python auxiliares
├── resultados/     → Gráficos y tablas generados por el análisis
└── README.md       → Este archivo

================================================================================
