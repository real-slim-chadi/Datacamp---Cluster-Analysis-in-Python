# Unsupervised Learning
Unsupervised learning happens when we have an unlabeled dataset

# Exploring
One good way of identifying the number of possible clusters in our data is to do a scatterplot
``` python
import matplotlib.pyplot as plt

plt.scatter(x,y)

plt.show()
```

# Cluster with Scipy
in this example, we cluster legendary Pokemons by x-y coordinates
```python
# Import linkage and fcluster functions
from scipy.cluster.hierarchy import linkage, fcluster

# Use the linkage() function to compute distance
Z = linkage(df, 'ward')

# Generate cluster labels
df['cluster_labels'] = fcluster(Z, 2, criterion='maxclust')

# Plot the points with seaborn
sns.scatterplot(x='x', y='y', hue='cluster_labels', data=df)
plt.show()
```
# K-means clustering with Scipy

- compute the centroids by defining two clusters
- assign cluster labels with `vq()`

```python
# Import kmeans and vq functions
from scipy.cluster.vq import kmeans, vq
# Compute cluster centers
centroids,_ = kmeans(df, 2)

# Assign cluster labels
df['cluster_labels'], _ = vq(df, centroids)

# Plot the points with seaborn
sns.scatterplot(x='x', y='y', hue='cluster_labels', data=df)
plt.show()
```
# Normalization of data
to normalize data, we divide by the standard deviaton
