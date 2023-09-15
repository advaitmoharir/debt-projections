# Debt Projections

This repository hosts the data and code for [Monetary Fiscal Coordination and the Evolution of Public Debt: A Simple Simulation Exercise](https://www.epw.in/journal/2022/22/commentary/monetary-fiscal-coordination-and-evolution-public.html), published in the [Economic and Political Weekly](https://www.epw.in/).

The paper simulates trajectories if India's debt to GDP ratio for the period 2022-2027, under four scenarios: Baseline, Fixed Deficit, Fixed Interest Rates, and Rising Inflation. The simulation is done using the [Law of Motion of Government Debt](https://fgeerolf.com/econ102/public-debt.html), given by:

$$ b_{t+1}= \frac{1+i}{1+g+\pi}b_{t}+d_{t}$$

where $b$ is the debt to GDP ratio, $i$ is the *nominal* interest rate, $g$ is the *nominal* growth rate, and $d$ is the primary deficit.

## Repo Structure

- `01_data`: Data needed to produce Figures 1 & 2
- `02_code`: Code to run projections and generate Figures 1 & 2
- `03_ figures`: Figures 1 and 2

## Replication

Ensure you have the following packages installed in Python: `pandas`, `plotly`, `kaleido`, `pyprojroot`, `matplotlib`, `numpy`. Now follow the steps below

1. Open the folder `debt-projections` after you download the repo in your text editor (say, VSCode).

2. Open and run `02_code/projections.py`. This should create Figures 1 and 2 in the folder `03_figures`.

## Software

Projections were run using Python 3.11 and csvs were stored in Microsoft Excel 16.

## Software

