import pandas as pd
import os

# --- Rutas ---
input_path  = "datos/estadisticas.txt"
output_path = "datos/datos.csv"

# --- Variables a conservar y sus nombres normalizados ---
VARIABLES_MAP = {
    "Temperatura m\xe1xima (\xb0C)": "TEMP.MAX",
    "Temperatura m\xednima (\xb0C)": "TEMP.MIN",
    "Precipitaci\xf3n (mm)":          "PRECIPITACIONES",
}

MESES = ["ENE", "FEB", "MAR", "ABR", "MAY", "JUN",
         "JUL", "AGO", "SEP", "OCT", "NOV", "DIC"]

# --- Lectura y limpieza ---
filas = []

with open(input_path, encoding="latin-1") as f:
    for linea in f:
        partes = linea.rstrip("\n").split("\t")
        if len(partes) != 14:
            continue
        estacion = partes[0].strip()
        variable  = partes[1].strip()
        if variable not in VARIABLES_MAP:
            continue
        valores = partes[2:]
        fila = {"ORIGEN": estacion, "VARIABLE": VARIABLES_MAP[variable]}
        for mes, val in zip(MESES, valores):
            v = val.strip()
            fila[mes] = None if v == "S/D" else float(v)
        filas.append(fila)

# --- Construcción del DataFrame y exportación ---
columnas = ["ORIGEN", "VARIABLE"] + MESES
df = pd.DataFrame(filas, columns=columnas)

os.makedirs("datos", exist_ok=True)
df.to_csv(output_path, index=False, encoding="utf-8")

print(f"CSV generado: {output_path}")
print(f"Estaciones  : {df['ORIGEN'].nunique()}")
print(f"Filas       : {len(df)}")
print(df.head(9).to_string(index=False))
