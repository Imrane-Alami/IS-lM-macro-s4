# ==========================================
# IS-LM PROJECT WITH FRED DATA
# ==========================================

from pandas_datareader import data as web
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm


# ==========================================
# 1. ANALYSIS PERIOD
# ==========================================

start = "2000-01-01"
end = "2025-12-31"

print("Downloading FRED data...")


# ==========================================
# 2. DOWNLOAD DATA
# ==========================================

# Real GDP = Y
gdp = web.DataReader(
    "GDPC1",
    "fred",
    start,
    end
)

# Interest rate = i
interest_rate = web.DataReader(
    "FEDFUNDS",
    "fred",
    start,
    end
)

# Money supply M2 = M
m2 = web.DataReader(
    "M2SL",
    "fred",
    start,
    end
)

# General price level = P
price_level = web.DataReader(
    "CPIAUCSL",
    "fred",
    start,
    end
)

# Real consumption = C
consumption = web.DataReader(
    "PCECC96",
    "fred",
    start,
    end
)

# Real private investment = I
investment = web.DataReader(
    "GPDIC1",
    "fred",
    start,
    end
)

# Real government spending = G
government_spending = web.DataReader(
    "GCEC1",
    "fred",
    start,
    end
)

print("Download completed!")


# ==========================================
# 3. CONVERT ALL DATA TO QUARTERLY FREQUENCY
# ==========================================

gdp = gdp.resample("QE").mean()

interest_rate = interest_rate.resample("QE").mean()

m2 = m2.resample("QE").mean()

price_level = price_level.resample("QE").mean()

consumption = consumption.resample("QE").mean()

investment = investment.resample("QE").mean()

government_spending = government_spending.resample("QE").mean()


# ==========================================
# 4. RENAME COLUMNS
# ==========================================

gdp.columns = ["Y"]

interest_rate.columns = ["i"]

m2.columns = ["M"]

price_level.columns = ["P"]

consumption.columns = ["C"]

investment.columns = ["I"]

government_spending.columns = ["G"]


# ==========================================
# 5. MERGE ALL DATA
# ==========================================

data = pd.concat(
    [
        gdp,
        interest_rate,
        m2,
        price_level,
        consumption,
        investment,
        government_spending
    ],
    axis=1
)


# ==========================================
# 6. REMOVE MISSING VALUES
# ==========================================

data = data.dropna()


# ==========================================
# 7. CALCULATE REAL MONEY BALANCES
# ==========================================

data["M_P"] = data["M"] / data["P"]


# ==========================================
# 8. DISPLAY THE DATA
# ==========================================

print("\nNumber of available observations:")
print(len(data))

print("\nFINAL DATASET:")
print(data.head())

print("\nLAST OBSERVATIONS:")
print(data.tail())


# ==========================================
# 9. SAVE THE DATA
# ==========================================

data.to_csv(
    "is_lm_data.csv"
)

print(
    "\nFile saved: is_lm_data.csv"
)


# ==========================================
# 10. ESTIMATE THE IS CURVE
# ==========================================

print("\n================================")
print("IS CURVE ESTIMATION")
print("================================")


# Dependent variable
Y_is = data["Y"]


# Explanatory variables
X_is = data[
    [
        "i",
        "G"
    ]
]


# Add a constant
X_is = sm.add_constant(
    X_is
)


# OLS regression
is_model = sm.OLS(
    Y_is,
    X_is
).fit()


# Display results
print(
    is_model.summary()
)


# ==========================================
# 11. ESTIMATE THE LM CURVE
# ==========================================

print("\n================================")
print("LM CURVE ESTIMATION")
print("================================")


# Dependent variable:
# interest rate
Y_lm = data["i"]


# Explanatory variables:
# GDP and real money balances
X_lm = data[
    [
        "Y",
        "M_P"
    ]
]


# Add a constant
X_lm = sm.add_constant(
    X_lm
)


# OLS regression
lm_model = sm.OLS(
    Y_lm,
    X_lm
).fit()


# Display results
print(
    lm_model.summary()
)


# ==========================================
# 12. REAL GDP AND INTEREST RATE GRAPH
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
    "Real GDP (Y)"
)


