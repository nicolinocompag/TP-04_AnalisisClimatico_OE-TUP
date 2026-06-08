
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable
import numpy as np
import os

# --- Configuración visual (dark theme) ---
plt.rcParams.update({
    "figure.facecolor":  "#0d1117",
    "axes.facecolor":    "#161b22",
    "axes.edgecolor":    "#30363d",
    "axes.labelcolor":   "#c9d1d9",
    "xtick.color":       "#8b949e",
    "ytick.color":       "#8b949e",
    "text.color":        "#c9d1d9",
    "grid.color":        "#21262d",
    "grid.linestyle":    "--",
    "grid.alpha":        0.6,
    "legend.facecolor":  "#161b22",
    "legend.edgecolor":  "#30363d",
    "font.family":       "DejaVu Sans",
})

MESES       = ["ENE", "FEB", "MAR", "ABR", "MAY", "JUN",
               "JUL", "AGO", "SEP", "OCT", "NOV", "DIC"]
MESES_LABEL = ["Ene","Feb","Mar","Abr","May","Jun",
               "Jul","Ago","Sep","Oct","Nov","Dic"]

# --- Carga ---
df   = pd.read_csv("datos/datos.csv", encoding="utf-8")
tmax = df[df["VARIABLE"] == "TEMP.MAX"].set_index("ORIGEN")[MESES].apply(pd.to_numeric, errors="coerce")
tmin = df[df["VARIABLE"] == "TEMP.MIN"].set_index("ORIGEN")[MESES].apply(pd.to_numeric, errors="coerce")
prec = df[df["VARIABLE"] == "PRECIPITACIONES"].set_index("ORIGEN")[MESES].apply(pd.to_numeric, errors="coerce")

os.makedirs("resultados", exist_ok=True)

# Estaciones destacadas con color
ESTACIONES_DESTACADAS = {
    "JUJUY AERO":          ("#ff6b6b", "Jujuy"),
    "TUCUMAN AERO":        ("#ffa94d", "Tucumán"),
    "CORDOBA AERO":        ("#63e6be", "Córdoba"),
    "BUENOS AIRES EZEIZA": ("#74c0fc", "Buenos Aires"),
    "MENDOZA AERO":        ("#a5d8ff", "Mendoza"),
    "BARILOCHE AERO":      ("#748ffc", "Bariloche"),
    "RIO GALLEGOS AERO":   ("#da77f2", "Río Gallegos"),
}

# ============================================================
# GRÁFICO 1 — Comparativa temperaturas por estación
# ============================================================
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 12), sharex=True)
fig.patch.set_facecolor("#0d1117")
fig.suptitle("Comparativa de Temperaturas Anuales — Estaciones Meteorológicas Argentina",
             fontsize=14, fontweight="bold", color="#e6edf3", y=0.98)

for ax, data, titulo in [
    (ax1, tmax, "Temperatura Máxima Mensual por Estación"),
    (ax2, tmin, "Temperatura Mínima Mensual por Estación"),
]:
    band_max = data.max(skipna=True)
    band_min = data.min(skipna=True)
    ax.fill_between(range(12), band_min, band_max, alpha=0.08, color="#58a6ff")

    for est in data.index:
        if est not in ESTACIONES_DESTACADAS:
            ax.plot(range(12), data.loc[est], color="#30363d", linewidth=0.6, alpha=0.5)

    for est, (color, label) in ESTACIONES_DESTACADAS.items():
        if est in data.index:
            ax.plot(range(12), data.loc[est], color=color, linewidth=2,
                    marker="o", markersize=4, label=label, zorder=5)

    ax.set_title(titulo, fontsize=12, fontweight="bold", color="#e6edf3", pad=10)
    ax.set_ylabel("Temperatura (°C)", color="#8b949e", fontsize=10)
    ax.grid(True)
    ax.axhline(0, color="#ff6b6b", linewidth=0.8, linestyle="--", alpha=0.5, label="0 °C")
    ax.legend(loc="lower center", ncol=4, fontsize=8,
              facecolor="#161b22", edgecolor="#30363d", labelcolor="#c9d1d9")

ax2.set_xticks(range(12))
ax2.set_xticklabels(MESES_LABEL, fontsize=10)
ax2.set_xlabel("Mes", color="#8b949e", fontsize=11)

plt.tight_layout()
plt.savefig("resultados/temperaturas_comparativas.png", dpi=150,
            bbox_inches="tight", facecolor="#0d1117")
plt.show()
print("Gráfico 1 guardado.")


# ============================================================
# GRÁFICO 2 — Temperatura promedio nacional por mes
# ============================================================
tmax_prom   = tmax.mean(skipna=True)
tmin_prom   = tmin.mean(skipna=True)
tmedia_prom = (tmax_prom + tmin_prom) / 2

