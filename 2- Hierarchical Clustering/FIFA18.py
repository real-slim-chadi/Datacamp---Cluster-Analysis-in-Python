import seaborn as sns
import matplotlib.pyplot as plt
from scipy.cluster.vq import whiten
from scipy.cluster.hierarchy import linkage, fcluster 
import pandas as pd

fifa=pd.read_csv("data/fifa_18_dataset.csv")
sliding_tackle= fifa['sliding_tackle']
agression= fifa['aggression']

#scaling
sliding_tackle_scaled=whiten(sliding_tackle)
agression_scaled=whiten(agression)

fifa['sliding_tackle_scaled']=sliding_tackle_scaled
fifa['agression_scaled']=agression_scaled
print (fifa.head(),'\n,',fifa.shape)

## Distance
distance_matrix=linkage(fifa[['sliding_tackle_scaled','agression_scaled']],"ward") 

# Assign cluster labels to each row of data
fifa['cluster_labels'] = fcluster(distance_matrix, 3, criterion='maxclust')

# Display cluster centers of each cluster
print(fifa[['sliding_tackle_scaled', 'agression_scaled', 'cluster_labels']].groupby('cluster_labels').mean())

# Create a scatter plot through seaborn
sns.scatterplot(x='sliding_tackle_scaled', y='agression_scaled', hue='cluster_labels', data=fifa)
plt.show()

# # Plot original data matplotlib
# plt.plot(sliding_tackle, label='original')

# # Plot scaled data
# plt.plot(sliding_tackle_scaled, label='scaled')

# # Show the legend in the plot
# plt.legend()
# plt.title("Sliding Tackle")
# # Display the plot
# plt.show()

# plt.plot(agression, label='original')
# plt.plot(agression_scaled, label='scaled')
# plt.title("Agression")
# plt.show()