import pandas as pd
import matplotlib.pyplot as plt
from scipy.cluster.vq import vq, whiten 



fifa=pd.read_csv("data/fifa_18_sample_data.csv")

print(fifa.head())
fifa['scaled_wage']=whiten(fifa.eur_wage)
fifa['scaled_value']=whiten(fifa.eur_value)

fifa.plot(x='scaled_wage',y='scaled_value',kind='scatter' )

plt.show()