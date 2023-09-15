# Debt Projections

This repository hosts the data and code for [Monetary Fiscal Coordination and the Evolution of Public Debt: A Simple Simulation Exercise](https://www.epw.in/journal/2022/22/commentary/monetary-fiscal-coordination-and-evolution-public.html), published in the [Economic and Political Weekly](https://www.epw.in/).

The paper simulates trajectories if India's debt to GDP ratio for the period 2022-2027, under four scenarios: Baseline, Fixed Deficit, Fixed Interest Rates, and Rising Inflation. The simulation is done using the [Law of Motion of Government Debt](https://fgeerolf.com/econ102/public-debt.html), given by:

$$ b_{t+1}= \frac{1+i}{1+g+\pi}b_{t}+d_{t}$$

where $b$ is the debt to GDP ratio, $i$ is the *nominal* interest rate, $g$ is the nominal growth rate, and $d$ is the primary deficit.

## Code

The script used to simulate the four scenarios is stored in the folder `code`. 

## Figures

These are stored in the folder `figures`.

## Software

