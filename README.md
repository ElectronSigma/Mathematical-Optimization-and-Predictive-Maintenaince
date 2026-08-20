# Reverse Osmosis Predictive Maintenance Model

## Description
This script models the membrane fouling behavior in a Reverse Osmosis (RO) desalination unit to predict optimal cleaning schedules. Using operational historical data of Net Driving Pressure (NDP), the model applies empirical regression and root-finding algorithms to determine the exact future date when the membrane pressure drop hits the critical manufacturer limit.

## Objective
To transition from reactive maintenance to predictive scheduling, minimizing downtime and optimizing chemical reagent consumption during Clean-In-Place (CIP) procedures.

## Technical Stack
*   **Language:** Python 3.8
*   **Libraries:** `scipy.optimize` (fsolve for root finding), `numpy` (polynomial fitting), `pandas`, `matplotlib.pyplot`.

## Methodology
1.  **Data Ingestion:** Loads historical daily records of operational NDP.
2.  **Polynomial Regression:** Fits a 2nd-degree polynomial curve to the noisy sensor data to map the physical fouling degradation over time.
3.  **Numerical Optimization:** Defines an objective function and utilizes `scipy.optimize.fsolve` to numerically compute the exact day ($t$) where the NDP function intersects the critical operational threshold (e.g., 10.5 bar).
4.  **Forecasting:** Projects the theoretical curve beyond the current dataset to visualize the failure point.

## Results
The algorithm successfully isolated the signal noise and projected that the critical NDP limit will be reached on **Day X**, providing the operations team with a precise window for CIP scheduling. 
