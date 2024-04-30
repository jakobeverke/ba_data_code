#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 11:54:14 2024

@author: jeverke
"""

import pandas as pd
import numpy as np
import pymannkendall as mk
import matplotlib
import matplotlib.pyplot as plt


overview = pd.read_excel("/Users/jeverke/Desktop/Bachelorarbeit/Datenanalyse/stations_bachelorThesis.xls"
                         , sheet_name= 0)




#%% Gesamt
results = []

# Loop über die Blätter
for sheet_num in range(1,17):
    # Daten für das aktuelle Blatt laden
    data = pd.read_excel("/Users/jeverke/Desktop/Bachelorarbeit/Datenanalyse/stations_bachelorThesis.xls",
                         sheet_name=sheet_num)
    
    # Daten vorbereiten
    data_prep = pd.DataFrame({'year': data["year"], 'Qmax': data["Qmax"]})
    qmax = data_prep["Qmax"]
    
    # Mann-Kendall-Test durchführen
    result = mk.original_test(qmax)
    
    # Ergebnisse extrahieren und in die Liste einfügen
    results.append({'Sheet': sheet_num, 'trend': result.trend, 'p': result.p, 's': result.s, 'slope': result.slope, 'intercept': result.intercept})

# Ergebnisse in DF
results_df = pd.DataFrame(results)

results_df.to_excel("ergebnisse.xlsx", index=False) 

#%% Visualisierung der sign. Trends
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Liste der ausgewählten Sheets und ihre entsprechenden Titel
selected_sheets = [9, 10, 2, 4, 12, 16]  # Beispielwerte
sheet_titles = ['Po - Casale Monferrato (IT)', 'Po-Pontelagoscuro (IT)', 
                'Elbe - Dresden (DE)', 'Weichsel - Torun (PL)', 
                'Ebro, Castejón (ES)', 'Seine - Méry-sur Seine (FR)']  # Beispielwerte

# Pfade zu den Daten
file_path = "/Users/jeverke/Desktop/Bachelorarbeit/Datenanalyse/stations_bachelorThesis.xls"

# Erstelle die Figure und die Subplots
fig, axs = plt.subplots(2, 3, figsize=(15, 10))

# Plotte die ausgewählten Sheets
for i, sheet_num in enumerate(selected_sheets):
    # Lese die Daten des aktuellen Sheets ein
    data = pd.read_excel(file_path, sheet_name=sheet_num)
    
    # Extrahiere Jahr und Qmax Daten
    year = data["year"]
    qmax = data["Qmax"]
    
    # Lineare Regression mit numpy.polyfit durchführen
    coeffs = np.polyfit(year, qmax, 1)
    trend_line = np.poly1d(coeffs)
    
    # Bestimme die Position des Subplots
    row = i // 3
    col = i % 3
    
    # Plotte die Datenpunkte und die Trendlinie
    axs[row, col].plot(year, qmax, 'o', markersize=3, label='Daten')  # Datenpunkte
    axs[row, col].plot(year, trend_line(year), '-', linewidth=2, label='Trendlinie')  # Trendlinie
    axs[row, col].set_xlabel('Jahr')  # Beschriftung der x-Achse
    axs[row, col].set_ylabel('Qmax [m^3/s]')  # Beschriftung der y-Achse
    axs[row, col].set_title(sheet_titles[i])  # Titel des Plots
    axs[row, col].grid(True)  # Gitter anzeigen
    axs[row, col].legend(loc='upper left')  # Legende platzieren

plt.tight_layout()  # Automatische Ausrichtung der Subplots
plt.show()  # Plot anzeigen




#%% Winter

results = []

# Loop über die Blätter
for sheet_num in range(1,16):
    # Daten für das aktuelle Blatt laden
    data = pd.read_excel("/Users/jeverke/Desktop/Bachelorarbeit/Datenanalyse/stations_bachelorThesis.xls",
                         sheet_name=sheet_num)
    
    # Daten vorbereiten
    data_prep = pd.DataFrame({'year': data["year"], 'month': data["month"], 'Qmax': data["Qmax"]})
    
    months_to_keep = [11,12,1,2]

    
    winter_data = data_prep[data_prep['month'].isin(months_to_keep)]

    qmax = winter_data["Qmax"]
    
    # Mann-Kendall-Test durchführen
    result = mk.original_test(qmax)
    
    # Ergebnisse extrahieren und in die Liste einfügen
    results.append({'Sheet': sheet_num, 'trend': result.trend, 'p': result.p, 's': result.s, 'slope': result.slope, 'intercept': result.intercept})

# Ergebnisse in DF
winter_results_df = pd.DataFrame(results)

winter_results_df.to_excel("ergebnisse_winter.xlsx", index=False) 

#%% Sommer

results = []

# Loop über die Blätter
for sheet_num in range(1,16):
    # Daten für das aktuelle Blatt laden
    data = pd.read_excel("/Users/jeverke/Desktop/Bachelorarbeit/Datenanalyse/stations_bachelorThesis.xls",
                         sheet_name=sheet_num)
    
    # Daten vorbereiten
    data_prep = pd.DataFrame({'year': data["year"], 'month': data["month"], 'Qmax': data["Qmax"]})
    
    months_to_keep = [5,6,7,8,9]

    
    sommer_data = data_prep[data_prep['month'].isin(months_to_keep)]

    qmax = sommer_data["Qmax"]
    
    # Mann-Kendall-Test durchführen
    result = mk.original_test(qmax)
    
    # Ergebnisse extrahieren und in die Liste einfügen
    results.append({'Sheet': sheet_num, 'trend': result.trend, 'p': result.p, 's': result.s, 'slope': result.slope, 'intercept': result.intercept})

# Ergebnisse in DF
sommer_results_df = pd.DataFrame(results)

sommer_results_df.to_excel("ergebnisse_sommer.xlsx", index=False) 



#%% POL_1



results_2 = []
# Daten für das aktuelle Blatt laden
data_3 = pd.read_excel("/Users/jeverke/Desktop/Bachelorarbeit/Datenanalyse/stations_bachelorThesis.xls",
                         sheet_name=3)
    
# Daten vorbereiten
data_prep3 = pd.DataFrame({'year': data_3["year"], 'Qmax': data_3["Qmax"]})
qmax3 = data_prep3["Qmax"]
    
    # Mann-Kendall-Test durchführen
result3 = mk.original_test(qmax3)
    
# Ergebnisse extrahieren und in die Liste einfügen
results_2.append({'Sheet': sheet_num, 'trend': result3.trend, 'p': result3.p, 's': result3.s, 'slope': result3.slope, 'intercept': result3.intercept})

# Ergebnisse in DF
results_3 = pd.DataFrame(results_2)




