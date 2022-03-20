from scipy.cluster.vq import kmeans,vq ,whiten
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from numpy import random


fifa= pd.read_csv('data/fifa_18_sample_data.csv')
# print(fifa['phy'])

fifa['scaled_def']=whiten(fifa['def'])
fifa['scaled_phy']=whiten( fifa['phy'])

# print( fifa['scaled_def'])

# Set up a random seed in numpy
random.seed([1000,2000])

# Fit the data into a k-means algorithm
cluster_centers,_ = kmeans(fifa[['scaled_def', 'scaled_phy']], 3)

# Assign cluster labels
fifa['cluster_labels'], _ = vq(fifa[['scaled_def', 'scaled_phy']], cluster_centers)

# Display cluster centers 
print(fifa[['scaled_def', 'scaled_phy', 'cluster_labels']].groupby('cluster_labels').mean())

# Create a scatter plot through seaborn
sns.scatterplot(x="scaled_def", y='scaled_phy', hue='cluster_labels', data=fifa)
plt.show()