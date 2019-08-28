# %%
import pandas as pd

df = pd.read_csv(
    "https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data"
    , header = None)
df.columns = [
    'Class label', 'Alcohol', 'Malic acid', 'Ash', 'Alcalinity of ash',
    'Magnesium', 'Total phenols', 'Flavanoids', 'Nonflavanoid phenols',
    'Proanthocyanins', 'Color intensity', 'Hue', 'OD280/OD315 of diluted wines',
    'Proline'
]
x = df.drop('Class label', 1)
y = df['Class label']
df.head(5)

#%%
import os
import matplotlib.pyplot as plt
import seaborn as sns

imgPath = 'c:\\Users\\prip\\Documents\\Sean\\vscode\\python\\NTHU\\DL\\output'
plt.rcParams["figure.figsize"] = (80,80)
sns.set(style='whitegrid')
# sns.reset_orig()
# sns.pairplot(df, hue="Class label", size=2.5)
plt.tight_layout()

# print(os.getcwd())
# if not os.path.exists(imgPath):
    # os.makedirs(imgPath)
# plt.savefig(os.path.join(imgPath, "fig-wine-scatter.png"), dpi=300)
plt.show()

#%%
import numpy as np
from sklearn.preprocessing import StandardScaler

plt.rcParams["figure.figsize"] = (18,18)
plt.rcParams["xtick.labelsize"]=20
plt.rcParams["ytick.labelsize"]=20
#Z-normalize data
sc = StandardScaler()
Z = sc.fit_transform(x)
z = sc.fit(x)
#*Estimate the correlation matrix
#!z-normalize後的data，其相關係數等於餘弦夾角。
R = np.dot(Z.T, Z) / df.shape[0]


ticklabels = [ s for s in x.columns ]

# hm = sns.heatmap(R,
                # cbar = True,
                # square = True,
                # yticklabels = ticklabels,
                # xticklabels = ticklabels)

plt.tight_layout()
# plt.savefig(os.path.join(imgPath, "fit-wine-corr.png"), dpi=300)
plt.show()
#%%

eigen_vals, eigen_vecs = np.linalg.eigh(R)
print("\nEignevalues: \n%s" %eign_vals)
#%%

import matplotlib.pyplot as plt

tot = sum(np.abs(eign_vals))
var_exp  =[(i / tot) for i in sorted(np.abs(np.abs(eign_vals)), reverse=True)]
# ?np.cumsum
# ?累加函數
cum_var_exp = np.cumsum(var_exp)

plt.bar(range(1, eigen))


#%%