fig, ax = plt.subplots(figsize=(13, 7))
fig.patch.set_facecolor("#0d1117")

ax.fill_between(range(12), tmin_prom, tmax_prom,
                alpha=0.25, color="#8b4513", label="Rango Máx-Mín")
ax.plot(range(12), tmax_prom,   color="#ff6b6b", linewidth=2.5, marker="o",
        markersize=6, label="Promedio Máxima", zorder=5)
ax.plot(range(12), tmedia_prom, color="#63e6be", linewidth=2, marker="s",
        markersize=5, linestyle="--", label="Promedio Medio", zorder=5)
ax.plot(range(12), tmin_prom,   color="#74c0fc", linewidth=2.5, marker="^",
        markersize=6, label="Promedio Mínima", zorder=5)

for i in range(12):
    ax.annotate(f"{tmax_prom[i]:.1f}", (i, tmax_prom[i]),
                textcoords="offset points", xytext=(0, 8),
                ha="center", fontsize=8, color="#ff6b6b")
    ax.annotate(f"{tmin_prom[i]:.1f}", (i, tmin_prom[i]),
                textcoords="offset points", xytext=(0, -14),
                ha="center", fontsize=8, color="#74c0fc")
    ax.annotate(f"{tmedia_prom[i]:.1f}", (i, tmedia_prom[i]),
                textcoords="offset points", xytext=(6, 0),
                ha="left", fontsize=7.5, color="#63e6be")

ax.axhline(0, color="#ff6b6b", linewidth=0.8, linestyle="--", alpha=0.5, label="0 °C")
ax.set_title("Temperatura Promedio Nacional por Mes\n(76 estaciones meteorológicas — Argentina)",
             fontsize=13, fontweight="bold", color="#e6edf3")
ax.set_xlabel("Mes", color="#8b949e", fontsize=11)
ax.set_ylabel("Temperatura (°C)", color="#8b949e", fontsize=11)
ax.set_xticks(range(12))
ax.set_xticklabels(MESES_LABEL, fontsize=10)
ax.legend(fontsize=9, facecolor="#161b22", edgecolor="#30363d", labelcolor="#c9d1d9")
ax.grid(True)

plt.tight_layout()
plt.savefig("resultados/temperatura_promedio_nacional.png", dpi=150,
            bbox_inches="tight", facecolor="#0d1117")
plt.show()
print("Gráfico 2 guardado.")


# ============================================================
# GRÁFICO 3 — Precipitaciones promedio anuales por estación
# ============================================================
prec_anual = prec.sum(axis=1, skipna=True).sort_values(ascending=False)

def acortar(nombre):
    return nombre.replace(" AERO", "").replace(" OBS.", "").replace(" B.A.", " B.A.").title()

etiquetas = [acortar(e) for e in prec_anual.index]

norm    = Normalize(vmin=prec_anual.min(), vmax=prec_anual.max())
cmap    = plt.cm.YlGnBu
colores = [cmap(norm(v)) for v in prec_anual.values]

fig_height = max(10, len(prec_anual) * 0.28)
fig, ax = plt.subplots(figsize=(13, fig_height))
fig.patch.set_facecolor("#0d1117")

bars = ax.barh(etiquetas, prec_anual.values, color=colores,
               edgecolor="#21262d", linewidth=0.4, height=0.75)

for bar, val in zip(bars, prec_anual.values):
    ax.text(val + 15, bar.get_y() + bar.get_height() / 2,
            f"{val:.0f} mm", va="center", ha="left", fontsize=7.5, color="#c9d1d9")

sm = ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
cbar = plt.colorbar(sm, ax=ax, pad=0.01)
cbar.set_label("mm / año", color="#8b949e", fontsize=9)
cbar.ax.yaxis.set_tick_params(color="#8b949e")
plt.setp(cbar.ax.yaxis.get_ticklabels(), color="#8b949e", fontsize=8)
cbar.outline.set_edgecolor("#30363d")

ax.set_title("Precipitación Total Anual por Estación Meteorológica\n(suma de promedios mensuales — Argentina)",
             fontsize=12, fontweight="bold", color="#e6edf3")
ax.set_xlabel("Precipitación Total Anual (mm)", color="#8b949e", fontsize=10)
ax.invert_yaxis()
ax.grid(axis="x")
ax.set_xlim(0, prec_anual.max() * 1.12)

plt.tight_layout()
plt.savefig("resultados/precipitaciones_por_estacion.png", dpi=150,
            bbox_inches="tight", facecolor="#0d1117")
plt.show()
print("Gráfico 3 guardado.")
print("Todos los gráficos guardados en resultados/")
