from scipy.cluster.vq import kmeans,vq ,whiten
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from numpy import random


fifa= pd.read_csv('data/fifa_18_sample_data.csv')
# print(fifa['phy'])
