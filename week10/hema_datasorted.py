#!/usr/bin/env python3

"""From .txt file to make an array of the data for numpy to generate heat map and compare gene expression"""

import sys
import numpy as np
import matplotlib.pylab as plt 
import scipy
import seaborn as sns  
import pandas as pd 
from scipy.cluster.hierarchy import dendrogram, linkage, leaves_list

datafile = open(sys.argv[1])

data = pd.read_csv(datafile, sep = "\t", header = 0, index_col = "gene")
#print(data)

linkage_1 = scipy.cluster.hierarchy.linkage(data, method='average')
leaf_1 = scipy.cluster.hierarchy.leaves_list(linkage_1)


leaves_list_1 = leaves_list(linkage_1)
new_data = data.iloc[leaves_list_1]
transposed_new_data = new_data.transpose()

linkage_2 = linkage(transposed_new_data, method='average')
leaves_list_2 = leaves_list(linkage_2)
finished_last_data = transposed_new_data.iloc[leaves_list_2]
final_transposed = finished_last_data.transpose()
sns.heatmap(final_transposed)
plt.show()










fig = plt.figure(figsize=(5, 3))
plt.xlabel('Cell Type')
plt.title('Dendrogram')
plt.grid(True)
label_list = ["CFU", "poly", "unk", "int", "mys", "mid"]
labels = np.array(label_list)
sort_label = labels[leaves_list_2]
ax1 = dendrogram(linkage_2, labels = sort_label)
plt.show()

cfu = data["CFU"].values
poly = data["poly"].values



from sklearn.cluster import KMeans
from pandas import DataFrame

Data = {'x':cfu,
        'y': poly
       }
  
df = DataFrame(Data,columns=['x','y'])
kmeans = KMeans(n_clusters=5).fit(df)
centroids = kmeans.cluster_centers_

plt.scatter(df['x'], df['y'], c= kmeans.labels_.astype(float), s=50, alpha=0.5)
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=50)
plt.xlabel("CFU")
plt.ylabel("poly")
plt.show()


cluster_map = pd.DataFrame()
cluster_map['data_index'] = df.index.values
cluster_map['cluster'] = kmeans.labels_
cluster_map[cluster_map.cluster == 5]







from scipy import stats

diff_exp_high = ((data['CFU'] + data['unk'])/2)/((data['poly'] + data['int'])/2) >= 2
diff_exp_low = ((data['CFU'] + data['unk'])/2)/((data['poly'] + data['int'])/2) <= 0.5

diff_exp_genes = data[diff_exp_high | diff_exp_low]

for gene_name, row in diff_exp_genes.iterrows():
    sample1 = [row['CFU'], row['unk']]
    sample2 = [row['poly'], row['int']]
    pval = stats.ttest_rel(sample1, sample2).pvalue
    if pval <= 0.05:
        print(gene_name, pval)



labels = list(kmeans.labels_)
genes = list(data.index.values)

goi_index = genes.index(sys.argv[2])
goi_cluster = labels[goi_index]

related_genes = []
for i, gene in enumerate(genes):
    if labels[i] == goi_cluster:
        related_genes.append(gene)

print(related_genes)

with open('list_of_genes.txt', 'w') as f:
    for item in related_genes:
        f.write("%s," % item)




