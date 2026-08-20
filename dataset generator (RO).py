import pandas as pd
import numpy as np


np.random.seed(101)
operation_days = np.arange(1,181) 

npd_start = 15
npd_ideal = npd_start - (0.005*operation_days) - (0.00008*operation_days**2)

noise = np.random.normal(0, 0.25, len(operation_days))
ndp_real = npd_ideal + noise

df_ro = pd.DataFrame({
	'Operation_Days':operation_days,
	'NDP_(bar)':ndp_real
	})

df_ro.to_csv('RO_dataset.csv', index=False)