# ==========================================
# PROJET IS-LM AVEC DONNEES FRED
# ==========================================

from pandas_datareader import data as web
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm


# ==========================================
# 1. PERIODE D'ANALYSE
# ==========================================

start = "2000-01-01"
end = "2025-12-31"

print("Téléchargement des données FRED...")


# ==========================================
# 2. TELECHARGEMENT DES DONNEES
# ==========================================

# PIB réel = Y
gdp = web.DataReader(
    "GDPC1",
    "fred",
    start,
    end
)

# Taux d'intérêt = i
taux = web.DataReader(
    "FEDFUNDS",
    "fred",
    start,
    end
)

# Masse monétaire M2 = M
m2 = web.DataReader(
    "M2SL",
    "fred",
    start,
    end
)

# Niveau général des prix = P
prix = web.DataReader(
    "CPIAUCSL",
    "fred",
    start,
    end
)

# Consommation réelle = C
consommation = web.DataReader(
    "PCECC96",
    "fred",
    start,
    end
)

# Investissement privé réel = I
investissement = web.DataReader(
    "GPDIC1",
    "fred",
    start,
    end
)

# Dépenses publiques réelles = G
depenses_publiques = web.DataReader(
    "GCEC1",
    "fred",
    start,
    end
)

print("Téléchargement terminé !")


# ==========================================
# 3. CONVERTIR TOUT EN DONNEES TRIMESTRIELLES
# ==========================================

gdp = gdp.resample("QE").mean()

taux = taux.resample("QE").mean()

m2 = m2.resample("QE").mean()

prix = prix.resample("QE").mean()

consommation = consommation.resample("QE").mean()

investissement = investissement.resample("QE").mean()

depenses_publiques = depenses_publiques.resample("QE").mean()


# ==========================================
# 4. RENOMMER LES COLONNES
# ==========================================

gdp.columns = ["Y"]

taux.columns = ["i"]

m2.columns = ["M"]

prix.columns = ["P"]

consommation.columns = ["C"]

investissement.columns = ["I"]

depenses_publiques.columns = ["G"]


# ==========================================
# 5. FUSIONNER TOUTES LES DONNEES
# ==========================================

data = pd.concat(
    [
        gdp,
        taux,
        m2,
        prix,
        consommation,
        investissement,
        depenses_publiques
    ],
    axis=1
)


# ==========================================
# 6. SUPPRIMER LES LIGNES VIDES
# ==========================================

data = data.dropna()


# ==========================================
# 7. CALCULER LA MASSE MONETAIRE REELLE
# ==========================================

data["M_P"] = data["M"] / data["P"]


# ==========================================
# 8. AFFICHER LES DONNEES
# ==========================================

print("\nNombre de lignes disponibles :")
print(len(data))

print("\nTABLEAU FINAL :")
print(data.head())

print("\nDERNIERES LIGNES :")
print(data.tail())


# ==========================================
# 9. SAUVEGARDER LES DONNEES
# ==========================================

data.to_csv(
    "donnees_is_lm.csv"
)

print(
    "\nFichier sauvegardé : donnees_is_lm.csv"
)


# ==========================================
# 10. ESTIMATION DE LA COURBE IS
# ==========================================

print("\n================================")
print("ESTIMATION DE LA COURBE IS")
print("================================")


# Variable expliquée
Y_is = data["Y"]


# Variables explicatives
X_is = data[
    [
        "i",
        "G"
    ]
]


# Ajouter une constante
X_is = sm.add_constant(
    X_is
)


# Régression OLS
modele_is = sm.OLS(
    Y_is,
    X_is
).fit()


# Afficher les résultats
print(
    modele_is.summary()
)


# ==========================================
# 11. ESTIMATION DE LA COURBE LM
# ==========================================

print("\n================================")
print("ESTIMATION DE LA COURBE LM")
print("================================")


# Variable expliquée :
# taux d'intérêt
Y_lm = data["i"]


# Variables explicatives :
# PIB et masse monétaire réelle
X_lm = data[
    [
        "Y",
        "M_P"
    ]
]


# Ajouter une constante
X_lm = sm.add_constant(
    X_lm
)


# Régression OLS
modele_lm = sm.OLS(
    Y_lm,
    X_lm
).fit()


# Afficher les résultats
print(
    modele_lm.summary()
)


# ==========================================
# 12. GRAPHIQUE PIB ET TAUX D'INTERET
# ==========================================

fig, ax1 = plt.subplots(
    figsize=(12, 6)
)


ax1.plot(
    data.index,
    data["Y"]
)

ax1.set_xlabel(
    "Date"
)

ax1.set_ylabel(
    "PIB réel Y"
)


ax2 = ax1.twinx()


ax2.plot(
    data.index,
    data["i"],
    linestyle="--"
)

ax2.set_ylabel(
    "Taux d'intérêt i"
)


plt.title(
    "PIB réel et taux d'intérêt - Données FRED"
)

plt.grid()

plt.show()


# ==========================================
# 13. AFFICHER MESSAGE FINAL
# ==========================================

print("\nAnalyse terminée avec succès !")