import pandas as pd
import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

#Load the dataset 
df = pd.read_csv('RO_dataset.csv')
#Create the polynomial
coef = np.polyfit(df['Operation_Days'], df['NDP_(bar)'], deg=2)
polynomial = np.poly1d(coef)

#Create a lambda function to solve later
lambda_ndp = lambda days: polynomial(days) - 10.5

#Solve the function with iterations
critical_day = fsolve(lambda_ndp, 120)

#Create the plot
plt.figure(figsize=(10, 6))

plt.plot(df['Operation_Days'], df['NDP_(bar)'], 'o', label='Historical Data', color='black', alpha=0.6)

extended_days = np.linspace(0, 250)
predicted_ndp = polynomial(extended_days)

plt.plot(extended_days, predicted_ndp, '--', label='Regression data', color='blue', linewidth=2)

plt.axvline(x=critical_day[0], color='red', linestyle=':', linewidth=2, label=f'Critical day ({critical_day[0]:.2f} days)')

plt.axhline(y=10.5, color='orange', linestyle='--', label='Critical limit (10.5 bar)')

plt.title('Predictive maintenance', fontsize=12)
plt.xlabel('Operation Days')
plt.ylabel('NDP (bar)')
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(loc='upper left')

plt.tight_layout()
plt.show()

print(f"The estimated critical day was {critical_day[0]:.2f}")