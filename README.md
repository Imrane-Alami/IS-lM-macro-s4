# IS-lM-macro-s4
# IS-LM Model: A Simple Empirical Application Using FRED Data

## Introduction

The IS-LM model is one of the most well-known frameworks in Keynesian macroeconomics. It provides a simple way to understand the interaction between the real economy and the financial sector.

The model was developed as a formal interpretation of the ideas introduced by John Maynard Keynes in *The General Theory of Employment, Interest and Money* (1936). The IS-LM framework was initially developed by John Hicks and later extended by economists such as Alvin Hansen and Franco Modigliani.

The model studies two major markets:

- The **goods market**, represented by the **IS curve**.
- The **money market**, represented by the **LM curve**.

The intersection of these two curves determines the simultaneous equilibrium level of output and the interest rate in the economy.

This project provides a simplified empirical application of the IS-LM model to the United States using macroeconomic data from the Federal Reserve Economic Data (FRED) database.

---

# 1. The IS Curve

IS stands for **Investment-Saving**.

The IS curve represents all combinations of output (Y) and the interest rate (i) for which the goods market is in equilibrium.

A simplified goods market equilibrium can be written as:

Y = C + I + G

where:

- **Y** = Real GDP or aggregate output
- **C** = Consumption
- **I** = Investment
- **G** = Government spending

In a more complete framework, aggregate demand may also include net exports.

The main idea behind the IS curve is the relationship between interest rates, investment, and aggregate demand.

When interest rates increase, borrowing becomes more expensive. This tends to reduce investment spending by firms and, potentially, other interest-sensitive expenditures.

Lower investment reduces aggregate demand, which can lead to lower equilibrium output.

Therefore, the traditional IS curve is downward sloping.

In simple terms:

**Higher interest rate → Lower investment → Lower aggregate demand → Lower output**

Conversely:

**Lower interest rate → Higher investment → Higher aggregate demand → Higher output**

For the empirical analysis, this project estimates a simplified IS relationship:

Y = α₀ + α₁i + α₂G + ε

The expected hypotheses are:

- **α₁ < 0**: Higher interest rates are associated with lower output.
- **α₂ > 0**: Higher government spending is associated with higher output.

An increase in government spending represents an expansionary fiscal policy. In the traditional IS-LM framework, this increases aggregate demand and shifts the IS curve to the right.

---

# 2. The LM Curve

LM stands for **Liquidity-Money**.

The LM curve represents equilibrium in the money market.

A simplified money market equilibrium condition can be written as:

M / P = L(Y, i)

where:

- **M** = Nominal money supply
- **P** = Price level
- **M/P** = Real money balances
- **Y** = Real output
- **i** = Interest rate
- **L(Y, i)** = Demand for real money balances

The basic idea is that economic activity affects the demand for money.

When output increases, households and firms conduct more economic transactions. This increases the demand for money.

For a given real money supply, higher money demand tends to put upward pressure on the equilibrium interest rate.

Therefore, the traditional LM curve is upward sloping.

In simple terms:

**Higher output → Higher money demand → Higher interest rate**

The empirical LM relationship used in this project is:

i = β₀ + β₁Y + β₂(M/P) + u

The expected hypotheses are:

- **β₁ > 0**: Higher output is associated with a higher interest rate.
- **β₂ < 0**: Higher real money balances are associated with a lower interest rate.

An increase in real money balances makes more liquidity available in the economy. In the traditional IS-LM framework, this tends to reduce the equilibrium interest rate and affects the position of the LM curve.

---

# 3. IS-LM Equilibrium

The general equilibrium of the IS-LM model occurs at the intersection of the IS and LM curves.

This point can be represented as:

E(Y*, i*)

where:

- **Y*** is the equilibrium level of output.
- **i*** is the equilibrium interest rate.

At this point, the goods market and the money market are simultaneously in equilibrium.

The IS curve explains how the interest rate affects equilibrium output through aggregate demand.

The LM curve explains how output interacts with money demand and the interest rate.

Together, the two curves provide a simplified representation of short-run macroeconomic equilibrium.

---

# 4. Fiscal Policy

The IS-LM model can be used to analyze fiscal policy.

Suppose the government increases government spending (G).

Higher government spending directly increases aggregate demand.

This can be represented as:

**Increase in G → Increase in aggregate demand → IS curve shifts to the right**

In the standard IS-LM model, this leads to a new equilibrium characterized by higher output and, generally, a higher interest rate.

Therefore, one of the main hypotheses of the model is that expansionary fiscal policy can stimulate economic activity, particularly when aggregate demand is insufficient.

---

# 5. Monetary Policy