ax2 = ax1.twinx()


ax2.plot(
    data.index,
    data["i"],
    linestyle="--"
)

ax2.set_ylabel(
    "Interest Rate (i)"
)


plt.title(
    "Real GDP and Interest Rate - FRED Data"
)

plt.grid()

plt.show()


# ==========================================
# 13. DISPLAY FINAL MESSAGE
# ==========================================

print("\nAnalysis completed successfully!")
# 12. PLOT THE ESTIMATED IS AND LM CURVES
# ==========================================

import numpy as np

print("\n================================")
print("IS-LM EQUILIBRIUM AND GRAPH")
print("================================")


# ==========================================
# GET IS COEFFICIENTS
# ==========================================

a_is = modele_is.params["const"]
b_is = modele_is.params["i"]
c_is = modele_is.params["G"]


# ==========================================
# GET LM COEFFICIENTS
# ==========================================

a_lm = modele_lm.params["const"]
b_lm = modele_lm.params["Y"]
c_lm = modele_lm.params["M_P"]


# ==========================================
# USE AVERAGE VALUES OF G AND M/P
# ==========================================

G_mean = data["G"].mean()
MP_mean = data["M_P"].mean()


# ==========================================
# CREATE A RANGE OF GDP VALUES
# ==========================================

Y_values = np.linspace(
    data["Y"].min(),
    data["Y"].max(),
    500
)


# ==========================================
# IS CURVE
#
# Estimated equation:
#
# Y = a + b*i + c*G
#
# Solving for i:
#
# i = (Y - a - c*G) / b
# ==========================================

IS_values = (
    Y_values
    - a_is
    - c_is * G_mean
) / b_is


# ==========================================
# LM CURVE
#
# Estimated equation:
#
# i = a + b*Y + c*(M/P)
# ==========================================

LM_values = (
    a_lm
    + b_lm * Y_values
    + c_lm * MP_mean
)


# ==========================================
# CALCULATE THE IS-LM EQUILIBRIUM
# ==========================================

IS_slope = 1 / b_is

IS_intercept = (
    -a_is
    - c_is * G_mean
) / b_is


LM_slope = b_lm

LM_intercept = (
    a_lm
    + c_lm * MP_mean
)


# Check that the curves are not parallel
if abs(IS_slope - LM_slope) > 1e-10:

    Y_equilibrium = (
        LM_intercept
        - IS_intercept
    ) / (
        IS_slope
        - LM_slope
    )

    i_equilibrium = (
        LM_slope * Y_equilibrium
        + LM_intercept
    )

    print(
        f"Equilibrium GDP Y* = {Y_equilibrium:.2f}"
    )

    print(
        f"Equilibrium interest rate i* = {i_equilibrium:.2f}"
    )

else:

    Y_equilibrium = None
    i_equilibrium = None

    print(
        "Unable to calculate equilibrium: "
        "the curves are nearly parallel."
    )


# ==========================================
# CREATE THE GRAPH
# ==========================================

plt.figure(
    figsize=(10, 6)
)


# Plot IS curve
plt.plot(
    Y_values,
    IS_values,
    label="Estimated IS Curve"
)


# Plot LM curve
plt.plot(
    Y_values,
    LM_values,
    label="Estimated LM Curve"
)


# ==========================================
# ADD THE EQUILIBRIUM POINT
# ==========================================

if Y_equilibrium is not None:

    plt.scatter(
        Y_equilibrium,
        i_equilibrium,
        s=100,
        label=(
            f"Equilibrium E "
            f"({Y_equilibrium:.2f}, "
            f"{i_equilibrium:.2f})"
        )
    )

    plt.axvline(
        Y_equilibrium,
        linestyle="--"
    )

    plt.axhline(
        i_equilibrium,
        linestyle="--"
    )


# ==========================================
# CUSTOMIZE THE GRAPH
# ==========================================

plt.xlabel(
    "Real GDP (Y)"
)

plt.ylabel(
    "Interest Rate (i)"
)

plt.title(
    "Estimated IS-LM Model Using FRED Data"
)

plt.legend()

plt.grid()

plt.show()
