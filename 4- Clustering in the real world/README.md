# Clustering on the real world
# Image color clustering
we will start by finding the dominant color in an image.

## Extract he RGB values of an image
we use the `matplotlib.image as img` module to get the values.

our code is 
```py
# Import image class of matplotlib
import matplotlib.image as img

# Read batman image and print dimensions
batman_image = img.imread('batman.jpg')
print(batman_image.shape)

# Store RGB values of all pixels in lists r, g and b
for row in batman_image:
    for temp_r, temp_g, temp_b in row:
        r.append(temp_r)
        g.append(temp_g)
        b.append(temp_b)
```
`img.imread` reads the image into a `(57, 90, 3)` matrix

## Get dominant colors
To get the dominant colors, we do a kmeans clustering.
This means:
1. Scale Values
2. `kmeans(data,num_clusters)`

to get the number of clusters we do an elbow plot.

    Elbow plot:
![elbow plot showing how many dominant colors](img/Figure%201.svg)

The elbow plot tells us that we have three clusters, so we know this for the next steps
 
    Python code:
``` py
distortions = []
num_clusters = range(1, 7)

# Create a list of distortions from the kmeans function
for i in num_clusters:
    cluster_centers, distortion = kmeans(batman_df[['scaled_red', 'scaled_blue', 'scaled_green']], i)
    distortions.append(distortion)

# Create a data frame with two lists, num_clusters and distortions
elbow_plot = pd.DataFrame({'num_clusters': num_clusters, 'distortions': distortions})

# Create a line plot of num_clusters and distortions
sns.lineplot(x='num_clusters', y='distortions', data = elbow_plot)
plt.xticks(num_clusters)
plt.show()
```

## Displaying the dominant colors
to displya the dominant colors, we go through the cluster centers and display each color.
### Get standard deviations of each color
r_std, g_std, b_std = batman_df[['red', 'green', 'blue']].std()
``` py
for cluster_center in cluster_centers:
    scaled_r, scaled_g, scaled_b = cluster_center
    # Convert each standardized value to scaled value
    colors.append((
        scaled_r * r_std / 255,
        scaled_g * g_std / 255,
        scaled_b * b_std / 255
    ))
```
### Display colors of cluster centers
``` py
plt.imshow([colors])
plt.show()

```

The dominant colors:
![Plotting the dominant colors](img/Figure%202.svg)
# Document clustering
NLP has more considerations to take than other hard data

## TF-IDF of movie plots
    tf-idf: term frequency/inverse document frequency

This steps cleans out words such as "the, a..."

### Import TfidfVectorizer class from sklearn
```py
from sklearn.feature_extraction.text import TfidfVectorizer
```
### Initialize TfidfVectorizer
```py
tfidf_vectorizer = TfidfVectorizer(max_df=0.75, max_features=50,
                    min_df= 0.1, tokenizer=remove_noise)
```
### Use the .fit_transform() method on the list plots
```py
tfidf_matrix = tfidf_vectorizer.fit_transform(plots)
```
## Clustering terms
We use k means cluster to get the top three terms of each.

The output is : 
```
1:['father', 'back', 'one']
1:['police', 'man', 'killed']
```
The python code to generate all this is:
``` py
num_clusters = 2

# Generate cluster centers through the kmeans function
cluster_centers, distortion = kmeans(tfidf_matrix.todense(), num_clusters)

# Generate terms from the tfidf_vectorizer object
terms = tfidf_vectorizer.get_feature_names()

for i in range(num_clusters):
    # Sort the terms and print top 3 terms
    center_terms = dict(zip(terms, list(cluster_centers[i])))
    sorted_terms = sorted(center_terms, key=center_terms.get, reverse=True)
    print(sorted_terms[:3])
```

# Clustering with multiple features
Hi FIFA.
## Vasic checks on clusters
### Print the size of the clusters
print(fifa.groupby('cluster_labels')['ID'].count())

### Print the mean value of wages in each cluster
print(fifa.groupby('cluster_labels')['eur_wage'].mean())