The IS-LM framework can also be used to study monetary policy.

In the traditional model, an increase in the real money supply increases liquidity available in the economy.

This tends to reduce interest rates and stimulate interest-sensitive components of aggregate demand, particularly investment.

The mechanism can be summarized as:

**Increase in real money supply → Lower interest rate → Higher investment → Higher aggregate demand → Higher output**

In the traditional graphical representation, monetary expansion affects the LM curve and produces a new IS-LM equilibrium.

It is important to note that modern central banks, including the Federal Reserve, typically conduct monetary policy primarily through interest-rate policy rather than by directly targeting monetary aggregates such as M2. Therefore, the traditional LM curve should be understood as a simplified theoretical representation of monetary equilibrium.

---

# 6. Empirical Application

This project applies these theoretical ideas to the U.S. economy using data from the Federal Reserve Economic Data (FRED) database.

The analysis covers the period from 2000 to 2025.

The following macroeconomic variables are used:

- **Real GDP (Y)** — GDPC1
- **Federal Funds Rate (i)** — FEDFUNDS
- **M2 Money Supply (M)** — M2SL
- **Consumer Price Index (P)** — CPIAUCSL
- **Real Consumption (C)** — PCECC96
- **Real Private Investment (I)** — GPDIC1
- **Real Government Spending (G)** — GCEC1

Real money balances are approximated by:

M/P

The data are converted to quarterly frequency and combined into a single dataset.

---

# 7. Empirical Hypotheses

Based on the theoretical IS-LM framework, this project examines four main hypotheses.

### Hypothesis 1: Interest Rates and Output

Higher interest rates are expected to be associated with lower real output.

**Expected sign: Negative**

This hypothesis reflects the traditional IS mechanism through which higher borrowing costs reduce investment and aggregate demand.

### Hypothesis 2: Government Spending and Output

Higher government spending is expected to be associated with higher real output.

**Expected sign: Positive**

This represents the expansionary effect of fiscal policy in the Keynesian framework.

### Hypothesis 3: Output and Interest Rates

Higher output is expected to be associated with higher equilibrium interest rates.

**Expected sign: Positive**

This reflects the idea that higher economic activity increases the demand for money.

### Hypothesis 4: Real Money Balances and Interest Rates

Higher real money balances are expected to be associated with lower interest rates.

**Expected sign: Negative**

This represents the traditional monetary mechanism of the LM curve.

---

# 8. Econometric Estimation

The theoretical relationships are examined empirically using Ordinary Least Squares (OLS) regressions.

The simplified IS equation is:

Y = α₀ + α₁i + α₂G + ε

The simplified LM equation is:

i = β₀ + β₁Y + β₂(M/P) + u

The estimated coefficients can then be compared with the theoretical predictions of the IS-LM model.

For the IS equation, we expect:

α₁ < 0  
α₂ > 0

For the LM equation, we expect:

β₁ > 0  
β₂ < 0

The purpose is to examine whether the relationships observed in U.S. macroeconomic data are broadly consistent with the theoretical predictions of the IS-LM framework.

---

# 9. Interpretation and Limitations

The results of this project should be interpreted carefully.

The IS-LM model is a simplified representation of a complex economy, and the regressions used in this project should be considered empirical illustrations rather than structural estimates of the true U.S. economy.

In particular, correlation does not necessarily imply causation.

GDP, interest rates, government spending, and monetary variables interact simultaneously. For example, interest rates may affect economic activity, but the Federal Reserve also changes interest rates in response to economic conditions.

The period from 2000 to 2025 also includes several exceptional macroeconomic events, such as the Global Financial Crisis, the period of very low interest rates, the COVID-19 pandemic, large fiscal interventions, and the post-pandemic inflation episode.

These events may have changed the relationships between output, interest rates, fiscal policy, and monetary conditions over time.

Despite these limitations, the project provides a simple empirical introduction to the IS-LM framework and demonstrates how macroeconomic theory can be connected to real-world economic data using Python.

---

# Conclusion

The IS-LM model provides a simple framework for understanding the interaction between the goods market and the money market.

The IS curve represents equilibrium in the goods market and highlights the relationship between interest rates and aggregate demand.

The LM curve represents equilibrium in the money market and highlights the relationship between output, money demand, real money balances, and interest rates.

Their intersection determines a simultaneous equilibrium level of output and the interest rate.

Using U.S. data from FRED, this project attempts to connect these theoretical relationships with observed macroeconomic data through simplified econometric estimation.

The project therefore serves as both an introduction to the IS-LM model and a practical example of how Python and real economic data can be used to explore fundamental macroeconomic relationships.
